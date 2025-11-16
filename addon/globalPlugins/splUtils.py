# StationPlaylist Utilities
# Copyright 2013-2025 Joseph Lee, released under GPL.
# Adds a few utility features such as switching focus to the SPL Studio window and some global scripts.

import sys
import globalPluginHandler
import api
import ui
import scriptHandler
import globalVars
import appModuleHandler
from appModules.splcommon import splbase, splconsts, splconfig
import tones
import windowUtils
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from winUser import OBJID_CLIENT, getWindowText
import addonHandler
# From NVDA 2026.1 onwards, winBindings package should be used to look for Windows API dll's.
try:
	from winBindings.user32 import dll as user32
except ModuleNotFoundError:
	from winUser import user32

addonHandler.initTranslation()


# SPL Studio uses WM messages to send and receive data, similar to Winamp.
# See NVDA source/appModules/winamp.py for more information.

# Various SPL IPC tags.
SPLPlay = 12
SPLStop = 13
SPLPause = 15
SPLAutomate = 16
SPLMic = 17
SPLLineIn = 18
SPLCartPlayer = 19
SPLLibraryScanCount = 32
SPLListenerCount = 35
SPLStatusInfo = 39
SPLTrackPlaybackStatus = 104
SPLCurTrackPlaybackTime = 105

# Translators: the text for SPL Controller help.
SPLConHelp = _("""After entering SPL Controller, press:
A: Turn automation on.
Shift+A: Turn automation off.
M: Turn microphone on.
Shift+M: Turn microphone off.
N: Turn microphone on without fade.
L: Turn line in on.
Shift+L: Turn line in off.
P: Play.
U: Pause.
S: Stop with fade.
T: Instant stop.
C: Announce name and duration of the currently playing track.
Shift+C: Announce name and duration of the upcoming track.
E: Announce connected encoders if any.
I: Announce listener count.
Q: Announce Studio status information.
R: Remaining time for the playing track.
Shift+R: Library scan progress.
Function keys and number row keys with or without Shift, Alt, and Control keys: Play carts.""")


# Announce connected encoders if any.
# Originally part of the global plugin, moved to SPl Engine app module, then returned to the global plugin.
def announceEncoderConnectionStatus() -> None:
	# For SAM encoders, descend into encoder window after locating the foreground window.
	# For others, look for a specific SysListView32 control.
	desktopHwnd = api.getDesktopObject().windowHandle
	try:
		samEncoderWindow = windowUtils.findDescendantWindow(desktopHwnd, className="TfoSCEncoders")
	except LookupError:
		samEncoderWindow = 0
	if samEncoderWindow:
		try:
			samEncoderWindow = windowUtils.findDescendantWindow(samEncoderWindow, className="TListView")
		except LookupError:
			samEncoderWindow = 0
	try:
		sysListView32EncoderWindow = windowUtils.findDescendantWindow(
			desktopHwnd, className="SysListView32", controlID=1004
		)
	except LookupError:
		sysListView32EncoderWindow = 0
	if not samEncoderWindow and not sysListView32EncoderWindow:
		# Translators: presented when no streaming encoders were found when trying to obtain connection status.
		ui.message(_("No encoders found"))
	elif samEncoderWindow and sysListView32EncoderWindow:
		# Translators: presented when more than one encoder type is active
		# when trying to obtain encoder connection status.
		ui.message(_("Only one encoder type can be active at once"))
	else:
		encoderWindow = max(samEncoderWindow, sysListView32EncoderWindow)
		encoderList = getNVDAObjectFromEvent(encoderWindow, OBJID_CLIENT, 0)
		connectedEncoders = [
			encoder.encoderId for encoder in encoderList.children
			# encoderId is an attribute defined in encoder class (see appModules.splengine.encoders.Encoder).
			if hasattr(encoder, "encoderId") and encoder.connected
		]
		if len(connectedEncoders) > 0:
			# Translators: presented when at least one encoder is connected.
			ui.message(_("Connected encoders: {encodersConnected}").format(
				encodersConnected=", ".join(connectedEncoders)
			))
		else:
			# Translators: presented when no encoders are connected.
			ui.message(_("No encoders connected"))

# Call Studio app module methods upon request.
# Func must be a string to allow getattr to work and return nothing.
# Applicable to local Studio (not Remote Studio).
def studioAppModuleCommand(func: str, *args, **kwargs) -> None:
	studioAppMod = getNVDAObjectFromEvent(
		user32.FindWindowW("TStudioForm", None), OBJID_CLIENT, 0
	).appModule
	getattr(studioAppMod, func)(*args, **kwargs)

