# StationPlaylist Studio update checker
# A support module for SPL add-on
# Copyright 2015-2016, Joseph Lee, released under GPL.

# Provides update check facility.

import urllib
import os # Essentially, update download is no different than file downloads.
from calendar import month_abbr # Last modified date formatting.
import gui
import wx
import tones
import addonHandler

# Add-on manifest routine (credit: various add-on authors including Noelia Martinez).
# Do not rely on using absolute path to open to manifest, as installation directory may change in a future NVDA Core version (highly unlikely, but...).
_addonDir = os.path.join(os.path.dirname(__file__), "..", "..")
# Move this to the main app module in case version will be queried by users.
SPLAddonVersion = addonHandler.Addon(_addonDir).manifest['version']

# Cache the file size for the last downloaded SPL add-on installer (stored in hexadecimal for security).
SPLAddonSize = "0x0"
# Update URL (the only way to change it is installing a different version from a different branch).
SPLUpdateURL = "http://addons.nvda-project.org/files/get.php?file=spl-dev"

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
	size = hex(int(url.info().getheader("Content-Length")))
	version = _versionFromURL(url.url)
	# In case we are running the latest version, check the content length (size).
	if version == SPLAddonVersion:
		if "-dev" not in version or ("-dev" in SPLAddonVersion and size == SPLAddonSize):
			return None
	elif version > SPLAddonVersion or ("-dev" in version and size != SPLAddonSize):
		return version
	else:
		return ""

def updateCheck():
	tones.beep(110, 40)
	# Try builds does not (and will not) support upgrade checking unless absolutely required.
	# All the information will be stored in the URL object, so just close it once the headers are downloaded.
	progressTone = wx.PyTimer(updateProgress)
	progressTone.Start(1000)
	updateCandidate = False
	url = urllib.urlopen(SPLUpdateURL)
	url.close()
	if url.code != 200:
		checkMessage = "Add-on update check failed."
	else:
		# Am I qualified to update?
		qualified = updateQualify(url)
		if qualified is None:
			checkMessage = "No add-on update available."
		elif qualified == "":
			checkMessage = "You appear to be running a version newer than the latest released version. Please reinstall the official version to downgrade."
		else:
			checkMessage = "Studio add-on {newVersion} ({modifiedDate}) is available. Would you like to update?".format(newVersion = qualified, modifiedDate = _lastModified(url.info().getheader("Last-Modified")))
			updateCandidate = True
	progressTone.Stop()
	if not updateCandidate: wx.CallAfter(gui.messageBox, checkMessage, "Check for add-on update")
	else: wx.CallAfter(getUpdateResponse, checkMessage, "Check for add-on update", url.info().getheader("Content-Length"))

def getUpdateResponse(message, caption, size):
	global SPLAddonSize
	if gui.messageBox(message, caption, wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
		SPLAddonSize = hex(int(size))
		os.startfile(SPLUpdateURL)

