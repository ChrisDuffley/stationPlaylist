# SPL Studio Configuration user interfaces
# An app module and global plugin package for NVDA
# Copyright 2016-2025 Joseph Lee, released under GPL.
# Split from SPL config module in 2016.
# Provides the configuration management UI package for SPL Studio app module.
# For code which provides foundation for code in this module, see splconfig module.

import sys
import threading
import gui
from gui.nvdaControls import CustomCheckListBox
import os
import weakref
import api
import wx
import ui
import globalVars
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from winUser import user32, OBJID_CLIENT
import tones
import addonHandler
from ..splcommon import splactions, splconfig, splbase
from ..skipTranslation import translate

addonHandler.initTranslation()

# Due to syntax/variable name issues, the actual add-on settings class can be found at the end of this module.

# Helper panels/dialogs for add-on settings dialog.


# Broadcast profiles
class BroadcastProfilesDialog(wx.Dialog):
	shouldSuspendConfigProfileTriggers = True

	def __init__(self, parent):
		# Translators: title of a dialog to configure broadcast profiles.
		super().__init__(parent, title=_("SPL Broadcast Profiles"))
		global _configDialogOpened
		_configDialogOpened = True
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		broadcastProfilesHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Profiles list and activate button on the left, management buttons on the right (credit: NV Access).
		profilesListGroupSizer = wx.StaticBoxSizer(wx.StaticBox(self), wx.HORIZONTAL)
		profilesListGroupContents = wx.BoxSizer(wx.HORIZONTAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		# Broadcast profile controls were inspired by Config Profiles dialog in NVDA Core.
		self.profileNames = list(splconfig.SPLConfig.profileNames)
		self.profileNames[0] = splconfig.defaultProfileName
		self.activeProfile = splconfig.SPLConfig.activeProfile
		self.switchProfile = splconfig.SPLConfig.instantSwitch
		changeProfilesSizer = wx.BoxSizer(wx.VERTICAL)
		# Include profile flags such as instant profile string for display purposes.
		self.profiles = wx.ListBox(
			self, choices=[self.getProfileFlags(profile, contained=False) for profile in self.profileNames]
		)
		self.profiles.Bind(wx.EVT_LISTBOX, self.onProfileSelection)
		self.profiles.SetSelection(self.profileNames.index(self.activeProfile))
		changeProfilesSizer.Add(self.profiles, proportion=1)
		changeProfilesSizer.AddSpacer(gui.guiHelper.SPACE_BETWEEN_BUTTONS_VERTICAL)

		# Borrowed directly from NVDA Core (credit: NV Access)
		# This allows Enter key to be pressed to activate the selected profile.
		# Translators: label for a button to activate the selected broadcast profile.
		self.changeStateButton = wx.Button(self, label=_("Activate"))
		self.changeStateButton.Bind(wx.EVT_BUTTON, self.onChangeState)
		# The selected profile is already active, so no need to present this button in tab order.
		self.changeStateButton.Disable()
		self.AffirmativeId = self.changeStateButton.Id
		self.changeStateButton.SetDefault()
		changeProfilesSizer.Add(self.changeStateButton)
		profilesListGroupContents.Add(changeProfilesSizer, flag=wx.EXPAND)
		profilesListGroupContents.AddSpacer(gui.guiHelper.SPACE_BETWEEN_ASSOCIATED_CONTROL_HORIZONTAL)

		# Profile controls code credit: NV Access (except copy button).
		# Most control labels come from NVDA Core.
		buttonHelper = gui.guiHelper.ButtonHelper(wx.VERTICAL)
		newButton = buttonHelper.addButton(self, label=translate("&New"))
		newButton.Bind(wx.EVT_BUTTON, self.onNew)
		# Translators: The label of a button to copy a broadcast profile.
		copyButton = buttonHelper.addButton(self, label=_("Cop&y"))
		copyButton.Bind(wx.EVT_BUTTON, self.onCopy)
		self.renameButton = buttonHelper.addButton(self, label=translate("&Rename"))
		self.renameButton.Bind(wx.EVT_BUTTON, self.onRename)
		self.deleteButton = buttonHelper.addButton(self, label=translate("&Delete"))
		self.deleteButton.Bind(wx.EVT_BUTTON, self.onDelete)
		self.triggerButton = buttonHelper.addButton(self, label=translate("&Triggers..."))
		self.triggerButton.Bind(wx.EVT_BUTTON, self.onTriggers)
		if globalVars.appArgs.secure:
			newButton.Disable()
			copyButton.Disable()
		if self.profiles.GetSelection() == 0 or globalVars.appArgs.secure:
			self.renameButton.Disable()
			self.deleteButton.Disable()
			self.triggerButton.Disable()
		profilesListGroupContents.Add(buttonHelper.sizer)
		profilesListGroupSizer.Add(
			profilesListGroupContents, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL
		)
		broadcastProfilesHelper.addItem(profilesListGroupSizer)
		# Used as sanity check in case switch profile is renamed or deleted.
		self.switchProfileRenamed = False
		self.switchProfileDeleted = False

		# Close button logic comes from NVDA Core (credit: NV Access)
		broadcastProfilesHelper.addDialogDismissButtons(wx.CLOSE, separated=True)
		self.Bind(wx.EVT_BUTTON, self.onClose, id=wx.ID_CLOSE)
		self.EscapeId = wx.ID_CLOSE

		mainSizer.Add(broadcastProfilesHelper.sizer, flag=wx.ALL, border=gui.guiHelper.BORDER_FOR_DIALOGS)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.profiles.SetFocus()
		self.CentreOnScreen()

	# Load settings from profiles.
	def onProfileSelection(self, evt):
		# Don't rely on SPLConfig here, as we don't want to interupt the show.
		selection = self.profiles.GetSelection()
		# No need to look at the profile flag.
		selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
		# Play a tone to indicate active profile.
		# Also enable/disable "activate" button.
		if self.activeProfile == selectedProfile:
			tones.beep(512, 40)
			self.changeStateButton.Disable()
		else:
			self.changeStateButton.Enable()
		if selection == 0 or globalVars.appArgs.secure:
			self.renameButton.Disable()
			self.deleteButton.Disable()
			self.triggerButton.Disable()
		else:
			self.renameButton.Enable()
			self.deleteButton.Enable()
			self.triggerButton.Enable()

	# Profile controls.
	# Rename and delete events come from GUI/config profiles dialog from NVDA core.
	def onNew(self, evt):
		self.Disable()
		NewProfileDialog(self).Show()

	def onCopy(self, evt):
		self.Disable()
		NewProfileDialog(self, copy=True).Show()

	def onRename(self, evt):
		oldDisplayName = self.profiles.GetStringSelection()
		state = oldDisplayName.split(" <")
		oldName = state[0]
		index = self.profiles.Selection
		profilePos = self.profileNames.index(oldName)
		with wx.TextEntryDialog(
			# Message comes from NVDA Core.
			self,
			translate("New name:"),
			# Message comes from NVDA Core.
			translate("Rename Profile"),
			value=oldName,
		) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
			newName = api.filterFileName(d.Value)
		if oldName == newName:
			return
		try:
			splconfig.SPLConfig.renameProfile(oldName, newName)
		except RuntimeError:
			gui.messageBox(
				# Message comes from NVDA Core.
				translate("That profile already exists. Please choose a different name."),
				translate("Error"),
				wx.OK | wx.ICON_ERROR,
				self,
			)
			return
		if self.switchProfile == oldName:
			self.switchProfile = newName
			self.switchProfileRenamed = True
		if self.activeProfile == oldName:
			self.activeProfile = newName
		self.profileNames[profilePos] = newName
		self.profiles.SetString(index, " <".join([newName, state[1]]) if len(state) > 1 else newName)
		self.profiles.Selection = index
		self.profiles.SetFocus()

	def onDelete(self, evt):
		# Prevent profile deletion while in the midst of a broadcast i.e. instant switch profile is active,
		# otherwise flags such as instant switch profile become inconsistent.
		# This was seen after deleting a profile one position before the previously active profile.
		if splconfig.SPLConfig.prevProfile is not None:
			gui.messageBox(
				_(
					# Translators: Message reported when attempting to delete a profile in the midst of a broadcast.
					"An instant switch profile might be active or you are in the midst of a broadcast. "
					"If so, please press SPL Assistant, F12 to switch back to a previously active profile "
					"before opening broadcast profiles dialog to delete a profile."
				),
				# Translators: Title of a dialog shown when profile cannot be deleted.
				_("Profile delete error"),
				wx.OK | wx.ICON_ERROR,
				self,
			)
			return
		name = self.profiles.GetStringSelection().split(" <")[0]
		# Ask once more if deleting an active profile.
		if name == self.activeProfile:
			if (
				gui.messageBox(
					# Translators: The confirmation prompt displayed
					# when the user requests to delete the active broadcast profile.
					_(
						"You are about to delete the currently active profile. Select yes if you wish to proceed."
					),
					# Translators: The title of the confirmation dialog for deletion of a profile.
					_("Delete active profile"),
					wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION,
					self,
				)
				== wx.NO
			):
				return
		index = self.profiles.Selection
		profilePos = self.profileNames.index(name)
		if (
			gui.messageBox(
				# Translators: The confirmation prompt displayed when the user requests to delete a broadcast profile.
				# The placeholder {} is replaced with the name of the broadcast profile that will be deleted.
				_("The profile {} will be permanently deleted. This action cannot be undone.").format(name),
				# Message comes from NVDA Core.
				translate("Confirm Deletion"),
				wx.OK | wx.CANCEL | wx.CANCEL_DEFAULT | wx.ICON_QUESTION,
				self,
			)
			!= wx.OK
		):
			return
		splconfig.SPLConfig.deleteProfile(name)
		# Make sure to connect to the right set of metadata servers
		# and enable/disable microphone alarm if appropriate.
		splactions.SPLActionProfileSwitched.notify(configDialogActive=True)
		if name == self.switchProfile or name == self.activeProfile:
			# Go through the below path if and only if instant switch profile is gone.
			if name == self.switchProfile:
				self.switchProfile = None
				splconfig.SPLConfig.prevProfile = None
			self.switchProfileDeleted = True
		self.profiles.Delete(index)
		del self.profileNames[profilePos]
		# Select normal profile if the active profile is gone.
		try:
			self.profiles.Selection = self.profileNames.index(self.activeProfile)
		except ValueError:
			self.activeProfile = splconfig.defaultProfileName
			self.profiles.Selection = 0
		self.onProfileSelection(None)
		self.profiles.SetFocus()

	def onTriggers(self, evt):
		self.Disable()
		TriggersDialog(self, self.profileNames[self.profiles.Selection]).Show()

	# Obtain profile flags for a given profile.
	# This is a proxy to the splconfig module level profile flag retriever with custom strings/maps as arguments.
	# Contained flag is set to False if this is called for display purposes,
	# otherwise it is used to set flags based on flag set.
	def getProfileFlags(self, name: str, contained: bool = True):
		return splconfig.SPLConfig.getProfileFlags(
			name, active=self.activeProfile, instant=self.switchProfile, contained=contained
		)

	# Handle flag modifications such as when toggling instant switch.
	# Unless given, flags will be queried.
	# This is a sister function to profile flags retriever.
	def setProfileFlags(self, index: int, action: str, flag: str, flags: str | set[str] | None = None):
		profile = self.profileNames[index]
		if flags is None:
			flags = self.getProfileFlags(profile)
		action = getattr(flags, action)
		action(flag)
		self.profiles.SetString(
			index, profile if not len(flags) else "{0} <{1}>".format(profile, ", ".join(flags))
		)

	def onChangeState(self, evt):
		selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
		if splconfig.SPLConfig.activeProfile != selectedProfile:
			splconfig.SPLConfig.swapProfiles(splconfig.SPLConfig.activeProfile, selectedProfile)
		splconfig.SPLConfig.instantSwitch = self.switchProfile
		# Make sure to nullify prev profile if instant switch profile is gone.
		if self.switchProfile is None:
			splconfig.SPLConfig.prevProfile = None
		splactions.SPLActionProfileSwitched.notify(configDialogActive=True)
		self.Close()

	def onClose(self, evt):
		if self.switchProfileRenamed or self.switchProfileDeleted:
			splconfig.SPLConfig.instantSwitch = self.switchProfile
		self.Destroy()
		global _configDialogOpened
		_configDialogOpened = False

	def onAppTerminate(self):
		self.onClose(None)


# New broadcast profile dialog: Modification of new config profile dialog from NVDA Core.
class NewProfileDialog(wx.Dialog):
	def __init__(self, parent, copy=False):
		self.copy = copy
		if not self.copy:
			# Message comes from NVDA Core.
			dialogTitle = translate("New Profile")
		else:
			# Translators: The title of the dialog to copy a broadcast profile.
			dialogTitle = _("Copy Profile")
		super().__init__(parent, title=dialogTitle)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		newProfileSizerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Message comes from NVDA Core.
		self.profileName = newProfileSizerHelper.addLabeledControl(translate("Profile name:"), wx.TextCtrl)

		if self.copy:
			self.baseProfiles = newProfileSizerHelper.addLabeledControl(
				# Translators: The label for a setting in SPL add-on dialog
				# to select a base  profile for copying.
				_("&Base profile:"),
				wx.Choice,
				choices=parent.profileNames,
			)
			self.baseProfiles.SetSelection(parent.profiles.GetSelection())

		# #152: do not add a separator if base profile list is not shown.
		newProfileSizerHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=self.copy)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(newProfileSizerHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.profileName.SetFocus()
		self.CenterOnScreen()

	def onOk(self, evt):
		parent = self.Parent
		name = api.filterFileName(self.profileName.Value)
		if not name:
			return
		if name in parent.profileNames:
			gui.messageBox(
				# Message comes from NVDA Core.
				translate("That profile already exists. Please choose a different name."),
				translate("Error"),
				wx.OK | wx.ICON_ERROR,
				self,
			)
			return
		namePath = name + ".ini"
		if not os.path.exists(splconfig.SPLProfiles):
			os.mkdir(splconfig.SPLProfiles)
		newProfilePath = os.path.join(splconfig.SPLProfiles, namePath)
		# Just build base profile dictionary here if copying a profile.
		if not self.copy:
			baseProfile = None
		else:
			baseConfig = splconfig.SPLConfig.profileByName(self.baseProfiles.GetStringSelection())
			# #140: it isn't enough to copy dictionaries.
			# Deep copy (config.dict()) must be performed to avoid accidental reference manipulation.
			baseProfile = {
				sect: key for sect, key in baseConfig.dict().items() if sect in splconfig.mutatableSettings
			}
		splconfig.SPLConfig.createProfile(newProfilePath, name, parent=baseProfile)
		parent.profileNames.append(name)
		parent.profiles.Append(name)
		parent.profiles.Selection = parent.profiles.Count - 1
		parent.onProfileSelection(None)
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()


# Broadcast profile triggers dialog.
# This dialog is similar to NVDA Core's profile triggers dialog
# and allows one to configure when to trigger this profile.
# As of 2020, the only trigger flag is instant switch profile.
class TriggersDialog(wx.Dialog):
	def __init__(self, parent, profile):
		# Translators: The title of the broadcast profile triggers dialog.
		title = _("Profile triggers for {profileName}").format(profileName=profile)
		super().__init__(parent, title=title)
		self.profile = profile
		self.selection = parent.profiles.GetSelection()
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		triggersHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: The label of a checkbox in SPL profile triggers dialog
		# to toggle if selected profile is an instant switch profile.
		instantSwitchLabel = _("This is an &instant switch profile")
		self.instantSwitchCheckbox = triggersHelper.addItem(wx.CheckBox(self, label=instantSwitchLabel))
		self.instantSwitchCheckbox.SetValue(parent.switchProfile == profile)

		# #152: unlike other dialogs, the only change is button bits
		# as the only prompt is instant switch checkbox.
		triggersHelper.addDialogDismissButtons(wx.OK | wx.CANCEL)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(triggersHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.CenterOnScreen()
		self.instantSwitchCheckbox.SetFocus()

	def onOk(self, evt):
		parent = self.Parent
		# Handle instant switch checkbox.
		if self.instantSwitchCheckbox.Value:
			if parent.switchProfile is not None and (self.profile != parent.switchProfile):
				# Instant switch flag is set on another profile, so remove the flag first.
				parent.setProfileFlags(
					parent.profileNames.index(parent.switchProfile), "discard", _("instant switch")
				)
			parent.setProfileFlags(self.selection, "add", _("instant switch"))
			parent.switchProfile = self.profile
		else:
			# Don't nullify switch profile just yet...
			if self.profile == parent.switchProfile:
				parent.switchProfile = None
			parent.setProfileFlags(self.selection, "discard", _("instant switch"))
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()


# A collection of general settings for the add-on.
class GeneralSettingsPanel(gui.settingsDialogs.SettingsPanel):
	# Message comes from NVDA Core.
	title = translate("General")

	def makeSettings(self, settingsSizer):
		generalSettingsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: the label for a setting in SPL add-on settings
		# to set status announcement between words and beeps.
		beepAnnounceLabel = _("&Beep for status announcements")
		self.beepAnnounceCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=beepAnnounceLabel))
		self.beepAnnounceCheckbox.SetValue(splconfig.SPLConfig["General"]["BeepAnnounce"])

		self.verbosityLevels = [
			# Translators: One of the message verbosity levels.
			("beginner", _("beginner")),
			# Translators: One of the message verbosity levels.
			("advanced", _("advanced")),
		]
		# Translators: the label for a setting in SPL add-on settings
		# to set message verbosity.
		verbosityListLabel = _("Message &verbosity:")
		self.verbosityList = generalSettingsHelper.addLabeledControl(
			verbosityListLabel, wx.Choice, choices=[x[1] for x in self.verbosityLevels]
		)
		currentVerbosity = splconfig.SPLConfig["General"]["MessageVerbosity"]
		selection = next((x for x, y in enumerate(self.verbosityLevels) if y[0] == currentVerbosity))
		self.verbosityList.SetSelection(selection)

		self.brailleTimerValues = [
			("off", translate("Off")),
			# Translators: One of the braille timer settings.
			("outro", _("Track ending")),
			# Translators: One of the braille timer settings.
			("intro", _("Track intro")),
			# Translators: One of the braille timer settings.
			("both", _("Track intro and ending")),
		]
		# Translators: the label for a setting in SPL add-on settings
		# to configure braille timer.
		brailleTimerListLabel = _("&Braille timer:")
		self.brailleTimerList = generalSettingsHelper.addLabeledControl(
			brailleTimerListLabel, wx.Choice, choices=[x[1] for x in self.brailleTimerValues]
		)
		brailleTimerCurValue = splconfig.SPLConfig["General"]["BrailleTimer"]
		selection = next((x for x, y in enumerate(self.brailleTimerValues) if y[0] == brailleTimerCurValue))
		self.brailleTimerList.SetSelection(selection)

		self.libScanValues = [
			("off", translate("Off")),
			# Translators: One of the library scan announcement settings.
			("ending", _("Start and end only")),
			# Translators: One of the library scan announcement settings.
			("progress", _("Scan progress")),
			# Translators: One of the library scan announcement settings.
			("numbers", _("Scan count")),
		]
		# Translators: The label for a setting in SPL add-on settings
		# to control library scan announcement.
		libScanListLabel = _("&Library scan announcement:")
		self.libScanList = generalSettingsHelper.addLabeledControl(
			libScanListLabel, wx.Choice, choices=[x[1] for x in self.libScanValues]
		)
		libScanCurValue = splconfig.SPLConfig["General"]["LibraryScanAnnounce"]
		selection = next((x for x, y in enumerate(self.libScanValues) if y[0] == libScanCurValue))
		self.libScanList.SetSelection(selection)

		# Translators: the label for a setting in SPL add-on settings
		# to announce time including hours.
		hourAnnounceLabel = _("Include &hours when announcing track or playlist duration")
		self.hourAnnounceCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=hourAnnounceLabel))
		self.hourAnnounceCheckbox.SetValue(splconfig.SPLConfig["General"]["TimeHourAnnounce"])

		# Translators: The label for a setting in SPL add-on dialog to set vertical column.
		verticalColLabel = _("&Vertical column navigation announcement:")
		verticalColChoices = [
			# Translators: One of the options for vertical column navigation
			# denoting NVDA will announce current column position (e.g. second column position from the left).
			_("whichever column I am reviewing")
		] + splconfig.SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
		self.verticalColumnsList = generalSettingsHelper.addLabeledControl(
			verticalColLabel, wx.Choice, choices=verticalColChoices
		)
		verticalColumn = splconfig.SPLConfig["General"]["VerticalColumnAnnounce"]
		selection = self.verticalColumnsList.FindString(verticalColumn) if verticalColumn is not None else 0
		self.verticalColumnsList.SetSelection(selection)

		# Translators: the label for a setting in SPL add-on settings
		# to toggle category sound announcement.
		categorySoundsLabel = _("&Beep for different track categories")
		self.categorySoundsCheckbox = generalSettingsHelper.addItem(
			wx.CheckBox(self, label=categorySoundsLabel)
		)
		self.categorySoundsCheckbox.SetValue(splconfig.SPLConfig["General"]["CategorySounds"])

		self.trackCommentValues = [
			("off", translate("Off")),
			# Translators: One of the track comment notification settings.
			("message", _("Message")),
			# Translators: One of the track comment notification settings.
			("beep", _("Beep")),
			# Translators: One of the track comment notification settings.
			("both", _("Both")),
		]
		# Translators: the label for a setting in SPL add-on settings
		# to set how track comments are announced.
		trackCommentListLabel = _("&Track comment announcement:")
		self.trackCommentList = generalSettingsHelper.addLabeledControl(
			trackCommentListLabel, wx.Choice, choices=[x[1] for x in self.trackCommentValues]
		)
		trackCommentCurValue = splconfig.SPLConfig["General"]["TrackCommentAnnounce"]
		selection = next((x for x, y in enumerate(self.trackCommentValues) if y[0] == trackCommentCurValue))
		self.trackCommentList.SetSelection(selection)

		# Translators: the label for a setting in SPL add-on settings
		# to toggle top and bottom notification.
		topBottomLabel = _("Notify when located at &top or bottom of playlist viewer")
		self.topBottomCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=topBottomLabel))
		self.topBottomCheckbox.SetValue(splconfig.SPLConfig["General"]["TopBottomAnnounce"])

		# Translators: the label for a setting in SPL add-on settings
		# to enable requests alert.
		requestsAlertLabel = _("Play a sound when listener &requests arrive")
		self.requestsAlertCheckbox = generalSettingsHelper.addItem(
			wx.CheckBox(self, label=requestsAlertLabel)
		)
		self.requestsAlertCheckbox.SetValue(splconfig.SPLConfig["General"]["RequestsAlert"])

	def onSave(self):
		splconfig.SPLConfig["General"]["BeepAnnounce"] = self.beepAnnounceCheckbox.Value
		splconfig.SPLConfig["General"]["MessageVerbosity"] = self.verbosityLevels[
			self.verbosityList.GetSelection()
		][0]
		splconfig.SPLConfig["General"]["BrailleTimer"] = self.brailleTimerValues[
			self.brailleTimerList.GetSelection()
		][0]
		splconfig.SPLConfig["General"]["LibraryScanAnnounce"] = self.libScanValues[
			self.libScanList.GetSelection()
		][0]
		splconfig.SPLConfig["General"]["TimeHourAnnounce"] = self.hourAnnounceCheckbox.Value
		splconfig.SPLConfig["General"]["VerticalColumnAnnounce"] = (
			self.verticalColumnsList.GetStringSelection()
			if self.verticalColumnsList.GetSelection() != 0
			else None
		)
		splconfig.SPLConfig["General"]["CategorySounds"] = self.categorySoundsCheckbox.Value
		splconfig.SPLConfig["General"]["TrackCommentAnnounce"] = self.trackCommentValues[
			self.trackCommentList.GetSelection()
		][0]
		splconfig.SPLConfig["General"]["TopBottomAnnounce"] = self.topBottomCheckbox.Value
		splconfig.SPLConfig["General"]["RequestsAlert"] = self.requestsAlertCheckbox.Value


