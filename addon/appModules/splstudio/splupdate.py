# StationPlaylist Studio update checker
# A support module for SPL add-on
# Copyright 2015-2018 Joseph Lee, released under GPL.

# Provides update check facility, basics borrowed from NVDA Core's update checker class and other support modules.
# This module won't be available if add-on update feature isn't supported.

# #50 (18.03): there are times when update check should not be supported.
# Raise runtime exceptions if this is the case.
try:
	import updateCheck
except RuntimeError:
	raise RuntimeError("NVDA itself cannot check for updates")
import globalVars
if globalVars.appArgs.secure:
	raise RuntimeError("NVDA in secure mode, cannot check for add-on update")
# Only applicable for custom try builds.
_customTryBuild = False
if _customTryBuild:
	# Communicate this flag with others.
	if not "--spl-customtrybuild" in globalVars.appArgsExtra: globalVars.appArgsExtra.append("--spl-customtrybuild")
	raise RuntimeError("Custom add-on try build detected, no add-on update possible")
import versionInfo
if not versionInfo.updateVersionType:
	raise RuntimeError("NVDA is running from source code, add-on update check is not supported")
# NVDA 2018.1 and later.
import config
if config.isAppX:
	raise RuntimeError("This is NVDA Windows Store edition")
import addonHandler
# Provided that NVDA issue 3208 is implemented.
if hasattr(addonHandler, "checkForAddonUpdate"):
	raise RuntimeError("NVDA itself will check for add-on updates")

import sys
py3 = sys.version.startswith("3")
import os # Essentially, update download is no different than file downloads.
import time
if py3:
	import pickle
	from urllib.request import urlopen
else:
	import cPickle as pickle
	from urllib import urlopen
import threading
import tempfile
import ctypes
import ssl
import gui
import wx
from . import splactions

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
SPLUpdateURL = "https://addons.nvda-project.org/files/get.php?file=spl-dev"
_pendingChannelChange = False
_updateNow = False
SPLUpdateChannel = "dev"
# Update check timer.
_SPLUpdateT = None
# How long it should wait between automatic checks.
_updateInterval = 86400
# Set if a socket error occurs.
_retryAfterFailure = False
# Stores update state.
_updatePickle = os.path.join(globalVars.appArgs.configPath, "splupdate.pickle")

channels={
	"stable":"https://addons.nvda-project.org/files/get.php?file=spl",
	"try":"http://www.josephsl.net/files/nvdaaddons/getupdate.php?file=spl-try",
	#"lts":"http://www.josephsl.net/files/nvdaaddons/getupdate.php?file=spl-ltsxp",
}

# Available channels and their UI labels (if there's only one, channel selection list will not be shown).
# 18.07: channels and their labels will be managed from update module instead of add-on settings to prepare for different settings interfaces.
_updateChannels = [
	("try","Test Drive Fast"),
	("dev","Test Drive Slow"),
	("stable","stable")
]

# Come forth, update check routines.
def initialize():
	global SPLAddonState, SPLAddonCheck, _updateNow, SPLUpdateChannel
	try:
		SPLAddonState = pickle.load(file(_updatePickle, "r"))
		SPLAddonCheck = SPLAddonState["PDT"]
		_updateNow = "pendingChannelChange" in SPLAddonState
		if _updateNow: del SPLAddonState["pendingChannelChange"]
		if "UpdateChannel" in SPLAddonState:
			SPLUpdateChannel = SPLAddonState["UpdateChannel"]
			"""if SPLUpdateChannel in ("beta", "prerelease") or (SPLUpdateChannel == "lts" and sys.getwindowsversion().build >= 7601) or (SPLUpdateChannel in ("try", "dev") and sys.getwindowsversion().build < 7601):
				# 17.10 to 17.12: do not touch LTS channel if Windows XP or Vista is in use.
				SPLUpdateChannel = "dev"
				"""
	except (IOError, KeyError):
		SPLAddonState["PDT"] = 0
		_updateNow = False
		SPLUpdateChannel = "dev"
	# Handle profile switches.
	splactions.SPLActionProfileSwitched.register(splupdate_actionProfileSwitched)
	# Check for add-on update if told to do so.
	# In case a time-based profile is active or other switch flags are on, give up, as update check will happen after a possible trigger is set.
	from . import splconfig, spldebugging
	if canUpdate() and splconfig.SPLConfig.switchProfileFlags == 0 and (splconfig.SPLConfig["Update"]["AutoUpdateCheck"] or _updateNow):
		spldebugging.debugOutput("checking for add-on updates from %s channel"%SPLUpdateChannel)
		# 7.0: Have a timer call the update function indirectly.
		import queueHandler
		queueHandler.queueFunction(queueHandler.eventQueue, updateInit)

