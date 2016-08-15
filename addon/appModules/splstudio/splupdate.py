# StationPlaylist Studio update checker
# A support module for SPL add-on
# Copyright 2015-2016, Joseph Lee, released under GPL.

# Provides update check facility, basics borrowed from NVDA Core's update checker class.

import urllib
import os # Essentially, update download is no different than file downloads.
import cPickle
import threading
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
# The Unix time stamp for add-on check time.
SPLAddonCheck = 0
# Update metadata storage.
SPLAddonState = {}
# Update URL (the only way to change it is installing a different version from a different branch).
SPLUpdateURL = "http://addons.nvda-project.org/files/get.php?file=spl"
_pendingChannelChange = False
_updateNow = False
SPLUpdateChannel = "stable"
# Update check timer.
_SPLUpdateT = None
# How long it should wait between automatic checks.
_updateInterval = 86400
# Set if a socket error occurs.
_retryAfterFailure = False
# Stores update state.
_updatePickle = os.path.join(globalVars.appArgs.configPath, "splupdate.pickle")

# Not all update channels are listed. The one not listed here is the default ("stable" for this branch).
channels={
	"lts":"http://spl.nvda-kr.org/files/get.php?file=spl-lts16",
	"beta":"http://spl.nvda-kr.org/files/get.php?file=spl-beta",
}

# Come forth, update check routines.
def initialize():
	global SPLAddonState, SPLAddonCheck, _updateNow, SPLUpdateChannel
	try:
		SPLAddonState = cPickle.load(file(_updatePickle, "r"))
		SPLAddonCheck = SPLAddonState["PDT"]
		if "PSZ" in SPLAddonState: del SPLAddonState["PSZ"]
		if "PCH" in SPLAddonState: del SPLAddonState["PCH"]
		_updateNow = "pendingChannelChange" in SPLAddonState
		if "UpdateChannel" in SPLAddonState:
			SPLUpdateChannel = SPLAddonState["UpdateChannel"]
	except IOError:
		SPLAddonState["PDT"] = 0
		_updateNow = False
		SPLUpdateChannel = "stable"

def terminate():
	global SPLAddonState
	# Store new values if it is absolutely required.
	stateChanged = SPLAddonState["PDT"] != SPLAddonCheck
	if stateChanged:
		SPLAddonState["PDT"] = SPLAddonCheck
		SPLAddonState["UpdateChannel"] = SPLUpdateChannel
		if _pendingChannelChange:
			SPLAddonState["pendingChannelChange"] = True
		cPickle.dump(SPLAddonState, file(_updatePickle, "wb"))
	SPLAddonState = None


def _versionFromURL(url):
	# 7.3: Be sure to handle both GitHub and old URL format.
	filename = url.split("/")[-1]
	return filename.split("stationPlaylist-")[1].split(".nvda-addon")[0]

def updateQualify(url):
	# The add-on version is of the form "major.minor". The "-dev" suffix indicates development release.
	# Anything after "-dev" indicates a try or a custom build.
	# LTS: Support upgrading between LTS releases.
	# 7.0: Just worry about version label differences (suggested by Jamie Teh from NV Access).
	version = _versionFromURL(url.url)
	return None if version == SPLAddonVersion else version

_progressDialog = None

# The update check routine.
# Auto is whether to respond with UI (manual check only), continuous takes in auto update check variable for restarting the timer.
# ConfUpdateInterval comes from add-on config dictionary.
def updateCheck(auto=False, continuous=False, confUpdateInterval=1):
	if _pendingChannelChange:
		wx.CallAfter(gui.messageBox, _("Did you recently tell SPL add-on to use a different update channel? If so, please restart NVDA before checking for add-on updates."), _("Update channel changed"), wx.ICON_ERROR)
		return
	global _SPLUpdateT, SPLAddonCheck, _retryAfterFailure, _progressDialog, _updateNow
	if _updateNow: _updateNow = False
	# Regardless of whether it is an auto check, update the check time.
	# However, this shouldnt' be done if this is a retry after a failed attempt.
	if not _retryAfterFailure: SPLAddonCheck = time.time()
	updateInterval = confUpdateInterval*_updateInterval*1000
	# Should the timer be set again?
	if continuous and not _retryAfterFailure: _SPLUpdateT.Start(updateInterval, True)
	# Auto disables UI portion of this function if no updates are pending.
	# All the information will be stored in the URL object, so just close it once the headers are downloaded.
	updateCandidate = False
	try:
		# Look up the channel if different from the default.
		url = urllib.urlopen(SPLUpdateURL if SPLUpdateChannel not in channels else channels[SPLUpdateChannel])
		url.close()
	except IOError:
		_retryAfterFailure = True
		if not auto:
			wx.CallAfter(_progressDialog.done)
			_progressDialog = None
			# Translators: Error text shown when add-on update check fails.
			wx.CallAfter(gui.messageBox, _("Error checking for update."), _("Studio add-on update"), wx.ICON_ERROR)
		if continuous: _SPLUpdateT.Start(600000, True)
		return
	if _retryAfterFailure:
		_retryAfterFailure = False
		# Now is the time to update the check time if this is a retry.
		SPLAddonCheck = time.time()
	if url.code != 200:
		if auto:
			if continuous: _SPLUpdateT.Start(updateInterval, True)
			return # No need to interact with the user.
		# Translators: Text shown when update check fails for some odd reason.
		checkMessage = _("Add-on update check failed.")
	else:
		# Am I qualified to update?
		qualified = updateQualify(url)
		if qualified is None:
			if auto:
				if continuous: _SPLUpdateT.Start(updateInterval, True)
				return
			# Translators: Presented when no add-on update is available.
			checkMessage = _("No add-on update available.")
		else:
			# Translators: Text shown if an add-on update is available.
			checkMessage = _("Studio add-on {newVersion} is available. Would you like to update?").format(newVersion = qualified)
			updateCandidate = True
	if not auto:
		wx.CallAfter(_progressDialog.done)
		_progressDialog = None
	# Translators: Title of the add-on update check dialog.
	if not updateCandidate: wx.CallAfter(gui.messageBox, checkMessage, _("Studio add-on update"))
	else: wx.CallAfter(getUpdateResponse, checkMessage, _("Studio add-on update"), url.info().getheader("Content-Length"))

def getUpdateResponse(message, caption, size):
	if gui.messageBox(message, caption, wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
		os.startfile(SPLUpdateURL)