# Various alarm settings (outro, intro, microphone).
class AlarmsPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: title of a panel to configure various alarms and related settings.
	title = _("Alarms")

	def makeSettings(self, settingsSizer):
		alarmsCenterHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: the label for a setting in SPL add-on settings
		# To set end of track alarm in seconds.
		outroAlarmLabel = _("&End of track alarm in seconds")
		self.outroAlarmEntry = alarmsCenterHelper.addLabeledControl(
			outroAlarmLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=1,
			max=59,
			initial=splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"],
		)

		# Translators: the label for a setting in SPL add-on settings
		# to enable end of track alarm.
		outroToggleLabel = _("&Notify when end of track is approaching")
		self.outroToggleCheckBox = alarmsCenterHelper.addItem(wx.CheckBox(self, label=outroToggleLabel))
		self.outroToggleCheckBox.SetValue(splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"])

		# Translators: the label for a setting in SPL add-on settings
		# To set trakc intro alarm in seconds.
		introAlarmLabel = _("&Track intro alarm in seconds")
		self.introAlarmEntry = alarmsCenterHelper.addLabeledControl(
			introAlarmLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=1,
			max=9,
			initial=splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"],
		)

		# Translators: the label for a setting in SPL add-on settings
		# to enable track intro alarm.
		introToggleLabel = _("&Notify when end of introduction is approaching")
		self.introToggleCheckBox = alarmsCenterHelper.addItem(wx.CheckBox(self, label=introToggleLabel))
		self.introToggleCheckBox.SetValue(splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"])

		# Translators: the label for a setting in SPL add-on settings
		# to set microphone active alarm in seconds.
		micAlarmLabel = _("&Microphone alarm in seconds (0 disables the alarm)")
		self.micAlarmEntry = alarmsCenterHelper.addLabeledControl(
			micAlarmLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0,
			max=7200,
			initial=splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"],
		)

		# Translators: the label for a setting in SPL add-on settings
		# to set microphone active alarm interval in seconds.
		micIntervalLabel = _("Microphone alarm &interval in seconds")
		self.micIntervalEntry = alarmsCenterHelper.addLabeledControl(
			micIntervalLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0,
			max=60,
			initial=splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"],
		)

		self.alarmAnnounceValues = [
			# Translators: One of the alarm notification options.
			("beep", _("beep")),
			# Translators: One of the alarm notification options.
			("message", _("message")),
			# Translators: One of the alarm notification options.
			("both", _("both beep and message")),
		]
		# Translators: The label for a setting in SPL add-on settings
		# to configure alarm announcement type.
		alarmAnnounceListLabel = _("&Alarm notification:")
		self.alarmAnnounceList = alarmsCenterHelper.addLabeledControl(
			alarmAnnounceListLabel, wx.Choice, choices=[x[1] for x in self.alarmAnnounceValues]
		)
		alarmAnnounceCurValue = splconfig.SPLConfig["General"]["AlarmAnnounce"]
		selection = next((x for x, y in enumerate(self.alarmAnnounceValues) if y[0] == alarmAnnounceCurValue))
		self.alarmAnnounceList.SetSelection(selection)

	def onSave(self):
		splconfig.SPLConfig["General"]["AlarmAnnounce"] = self.alarmAnnounceValues[
			self.alarmAnnounceList.GetSelection()
		][0]
		splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"] = self.outroAlarmEntry.GetValue()
		splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"] = self.outroToggleCheckBox.GetValue()
		splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"] = self.introAlarmEntry.GetValue()
		splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"] = self.introToggleCheckBox.GetValue()
		splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"] = self.micAlarmEntry.GetValue()
		splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] = self.micIntervalEntry.GetValue()
		# #42: don't forget to restart microphone alarm timer.
		# At least try notifying the app module that microphone alarm settings have changed.
		studioWindow = getNVDAObjectFromEvent(user32.FindWindowW("TStudioForm", None), OBJID_CLIENT, 0)
		if studioWindow is not None:
			studioWindow.appModule.actionProfileSwitched()


# Playlist snapshot flags
# For things such as checkboxes for average duration and top category count.
class PlaylistSnapshotsPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: title of a panel to configure playlist snapshot information.
	title = _("Playlist snapshots")

	def makeSettings(self, settingsSizer):
		playlistSnapshotsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: Help text for playlist snapshots panel.
		labelText = _("""Select information to be included when obtaining playlist snapshots.
		Track count and total duration are always included.""")
		playlistSnapshotsHelper.addItem(wx.StaticText(self, label=labelText))

		# Translators: the label for a setting in SPL add-on settings
		# to include shortest and longest track duration in playlist snapshots window.
		durationMinMaxLabel = _("Shortest and longest tracks")
		self.playlistDurationMinMaxCheckbox = playlistSnapshotsHelper.addItem(
			wx.CheckBox(self, label=durationMinMaxLabel)
		)
		self.playlistDurationMinMaxCheckbox.SetValue(
			splconfig.SPLConfig["PlaylistSnapshots"]["DurationMinMax"]
		)

		# Translators: the label for a setting in SPL add-on settings
		# to include average track duration in playlist snapshots window.
		durationAverageLabel = _("Average track duration")
		self.playlistDurationAverageCheckbox = playlistSnapshotsHelper.addItem(
			wx.CheckBox(self, label=durationAverageLabel)
		)
		self.playlistDurationAverageCheckbox.SetValue(
			splconfig.SPLConfig["PlaylistSnapshots"]["DurationAverage"]
		)

		# Translators: the label for a setting in SPL add-on settings
		# to include track artist count in playlist snapshots window.
		artistCountLabel = _("Artist count")
		self.playlistArtistCountCheckbox = playlistSnapshotsHelper.addItem(
			wx.CheckBox(self, label=artistCountLabel)
		)
		self.playlistArtistCountCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCount"])

		# Translators: the label for a setting in SPL add-on settings
		# to set top artist count limit in playlist snapshots window.
		artistCountLimitLabel = _("Top artist count (0 displays all artists)")
		self.playlistArtistCountLimit = playlistSnapshotsHelper.addLabeledControl(
			artistCountLimitLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0,
			max=10,
			initial=splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"],
		)

		# Translators: the label for a setting in SPL add-on settings
		# to include track category count in playlist snapshots window.
		categoryCountLabel = _("Category count")
		self.playlistCategoryCountCheckbox = playlistSnapshotsHelper.addItem(
			wx.CheckBox(self, label=categoryCountLabel)
		)
		self.playlistCategoryCountCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCount"])

		# Translators: the label for a setting in SPL add-on settings
		# to set top track category count limit in playlist snapshots window.
		categoryCountLimitLabel = _("Top category count (0 displays all categories)")
		self.playlistCategoryCountLimit = playlistSnapshotsHelper.addLabeledControl(
			categoryCountLimitLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0,
			max=10,
			initial=splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"],
		)

		# Translators: the label for a setting in SPL add-on settings
		# to include track genre count in playlist snapshots window.
		genreCountLabel = _("Genre count")
		self.playlistGenreCountCheckbox = playlistSnapshotsHelper.addItem(
			wx.CheckBox(self, label=genreCountLabel)
		)
		self.playlistGenreCountCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["GenreCount"])

		# Translators: the label for a setting in SPL add-on settings
		# to set top track genre count limit in playlist snapshots window.
		genreCountLimitLabel = _("Top genre count (0 displays all genres)")
		self.playlistGenreCountLimit = playlistSnapshotsHelper.addLabeledControl(
			genreCountLimitLabel,
			gui.nvdaControls.SelectOnFocusSpinCtrl,
			min=0,
			max=10,
			initial=splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"],
		)

		# Translators: the label for a setting in SPL add-on settings
		# to show playlist snapshots window when the snapshots command is pressed once.
		resultsWindowOnFirstPressLabel = _(
			"&Show results window when playlist snapshots command is performed once"
		)
		self.resultsWindowOnFirstPressCheckbox = playlistSnapshotsHelper.addItem(
			wx.CheckBox(self, label=resultsWindowOnFirstPressLabel)
		)
		self.resultsWindowOnFirstPressCheckbox.SetValue(
			splconfig.SPLConfig["PlaylistSnapshots"]["ShowResultsWindowOnFirstPress"]
		)

	def onSave(self):
		splconfig.SPLConfig["PlaylistSnapshots"]["DurationMinMax"] = self.playlistDurationMinMaxCheckbox.Value
		splconfig.SPLConfig["PlaylistSnapshots"]["DurationAverage"] = (
			self.playlistDurationAverageCheckbox.Value
		)
		splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCount"] = self.playlistArtistCountCheckbox.Value
		splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"] = (
			self.playlistArtistCountLimit.GetValue()
		)
		splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCount"] = self.playlistCategoryCountCheckbox.Value
		splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"] = (
			self.playlistCategoryCountLimit.GetValue()
		)
		splconfig.SPLConfig["PlaylistSnapshots"]["GenreCount"] = self.playlistGenreCountCheckbox.Value
		splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"] = self.playlistGenreCountLimit.GetValue()
		splconfig.SPLConfig["PlaylistSnapshots"]["ShowResultsWindowOnFirstPress"] = (
			self.resultsWindowOnFirstPressCheckbox.Value
		)


