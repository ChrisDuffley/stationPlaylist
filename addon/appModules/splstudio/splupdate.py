# StationPlaylist Studio update checker
# A support module for SPL add-on
# Copyright 2015-2017 Joseph Lee, released under GPL.

# Provides update check facility, basics borrowed from NVDA Core's update checker class.

import os # Essentially, update download is no different than file downloads.
import cPickle
import threading
import tempfile
import ctypes
import ssl
import gui
import wx
import addonHandler
import globalVars
import updateCheck

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
	"try":"http://www.josephsl.net/files/nvdaaddons/get.php?file=spl-try",
}

# Come forth, update check routines.
def initialize():
	global SPLAddonState, SPLAddonCheck, _updateNow, SPLUpdateChannel
	try:
		SPLAddonState = cPickle.load(file(_updatePickle, "r"))
		SPLAddonCheck = SPLAddonState["PDT"]
		_updateNow = "pendingChannelChange" in SPLAddonState
		if _updateNow: del SPLAddonState["pendingChannelChange"]
		if "UpdateChannel" in SPLAddonState:
			SPLUpdateChannel = SPLAddonState["UpdateChannel"]
			if SPLUpdateChannel in ("beta", "preview", "lts"):
				SPLUpdateChannel = "dev"
	except IOError, KeyError:
		SPLAddonState["PDT"] = 0
		_updateNow = False
		SPLUpdateChannel = "dev"

def terminate():
	global SPLAddonState
	# Store new values if it is absolutely required.
	# Take care of a case where one might be "downgrading" from try builds.
	stateChanged = "UpdateChannel" not in SPLAddonState or (SPLAddonState["PDT"] != SPLAddonCheck or SPLAddonState["UpdateChannel"] != SPLUpdateChannel)
	if stateChanged:
		SPLAddonState["PDT"] = SPLAddonCheck
		SPLAddonState["UpdateChannel"] = SPLUpdateChannel
		if _pendingChannelChange:
			SPLAddonState["pendingChannelChange"] = True
		cPickle.dump(SPLAddonState, file(_updatePickle, "wb"))
	SPLAddonState = None

def checkForAddonUpdate():
	import urllib
	updateURL = SPLUpdateURL if SPLUpdateChannel not in channels else channels[SPLUpdateChannel]
	try:
		# Look up the channel if different from the default.
		res = urllib.urlopen(updateURL)
		res.close()
	except IOError as e:
		# NVDA Core 2015.1 and later.
		if isinstance(e.strerror, ssl.SSLError) and e.strerror.reason == "CERTIFICATE_VERIFY_FAILED":
			_updateWindowsRootCertificates()
			res = urllib.urlopen(updateURL)
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
	import time
	from logHandler import log
	# Regardless of whether it is an auto check, update the check time.
	# However, this shouldnt' be done if this is a retry after a failed attempt.
	if not _retryAfterFailure: SPLAddonCheck = time.time()
	updateInterval = confUpdateInterval*_updateInterval*1000
	# Should the timer be set again?
	if continuous and not _retryAfterFailure: _SPLUpdateT.Start(updateInterval, True)
	# Auto disables UI portion of this function if no updates are pending.
	try:
		info = checkForAddonUpdate()
	except:
		log.debugWarning("Error checking for update", exc_info=True)
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
	if not auto:
		wx.CallAfter(_progressDialog.done)
		_progressDialog = None
	# Translators: Title of the add-on update check dialog.
	dialogTitle = _("Studio add-on update")
	if info is None:
		if auto:
			if continuous: _SPLUpdateT.Start(updateInterval, True)
			return # No need to interact with the user.
		# Translators: Presented when no add-on update is available.
		wx.CallAfter(gui.messageBox, _("No add-on update available."), dialogTitle)
	else:
		# Translators: Text shown if an add-on update is available.
		checkMessage = _("Studio add-on {newVersion} is available. Would you like to update?").format(newVersion = info["newVersion"])
		wx.CallAfter(getUpdateResponse, checkMessage, dialogTitle, info["path"])

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
		super(SPLUpdateDownloader, self).__init__(urls, fileHash)
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
	u = urllib.urlopen("https://addons.nvda-project.org", context=sslCont)
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
