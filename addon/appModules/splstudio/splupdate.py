# StationPlaylist Studio update checker
# A support module for SPL add-on
# Copyright 2015-2016, Joseph Lee, released under GPL.

# Provides update check facility.

import urllib
import os # Essentially, update download is no different than file downloads.
from calendar import month_abbr # Last modified date formatting.
import cPickle
import gui
import wx
import tones
import time
import addonHandler
import globalVars

# Add-on manifest routine (credit: various add-on authors including Noelia Martinez).
# Do not rely on using absolute path to open to manifest, as installation directory may change in a future NVDA Core version (highly unlikely, but...).
_addonDir = os.path.join(os.path.dirname(__file__), "..", "..")
# Move this to the main app module in case version will be queried by users.
SPLAddonVersion = addonHandler.Addon(_addonDir).manifest['version']
# Cache the file size for the last downloaded SPL add-on installer (stored in hexadecimal for security).
SPLAddonSize = "0x0"
# The Unix time stamp for add-on check time.
SPLAddonCheck = 0
# Update metadata storage.
SPLAddonState = {}
# Update URL (the only way to change it is installing a different version from a different branch).
SPLUpdateURL = "http://addons.nvda-project.org/files/get.php?file=spl-dev"
# Update check timer.
_SPLUpdateT = None
# How long it should wait between automatic checks.
_updateInterval = 86400
# Set if a socket error occurs.
_retryAfterFailure = False
# Stores update state.
_updatePickle = os.path.join(globalVars.appArgs.configPath, "splupdate.pickle")

# Come forth, update check routines.
def initialize():
	global SPLAddonState, SPLAddonSize, SPLAddonCheck
	try:
		SPLAddonState = cPickle.load(file(_updatePickle, "r"))
		SPLAddonCheck = SPLAddonState["PDT"]
		SPLAddonSize = SPLAddonState["PSZ"]
	except IOError:
		SPLAddonState["PDT"] = 0
		SPLAddonState["PSZ"] = 0x0

def terminate():
	global SPLAddonState
	# Store new values if it is absolutely required.
	stateChanged = SPLAddonState["PSZ"] != SPLAddonSize or SPLAddonState["PDT"] != SPLAddonCheck
	if stateChanged:
		SPLAddonState["PSZ"] = SPLAddonSize
		SPLAddonState["PDT"] = SPLAddonCheck
		cPickle.dump(SPLAddonState, file(_updatePickle, "wb"))
	SPLAddonState = None


def _versionFromURL(url):
	filename = url.split("/")[-1]
	name = filename.split(".nvda-addon")[0]
	return name[name.find("-")+1:]

def _lastModified(lastModified):
	# Add-ons server uses British date format (dd-mm-yyyy).
	day, month, year = lastModified.split()[1:4]
	# Adapted an entry on Stack Overflow on how to convert month names to indecies.
	month = str({v: k for k,v in enumerate(month_abbr)}[month]).zfill(2)
	return "-".join([year, month, day])

def updateProgress():
	tones.beep(440, 40)

def updateQualify(url):
	# The add-on version is of the form "major.minor". The "-dev" suffix indicates development release.
	# Anything after "-dev" indicates a try or a custom build.
	curVersion =SPLAddonVersion.split("-")[0]
	# Because we'll be using the same file name for snapshots...
	if "-dev" in SPLAddonVersion: curVersion+="-dev"
	size = hex(int(url.info().getheader("Content-Length")))
	version = _versionFromURL(url.url)
	# In case we are running the latest version, check the content length (size).
	if version == curVersion:
		if "-dev" not in version:
			return None
		elif ("-dev" in SPLAddonVersion and size != SPLAddonSize):
			return version
	elif version > curVersion:
		return version
	else:
		return ""

# The update check routine.
# Auto is whether to respond with UI (manual check only), continuous takes in auto update check variable for restarting the timer.
def updateCheck(auto=False, continuous=False):
	global _SPLUpdateT, SPLAddonCheck, _retryAfterFailure
	# Regardless of whether it is an auto check, update the check time.
	# However, this shouldnt' be done if this is a retry after a failed attempt.
	if not _retryAfterFailure: SPLAddonCheck = time.time()
	# Should the timer be set again?
	if continuous and not _retryAfterFailure: _SPLUpdateT.Start(_updateInterval*1000, True)
	# Auto disables UI portion of this function if no updates are pending.
	if not auto: tones.beep(110, 40)
	# Try builds does not (and will not) support upgrade checking unless absolutely required.
	# All the information will be stored in the URL object, so just close it once the headers are downloaded.
	if not auto:
		progressTone = wx.PyTimer(updateProgress)
		progressTone.Start(1000)
	updateCandidate = False
	try:
		url = urllib.urlopen(SPLUpdateURL)
		url.close()
	except IOError:
		_retryAfterFailure = True
		if not auto:
			progressTone.Stop()
			wx.CallAfter(gui.messageBox, "Error checking for update.", "Check for add-on update", wx.ICON_ERROR)
		if continuous: _SPLUpdateT.Start(600000, True)
		return
	if _retryAfterFailure:
		_retryAfterFailure = False
		# Now is the time to update the check time if this is a retry.
		SPLAddonCheck = time.time()
	if url.code != 200:
		if auto:
			if continuous: _SPLUpdateT.Start(_updateInterval*1000, True)
			return # No need to interact with the user.
		checkMessage = "Add-on update check failed."
	else:
		# Am I qualified to update?
		qualified = updateQualify(url)
		if qualified is None:
			if auto:
				if continuous: _SPLUpdateT.Start(_updateInterval*1000, True)
				return
			checkMessage = "No add-on update available."
		elif qualified == "":
			if auto:
				if continuous: _SPLUpdateT.Start(_updateInterval*1000, True)
				return
			checkMessage = "You appear to be running a version newer than the latest released version. Please reinstall the official version to downgrade."
		else:
			checkMessage = "Studio add-on {newVersion} ({modifiedDate}) is available. Would you like to update?".format(newVersion = qualified, modifiedDate = _lastModified(url.info().getheader("Last-Modified")))
			updateCandidate = True
	if not auto: progressTone.Stop()
	if not updateCandidate: wx.CallAfter(gui.messageBox, checkMessage, "Check for add-on update")
	else: wx.CallAfter(getUpdateResponse, checkMessage, "Check for add-on update", url.info().getheader("Content-Length"))

def getUpdateResponse(message, caption, size):
	global SPLAddonSize
	if gui.messageBox(message, caption, wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
		SPLAddonSize = hex(int(size))
		os.startfile(SPLUpdateURL)