# Metadata reminder controller.
# Select notification/streaming URL's for metadata streaming.
metadataStreamLabels = ("DSP encoder", "URL 1", "URL 2", "URL 3", "URL 4")


class MetadataStreamingDialog(wx.Dialog):
	"""A dialog to toggle metadata streaming quickly and optionally save changes to add-on configuration."""

	@classmethod
	def _instance(cls):
		return None

	def __new__(cls, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _configDialogOpened:
			raise RuntimeError("An instance of metadata streaming dialog is opened")
		instance = MetadataStreamingDialog._instance()
		if instance is None:
			return super(MetadataStreamingDialog, cls).__new__(cls, *args, **kwargs)
		return instance

	def __init__(self, parent):
		global _configDialogOpened
		if MetadataStreamingDialog._instance() is not None:
			return
		# Use a weakref so the instance can die.
		MetadataStreamingDialog._instance = weakref.ref(self)

		# Translators: Title of a dialog to configure metadata streaming status
		# for DSP encoder and four additional URL's.
		super().__init__(parent, title=_("Metadata streaming options"))
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		metadataSizerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		# Translators: dialog description for metadata streaming options dialog.
		labelText = _("Check to enable metadata streaming, uncheck to disable.")
		metadataSizerHelper.addItem(wx.StaticText(self, label=labelText))

		SPLMetadataStreaming = 36
		streams = [splbase.studioAPI(pos, SPLMetadataStreaming) for pos in range(5)]
		self.checkedStreams = metadataSizerHelper.addLabeledControl(
			# Translators: the label for a setting in SPL add-on settings
			# to configure streaming status for metadata streams.
			_("&Stream:"),
			CustomCheckListBox,
			choices=metadataStreamLabels,
		)
		for stream in range(5):
			self.checkedStreams.Check(stream, check=streams[stream])
		self.checkedStreams.SetSelection(0)

		# Translators: A checkbox to let metadata streaming status
		# be applied to the currently active broadcast profile.
		applyLabel = _("&Apply streaming changes to the selected profile")
		self.applyCheckbox = metadataSizerHelper.addItem(wx.CheckBox(self, label=applyLabel))
		self.applyCheckbox.SetValue(True)
		# Security: no, apply to config checkbox should be disabled in secure mode.
		# Although metadata streaming settings may appear to be saved, it is ultimately discarded in the end.
		if globalVars.appArgs.secure:
			self.applyCheckbox.Disable()

		metadataSizerHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=True)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(metadataSizerHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedStreams.SetFocus()
		self.CenterOnScreen()
		_configDialogOpened = True

	def onOk(self, evt):
		global _configDialogOpened
		# Prepare checkbox values first for various reasons.
		# #76: traverse check list box and build boolean list accordingly.
		metadataEnabled = [self.checkedStreams.IsChecked(url) for url in range(5)]
		SPLMetadataStreaming = 36
		for url in range(5):
			dataLo = 0x00010000 if metadataEnabled[url] else 0xFFFF0000
			splbase.studioAPI(dataLo | url, SPLMetadataStreaming)
		# Store just toggled settings to profile if told to do so.
		if self.applyCheckbox.Value:
			splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"] = metadataEnabled
		self.Destroy()
		_configDialogOpened = False

	def onCancel(self, evt):
		global _configDialogOpened
		self.Destroy()
		_configDialogOpened = False

	def onAppTerminate(self):
		self.onCancel(None)


class MetadataStreamingPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: title of a panel to configure metadata streaming status
	# for DSP encoder and four additional URL's.
	title = _("Metadata streaming")

	def makeSettings(self, settingsSizer):
		metadataSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		self.metadataValues = [
			("off", translate("Off")),
			# Translators: One of the metadata notification settings.
			("startup", _("When Studio starts")),
			# Translators: One of the metadata notification settings.
			("instant", _("When instant switch profile is active")),
		]
		# Translators: the label for a setting in SPL add-on settings
		# to be notified that metadata streaming is enabled.
		metadataListLabel = _("&Metadata streaming notification and connection")
		self.metadataList = metadataSizerHelper.addLabeledControl(
			metadataListLabel, wx.Choice, choices=[x[1] for x in self.metadataValues]
		)
		metadataCurValue = splconfig.SPLConfig["General"]["MetadataReminder"]
		selection = next((x for x, y in enumerate(self.metadataValues) if y[0] == metadataCurValue))
		self.metadataList.SetSelection(selection)

		# # Translators: the label for a setting in SPL add-on settings
		# to configure streaming status for metadata streams.
		checkedStreamsLabel = _("&Select the URL for metadata streaming upon request:")
		self.checkedStreams = metadataSizerHelper.addLabeledControl(
			checkedStreamsLabel, CustomCheckListBox, choices=metadataStreamLabels
		)
		for stream in range(5):
			self.checkedStreams.Check(
				stream, check=splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"][stream]
			)
		self.checkedStreams.SetSelection(0)

	def onSave(self):
		splconfig.SPLConfig["General"]["MetadataReminder"] = self.metadataValues[
			self.metadataList.GetSelection()
		][0]
		# #76: traverse check list box and build boolean list accordingly.
		metadataEnabled = [self.checkedStreams.IsChecked(url) for url in range(5)]
		splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"] = metadataEnabled
		# Try connecting to metadata streaming servers if any.
		SPLMetadataStreaming = 36
		for url in range(5):
			dataLo = 0x00010000 if metadataEnabled[url] else 0xFFFF0000
			splbase.studioAPI(dataLo | url, SPLMetadataStreaming)


# Column announcement manager.
# Select which track columns should be announced and in which order.
# Also serves as a base panel for Playlist Transcripts/column selector setting.
class ColumnAnnouncementsBasePanel(gui.settingsDialogs.SettingsPanel):
	def _onMakeSettingsBase(self, sHelper, includedColumnsLabel):
		# Provides common user interface elements for column inclusion/order controls across settings panels
		# (leave it as a private method).

		checkableColumns = (
			"Duration",
			"Intro",
			"Category",
			"Filename",
			"Outro",
			"Year",
			"Album",
			"Genre",
			"Mood",
			"Energy",
			"Tempo",
			"BPM",
			"Gender",
			"Rating",
			"Time Scheduled",
		)
		self.checkedColumns = sHelper.addLabeledControl(
			includedColumnsLabel, CustomCheckListBox, choices=checkableColumns
		)
		self.checkedColumns.SetCheckedStrings(self.includedColumns)
		self.checkedColumns.SetSelection(0)

		# Translators: The label for a group in SPL add-on settings
		# to select column announcement order.
		columnOrderGroupLabel = _("Column order")
		columnOrderGroup = gui.guiHelper.BoxSizerHelper(
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=columnOrderGroupLabel), wx.HORIZONTAL)
		)
		sHelper.addItem(columnOrderGroup)

		# wxPython contains RearrangeList to allow item orders to be changed automatically.
		# Due to usability quirks (focus bouncing and what not), work around by
		# using a variant of list box and move up/down buttons.
		# The label for the list below is above the list,
		# so move move up/down buttons to the right of the list box.
		self.trackColumns = columnOrderGroup.addItem(wx.ListBox(self, choices=self.columnOrder))
		self.trackColumns.Bind(wx.EVT_LISTBOX, self.onColumnSelection)
		self.trackColumns.SetSelection(0)

		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		self.upButton = wx.Button(self, wx.ID_UP)
		self.upButton.Bind(wx.EVT_BUTTON, self.onMoveUp)
		self.upButton.Disable()
		self.dnButton = wx.Button(self, wx.ID_DOWN)
		self.dnButton.Bind(wx.EVT_BUTTON, self.onMoveDown)
		sizer.sizer.AddMany((self.upButton, self.dnButton))
		columnOrderGroup.addItem(sizer.sizer)

	def onColumnSelection(self, evt):
		selIndex = self.trackColumns.GetSelection()
		self.upButton.Disable() if selIndex == 0 else self.upButton.Enable()
		if selIndex == self.trackColumns.GetCount() - 1:
			self.dnButton.Disable()
		else:
			self.dnButton.Enable()

	def onMoveUp(self, evt):
		tones.beep(1000, 200)
		selIndex = self.trackColumns.GetSelection()
		if selIndex > 0:
			selItem = self.trackColumns.GetString(selIndex)
			self.trackColumns.Delete(selIndex)
			self.trackColumns.Insert(selItem, selIndex - 1)
			self.trackColumns.Select(selIndex - 1)
			self.onColumnSelection(None)

	def onMoveDown(self, evt):
		tones.beep(500, 200)
		selIndex = self.trackColumns.GetSelection()
		if selIndex < self.trackColumns.GetCount() - 1:
			selItem = self.trackColumns.GetString(selIndex)
			self.trackColumns.Delete(selIndex)
			self.trackColumns.Insert(selItem, selIndex + 1)
			self.trackColumns.Select(selIndex + 1)
			self.onColumnSelection(None)
			# Hack: Wen the last item is selected, forcefully move the focus to "move up" button.
			# This will cause NVDA to say "unavailable" as focus is lost momentarily.
			# A bit anoying but a necessary hack.
			if self.FindFocus().GetId() == wx.ID_OK:
				self.upButton.SetFocus()