# Process add-on specific command-line switches.
# --spl-configinmemory: load add-on settings from memory as if the add-on is run for the first time.
# --spl-normalprofileonly: load only the default broadcast profile.
# --spl-apidebug: record Studio API specific debug messages (requires debug log to be enabled).
def processArgs(cliArgument: str) -> bool:
	splAddonCLIParems = ("--spl-configinmemory", "--spl-normalprofileonly", "--spl-apidebug")
	if cliArgument in splAddonCLIParems:
		# Remove the command-line switch from sys.argv so the add-on can
		# function normally unless restarted with these switches added.
		# This should not be part of global plugin terminate method because sys.argv is kept
		# when NVDA is restarted from Exit NVDA dialog.
		sys.argv.remove(cliArgument)
		return True
	return False


# Security: disable the global plugin altogether in secure mode.
def disableInSecureMode(cls):
	return globalPluginHandler.GlobalPlugin if globalVars.appArgs.secure else cls


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: Script category for StationPlaylist commands in input gestures dialog.
	scriptCategory = _("StationPlaylist")

	def __init__(self):
		super().__init__()
		# Tell NVDA that the add-on accepts additional command-line switches.
		addonHandler.isCLIParamKnown.register(processArgs)
		# SPL Streamer provides a streaming UI on top of SPL Engine components, thus treat it as an alias.
		appModuleHandler.registerExecutableWithAppModule("splstreamer", "splengine")

	# Global layer environment (see Studio app module for more information).

	# Control Studio from anywhere.
	SPLController = False

	def getScript(self, gesture):
		if not self.SPLController:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			script = self.script_error
		return splbase.finally_(script, self.script_finish)

	@scriptHandler.script(speakOnDemand=True)
	def script_finish(self):
		self.SPLController = False
		self.activeStudioComponent = None
		self.clearGestureBindings()

	def script_error(self, gesture):
		tones.beep(120, 100)

	# Switch focus to SPL Studio window from anywhere.
	@scriptHandler.script(
		# Translators: Input help mode message for a command to switch to StationPlaylist Studio from any program.
		description=_("Moves to SPL Studio window from other programs.")
	)
	def script_focusToSPLWindow(self, gesture):
		# Don't do anything if we're already focus on SPL Studio.
		if "splstudio" in api.getForegroundObject().appModule.appName:
			return
		if not splbase.studioIsRunning(justChecking=True):
			ui.message(_("SPL Studio is not running."))
		else:
			splbase.focusToSPLWindow()

	# Direct global plugin scripts to use the correct SPL component/scope.
	# Priority: local Studio -> Remote Studio.
	# Returns the configured scope and the first active component.
	def actualSPLConScope(self) -> list[str | None]:
		# Forcefully open config database if not done so.
		splConScope = None
		studioWindow = getNVDAObjectFromEvent(
			user32.FindWindowW("TStudioForm", None), OBJID_CLIENT, 0
		)
		if studioWindow:
			splConScope = splconfig.SPLConfig["Advanced"]["SPLConScope"]
		# Locate any active Studio components.
		activeStudioComponents = [
			component.lower() for component in ("SPLStudio", "RemoteStudio")
			if user32.FindWindowW(component, None)
		]
		if not activeStudioComponents:
			return [splConScope, None]
		activeStudioComponent = None
		if splConScope and splConScope in activeStudioComponents:  # Scope limited to Local or Remote Studio
			activeStudioComponent = splConScope
		elif not splConScope:  # Either local or Remote Studio
			activeStudioComponent = activeStudioComponents[0]
		return [splConScope, activeStudioComponent]

	# Record the active Studio component for use by Studio API clalers.
	activeStudioComponent: str | None = None

	# The SPL Controller:
	# This layer set allows the user to control various aspects of SPL local and Remote Studio from anywhere.
	@scriptHandler.script(
		# Translators: Input help mode message for a layer command in StationPlaylist add-on.
		description=_("SPl Controller layer command. See add-on guide for available commands."),
		speakOnDemand=True,
	)
	def script_SPLControllerPrefix(self, gesture):
		# Error checks:
		# 1. If SPL Studio is not running, print an error message.
		# 2. If we're already  in Studio, ask Studio app module if SPL Assistant can be invoked with this command.
		foregroundAppMod = api.getForegroundObject().appModule
		if hasattr(foregroundAppMod, "SPLConPassthrough"):
			if not foregroundAppMod.SPLConPassthrough():
				# Translators: Presented when NVDA cannot enter SPL Controller layer since SPL Studio is focused.
				ui.message(
					_(
						"You are already in SPL Studio window. For status commands, use SPL Assistant commands."
					)
				)
				self.script_finish()
				return
			else:
				foregroundAppMod.script_SPLAssistantToggle(gesture)
				return
		# Locate SPL Controller scope and active Studio component if any.
		splConScope, activeStudioComponent = self.actualSPLConScope()
		if not activeStudioComponent:
			if splConScope == "remotestudio":
				# Translators: Presented when StationPlaylist Remote Studio is not running.
				ui.message(_("SPL Remote Studio is not running."))
			else:
				# Translators: Presented when StationPlaylist Studio is not running.
				ui.message(_("SPL Studio is not running."))
			self.script_finish()
			return
		# No errors, so continue.
		if not self.SPLController:
			self.bindGestures(self.__SPLControllerGestures)
			self.activeStudioComponent = activeStudioComponent
			# Also bind cart keys.
			# Exclude number row if Studio Standard is running.
			# #147: truncate to function key carts if Studio Standard is in use
			# as cart keys are now a single list.
			# Local Studio only
			if self.activeStudioComponent == "splstudio":
				if not getWindowText(
					user32.FindWindowW("TStudioForm", None)
				).startswith("StationPlaylist Studio Standard"):
					lastCart = 24
				else:
					lastCart = 12
				for cart in splconsts.cartKeys[:lastCart]:
					self.bindGesture(f"kb:{cart}", "cartsWithoutBorders")
					self.bindGesture(f"kb:shift+{cart}", "cartsWithoutBorders")
					self.bindGesture(f"kb:control+{cart}", "cartsWithoutBorders")
					self.bindGesture(f"kb:alt+{cart}", "cartsWithoutBorders")
			self.SPLController = True
			if self.activeStudioComponent == "remotestudio":
				# Translators: The name of a layer command set for StationPlaylist add-on.
				# Hint: it is better to translate it as "SPL Control Panel."
				ui.message(_("SPL Remote Controller"))
			else:
				# Translators: The name of a layer command set for StationPlaylist add-on.
				# Hint: it is better to translate it as "SPL Control Panel."
				ui.message(_("SPL Controller"))
		else:
			self.script_error(gesture)
			self.script_finish()

	# The layer commands themselves. Calls user32.SendMessage method (via splbase.studioAPI) for each script.

	def script_automateOn(self, gesture):
		splbase.studioAPI(1, SPLAutomate)
		self.script_finish()

	def script_automateOff(self, gesture):
		splbase.studioAPI(0, SPLAutomate)
		self.script_finish()

	def script_micOn(self, gesture):
		splbase.studioAPI(1, SPLMic)
		self.script_finish()

	def script_micOff(self, gesture):
		splbase.studioAPI(0, SPLMic)
		self.script_finish()

	def script_micNoFade(self, gesture):
		splbase.studioAPI(2, SPLMic)
		self.script_finish()

	def script_lineInOn(self, gesture):
		splbase.studioAPI(1, SPLLineIn)
		self.script_finish()

	def script_lineInOff(self, gesture):
		splbase.studioAPI(0, SPLLineIn)
		self.script_finish()

	def script_stopFade(self, gesture):
		splbase.studioAPI(0, SPLStop)
		self.script_finish()

	def script_stopInstant(self, gesture):
		splbase.studioAPI(1, SPLStop)
		self.script_finish()

	def script_play(self, gesture):
		splbase.studioAPI(0, SPLPlay)
		self.script_finish()

	def script_pause(self, gesture):
		playingNow = splbase.studioAPI(0, SPLTrackPlaybackStatus)
		if not playingNow:
			# Translators: Presented when no track is playing in StationPlaylist Studio.
			ui.message(_("There is no track playing. Try pausing while a track is playing."))
		elif playingNow == 3:
			splbase.studioAPI(0, SPLPause)
		else:
			splbase.studioAPI(1, SPLPause)
		self.script_finish()

	def script_libraryScanProgress(self, gesture):
		scanned = splbase.studioAPI(1, SPLLibraryScanCount)
		if scanned is not None and scanned >= 0:
			# Translators: Announces number of items in the Studio's track library (example: 1000 items scanned).
			ui.message(_("Scan in progress with {itemCount} items scanned").format(itemCount=scanned))
		else:
			# Translators: Announces number of items in the Studio's track library (example: 1000 items scanned).
			ui.message(_("Scan complete with {itemCount} items scanned").format(
				itemCount=splbase.studioAPI(0, SPLLibraryScanCount)
			))
		self.script_finish()

	def script_listenerCount(self, gesture):
		ui.message(
			# Translators: Announces number of stream listeners.
			_("Listener count: {listenerCount}").format(
				listenerCount=splbase.studioAPI(0, SPLListenerCount)
			)
		)
		self.script_finish()

	def script_remainingTime(self, gesture):
		remainingTime = splbase.studioAPI(3, SPLCurTrackPlaybackTime)
		if remainingTime is not None and remainingTime < 0:
			# Translators: Presented when no track is playing in StationPlaylist Studio.
			ui.message(_("There is no track playing."))
		else:
			studioAppModuleCommand("announceTime", remainingTime, offset=1, includeHours=True)
		self.script_finish()

	@scriptHandler.script(
		# Translators: Input help message for a SPL Controller command.
		description=_("Announces stream encoder status from other programs"),
		speakOnDemand=True,
	)
	def script_encoderStatus(self, gesture):
		# Go through below procedure, as custom commands can be assigned for this script.
		if not splbase.studioIsRunning(justChecking=True):
			ui.message(_("SPL Studio is not running."))
			self.script_finish()
			return
		try:
			announceEncoderConnectionStatus()
		except Exception:
			# Translators: presented if encoder connection status cannot be obtained.
			ui.message(_("Cannot obtain encoder connection status"))
		self.script_finish()

	@scriptHandler.script(
		# Translators: Input help message for a SPL Controller command.
		description=_("Announces Studio status such as track playback status from other programs"),
		speakOnDemand=True,
	)
	def script_statusInfo(self, gesture):
		# Go through below procedure, as custom commands can be assigned for this script.
		if not splbase.studioIsRunning(justChecking=True):
			ui.message(_("SPL Studio is not running."))
			self.script_finish()
			return
		statusInfo = [
			splconsts.studioStatusMessages[status][splbase.studioAPI(status, SPLStatusInfo)]
			for status in range(5)  # Playback/automation/mic/line-in/record to file
		]
		# Special handling for cart edit/insert.
		cartEdit = splbase.studioAPI(5, SPLStatusInfo)
		cartInsert = splbase.studioAPI(6, SPLStatusInfo)
		if cartEdit:
			statusInfo.append("Cart Edit On")
		elif not cartEdit and cartInsert:
			statusInfo.append("Cart Insert On")
		else:
			statusInfo.append("Cart Edit Off")
		ui.message("; ".join(statusInfo))
		self.script_finish()

	def script_currentTrackTitle(self, gesture):
		studioAppModuleCommand("script_sayCurrentTrackTitle", None)
		self.script_finish()

	def script_nextTrackTitle(self, gesture):
		studioAppModuleCommand("script_sayNextTrackTitle", None)
		self.script_finish()

	def script_cartsWithoutBorders(self, gesture):
		try:
			modifier, cart = gesture.displayName.split("+")
		except ValueError:
			modifier, cart = None, gesture.displayName
		# Pull in modifier values from the following list.
		# Multiply modifiers by 24 (1 (None), 25 (Shift), 49 (Control), 73 (Alt)).
		modifier = (None, "shift", "ctrl", "alt").index(modifier) * 24
		# Add 1 to cart index to comply with Studio API.
		cart = splconsts.cartKeys.index(cart) + 1
		splbase.studioAPI(cart + modifier, SPLCartPlayer)
		self.script_finish()

	def script_conHelp(self, gesture):
		# Translators: The title for SPL Controller help screen.
		ui.browseableMessage(SPLConHelp, title=_("SPL Controller help"), closeButton=True)
		self.script_finish()

	__SPLControllerGestures = {
		"kb:p": "play",
		"kb:a": "automateOn",
		"kb:shift+a": "automateOff",
		"kb:m": "micOn",
		"kb:shift+m": "micOff",
		"kb:n": "micNoFade",
		"kb:l": "lineInOn",
		"kb:shift+l": "lineInOff",
		"kb:shift+r": "libraryScanProgress",
		"kb:s": "stopFade",
		"kb:t": "stopInstant",
		"kb:u": "pause",
		"kb:r": "remainingTime",
		"kb:e": "encoderStatus",
		"kb:i": "listenerCount",
		"kb:q": "statusInfo",
		"kb:c": "currentTrackTitle",
		"kb:shift+c": "nextTrackTitle",
		"kb:h": "conHelp",
	}