def terminate():
	global SPLAddonState
	splactions.SPLActionProfileSwitched.unregister(splupdate_actionProfileSwitched)
	# 7.0: Turn off auto update check timer.
	updateCheckTimerEnd()
	# Store new values if it is absolutely required.
	# Take care of a case where one might be "downgrading" from try builds.
	stateChanged = "UpdateChannel" not in SPLAddonState or (SPLAddonState["PDT"] != SPLAddonCheck or SPLAddonState["UpdateChannel"] != SPLUpdateChannel)
	if stateChanged:
		SPLAddonState["PDT"] = SPLAddonCheck
		SPLAddonState["UpdateChannel"] = SPLUpdateChannel
		if _pendingChannelChange:
			SPLAddonState["pendingChannelChange"] = True
		pickle.dump(SPLAddonState, file(_updatePickle, "wb"))
	SPLAddonState = None

# Turn off update check timer.
def updateCheckTimerEnd():
	global _SPLUpdateT
	if _SPLUpdateT is not None and _SPLUpdateT.IsRunning(): _SPLUpdateT.Stop()
	_SPLUpdateT = None

# Enable or disable update checking facility if told by config changes action.
def splupdate_actionProfileSwitched():
	pass

# Handle several cases that disables update feature completely (or partially).
SPLUpdateErrorNone = 0
SPLUpdateErrorGeneric = 1
SPLUpdateErrorSecureMode = 2
SPLUpdateErrorTryBuild = 3
SPLUpdateErrorSource = 4
SPLUpdateErrorAppx = 5
SPLUpdateErrorAddonsManagerUpdate = 6
SPLUpdateErrorNoNetConnection = 7

# These conditions are set when NVDA starts and cannot be changed at runtime, hence major errors.
# This means no update channel selection, no retrys, etc.
SPLUpdateMajorErrors = (SPLUpdateErrorSecureMode, SPLUpdateErrorTryBuild, SPLUpdateErrorSource, SPLUpdateErrorAppx, SPLUpdateErrorAddonsManagerUpdate)