class ColumnAnnouncementsPanel(ColumnAnnouncementsBasePanel):
	# Translators: title of a panel to configure column announcements
	# (order and what columns should be announced).
	title = _("Column announcements")

	def makeSettings(self, settingsSizer):
		colAnnouncementsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Without manual conversion below, it produces a rare bug
		# where clicking cancel after changing column inclusion causes new set to be retained.
		# Of course take away artist and title.
		self.includedColumns = set(splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"]) - {
			"Artist",
			"Title",
		}
		self.columnOrder = splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"]

		labelText = _(
			# Translators: Help text explaining custom column order and inclusion controls.
			"To apply custom column order and inclusion when announcing track columns in Studio's playlist viewer, "
			"uncheck 'Announce columns in the order shown on screen' and configure column inclusion and order."
		)
		colAnnouncementsHelper.addItem(wx.StaticText(self, label=labelText))

		# Translators: the label for a setting in SPL add-on settings
		# to toggle custom column announcement.
		columnOrderLabel = _("Announce columns in the &order shown on screen")
		self.columnOrderCheckbox = colAnnouncementsHelper.addItem(
			wx.CheckBox(self, wx.ID_ANY, label=columnOrderLabel)
		)
		self.columnOrderCheckbox.SetValue(splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"])

		labelText = _(
			# Translators: Help text to select columns to be announced.
			"&Select columns to be announced\n" "(artist and title are announced by default):"
		)
		# Column inclusion/order are processed via a private method.
		self._onMakeSettingsBase(colAnnouncementsHelper, labelText)

	def onSave(self):
		splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"] = self.columnOrderCheckbox.Value
		splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"] = set(
			self.checkedColumns.GetCheckedStrings()
		) | {"Artist", "Title"}
		splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"] = self.trackColumns.GetItems()


