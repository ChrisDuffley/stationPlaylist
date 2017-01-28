# StationPlaylist Studio update checker
# A support module for SPL add-on
# Copyright 2015-2017 Joseph Lee, released under GPL.

# Provides update check facility, basics borrowed from NVDA Core's update checker class.

import os # Essentially, update download is no different than file downloads.
import cPickle
import threading
import tempfile
import hashlib
import ctypes.wintypes
import ssl
import wx
import shellapi
import gui
import wx
import addonHandler
import globalVars
import updateCheck
import config
import winUser

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
SPLUpdateURL = "http://addons.nvda-project.org/files/get.php?file=spl-dev"
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

# Not all update channels are listed. The one not listed here is the default ("stable" for this branch).
channels={
	"stable":"http://addons.nvda-project.org/files/get.php?file=spl",
	#"beta":"http://spl.nvda-kr.org/files/get.php?file=spl-beta",
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
			if SPLUpdateChannel in ("beta", "lts"):
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

def updateQualify(url):
	# The add-on version is of the form "x.y.z". The "-dev" suffix indicates development release.
	# Anything after "-dev" indicates a try or a custom build.
	# LTS: Support upgrading between LTS releases.
	# 7.0: Just worry about version label differences (suggested by Jamie Teh from NV Access).
	# 17.04: Version is of the form year.month.revision, and regular expression will be employed (looks cleaner).
	import re
	version = re.search("stationPlaylist-(?P<version>.*).nvda-addon", url.url).groupdict()["version"]
	return None if version == SPLAddonVersion else version

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
	# Regardless of whether it is an auto check, update the check time.
	# However, this shouldnt' be done if this is a retry after a failed attempt.
	if not _retryAfterFailure: SPLAddonCheck = time.time()
	updateInterval = confUpdateInterval*_updateInterval*1000
	# Should the timer be set again?
	if continuous and not _retryAfterFailure: _SPLUpdateT.Start(updateInterval, True)
	# Auto disables UI portion of this function if no updates are pending.
	# All the information will be stored in the URL object, so just close it once the headers are downloaded.
	updateCandidate = False
	updateURL = SPLUpdateURL if SPLUpdateChannel not in channels else channels[SPLUpdateChannel]
	try:
		import urllib
		# Look up the channel if different from the default.
		url = urllib.urlopen(updateURL)
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
	else: wx.CallAfter(getUpdateResponse, checkMessage, _("Studio add-on update"), updateURL)

def getUpdateResponse(message, caption, updateURL):
	if gui.messageBox(message, caption, wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
		SPLUpdateDownloader([updateURL]).start()

# Update downloader (credit: NV Access)
# Customized for SPL add-on.

#: The download block size in bytes.
DOWNLOAD_BLOCK_SIZE = 8192 # 8 kb

def checkForUpdate(auto=False):
	"""Check for an updated version of NVDA.
	This will block, so it generally shouldn't be called from the main thread.
	@param auto: Whether this is an automatic check for updates.
	@type auto: bool
	@return: Information about the update or C{None} if there is no update.
	@rtype: dict
	@raise RuntimeError: If there is an error checking for an update.
	"""
	params = {
		"autoCheck": auto,
		"version": versionInfo.version,
		"versionType": versionInfo.updateVersionType,
		"osVersion": winVersion.winVersionText,
		"x64": os.environ.get("PROCESSOR_ARCHITEW6432") == "AMD64",
		"language": languageHandler.getLanguage(),
		"installed": config.isInstalledCopy(),
	}
	url = "%s?%s" % (CHECK_URL, urllib.urlencode(params))
	try:
		res = urllib.urlopen(url)
	except IOError as e:
		if isinstance(e.strerror, ssl.SSLError) and e.strerror.reason == "CERTIFICATE_VERIFY_FAILED":
			# #4803: Windows fetches trusted root certificates on demand.
			# Python doesn't trigger this fetch (PythonIssue:20916), so try it ourselves
			_updateWindowsRootCertificates()
			# and then retry the update check.
			res = urllib.urlopen(url)
		else:
			raise
	if res.code != 200:
		raise RuntimeError("Checking for update failed with code %d" % res.code)
	info = {}
	for line in res:
		line = line.rstrip()
		try:
			key, val = line.split(": ", 1)
		except ValueError:
			raise RuntimeError("Error in update check output")
		info[key] = val
	if not info:
		return None
	return info


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
		from gui import addonGui
		wx.CallAfter(addonGui.AddonsDialog.handleRemoteAddonInstall, self.destPath.decode("mbcs"))


# These structs are only complete enough to achieve what we need.
class CERT_USAGE_MATCH(ctypes.Structure):
	_fields_ = (
		("dwType", ctypes.wintypes.DWORD),
		# CERT_ENHKEY_USAGE struct
		("cUsageIdentifier", ctypes.wintypes.DWORD),
		("rgpszUsageIdentifier", ctypes.c_void_p), # LPSTR *
	)

class CERT_CHAIN_PARA(ctypes.Structure):
	_fields_ = (
		("cbSize", ctypes.wintypes.DWORD),
		("RequestedUsage", CERT_USAGE_MATCH),
		("RequestedIssuancePolicy", CERT_USAGE_MATCH),
		("dwUrlRetrievalTimeout", ctypes.wintypes.DWORD),
		("fCheckRevocationFreshnessTime", ctypes.wintypes.BOOL),
		("dwRevocationFreshnessTime", ctypes.wintypes.DWORD),
		("pftCacheResync", ctypes.c_void_p), # LPFILETIME
		("pStrongSignPara", ctypes.c_void_p), # PCCERT_STRONG_SIGN_PARA
		("dwStrongSignFlags", ctypes.wintypes.DWORD),
	)

# Borrowed from NVDA Core (the only difference is the URL).
def _updateWindowsRootCertificates():
	crypt = ctypes.windll.crypt32
	# Get the server certificate.
	sslCont = ssl._create_unverified_context()
	u = urllib.urlopen("https://www.nvaccess.org/nvdaUpdateCheck", context=sslCont)
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
		ctypes.byref(CERT_CHAIN_PARA(cbSize=ctypes.sizeof(CERT_CHAIN_PARA),
			RequestedUsage=CERT_USAGE_MATCH())),
		0, None,
		ctypes.byref(chainCont))
	crypt.CertFreeCertificateChain(chainCont)
	crypt.CertFreeCertificateContext(certCont)