updateErrorMessages={
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorGeneric: _("An error occured while checking for add-on update. Please check NVDA log for details."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorSecureMode: _("NVDA is in secure mode. Please restart with secure mode disabled before checking for add-on updates."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorTryBuild: _("This is a try build of StationPlaylist Studio add-on. Please install the latest stable release to receive updates again."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorSource: _("Update checking not supported while running NVDA from source. Please run this add-on from an installed or a portable version of NVDA."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorAppx: _("This is a Windows Store version of NVDA. Add-on updating is supported on desktop version of NVDA."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorAddonsManagerUpdate: _("Cannot update add-on directly. Please check for add-on updates by going to add-ons manager."),
	# Translators: one of the error messages when trying to update the add-on.
	SPLUpdateErrorNoNetConnection: _("No internet connection. Please connect to the internet before checking for add-on update."),
}

# Check to really make sure add-on updating is supported.
# Contrary to its name, 0 means yes, otherwise no.
# For most cases, it'll return no errors except for scenarios outlined below.
# The generic error (1) is meant to catch all errors not listed here, and for now, not used.
def isAddonUpdatingSupported():
	if globalVars.appArgs.secure:
		return SPLUpdateErrorSecureMode
	if _customTryBuild:
		return SPLUpdateErrorTryBuild
	import versionInfo
	if not versionInfo.updateVersionType:
		return SPLUpdateErrorSource
	# NVDA 2018.1 and later.
	import config
	if config.isAppX:
		return SPLUpdateErrorAppx
	# Provided that NVDA issue 3208 is implemented.
	if hasattr(addonHandler, "checkForAddonUpdate"):
		return SPLUpdateErrorAddonsManagerUpdate
	return SPLUpdateErrorNone

def canUpdate():
	return isAddonUpdatingSupported() == SPLUpdateErrorNone

def updateInit():
	autoUpdateCheck()

def autoUpdateCheck():
	# #48 (18.02/15.13-LTS): no, not when secure mode flag is on.
	if globalVars.appArgs.secure: return
	# LTS: Launch updater if channel change is detected.
	# #53 (18.04): also if last update check time is way in the past.
	# Use a background thread for this as urllib blocks.
	# 17.08: if update interval is zero (check whenever Studio starts), treat it as update now.
	# #36: only the first part will be used later due to the fact that update checker will check current time versus next check time.
	# #53 (18.04): vastly changed.
	from . import splconfig
	global _updateNow
	currentTime = time.time()
	updateInterval = splconfig.SPLConfig["Update"]["UpdateInterval"]
	if not _updateNow: _updateNow = (currentTime-SPLAddonCheck >= _updateInterval * updateInterval) or updateInterval == 0
	if _updateNow:
		t = threading.Thread(target=updateChecker, kwargs={"auto": True, "confUpdateInterval": updateInterval}) # No repeat here.
		t.daemon = True
		t.start()
		_updateNow = False
	else: startAutoUpdateCheck(interval=divmod((SPLAddonCheck-currentTime), _updateInterval)[-1])

def startAutoUpdateCheck(interval=None):
	if globalVars.appArgs.secure: return
	from . import splconfig
	if not splconfig.SPLConfig["Update"]["UpdateInterval"]: return
	global _SPLUpdateT
	if _SPLUpdateT is not None:
		wx.CallAfter(_SPLUpdateT.Stop)
	_SPLUpdateT = wx.PyTimer(autoUpdateCheck)
	wx.CallAfter(_SPLUpdateT.Start, (_updateInterval if interval is None else interval) * 1000, True)
	#updateChecker(auto=True, continuous=SPLConfig["Update"]["AutoUpdateCheck"], confUpdateInterval=SPLConfig["Update"]["UpdateInterval"])

def checkForAddonUpdate():
	updateURL = SPLUpdateURL if SPLUpdateChannel not in channels else channels[SPLUpdateChannel]
	# Skip ahead:
	#import versionInfo
	#if SPLUpdateChannel == "try" and (versionInfo.version_year, versionInfo.version_major) >= (2017, 4):
		#updateURL = "http://www.josephsl.net/files/nvdaaddons/getupdate.php?file=spl-tryahead"
	# Skip ahead end
	try:
		# Look up the channel if different from the default.
		res = urlopen(updateURL)
		res.close()
	except IOError as e:
		# NVDA Core 2015.1 and later.
		if isinstance(e.strerror, ssl.SSLError) and e.strerror.reason == "CERTIFICATE_VERIFY_FAILED":
			_updateWindowsRootCertificates()
			res = urlopen(updateURL)
		else:
			raise
	if res.code != 200:
		raise RuntimeError("Checking for update failed with code %d" % res.code)
	# Build emulated add-on update dictionary if there is indeed a new version.
	# The add-on version is of the form "x.y.z". The "-dev" suffix indicates development release.
	# Anything after "-dev" indicates a try or a custom build.
	# LTS: Support upgrading between LTS releases.
	# 7.0: Just worry about version label differences (suggested by Jamie Teh from NV Access).
	# 17.04: Version is of the form year.month.revision, and regular expression will be employed (looks cleaner).
	import re
	version = re.search("stationPlaylist-(?P<version>.*).nvda-addon", res.url).groupdict()["version"]
	if version != SPLAddonVersion:
		return {"curVersion": SPLAddonVersion, "newVersion": version, "path": res.url}
	return None

_progressDialog = None
# The update check routine.
# Auto is whether to respond with UI (manual check only), continuous takes in auto update check variable for restarting the timer.
# ConfUpdateInterval comes from add-on config dictionary.
def updateChecker(auto=False, continuous=False, confUpdateInterval=1):
	if _pendingChannelChange:
		wx.CallAfter(gui.messageBox, _("Did you recently tell SPL add-on to use a different update channel? If so, please restart NVDA before checking for add-on updates."), _("Update channel changed"), wx.ICON_ERROR)
		return
	global _SPLUpdateT, SPLAddonCheck, _retryAfterFailure, _progressDialog, _updateNow
	if _updateNow: _updateNow = False
	from logHandler import log
	# Regardless of whether it is an auto check, update the check time.
	# However, this shouldnt' be done if this is a retry after a failed attempt.
	# #36 (17.08): in order to avoid integer overflows, update the check time if it is past the update interval in days.
	# Also, no need to continue if interval did not pass.
	# #53 (18.05): legacy code now, as auto update check starter will take care of this and because we'll come here every day.
	currentTime = time.time()
	shouldCheckForUpdate = currentTime-SPLAddonCheck >= (confUpdateInterval*_updateInterval)
	#if auto and not shouldCheckForUpdate: return
	if not _retryAfterFailure and shouldCheckForUpdate: SPLAddonCheck = currentTime
	# Auto disables UI portion of this function if no updates are pending.
	try:
		info = checkForAddonUpdate()
	except:
		log.error("Error checking for update", exc_info=True)
		_retryAfterFailure = True
		if not auto:
			wx.CallAfter(_progressDialog.done)
			_progressDialog = None
			wx.CallAfter(gui.messageBox, updateErrorMessages[SPLUpdateErrorGeneric], _("Studio add-on update"), wx.ICON_ERROR)
		if continuous: _SPLUpdateT.Start(600000, True)
		return
	if _retryAfterFailure:
		_retryAfterFailure = False
		# Now is the time to update the check time if this is a retry.
		SPLAddonCheck = currentTime
	if not auto:
		wx.CallAfter(_progressDialog.done)
		_progressDialog = None
	# Translators: Title of the add-on update check dialog.
	dialogTitle = _("Studio add-on update")
	if info is None:
		if auto:
			startAutoUpdateCheck()
			return # No need to interact with the user.
		# Translators: Presented when no add-on update is available.
		wx.CallAfter(gui.messageBox, _("No add-on update available."), dialogTitle)
	else:
		# Translators: Text shown if an add-on update is available.
		checkMessage = _("Studio add-on {newVersion} is available. Would you like to update?").format(newVersion = info["newVersion"])
		wx.CallAfter(getUpdateResponse, checkMessage, dialogTitle, info["path"])
		if auto: startAutoUpdateCheck()

def getUpdateResponse(message, caption, updateURL):
	if gui.messageBox(message, caption, wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
		SPLUpdateDownloader([updateURL]).start()

# Update downloader (credit: NV Access)
# Customized for SPL add-on.
class SPLUpdateDownloader(updateCheck.UpdateDownloader):
	"""Overrides NVDA Core's downloader.)
	No hash checking for now, and URL's and temp file paths are different.
	"""

	def __init__(self, urls, fileHash=None):
		"""Constructor.
		@param urls: URLs to try for the update file.
		@type urls: list of str
		@param fileHash: The SHA-1 hash of the file as a hex string.
		@type fileHash: basestring
		"""
		# In recent NVDA next snapshots (February 2018), update downloader was changed to take in update info dictionary.
		try:
			super(SPLUpdateDownloader, self).__init__(urls, fileHash)
		except:
			pass
		self.urls = urls
		self.destPath = tempfile.mktemp(prefix="stationPlaylist_update-", suffix=".nvda-addon")
		self.fileHash = fileHash

	def start(self):
		"""Start the download.
		"""
		self._shouldCancel = False
		# Use a timer because timers aren't re-entrant.
		self._guiExecTimer = wx.PyTimer(self._guiExecNotify)
		gui.mainFrame.prePopup()
		# Translators: The title of the dialog displayed while downloading add-on update.
		self._progressDialog = wx.ProgressDialog(_("Downloading Add-on Update"),
			# Translators: The progress message indicating that a connection is being established.
			_("Connecting"),
			# PD_AUTO_HIDE is required because ProgressDialog.Update blocks at 100%
			# and waits for the user to press the Close button.
			style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME | wx.PD_AUTO_HIDE,
			parent=gui.mainFrame)
		self._progressDialog.Raise()
		t = threading.Thread(target=self._bg)
		t.daemon = True
		t.start()

	def _error(self):
		self._stopped()
		gui.messageBox(
			# Translators: A message indicating that an error occurred while downloading an update to NVDA.
			_("Error downloading add-on update."),
			_("Error"),
			wx.OK | wx.ICON_ERROR)

	def _downloadSuccess(self):
		self._stopped()
		# Emulate add-on update (don't prompt to install).
		from gui import addonGui
		closeAfter = addonGui.AddonsDialog._instance is None
		try:
			try:
				bundle=addonHandler.AddonBundle(self.destPath.decode("mbcs"))
			except:
				log.error("Error opening addon bundle from %s"%self.destPath,exc_info=True)
				# Translators: The message displayed when an error occurs when opening an add-on package for adding. 
				gui.messageBox(_("Failed to open add-on package file at %s - missing file or invalid file format")%self.destPath,
					# Translators: The title of a dialog presented when an error occurs.
					_("Error"),
					wx.OK | wx.ICON_ERROR)
				return
			bundleName=bundle.manifest['name']
			for addon in addonHandler.getAvailableAddons():
				if not addon.isPendingRemove and bundleName==addon.manifest['name']:
					addon.requestRemove()
					break
			progressDialog = gui.IndeterminateProgressDialog(gui.mainFrame,
			# Translators: The title of the dialog presented while an Addon is being updated.
			_("Updating Add-on"),
			# Translators: The message displayed while an addon is being updated.
			_("Please wait while the add-on is being updated."))
			try:
				gui.ExecAndPump(addonHandler.installAddonBundle,bundle)
			except:
				log.error("Error installing  addon bundle from %s"%self.destPath,exc_info=True)
				if not closeAfter: addonGui.AddonsDialog(gui.mainFrame).refreshAddonsList()
				progressDialog.done()
				del progressDialog
				# Translators: The message displayed when an error occurs when installing an add-on package.
				gui.messageBox(_("Failed to update add-on  from %s")%self.destPath,
					# Translators: The title of a dialog presented when an error occurs.
					_("Error"),
					wx.OK | wx.ICON_ERROR)
				return
			else:
				if not closeAfter: addonGui.AddonsDialog(gui.mainFrame).refreshAddonsList(activeIndex=-1)
				progressDialog.done()
				del progressDialog
		finally:
			try:
				os.remove(self.destPath)
			except OSError:
				pass
			if closeAfter:
				wx.CallLater(1, addonGui.AddonsDialog(gui.mainFrame).Close)


# Borrowed from NVDA Core (the only difference is the URL and where structures are coming from).
def _updateWindowsRootCertificates():
	crypt = ctypes.windll.crypt32
	# Get the server certificate.
	sslCont = ssl._create_unverified_context()
	u = urlopen("https://addons.nvda-project.org", context=sslCont)
	cert = u.fp._sock.getpeercert(True)
	u.close()
	# Convert to a form usable by Windows.
	certCont = crypt.CertCreateCertificateContext(
		0x00000001, # X509_ASN_ENCODING
		cert,
		len(cert))
	# Ask Windows to build a certificate chain, thus triggering a root certificate update.
	chainCont = ctypes.c_void_p()
	crypt.CertGetCertificateChain(None, certCont, None, None,
		ctypes.byref(updateCheck.CERT_CHAIN_PARA(cbSize=ctypes.sizeof(updateCheck.CERT_CHAIN_PARA),
			RequestedUsage=updateCheck.CERT_USAGE_MATCH())),
		0, None,
		ctypes.byref(chainCont))
	crypt.CertFreeCertificateChain(chainCont)
	crypt.CertFreeCertificateContext(certCont)