class PlaylistTranscriptsPanel(ColumnAnnouncementsBasePanel):
	# Translators: Title of a panel to configure playlist transcripts options.
	title = _("Playlist transcripts")

	def makeSettings(self, settingsSizer):
		playlistTranscriptsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Again manually create a new set minus artist and title.
		self.includedColumns = set(splconfig.SPLConfig["PlaylistTranscripts"]["IncludedColumns"]) - {
			"Artist",
			"Title",
		}
		self.columnOrder = splconfig.SPLConfig["PlaylistTranscripts"]["ColumnOrder"]

		labelText = _(
			# Translators: Help text to select columns to be announced.
			"&Select columns to be included in playlist transcripts\n"
			"(artist and title are always included):"
		)
		# Just like column announcements panel,
		# column inclusion and order controls are generated by the base class.
		self._onMakeSettingsBase(playlistTranscriptsHelper, labelText)

	def onSave(self):
		splconfig.SPLConfig["PlaylistTranscripts"]["IncludedColumns"] = set(
			self.checkedColumns.GetCheckedStrings()
		) | {"Artist", "Title"}
		splconfig.SPLConfig["PlaylistTranscripts"]["ColumnOrder"] = self.trackColumns.GetItems()


# Columns Explorer for Studio, Track Tool, Creator, and playlist editor (Creator and Remote VT)
# Configure which column will be announced when Control+NVDA+number row keys are pressed.
class ColumnsExplorerPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: title of a panel to configure columns explorer settings.
	title = _("Columns explorer")

	def makeSettings(self, settingsSizer):
		colExplorerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: The label of a button to configure columns explorer slots (Control+NvDA+1 through 0)
		# for StationPlaylist Studio.
		columnsExplorerButton = wx.Button(self, label=_("Columns E&xplorer for SPL Studio..."))
		columnsExplorerButton.Bind(wx.EVT_BUTTON, self.onColumnsExplorer)
		self.exploreColumns = splconfig.SPLConfig["ExploreColumns"]["Studio"]

		# Translators: The label of a button to configure columns explorer slots (Control+NvDA+1 through 0)
		# for Track Tool.
		columnsExplorerTTButton = wx.Button(self, label=_("Columns Explorer for &Track Tool..."))
		columnsExplorerTTButton.Bind(wx.EVT_BUTTON, self.onColumnsExplorerTT)
		self.exploreColumnsTT = splconfig.SPLConfig["ExploreColumns"]["TrackTool"]

		# Translators: The label of a button to configure columns explorer slots (Control+NvDA+1 through 0)
		# for StationPlaylist Creator.
		columnsExplorerCreatorButton = wx.Button(self, label=_("Columns Explorer for &SPL Creator..."))
		columnsExplorerCreatorButton.Bind(wx.EVT_BUTTON, self.onColumnsExplorerCreator)
		self.exploreColumnsCreator = splconfig.SPLConfig["ExploreColumns"]["Creator"]

		# Translators: The label of a button to configure columns explorer slots (Control+NvDA+1 through 0)
		# for Creator and Remote VT playlist editor.
		columnsExplorerPlsEditorButton = wx.Button(self, label=_("Columns Explorer for &playlist editor..."))
		columnsExplorerPlsEditorButton.Bind(wx.EVT_BUTTON, self.onColumnsExplorerPlsEditor)
		self.exploreColumnsPlsEditor = splconfig.SPLConfig["ExploreColumns"]["PlaylistEditor"]
		colExplorerHelper.sizer.AddMany(
			(
				columnsExplorerButton,
				columnsExplorerTTButton,
				columnsExplorerCreatorButton,
				columnsExplorerPlsEditorButton
			)
		)

	def onSave(self):
		splconfig.SPLConfig["ExploreColumns"]["Studio"] = self.exploreColumns
		splconfig.SPLConfig["ExploreColumns"]["TrackTool"] = self.exploreColumnsTT
		splconfig.SPLConfig["ExploreColumns"]["Creator"] = self.exploreColumnsCreator
		splconfig.SPLConfig["ExploreColumns"]["PlaylistEditor"] = self.exploreColumnsPlsEditor

	# Columns Explorer configuration.
	def onColumnsExplorer(self, evt):
		ColumnsExplorerDialog(self).ShowModal()

	# Track Tool Columns Explorer configuration.
	def onColumnsExplorerTT(self, evt):
		ColumnsExplorerDialog(self, level=1).ShowModal()

	# SPL Creator Columns Explorer configuration.
	def onColumnsExplorerCreator(self, evt):
		ColumnsExplorerDialog(self, level=2).ShowModal()

	# Playlist editor Columns Explorer configuration.
	def onColumnsExplorerPlsEditor(self, evt):
		ColumnsExplorerDialog(self, level=3).ShowModal()


