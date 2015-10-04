# StationPlaylist Studio update checker
# A support module for SPL add-on
# Copyright 2015-2016, Joseph Lee, released under GPL.

# Provides update check facility.

import urllib
import os # Essentially, update download is no different than file downloads.
import gui
import wx
import tones
import splconfig

# Cache the file size for the last downloaded SPL add-on installer.
SPLAddonSize = 0
# Update URL.
SPLUpdateURL = "http://addons.nvda-project.org/files/get.php?file=spl-dev"

def _versionFromURL(url):
	filename = url.split("/")[-1]
	name = filename.split(".nvda-addon")[0]
	return name[name.find("-")+1:]

def updateCheck():
	#global SPLAddonSize
	tones.beep(900, 200)
	# All the information will be stored in the URL object, so just close it once the headers are downloaded.
	url = urllib.urlopen(SPLUpdateURL)
	url.close()
	if url.code != 200:
		wx.CallAfter(gui.messageBox, "Add-on update check failed.", "Check for add-on update")
		return
	size = int(url.info().getheader("Content-Length"))
	if size == SPLAddonSize:
		wx.CallAfter(gui.messageBox, "No add-on update available.", "Check for add-on update")
		return
	else:
		version = _versionFromURL(url.url)
		wx.CallAfter(gui.messageBox, "Studio add-on {newVersion} is available.".format(newVersion = version), "Check for add-on update")
		#SPLAddonSize = size

def _updateCheckEx():
	#global SPLAddonSize
	url = urllib.urlopen(SPLUpdateURL)
	if url.code != 200:
		print "Update check failed"
		url.close()
		return
	size = int(url.info().getheader("Content-Length"))
	if size == SPLAddonSize:
		print "You have the latest version"
		url.close()
		return
	else:
		version = _versionFromURL(url.url)
		print "Add-on version {newVersion} is available.".format(newVersion = version)
		url.close()
		#SPLAddonSize = size

