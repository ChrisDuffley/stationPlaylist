# SPL Studio Miscellaneous User Interfaces and internal services
# An app module and global plugin package for NVDA
# Copyright 2015-2026 Joseph Lee, released under GPL.
# Miscellaneous functions and user interfaces
# Split from config module in 2015.

import os
import threading
import api
import nvwave
import queueHandler
import speech
import ui
import addonHandler
from ..splcommon import splbase, splconfig

addonHandler.initTranslation()

# Various SPL IPC tags.
SPLMetadataStreaming = 36

# Metadata and encoders management, including connection, announcement and so on.


# Gather streaming flags into a list.
# Raise runtime error if list is nothing
# (thankfully the splbase's StudioAPI will return None if Studio handle is not found).
def metadataList() -> list[int | None]:
	metadata = [splbase.studioAPI(pos, SPLMetadataStreaming) for pos in range(5)]
	# Make sure None is not included in metadata list, otherwise it results in no metadata data for streams.
	# This could happen if Studio dies while retrieving metadata list with some items returning None.
	if None in metadata:
		raise RuntimeError("Studio handle not found, no metadata list to return")
	return metadata


# Metadata server connector, to be utilized from many modules.
# Servers refer to a list of connection flags to pass to Studio API,
# and if not present, will be pulled from add-on settings.
def metadataConnector(servers: list[bool] | None = None) -> None:
	if servers is None:
		servers = splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"]
	for url in range(5):
		dataLo = 0x00010000 if servers[url] else 0xFFFF0000
		splbase.studioAPI(dataLo | url, SPLMetadataStreaming)


# Metadata status formatter (say something if Studio handle is not found).
def metadataStatus() -> str:
	try:
		streams = metadataList()
	except RuntimeError:
		# Translators: presented when metadata streaming status cannot be obtained.
		return _("Cannot obtain metadata streaming status information")
	# DSP is treated specially.
	# Remove it from the streams list early so only URL's can be checked later.
	dsp = streams.pop(0)
	# Unless all URL's are streaming, use of any function is faster as it returns True
	# whenever anything inside streams list is set to 1.
	if not any(streams):
		if not dsp:
			# Translators: Status message for metadata streaming.
			return _("No metadata streaming URL's defined")
		else:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for DSP encoder")
	# For others, a simple enumeration will do.
	streamCount = [str(pos) for pos, stream in enumerate(streams, start=1) if stream]
	if len(streamCount) == 1:
		if dsp:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for DSP encoder and URL {URL}").format(URL=streamCount[0])
		else:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for URL {URL}").format(URL=streamCount[0])
	else:
		# Prepare URL list string early.
		urls = ", ".join(streamCount)
		if dsp:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for DSP encoder and URL's {URL}").format(URL=urls)
		else:
			# Translators: Status message for metadata streaming.
			return _("Metadata streaming configured for URL's {URL}").format(URL=urls)


# Handle a case where instant profile switch occurs twice within the switch time-out.
_earlyMetadataAnnouncer: threading.Timer | None = None


# Internal metadata status announcer.
# The idea is to pause for a while and announce the status message and playing the accompanying wave file.
# This is necessary in order to allow extension points to work correctly
# and to not hold up other registered action handlers.
# A special startup flag will be used so other text sequences will not be cut off.
def _metadataAnnouncerInternal(status: str, startup: bool = False) -> None:
	if not startup:
		speech.cancelSpeech()
	queueHandler.queueFunction(queueHandler.eventQueue, ui.message, status)
	nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "SPL_Metadata.wav"))
	# #51: close link to metadata announcer thread when finished.
	global _earlyMetadataAnnouncer
	_earlyMetadataAnnouncer = None


def _earlyMetadataAnnouncerInternal(status: str, startup: bool = False) -> None:
	global _earlyMetadataAnnouncer
	if _earlyMetadataAnnouncer is not None:
		_earlyMetadataAnnouncer.cancel()
		_earlyMetadataAnnouncer = None
	_earlyMetadataAnnouncer = threading.Timer(
		2, _metadataAnnouncerInternal, args=[status], kwargs={"startup": startup}
	)
	_earlyMetadataAnnouncer.start()


# Delay the action handler if Studio handle is not found.
_delayMetadataAction = False


# Announce and connect to metadata streams at Studio startup.
def startupMetadataReminder(startupEvent: threading.Event) -> None:
	global _delayMetadataAction
	if splconfig.SPLConfig["General"]["MetadataReminder"] == "startup" or _delayMetadataAction:
		_delayMetadataAction = False
		# If told to remind and connect, metadata streaming will be enabled at this time
		# (call the metadata connector).
		metadataConnector()
		# #40: call the internal metadata announcer in order to not hold up action handler queue.
		# #82: wait until Studio window shows up (foreground or background) for the first time.
		# #83: if NVDA restarts while Studio is running and foreground window is
		# something other than playlist viewer, the below method won't work at all.
		# Thankfully, NVDA's notion of foreground window depends on a global variable,
		# and if it is not set, this is a restart with Studio running, so just announce it.
		if api.getForegroundObject() is not None:
			startupEvent.wait()
		_earlyMetadataAnnouncerInternal(metadataStatus(), startup=True)


# Connect and/or announce metadata status when broadcast profile switching occurs.
# The config dialog active flag is only invoked when being notified while add-on settings dialog is focused.
# Settings reset flag is used to prevent metadata server connection
# when settings are reloaded from disk or reset to defaults.
def metadata_actionProfileSwitched(configDialogActive: bool = False, settingsReset: bool = False) -> None:
	# Only connect if add-on settings is active in order to avoid wasting thread running time.
	if configDialogActive:
		metadataConnector(servers=splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"])
		return
	global _delayMetadataAction
	# Ordinarily, errors would have been dealt with, but Action.notify will catch errors and log messages.
	# #40: the only possible error is if Studio handle is invalid, which won't be the case,
	# otherwise no point handling this action.
	# #49: no, don't announce this if the app module is told to announce metadata status at startup only.
	if splconfig.SPLConfig["General"]["MetadataReminder"] == "instant":
		# If told to remind and connect, metadata streaming will be enabled at this time.
		# Ask the handle finder to return to this place if Studio isn't ready.
		# This is typically the case when launching Studio
		# and profile switch occurs while demo registration screen is up.
		if not splbase.studioIsRunning(justChecking=True):
			_delayMetadataAction = True
			return
		if not settingsReset:
			metadataConnector()
		# #47: call the internal announcer via wx.CallLater
		# in order to not hold up action handler queue.
		# #51: wx.CallLater isn't enough - there must be ability to cancel it.
		_earlyMetadataAnnouncerInternal(metadataStatus())


# The only job of this action handler is to call profile switch handler above with special flags.
def metadata_actionSettingsReset(factoryDefaults: bool = False) -> None:
	metadata_actionProfileSwitched(settingsReset=True)