class ColumnsExplorerDialog(wx.Dialog):
	def __init__(self, parent, level=0):
		self.level = level
		# Counterintuitive, but start with level 1 (fallback will be level 0/Studio).
		match level:
			case 1:  # Track Tool
				# Translators: The title of Columns Explorer configuration dialog.
				actualTitle = _("Columns Explorer for Track Tool")
				cols = (
					"Artist",
					"Title",
					"Duration",
					"Cue",
					"Overlap",
					"Intro",
					"Segue",
					"Filename",
					"Album",
					"CD Code",
					"Outro",
					"Year",
					"URL 1",
					"URL 2",
					"Genre",
				)
				slots = parent.exploreColumnsTT
			case 2:  # Creator
				# Translators: The title of Columns Explorer configuration dialog.
				actualTitle = _("Columns Explorer for SPL Creator")
				cols = (
					"Artist",
					"Title",
					"Position",
					"Cue",
					"Intro",
					"Outro",
					"Segue",
					"Duration",
					"Last Scheduled",
					"7 Days",
					"Restrictions",
					"Year",
					"Album",
					"Genre",
					"Mood",
					"Energy",
					"Tempo",
					"BPM",
					"Gender",
					"Rating",
					"File Created",
					"Filename",
					"Client",
					"Other",
					"Intro Link",
					"Outro Link",
				)
				slots = parent.exploreColumnsCreator
			case 3:  # Playlist editor
				# Translators: The title of Columns Explorer configuration dialog.
				actualTitle = _("Columns Explorer for playlist editor (Creator and Remote VT)")
				cols = (
					"Artist",
					"Title",
					"Duration",
					"Intro",
					"Outro",
					"Category",
					"Year",
					"Album",
					"Genre",
					"Mood",
					"Energy",
					"Tempo",
					"Gender",
					"Rating",
					"Filename",
				)
				slots = parent.exploreColumnsPlsEditor
			case _:  # Studio
				# Translators: The title of Columns Explorer configuration dialog.
				actualTitle = _("Columns Explorer for SPL Studio")
				cols = splconfig.SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
				slots = parent.exploreColumns
		# Gather column slots.
		self.columnSlots = []

		super().__init__(parent, title=actualTitle)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		colExplorerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Display column combo boxes in a five by two grid.
		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for slot in range(5):
			# Translators: The label for a setting in SPL add-on settings
			# to select column for this column slot.
			columns = sizer.addLabeledControl(
				_("Slot {position}").format(position=slot + 1), wx.Choice, choices=cols
			)
			try:
				columns.SetSelection(cols.index(slots[slot]))
			except Exception:
				pass
			self.columnSlots.append(columns)
		colExplorerHelper.addItem(sizer.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for slot in range(5, 10):
			columns = sizer.addLabeledControl(
				_("Slot {position}").format(position=slot + 1), wx.Choice, choices=cols
			)
			try:
				columns.SetSelection(cols.index(slots[slot]))
			except Exception:
				pass
			self.columnSlots.append(columns)
		colExplorerHelper.addItem(sizer.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		colExplorerHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=True)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(colExplorerHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.columnSlots[0].SetFocus()
		self.CenterOnScreen()

	def onOk(self, evt):
		parent = self.Parent
		# #62: manually build a list so changes won't be retained
		# when Cancel button is clicked from main settings, caused by reference problem.
		# Note that item count is based on how many column combo boxes are present in this dialog.
		slots = [self.columnSlots[slot].GetStringSelection() for slot in range(10)]
		match self.level:
			case 0:
				parent.exploreColumns = slots
			case 1:
				parent.exploreColumnsTT = slots
			case 2:
				parent.exploreColumnsCreator = slots
			case 3:
				parent.exploreColumnsPlsEditor = slots
			case _:
				pass
		parent.Enable()
		self.Destroy()

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()


# Say status panel.
# Houses options such as announcing cart names.
class SayStatusPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: title of a panel to configure various status announcements such as announcing listener count.
	title = _("Status announcements")

	def makeSettings(self, settingsSizer):
		sayStatusHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: the label for a setting in SPL add-on settings
		# to announce scheduled time.
		scheduledForLabel = _("Announce &scheduled time for the selected track")
		self.scheduledForCheckbox = sayStatusHelper.addItem(wx.CheckBox(self, label=scheduledForLabel))
		self.scheduledForCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayScheduledFor"])

		# Translators: the label for a setting in SPL add-on settings
		# to announce listener count.
		listenerCountLabel = _("Announce &listener count")
		self.listenerCountCheckbox = sayStatusHelper.addItem(wx.CheckBox(self, label=listenerCountLabel))
		self.listenerCountCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayListenerCount"])

		# Translators: the label for a setting in SPL add-on settings
		# to announce currently playing cart.
		cartNameLabel = _("&Announce name of the currently playing cart")
		self.cartNameCheckbox = sayStatusHelper.addItem(wx.CheckBox(self, label=cartNameLabel))
		self.cartNameCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"])

		# Translators: the label for a setting in SPL add-on settings
		# to announce player position for the current and next tracks.
		playerPositionLabel = _(
			"Include track player &position when announcing current and next track information"
		)
		self.playerPositionCheckbox = sayStatusHelper.addItem(wx.CheckBox(self, label=playerPositionLabel))
		self.playerPositionCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"])

	def onSave(self):
		splconfig.SPLConfig["SayStatus"]["SayScheduledFor"] = self.scheduledForCheckbox.Value
		splconfig.SPLConfig["SayStatus"]["SayListenerCount"] = self.listenerCountCheckbox.Value
		splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"] = self.cartNameCheckbox.Value
		splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"] = self.playerPositionCheckbox.Value


# Advanced options
# This panel houses advanced options such as using SPL Controller command to invoke SPL Assistant.
class AdvancedOptionsPanel(gui.settingsDialogs.SettingsPanel):
	# Message comes from NVDA Core.
	title = translate("Advanced")

	def makeSettings(self, settingsSizer):
		advOptionsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: The label for a checkbox in SPL add-on settings
		# to toggle if SPL Controller command can be used to invoke Assistant layer.
		splConPassthroughLabel = _("Allow SPL C&ontroller command to invoke SPL Assistant layer")
		self.splConPassthroughCheckbox = advOptionsHelper.addItem(
			wx.CheckBox(self, label=splConPassthroughLabel)
		)
		self.splConPassthroughCheckbox.SetValue(splconfig.SPLConfig["Advanced"]["SPLConPassthrough"])

		self.compatibilityLayouts = [("off", "NVDA"), ("jfw", "JAWS for Windows")]
		# Translators: The label for a setting in SPL add-on settings
		# to set keyboard layout for SPL Assistant.
		compatibilityListLabel = _("SPL Assistant command &layout:")
		self.compatibilityList = advOptionsHelper.addLabeledControl(
			compatibilityListLabel, wx.Choice, choices=[x[1] for x in self.compatibilityLayouts]
		)
		compatibilityCurValue = splconfig.SPLConfig["Advanced"]["CompatibilityLayer"]
		selection = next(
			(x for x, y in enumerate(self.compatibilityLayouts) if y[0] == compatibilityCurValue)
		)
		self.compatibilityList.SetSelection(selection)

	def onSave(self):
		splconfig.SPLConfig["Advanced"]["SPLConPassthrough"] = self.splConPassthroughCheckbox.Value
		splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] = self.compatibilityLayouts[
			self.compatibilityList.GetSelection()
		][0]


# A dialog to reset add-on config including encoder settings and others.
class ResetDialog(wx.Dialog):
	def __init__(self, parent):
		# Translators: Title of the dialog to reset various add-on settings.
		super().__init__(parent, title=_("Reset settings"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		resetHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: the label for a checkbox in SPL add-on settings
		# to reset instant switch profile.
		resetInstantProfileLabel = _("Reset instant switch profile")
		self.resetInstantProfileCheckbox = resetHelper.addItem(
			wx.CheckBox(self, label=resetInstantProfileLabel)
		)

		# Translators: the label for a checkbox in SPL add-on settings
		# to reset encoder settings.
		resetEncodersLabel = _("Remove encoder settings")
		self.resetEncodersCheckbox = resetHelper.addItem(wx.CheckBox(self, label=resetEncodersLabel))

		# Translators: the label for a checkbox in SPL add-on settings
		# to reset track comments.
		resetTrackCommentsLabel = _("Erase track comments")
		self.resetTrackCommentsCheckbox = resetHelper.addItem(
			wx.CheckBox(self, label=resetTrackCommentsLabel)
		)

		resetHelper.addDialogDismissButtons(wx.OK | wx.CANCEL, separated=True)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(resetHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.resetInstantProfileCheckbox.SetFocus()
		self.CenterOnScreen()

	def onOk(self, evt):
		parent = self.Parent
		if (
			gui.messageBox(
				# Translators: A message to warn about resetting SPL config settings to factory defaults.
				_("Are you sure you wish to reset SPL add-on settings to defaults?"),
				# Translators: The title of the warning dialog.
				_("Warning"),
				wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING,
				self,
			)
			!= wx.YES
		):
			parent.Enable()
			self.Destroy()
			return
		# Reset all profiles.
		# Only a priveleged thread should do this, otherwise unexpected things may happen.
		with threading.Lock():
			global _configDialogOpened
			# Call config reset method.
			# Without an exception, reset will continue.
			try:
				splconfig.SPLConfig.reset(factoryDefaults=True, resetViaConfigDialog=True)
			except RuntimeError:
				return
			if self.resetInstantProfileCheckbox.Value:
				if splconfig.SPLConfig.instantSwitch is not None:
					splconfig.SPLConfig.instantSwitch = None
					splconfig.SPLConfig.prevProfile = None
			if self.resetTrackCommentsCheckbox.Value:
				splconfig.trackComments.clear()
			if self.resetEncodersCheckbox.Value:
				if "appModules.splengine.encoders" in sys.modules:
					from appModules.splengine import encoders
					encoders.resetEncoderConfig(factoryDefaults=True)
			_configDialogOpened = False
			wx.CallAfter(
				# Translators: A dialog message shown when settings were reset to defaults.
				gui.messageBox,
				_("Successfully applied default add-on settings."),
				# Translators: Title of the reset config dialog.
				_("Reset configuration"),
				wx.OK | wx.ICON_INFORMATION,
			)
		self.Destroy()
		# #6: because the parent isn't add-on settings but the categories/panel sizer, fetch its ancestor.
		parent.Parent.Parent.Destroy()

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()


# Reset panel.
class ResetSettingsPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: title of a panel to reset add-on settings.
	title = _("Reset settings")

	def makeSettings(self, settingsSizer):
		resetHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		labelText = _(
			# Translators: Help text explaining what will happen when settings are reset.
			"Warning! "
			"Selecting Reset button and choosing various reset options "
			"will reset add-on settings to defaults."
		)
		resetHelper.addItem(wx.StaticText(self, label=labelText))

		# Translators: The label of a button to open reset dialog.
		resetButton = resetHelper.addItem(wx.Button(self, label=_("Reset settings...")))
		resetButton.Bind(wx.EVT_BUTTON, self.onResetConfig)

	def onSave(self):
		# Without this, not implemented error is raised by the superclass.
		pass

	def onResetConfig(self, evt):
		ResetDialog(self).ShowModal()


# Configuration dialog.
_configDialogOpened = False


class SPLConfigDialog(gui.MultiCategorySettingsDialog):
	# Translators: This is the label for the StationPlaylist add-on configuration dialog.
	title = _("StationPlaylist Add-on Settings")
	categoryClasses = [
		GeneralSettingsPanel,
		AlarmsPanel,
		PlaylistSnapshotsPanel,
		MetadataStreamingPanel,
		ColumnAnnouncementsPanel,
		ColumnsExplorerPanel,
		PlaylistTranscriptsPanel,
		SayStatusPanel,
	]
	# Security: only add the following panels if not in secure mode.
	if not globalVars.appArgs.secure:
		categoryClasses.append(AdvancedOptionsPanel)
		categoryClasses.append(ResetSettingsPanel)

	def makeSettings(self, settingsSizer):
		super(SPLConfigDialog, self).makeSettings(settingsSizer)
		global _configDialogOpened
		# #40: respond to app terminate notification by closing this dialog.
		# All top-level dialogs will be affected by this, and apart from this one, others will check for flags also.
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)
		# Let everyone know add-on settings is opened.
		_configDialogOpened = True

	def onOk(self, evt):
		super(SPLConfigDialog, self).onOk(evt)
		global _configDialogOpened
		_configDialogOpened = False

	def onCancel(self, evt):
		super(SPLConfigDialog, self).onCancel(evt)
		global _configDialogOpened
		_configDialogOpened = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)


# Open various add-on settings dialogs.


# Centralize error handling for various SPL add-on settings dialogs.
# The below error message came directly from NVDA Core's settings dialog opener method (credit: NV Access)
def configDialogOpenError() -> None:
	gui.messageBox(
		translate("An NVDA settings dialog is already open. Please close it first."),
		translate("Error"),
		style=wx.OK | wx.ICON_ERROR,
	)


# #125: open any settings panel from main add-on settings, also checking if other dialogs are open.
def openAddonSettingsPanel(panel: gui.settingsDialogs.SettingsPanel):
	if _configDialogOpened:
		wx.CallAfter(configDialogOpenError)
	else:
		gui.mainFrame.popupSettingsDialog(SPLConfigDialog, panel)


# Main add-on settings screen.
def onConfigDialog(evt):
	wx.CallAfter(openAddonSettingsPanel, None)


# Open broadcast profiles dialog and its friends upon request.
def onBroadcastProfilesDialog(evt):
	if _configDialogOpened:
		wx.CallAfter(configDialogOpenError)
		return
	# Present an error message if only normal profile is in use.
	if splconfig.SPLConfig.configInMemory or splconfig.SPLConfig.normalProfileOnly:
		wx.CallAfter(
			# Translators: presented when only normal profile is in use.
			gui.messageBox,
			_("Normal profile is in use, cannot open broadcast profiles dialog."),
			_("SPL Broadcast Profiles"),
			wx.OK | wx.ICON_ERROR,
		)
		return
	gui.mainFrame.prePopup()
	BroadcastProfilesDialog(gui.mainFrame).Show()
	gui.mainFrame.postPopup()


# Disable instant profile switching if a config dialogs (including broadcast profiles dialog) is open.
def instantProfileSwitchConfigUICheck() -> None:
	# #118: do not allow profile switching while add-on settings screen is shown.
	if _configDialogOpened:
		# Translators: Presented when trying to switch to an instant switch profile
		# when add-on settings dialog is active.
		ui.message(_("Add-on settings dialog is open, cannot switch profiles"))
		return
	splconfig.instantProfileSwitch()
