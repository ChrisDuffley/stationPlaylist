# SPL Studio Configuration user interfaces
# An app module and global plugin package for NVDA
# Copyright 2016-2020 Joseph Lee and others, released under GPL.
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
from winUser import user32
import tones
import addonHandler
addonHandler.initTranslation()
from . import splconfig
from . import splactions
from ..skipTranslation import translate

# Due to syntax/variable name issues, the actual add-on settings class can be found at the end of this module.

# Helper panels/dialogs for add-on settings dialog.


# Broadcast profiles
# #129 (20.04): formerly a settings panel, now a dedicated settings dialog.
class BroadcastProfilesDialog(wx.Dialog):
	shouldSuspendConfigProfileTriggers = True

	def __init__(self, parent):
		# Translators: title of a dialog to configure broadcast profiles.
		super(BroadcastProfilesDialog, self).__init__(parent, title=_("SPL Broadcast Profiles"))
		global _configDialogOpened
		_configDialogOpened = True
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		broadcastProfilesHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		# Profiles list and activate button on the left, management buttons on the right (credit: NV Access).
		profilesListGroupSizer = wx.StaticBoxSizer(wx.StaticBox(self), wx.HORIZONTAL)
		profilesListGroupContents = wx.BoxSizer(wx.HORIZONTAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		# Broadcast profile controls were inspired by Config Profiles dialog in NVDA Core.
		# 7.0: Have a copy of the sorted profiles so the actual combo box items can show profile flags.
		# 8.0: No need to sort as profile names from ConfigHub knows what to do.
		# 17.10: skip this if only normal profile is in use.
		# #6: display a read-only explanatory text.
		# #129 (20.04): explanatory text will be provided when attempting to open this dialog, not here.
		self.profileNames = list(splconfig.SPLConfig.profileNames)
		self.profileNames[0] = splconfig.defaultProfileName
		changeProfilesSizer = wx.BoxSizer(wx.VERTICAL)
		self.profiles = wx.ListBox(self, choices=self.displayProfiles(list(self.profileNames)))
		self.profiles.Bind(wx.EVT_LISTBOX, self.onProfileSelection)
		try:
			self.profiles.SetSelection(self.profileNames.index(splconfig.SPLConfig.activeProfile))
		except:
			pass
		changeProfilesSizer.Add(self.profiles, proportion=1.0)
		changeProfilesSizer.AddSpacer(gui.guiHelper.SPACE_BETWEEN_BUTTONS_VERTICAL)

		# Borrowed directly from NvDA Core (credit: NV Access)
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
		# Most control labels come from NvDA Core.
		# 17.10: if restrictions such as volatile config are applied, disable this area entirely.
		# #129 (20.04): no need for this check in standalone dialog.
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
		if self.profiles.GetSelection() == 0:
			self.renameButton.Disable()
			self.deleteButton.Disable()
			self.triggerButton.Disable()
		profilesListGroupContents.Add(buttonHelper.sizer)
		profilesListGroupSizer.Add(profilesListGroupContents, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		broadcastProfilesHelper.addItem(profilesListGroupSizer)
		self.switchProfile = splconfig.SPLConfig.instantSwitch
		self.activeProfile = splconfig.SPLConfig.activeProfile
		# Used as sanity check in case switch profile is renamed or deleted.
		self.switchProfileRenamed = False
		self.switchProfileDeleted = False

		# Close button logic comes from NVDA Core (credit: NV Access)
		closeButton = wx.Button(self, wx.ID_CLOSE, label=translate("&Close"))
		closeButton.Bind(wx.EVT_BUTTON, lambda evt: self.Close())
		broadcastProfilesHelper.addDialogDismissButtons(closeButton)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.EscapeId = wx.ID_CLOSE

		mainSizer.Add(broadcastProfilesHelper.sizer, flag=wx.ALL, border=gui.guiHelper.BORDER_FOR_DIALOGS)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.profiles.SetFocus()
		self.CentreOnScreen()

	# Include profile flags such as instant profile string for display purposes.
	def displayProfiles(self, profiles):
		for index in range(len(profiles)):
			profiles[index] = splconfig.getProfileFlags(profiles[index])
		return profiles

	# Load settings from profiles.
	# #6: set selected profile flag so other panels can pull in appropriate settings.
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
		if selection == 0:
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
		# #70 (18.07): in wxPython 4, name for the value keyword argument for text entry dialog constructor has changed.
		with wx.TextEntryDialog(
			# Translators: The label of a field to enter a new name for a broadcast profile.
			self, _("New name:"),
			# Translators: The title of the dialog to rename a profile.
			_("Rename Profile"), value=oldName
		) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
			newName = api.filterFileName(d.Value)
		if oldName == newName: return
		try:
			splconfig.SPLConfig.renameProfile(oldName, newName)
		except RuntimeError:
			gui.messageBox(
				# Translators: An error displayed when renaming a configuration profile
				# and a profile with the new name already exists.
				_("That profile already exists. Please choose a different name."),
				translate("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		if self.switchProfile == oldName:
			self.switchProfile = newName
			self.switchProfileRenamed = True
		if self.activeProfile == oldName:
			self.activeProfile = newName
		self.profileNames[profilePos] = newName
		if oldName in splconfig._SPLCache:
			splconfig._SPLCache[newName] = splconfig._SPLCache[oldName]
			del splconfig._SPLCache[oldName]
		self.profiles.SetString(index, " <".join([newName, state[1]]) if len(state) > 1 else newName)
		self.profiles.Selection = index
		self.profiles.SetFocus()

	def onDelete(self, evt):
		# Prevent profile deletion while a trigger is active (in the midst of a broadcast), otherwise flags such as instant switch and time-based profiles become inconsistent.
		# 6.4: This was seen after deleting a profile one position before the previously active profile.
		# 7.0: One should never delete the currently active time-based profile.
		# 7.1: Find a way to safely proceed via two-step verification if trying to delete currently active time-based profile.
		# 20.06: just focus on instant switch profile.
		if splconfig.SPLConfig.prevProfile is not None:
			gui.messageBox(
				# Translators: Message reported when attempting to delete a profile in the midst of a broadcast.
				_("An instant switch profile might be active or you are in the midst of a broadcast. If so, please press SPL Assistant, F12 to switch back to a previously active profile before opening broadcast profiles dialog to delete a profile."),
				# Translators: Title of a dialog shown when profile cannot be deleted.
				_("Profile delete error"), wx.OK | wx.ICON_ERROR, self)
			return
		name = self.profiles.GetStringSelection().split(" <")[0]
		# 17.11/15.10-lts: ask once more if deleting an active profile.
		if name == self.activeProfile:
			if gui.messageBox(
				# Translators: The confirmation prompt displayed when the user requests to delete the active broadcast profile.
				_("You are about to delete the currently active profile. Select yes if you wish to proceed."),
				# Translators: The title of the confirmation dialog for deletion of a profile.
				_("Delete active profile"),
				wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self
			) == wx.NO:
				return
		index = self.profiles.Selection
		profilePos = self.profileNames.index(name)
		if gui.messageBox(
			# Translators: The confirmation prompt displayed when the user requests to delete a broadcast profile.
			_("Are you sure you want to delete this profile? This cannot be undone."),
			# Translators: The title of the confirmation dialog for deletion of a profile.
			_("Confirm Deletion"),
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self
		) == wx.NO:
			return
		splconfig.SPLConfig.deleteProfile(name)
		# 17.11: make sure to connect to the right set of metadata servers and enable/disable microphone alarm if appropriate.
		splactions.SPLActionProfileSwitched.notify(configDialogActive=True)
		if name == self.switchProfile or name == self.activeProfile:
			# 17.11/15.10-LTS: go through the below path if and only if instant switch profile is gone.
			if name == self.switchProfile:
				self.switchProfile = None
				splconfig.SPLConfig.prevProfile = None
			self.switchProfileDeleted = True
		self.profiles.Delete(index)
		del self.profileNames[profilePos]
		if name in splconfig._SPLCache: del splconfig._SPLCache[name]
		# 6.3: Select normal profile if the active profile is gone.
		# 7.0: Consult profile names instead.
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
	def getProfileFlags(self, name):
		return splconfig.getProfileFlags(name, active=self.activeProfile, instant=self.switchProfile, contained=True)

	# Handle flag modifications such as when toggling instant switch.
	# Unless given, flags will be queried.
	# This is a sister function to profile flags retriever.
	def setProfileFlags(self, index, action, flag, flags=None):
		profile = self.profileNames[index]
		if flags is None: flags = self.getProfileFlags(profile)
		action = getattr(flags, action)
		action(flag)
		self.profiles.SetString(index, profile if not len(flags) else "{0} <{1}>".format(profile, ", ".join(flags)))

	def onChangeState(self, evt):
		selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
		if splconfig.SPLConfig.activeProfile != selectedProfile:
			splconfig.SPLConfig.swapProfiles(splconfig.SPLConfig.activeProfile, selectedProfile)
			# 8.0: Make sure NVDA knows this must be cached (except for normal profile).
			# 17.10: but not when config is volatile.
			# #71 (18.07): must be done here, otherwise cache failure occurs where settings won't be saved when in fact it may have been changed from add-on settings.
			try:
				if selectedProfile != splconfig.defaultProfileName and selectedProfile not in splconfig._SPLCache:
					splconfig.SPLConfig._cacheConfig(splconfig.SPLConfig.profileByName(selectedProfile))
			except NameError:
				pass
		splconfig.SPLConfig.instantSwitch = self.switchProfile
		# Make sure to nullify prev profile if instant switch profile is gone.
		# 7.0: Don't do the following in the midst of a broadcast.
		# 20.07: find a way to work around this as time-based profiles feature is gone.
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


# New broadcast profile dialog: Modification of new config profile dialog from NvDA Core.
class NewProfileDialog(wx.Dialog):

	def __init__(self, parent, copy=False):
		self.copy = copy
		if not self.copy:
			# Translators: The title of the dialog to create a new broadcast profile.
			dialogTitle = _("New Profile")
		else:
			# Translators: The title of the dialog to copy a broadcast profile.
			dialogTitle = _("Copy Profile")
		super(NewProfileDialog, self).__init__(parent, title=dialogTitle)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		newProfileSizerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: The label of a field to enter the name of a new broadcast profile.
		self.profileName = newProfileSizerHelper.addLabeledControl(_("Profile name:"), wx.TextCtrl)

		if self.copy:
			# Translators: The label for a setting in SPL add-on dialog to select a base  profile for copying.
			self.baseProfiles = newProfileSizerHelper.addLabeledControl(_("&Base profile:"), wx.Choice, choices=parent.profileNames)
			try:
				self.baseProfiles.SetSelection(parent.profiles.GetSelection())
			except:
				pass

		newProfileSizerHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(newProfileSizerHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.profileName.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		name = api.filterFileName(self.profileName.Value)
		if not name:
			return
		if name in parent.profileNames:
			gui.messageBox(
				# Translators: An error displayed when the user attempts to create a profile which already exists.
				_("That profile already exists. Please choose a different name."),
				translate("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		namePath = name + ".ini"
		if not os.path.exists(splconfig.SPLProfiles):
			os.mkdir(splconfig.SPLProfiles)
		newProfilePath = os.path.join(splconfig.SPLProfiles, namePath)
		# LTS optimization: just build base profile dictionary here if copying a profile.
		if self.copy:
			baseConfig = splconfig.SPLConfig.profileByName(self.baseProfiles.GetStringSelection())
			# #140 (20.07): it isn't enough to copy dictionaries - deep copy (config.dict()) must be performed to avoid accidental reference manipulation.
			baseProfile = {sect: key for sect, key in baseConfig.dict().items() if sect in splconfig._mutatableSettings}
		else: baseProfile = None
		splconfig.SPLConfig.createProfile(newProfilePath, profileName=name, parent=baseProfile)
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
# This dialog is similar to NVDA Core's profile triggers dialog and allows one to configure when to trigger this profile.
class TriggersDialog(wx.Dialog):

	def __init__(self, parent, profile):
		# Translators: The title of the broadcast profile triggers dialog.
		super(TriggersDialog, self).__init__(parent, title=_("Profile triggers for {profileName}").format(profileName=profile))
		self.profile = profile
		self.selection = parent.profiles.GetSelection()
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		triggersHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: The label of a checkbox to toggle if selected profile is an instant switch profile.
		self.instantSwitchCheckbox = triggersHelper.addItem(wx.CheckBox(self, label=_("This is an &instant switch profile")))
		self.instantSwitchCheckbox.SetValue(parent.switchProfile == profile)

		triggersHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(triggersHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.instantSwitchCheckbox.SetFocus()

	def onOk(self, evt):
		parent = self.Parent
		# Handle instant switch checkbox.
		if self.instantSwitchCheckbox.Value:
			if parent.switchProfile is not None and (self.profile != parent.switchProfile):
				# Instant switch flag is set on another profile, so remove the flag first.
				parent.setProfileFlags(parent.profileNames.index(parent.switchProfile), "discard", _("instant switch"))
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
class GeneralSettingsPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure various general add-on settings such as top and bottom announcement for playlists.
	title = _("General")

	def makeSettings(self, settingsSizer):
		generalSettingsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: the label for a setting in SPL add-on settings to set status announcement between words and beeps.
		self.beepAnnounceCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("&Beep for status announcements")))
		self.beepAnnounceCheckbox.SetValue(splconfig.SPLConfig["General"]["BeepAnnounce"])

		self.verbosityLevels = [
			# Translators: One of the message verbosity levels.
			("beginner", _("beginner")),
			# Translators: One of the message verbosity levels.
			("advanced", _("advanced"))
		]
		# Translators: The label for a setting in SPL add-on dialog to set message verbosity.
		self.verbosityList = generalSettingsHelper.addLabeledControl(_("Message &verbosity:"), wx.Choice, choices=[x[1] for x in self.verbosityLevels])
		currentVerbosity = splconfig.SPLConfig["General"]["MessageVerbosity"]
		selection = next((x for x, y in enumerate(self.verbosityLevels) if y[0] == currentVerbosity))
		try:
			self.verbosityList.SetSelection(selection)
		except:
			pass

		self.brailleTimerValues = [
			("off", _("Off")),
			# Translators: One of the braille timer settings.
			("outro", _("Track ending")),
			# Translators: One of the braille timer settings.
			("intro", _("Track intro")),
			# Translators: One of the braille timer settings.
			("both", _("Track intro and ending"))
		]
		# Translators: The label for a setting in SPL add-on dialog to control braille timer.
		self.brailleTimerList = generalSettingsHelper.addLabeledControl(_("&Braille timer:"), wx.Choice, choices=[x[1] for x in self.brailleTimerValues])
		brailleTimerCurValue = splconfig.SPLConfig["General"]["BrailleTimer"]
		selection = next((x for x, y in enumerate(self.brailleTimerValues) if y[0] == brailleTimerCurValue))
		try:
			self.brailleTimerList.SetSelection(selection)
		except:
			pass

		self.libScanValues = [
			("off", _("Off")),
			# Translators: One of the library scan announcement settings.
			("ending", _("Start and end only")),
			# Translators: One of the library scan announcement settings.
			("progress", _("Scan progress")),
			# Translators: One of the library scan announcement settings.
			("numbers", _("Scan count"))
		]
		# Translators: The label for a setting in SPL add-on dialog to control library scan announcement.
		self.libScanList = generalSettingsHelper.addLabeledControl(_("&Library scan announcement:"), wx.Choice, choices=[x[1] for x in self.libScanValues])
		libScanCurValue = splconfig.SPLConfig["General"]["LibraryScanAnnounce"]
		selection = next((x for x, y in enumerate(self.libScanValues) if y[0] == libScanCurValue))
		try:
			self.libScanList.SetSelection(selection)
		except:
			pass

		# Translators: the label for a setting in SPL add-on settings to announce time including hours.
		self.hourAnnounceCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("Include &hours when announcing track or playlist duration")))
		self.hourAnnounceCheckbox.SetValue(splconfig.SPLConfig["General"]["TimeHourAnnounce"])

		# Translators: The label for a setting in SPL add-on dialog to set vertical column.
		verticalColLabel = _("&Vertical column navigation announcement:")
		# Translators: One of the options for vertical column navigation denoting NVDA will announce current column positoin (e.g. second column position from the left).
		self.verticalColumnsList = generalSettingsHelper.addLabeledControl(verticalColLabel, wx.Choice, choices=[_("whichever column I am reviewing"), "Status"] + splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"])
		verticalColumn = splconfig.SPLConfig["General"]["VerticalColumnAnnounce"]
		selection = self.verticalColumnsList.FindString(verticalColumn) if verticalColumn is not None else 0
		try:
			self.verticalColumnsList.SetSelection(selection)
		except:
			pass

		# Translators: the label for a setting in SPL add-on settings to toggle category sound announcement.
		self.categorySoundsCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("&Beep for different track categories")))
		self.categorySoundsCheckbox.SetValue(splconfig.SPLConfig["General"]["CategorySounds"])

		self.trackCommentValues = [
			("off", _("Off")),
			# Translators: One of the track comment notification settings.
			("message", _("Message")),
			# Translators: One of the track comment notification settings.
			("beep", _("Beep")),
			# Translators: One of the track comment notification settings.
			("both", _("Both"))
		]
		# Translators: the label for a setting in SPL add-on settings to set how track comments are announced.
		self.trackCommentList = generalSettingsHelper.addLabeledControl(_("&Track comment announcement:"), wx.Choice, choices=[x[1] for x in self.trackCommentValues])
		trackCommentCurValue = splconfig.SPLConfig["General"]["TrackCommentAnnounce"]
		selection = next((x for x, y in enumerate(self.trackCommentValues) if y[0] == trackCommentCurValue))
		try:
			self.trackCommentList.SetSelection(selection)
		except:
			pass

		# Translators: the label for a setting in SPL add-on settings to toggle top and bottom notification.
		self.topBottomCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("Notify when located at &top or bottom of playlist viewer")))
		self.topBottomCheckbox.SetValue(splconfig.SPLConfig["General"]["TopBottomAnnounce"])

		# Translators: the label for a setting in SPL add-on settings to enable requests alert.
		self.requestsAlertCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("Play a sound when listener &requests arrive")))
		self.requestsAlertCheckbox.SetValue(splconfig.SPLConfig["General"]["RequestsAlert"])

	def onSave(self):
		splconfig.SPLConfig["General"]["BeepAnnounce"] = self.beepAnnounceCheckbox.Value
		splconfig.SPLConfig["General"]["MessageVerbosity"] = self.verbosityLevels[self.verbosityList.GetSelection()][0]
		splconfig.SPLConfig["General"]["BrailleTimer"] = self.brailleTimerValues[self.brailleTimerList.GetSelection()][0]
		splconfig.SPLConfig["General"]["LibraryScanAnnounce"] = self.libScanValues[self.libScanList.GetSelection()][0]
		splconfig.SPLConfig["General"]["TimeHourAnnounce"] = self.hourAnnounceCheckbox.Value
		splconfig.SPLConfig["General"]["VerticalColumnAnnounce"] = self.verticalColumnsList.GetStringSelection() if self.verticalColumnsList.GetSelection() != 0 else None
		splconfig.SPLConfig["General"]["CategorySounds"] = self.categorySoundsCheckbox.Value
		splconfig.SPLConfig["General"]["TrackCommentAnnounce"] = self.trackCommentValues[self.trackCommentList.GetSelection()][0]
		splconfig.SPLConfig["General"]["TopBottomAnnounce"] = self.topBottomCheckbox.Value
		splconfig.SPLConfig["General"]["RequestsAlert"] = self.requestsAlertCheckbox.Value


# Various alarm settings (outro, intro, microphone).
class AlarmsPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure various alarms and related settings.
	title = _("Alarms")

	def makeSettings(self, settingsSizer):
		alarmsCenterHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		self.outroAlarmEntry = alarmsCenterHelper.addLabeledControl(_("&End of track alarm in seconds"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=1, max=59, initial=splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"])
		self.outroToggleCheckBox = alarmsCenterHelper.addItem(wx.CheckBox(self, label=_("&Notify when end of track is approaching")))
		self.outroToggleCheckBox.SetValue(splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"])

		self.introAlarmEntry = alarmsCenterHelper.addLabeledControl(_("&Track intro alarm in seconds"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=1, max=9, initial=splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"])
		self.introToggleCheckBox = alarmsCenterHelper.addItem(wx.CheckBox(self, label=_("&Notify when end of introduction is approaching")))
		self.introToggleCheckBox.SetValue(splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"])

		self.micAlarmEntry = alarmsCenterHelper.addLabeledControl(_("&Microphone alarm in seconds (0 disables the alarm)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=7200, initial=splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"])
		self.micIntervalEntry = alarmsCenterHelper.addLabeledControl(_("Microphone alarm &interval in seconds"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=60, initial=splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"])

		self.alarmAnnounceValues = [
			# Translators: One of the alarm notification options.
			("beep", _("beep")),
			# Translators: One of the alarm notification options.
			("message", _("message")),
			# Translators: One of the alarm notification options.
			("both", _("both beep and message"))
		]
		# Translators: The label for a setting in SPL add-on dialog to control alarm announcement type.
		self.alarmAnnounceList = alarmsCenterHelper.addLabeledControl(_("&Alarm notification:"), wx.Choice, choices=[x[1] for x in self.alarmAnnounceValues])
		alarmAnnounceCurValue = splconfig.SPLConfig["General"]["AlarmAnnounce"]
		selection = next((x for x, y in enumerate(self.alarmAnnounceValues) if y[0] == alarmAnnounceCurValue))
		try:
			self.alarmAnnounceList.SetSelection(selection)
		except:
			pass

	def onSave(self):
		splconfig.SPLConfig["General"]["AlarmAnnounce"] = self.alarmAnnounceValues[self.alarmAnnounceList.GetSelection()][0]
		splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"] = self.outroAlarmEntry.GetValue()
		splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"] = self.outroToggleCheckBox.GetValue()
		splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"] = self.introAlarmEntry.GetValue()
		splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"] = self.introToggleCheckBox.GetValue()
		splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"] = self.micAlarmEntry.GetValue()
		splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] = self.micIntervalEntry.GetValue()
		# #42 (18.01/15.12-LTS): don't forget to restart microphone alarm timer.
		# 18.02: do it here at once.
		# At least try notifying the app module that microphone alarm settings have changed.
		from winUser import OBJID_CLIENT
		from NVDAObjects.IAccessible import getNVDAObjectFromEvent
		studioWindow = getNVDAObjectFromEvent(user32.FindWindowW("TStudioForm", None), OBJID_CLIENT, 0)
		if studioWindow is not None: studioWindow.appModule.actionProfileSwitched()


# Playlist snapshot flags
# For things such as checkboxes for average duration and top category count.
class PlaylistSnapshotsPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure playlist snapshot information.
	title = _("Playlist snapshots")

	def makeSettings(self, settingsSizer):
		playlistSnapshotsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: Help text for playlist snapshots dialog.
		labelText = _("""Select information to be included when obtaining playlist snapshots.
		Track count and total duration are always included.""")
		playlistSnapshotsHelper.addItem(wx.StaticText(self, label=labelText))

		# Translators: the label for a setting in SPL add-on settings to include shortest and longest track duration in playlist snapshots window.
		self.playlistDurationMinMaxCheckbox = playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Shortest and longest tracks")))
		self.playlistDurationMinMaxCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["DurationMinMax"])
		# Translators: the label for a setting in SPL add-on settings to include average track duration in playlist snapshots window.
		self.playlistDurationAverageCheckbox = playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Average track duration")))
		self.playlistDurationAverageCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["DurationAverage"])
		# Translators: the label for a setting in SPL add-on settings to include track artist count in playlist snapshots window.
		self.playlistArtistCountCheckbox = playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Artist count")))
		self.playlistArtistCountCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCount"])
		# Translators: the label for a setting in SPL add-on settings to set top artist count limit in playlist snapshots window.
		self.playlistArtistCountLimit = playlistSnapshotsHelper.addLabeledControl(_("Top artist count (0 displays all artists)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"])
		# Translators: the label for a setting in SPL add-on settings to include track category count in playlist snapshots window.
		self.playlistCategoryCountCheckbox = playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Category count")))
		self.playlistCategoryCountCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCount"])
		# Translators: the label for a setting in SPL add-on settings to set top track category count limit in playlist snapshots window.
		self.playlistCategoryCountLimit = playlistSnapshotsHelper.addLabeledControl(_("Top category count (0 displays all categories)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"])
		# Translators: the label for a setting in SPL add-on settings to include track genre count in playlist snapshots window.
		self.playlistGenreCountCheckbox = playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Genre count")))
		self.playlistGenreCountCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["GenreCount"])
		# Translators: the label for a setting in SPL add-on settings to set top track genre count limit in playlist snapshots window.
		self.playlistGenreCountLimit = playlistSnapshotsHelper.addLabeledControl(_("Top genre count (0 displays all genres)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"])
		# Translators: the label for a setting in SPL add-on settings to show playlist snaphsots window when the snapshots command is pressed once.
		self.resultsWindowOnFirstPressCheckbox = playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("&Show results window when playlist snapshots command is performed once")))
		self.resultsWindowOnFirstPressCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["ShowResultsWindowOnFirstPress"])

	def onSave(self):
		splconfig.SPLConfig["PlaylistSnapshots"]["DurationMinMax"] = self.playlistDurationMinMaxCheckbox.Value
		splconfig.SPLConfig["PlaylistSnapshots"]["DurationAverage"] = self.playlistDurationAverageCheckbox.Value
		splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCount"] = self.playlistArtistCountCheckbox.Value
		splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"] = self.playlistArtistCountLimit.GetValue()
		splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCount"] = self.playlistCategoryCountCheckbox.Value
		splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"] = self.playlistCategoryCountLimit.GetValue()
		splconfig.SPLConfig["PlaylistSnapshots"]["GenreCount"] = self.playlistGenreCountCheckbox.Value
		splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"] = self.playlistGenreCountLimit.GetValue()
		splconfig.SPLConfig["PlaylistSnapshots"]["ShowResultsWindowOnFirstPress"] = self.resultsWindowOnFirstPressCheckbox.Value


# Metadata reminder controller.
# Select notification/streaming URL's for metadata streaming.
metadataStreamLabels = ("DSP encoder", "URL 1", "URL 2", "URL 3", "URL 4")


class MetadataStreamingDialog(wx.Dialog):
	"""A dialog to toggle metadata streaming quickly and optionally save changes to add-on configuration.
	"""
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _configDialogOpened:
			raise RuntimeError("An instance of metadata streaming dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent):
		inst = MetadataStreamingDialog._instance() if MetadataStreamingDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		MetadataStreamingDialog._instance = weakref.ref(self)

		# Translators: Title of a dialog to configure metadata streaming status for DSP encoder and four additional URL's.
		super(MetadataStreamingDialog, self).__init__(parent, title=_("Metadata streaming options"))
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		metadataSizerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		labelText = _("Check to enable metadata streaming, uncheck to disable.")
		metadataSizerHelper.addItem(wx.StaticText(self, label=labelText))

		# WX's native CheckListBox isn't user friendly.
		# Therefore use checkboxes laid out across the top.
		# 17.04: instead of two loops, just use one loop, with labels deriving from a stream labels tuple.
		# Only one loop is needed as helper.addLabelControl returns the checkbox itself and that can be appended.
		# Add checkboxes for each stream, beginning with the DSP encoder.
		# #76 (18.09-LTS): completely changed to use custom check list box (NVDA Core issue 7491).
		from . import splmisc
		streams = splmisc.metadataList()
		self.checkedStreams = metadataSizerHelper.addLabeledControl(_("&Stream:"), CustomCheckListBox, choices=metadataStreamLabels)
		for stream in range(5):
			self.checkedStreams.Check(stream, check=streams[stream])
		self.checkedStreams.SetSelection(0)

		# Translators: A checkbox to let metadata streaming status be applied to the currently active broadcast profile.
		self.applyCheckbox = metadataSizerHelper.addItem(wx.CheckBox(self, label=_("&Apply streaming changes to the selected profile")))
		self.applyCheckbox.SetValue(True)

		metadataSizerHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(metadataSizerHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedStreams.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global _configDialogOpened
		# Prepare checkbox values first for various reasons.
		# #76 (18.09-LTS): traverse check list box and build boolean list accordingly.
		metadataEnabled = [self.checkedStreams.IsChecked(url) for url in range(5)]
		from . import splmisc
		splmisc.metadataConnector(servers=metadataEnabled)
		# 6.1: Store just toggled settings to profile if told to do so.
		if self.applyCheckbox.Value: splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"] = metadataEnabled
		self.Destroy()
		_configDialogOpened = False

	def onCancel(self, evt):
		global _configDialogOpened
		self.Destroy()
		_configDialogOpened = False

	def onAppTerminate(self):
		self.onCancel(None)


class MetadataStreamingPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure metadata streaming status for DSP encoder and four additional URL's.
	title = _("Metadata streaming")

	def makeSettings(self, settingsSizer):
		metadataSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		self.metadataValues = [
			("off", _("Off")),
			# Translators: One of the metadata notification settings.
			("startup", _("When Studio starts")),
			# Translators: One of the metadata notification settings.
			("instant", _("When instant switch profile is active"))
		]
		# Translators: the label for a setting in SPL add-on settings to be notified that metadata streaming is enabled.
		self.metadataList = metadataSizerHelper.addLabeledControl(_("&Metadata streaming notification and connection"), wx.Choice, choices=[x[1] for x in self.metadataValues])
		metadataCurValue = splconfig.SPLConfig["General"]["MetadataReminder"]
		selection = next((x for x, y in enumerate(self.metadataValues) if y[0] == metadataCurValue))
		try:
			self.metadataList.SetSelection(selection)
		except:
			pass

		# WX's native CheckListBox isn't user friendly.
		# Therefore use checkboxes laid out across the top.
		# 17.04: instead of two loops, just use one loop, with labels deriving from a stream labels tuple.
		# Only one loop is needed as helper.addLabelControl returns the checkbox itself and that can be appended.
		# Add checkboxes for each stream, beginning with the DSP encoder.
		# #76 (18.09-LTS): completely changed to use custom check list box (NVDA Core issue 7491).
		self.checkedStreams = metadataSizerHelper.addLabeledControl(_("&Select the URL for metadata streaming upon request:"), CustomCheckListBox, choices=metadataStreamLabels)
		for stream in range(5):
			self.checkedStreams.Check(stream, check=splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"][stream])
		self.checkedStreams.SetSelection(0)

	def onSave(self):
		splconfig.SPLConfig["General"]["MetadataReminder"] = self.metadataValues[self.metadataList.GetSelection()][0]
		# #76 (18.09-LTS): traverse check list box and build boolean list accordingly.
		splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"] = [self.checkedStreams.IsChecked(url) for url in range(5)]
		# Try connecting to metadata streaming servers if any.
		from . import splmisc
		splmisc.metadata_actionProfileSwitched(configDialogActive=True)


# Column announcement manager.
# Select which track columns should be announced and in which order.
# 18.08: also serves as a base dialog for Playlist Transcripts/column selector setting.
# #97 (19.04): converted into a base panel (to be flagged as "abstract" later).
class ColumnAnnouncementsBasePanel(gui.SettingsPanel):

	def _onMakeSettingsBase(self, sHelper, includedColumnsLabel):
		# Provides common user interface elements for column inclusion/order controls across settings panels (leave it as a private method).

		# Same as metadata dialog (wx.CheckListBox isn't user friendly).
		# Gather values for checkboxes except artist and title.
		# 6.1: Split these columns into rows.
		# 17.04: Gather items into a single list instead of three.
		# #76 (18.09-LTS): completely changed to use custom check list box (NVDA Core issue 7491).
		checkableColumns = ("Duration", "Intro", "Category", "Filename", "Outro", "Year", "Album", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "Time Scheduled")
		self.checkedColumns = sHelper.addLabeledControl(includedColumnsLabel, CustomCheckListBox, choices=checkableColumns)
		self.checkedColumns.SetCheckedStrings(self.includedColumns)
		self.checkedColumns.SetSelection(0)

		# Translators: The label for a group in SPL add-on dialog to select column announcement order.
		columnOrderGroup = gui.guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("Column order")), wx.HORIZONTAL))
		sHelper.addItem(columnOrderGroup)

		# wxPython 4 contains RearrangeList to allow item orders to be changed automatically.
		# Due to usability quirks (focus bouncing and what not), work around by using a variant of list box and move up/down buttons.
		# 17.04: The label for the list below is above the list, so move move up/down buttons to the right of the list box.
		# 20.09: the list and move up/down buttons are now part of a grouping.
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
		if selIndex == self.trackColumns.GetCount()-1:
			self.dnButton.Disable()
		else: self.dnButton.Enable()

	def onMoveUp(self, evt):
		tones.beep(1000, 200)
		selIndex = self.trackColumns.GetSelection()
		if selIndex > 0:
			selItem = self.trackColumns.GetString(selIndex)
			self.trackColumns.Delete(selIndex)
			self.trackColumns.Insert(selItem, selIndex-1)
			self.trackColumns.Select(selIndex-1)
			self.onColumnSelection(None)

	def onMoveDown(self, evt):
		tones.beep(500, 200)
		selIndex = self.trackColumns.GetSelection()
		if selIndex < self.trackColumns.GetCount()-1:
			selItem = self.trackColumns.GetString(selIndex)
			self.trackColumns.Delete(selIndex)
			self.trackColumns.Insert(selItem, selIndex+1)
			self.trackColumns.Select(selIndex+1)
			self.onColumnSelection(None)
			# Hack: Wen the last item is selected, forcefully move the focus to "move up" button.
			# This will cause NVDA to say "unavailable" as focus is lost momentarily. A bit anoying but a necessary hack.
			if self.FindFocus().GetId() == wx.ID_OK:
				self.upButton.SetFocus()


class ColumnAnnouncementsPanel(ColumnAnnouncementsBasePanel):
	# Translators: title of a panel to configure column announcements (order and what columns should be announced).
	title = _("Column announcements")

	def makeSettings(self, settingsSizer):
		colAnnouncementsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Without manual conversion below, it produces a rare bug where clicking cancel after changing column inclusion causes new set to be retained.
		# Of course take away artist and title.
		self.includedColumns = set(splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"]) - {"Artist", "Title"}
		self.columnOrder = splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"]

		# Translators: the label for a setting in SPL add-on settings to toggle custom column announcement.
		self.columnOrderCheckbox = colAnnouncementsHelper.addItem(wx.CheckBox(self, wx.ID_ANY, label=_("Announce columns in the &order shown on screen")))
		self.columnOrderCheckbox.SetValue(splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"])

		# Translators: Help text to select columns to be announced.
		labelText = _("&Select columns to be announced\n(artist and title are announced by default):")

		# Same as metadata dialog (wx.CheckListBox isn't user friendly).
		# 6.1: Split these columns into rows.
		# 17.04: Gather items into a single list instead of three.
		# #76 (18.09-LTS): completely changed to use custom check list box (NVDA Core issue 7491).
		checkableColumns = ("Duration", "Intro", "Category", "Filename", "Outro", "Year", "Album", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "Time Scheduled")
		self.checkedColumns = colAnnouncementsHelper.addLabeledControl(labelText, CustomCheckListBox, choices=checkableColumns)
		self.checkedColumns.SetCheckedStrings(self.includedColumns)
		self.checkedColumns.SetSelection(0)

		# Translators: The label for a group in SPL add-on dialog to select column announcement order.
		columnOrderGroup = gui.guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("Column order")), wx.HORIZONTAL))
		colAnnouncementsHelper.addItem(columnOrderGroup)

		# wxPython 4 contains RearrangeList to allow item orders to be changed automatically.
		# Due to usability quirks (focus bouncing and what not), work around by using a variant of list box and move up/down buttons.
		# 17.04: The label for the list below is above the list, so move move up/down buttons to the right of the list box.
		# 20.09: the list and move up/down buttons are now part of a grouping.
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

		# Translators: the label for a setting in SPL add-on settings to toggle whether column headers should be included when announcing track information.
		self.columnHeadersCheckbox = colAnnouncementsHelper.addItem(wx.CheckBox(self, label=_("Include column &headers when announcing track information")))
		self.columnHeadersCheckbox.SetValue(splconfig.SPLConfig["ColumnAnnouncement"]["IncludeColumnHeaders"])

	def onSave(self):
		splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"] = self.columnOrderCheckbox.Value
		splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"] = set(self.checkedColumns.GetCheckedStrings()) | {"Artist", "Title"}
		splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"] = self.trackColumns.GetItems()
		splconfig.SPLConfig["ColumnAnnouncement"]["IncludeColumnHeaders"] = self.columnHeadersCheckbox.Value


class PlaylistTranscriptsPanel(ColumnAnnouncementsBasePanel):
	# Translators: Title of a panel to configure playlsit transcripts options.
	title = _("Playlist transcripts")

	def makeSettings(self, settingsSizer):
		playlistTranscriptsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Again manually create a new set minus artist and title.
		self.includedColumns = set(splconfig.SPLConfig["PlaylistTranscripts"]["IncludedColumns"]) - {"Artist", "Title"}
		self.columnOrder = splconfig.SPLConfig["PlaylistTranscripts"]["ColumnOrder"]

		# Translators: Help text to select columns to be announced.
		labelText = _("&Select columns to be included in playlist transcripts\n(artist and title are always included):")

		# 6.1: Split these columns into rows.
		# 17.04: Gather items into a single list instead of three.
		# #76 (18.09-LTS): completely changed to use custom check list box (NVDA Core issue 7491).
		checkableColumns = ("Duration", "Intro", "Category", "Filename", "Outro", "Year", "Album", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "Time Scheduled")
		self.checkedColumns = playlistTranscriptsHelper.addLabeledControl(labelText, CustomCheckListBox, choices=checkableColumns)
		self.checkedColumns.SetCheckedStrings(self.includedColumns)
		self.checkedColumns.SetSelection(0)

		columnOrderGroup = gui.guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("Column order")), wx.HORIZONTAL))
		playlistTranscriptsHelper.addItem(columnOrderGroup)

		# wxPython 4 contains RearrangeList to allow item orders to be changed automatically.
		# Due to usability quirks (focus bouncing and what not), work around by using a variant of list box and move up/down buttons.
		# 17.04: The label for the list below is above the list, so move move up/down buttons to the right of the list box.
		# 20.09: the list and move up/down buttons are now part of a grouping.
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

	def onSave(self):
		splconfig.SPLConfig["PlaylistTranscripts"]["IncludedColumns"] = set(self.checkedColumns.GetCheckedStrings()) | {"Artist", "Title"}
		splconfig.SPLConfig["PlaylistTranscripts"]["ColumnOrder"] = self.trackColumns.GetItems()


# Columns Explorer for Studio, Track Tool and Creator
# Configure which column will be announced when Control+NVDA+number row keys are pressed.
# In 2018, the panel will house Columns Explorer buttons, but eventually columns combo boxes should be part of main settings interface.
class ColumnsExplorerPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure columns explorer settings.
	title = _("Columns explorer")

	def makeSettings(self, settingsSizer):
		colExplorerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: The label of a button to configure columns explorer slots (SPL Assistant, number row keys to announce specific columns).
		columnsExplorerButton = wx.Button(self, label=_("Columns E&xplorer..."))
		columnsExplorerButton.Bind(wx.EVT_BUTTON, self.onColumnsExplorer)
		self.exploreColumns = splconfig.SPLConfig["General"]["ExploreColumns"]
		# Translators: The label of a button to configure columns explorer slots for Track Tool (SPL Assistant, number row keys to announce specific columns).
		columnsExplorerTTButton = wx.Button(self, label=_("Columns Explorer for &Track Tool..."))
		columnsExplorerTTButton.Bind(wx.EVT_BUTTON, self.onColumnsExplorerTT)
		self.exploreColumnsTT = splconfig.SPLConfig["General"]["ExploreColumnsTT"]
		# Translators: The label of a button to configure columns explorer slots (SPL Assistant, number row keys to announce specific columns).
		columnsExplorerCreatorButton = wx.Button(self, label=_("Columns Explorer for &SPL Creator..."))
		columnsExplorerCreatorButton.Bind(wx.EVT_BUTTON, self.onColumnsExplorerCreator)
		self.exploreColumnsCreator = splconfig.SPLConfig["General"]["ExploreColumnsCreator"]
		colExplorerHelper.sizer.AddMany((columnsExplorerButton, columnsExplorerTTButton, columnsExplorerCreatorButton))

	def onSave(self):
		splconfig.SPLConfig["General"]["ExploreColumns"] = self.exploreColumns
		splconfig.SPLConfig["General"]["ExploreColumnsTT"] = self.exploreColumnsTT
		splconfig.SPLConfig["General"]["ExploreColumnsCreator"] = self.exploreColumnsCreator

	# Columns Explorer configuration.
	def onColumnsExplorer(self, evt):
		self.Disable()
		ColumnsExplorerDialog(self).Show()

	# Track Tool Columns Explorer configuration.
	def onColumnsExplorerTT(self, evt):
		self.Disable()
		ColumnsExplorerDialog(self, level=1).Show()

	# SPL CreatorColumns Explorer configuration.
	def onColumnsExplorerCreator(self, evt):
		self.Disable()
		ColumnsExplorerDialog(self, level=2).Show()


class ColumnsExplorerDialog(wx.Dialog):

	def __init__(self, parent, level=0):
		self.level = level
		if level == 0:
			# Translators: The title of Columns Explorer configuration dialog.
			actualTitle = _("Columns Explorer")
			cols = splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
			slots = parent.exploreColumns
		elif level == 1:
			# Translators: The title of Columns Explorer configuration dialog.
			actualTitle = _("Columns Explorer for Track Tool")
			cols = ("Artist", "Title", "Duration", "Cue", "Overlap", "Intro", "Segue", "Filename", "Album", "CD Code", "Outro", "Year", "URL 1", "URL 2", "Genre")
			slots = parent.exploreColumnsTT
		elif level == 2:
			# Translators: The title of Columns Explorer configuration dialog.
			actualTitle = _("Columns Explorer for SPL Creator")
			cols = ("Artist", "Title", "Position", "Cue", "Intro", "Outro", "Segue", "Duration", "Last Scheduled", "7 Days", "Date Restriction", "Year", "Album", "Genre", "Mood", "Energy", "Tempo", "BPM", "Gender", "Rating", "File Created", "Filename", "Client", "Other", "Intro Link", "Outro Link")
			slots = parent.exploreColumnsCreator
		# Gather column slots.
		self.columnSlots = []

		super(ColumnsExplorerDialog, self).__init__(parent, title=actualTitle)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		colExplorerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# 7.0: Studio 5.0x columns.
		# 17.04: Five by two grid layout as 5.0x is no longer supported.
		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for slot in range(5):
			# Translators: The label for a setting in SPL add-on dialog to select column for this column slot.
			columns = sizer.addLabeledControl(_("Slot {position}").format(position=slot+1), wx.Choice, choices=cols)
			try:
				columns.SetSelection(cols.index(slots[slot]))
			except:
				pass
			self.columnSlots.append(columns)
		colExplorerHelper.addItem(sizer.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for slot in range(5, 10):
			columns = sizer.addLabeledControl(_("Slot {position}").format(position=slot+1), wx.Choice, choices=cols)
			try:
				columns.SetSelection(cols.index(slots[slot]))
			except:
				pass
			self.columnSlots.append(columns)
		colExplorerHelper.addItem(sizer.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		colExplorerHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(colExplorerHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.columnSlots[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		# #62 (18.06): manually build a list so changes won't be retained when Cancel button is clicked from main settings, caused by reference problem.
		# Note that item count is based on how many column combo boxes are present in this dialog.
		# #63 (18.06): use levels instead due to introduction of Columns Explorer for SPL Creator.
		slots = [self.columnSlots[slot].GetStringSelection() for slot in range(10)]
		if self.level == 0: parent.exploreColumns = slots
		elif self.level == 1: parent.exploreColumnsTT = slots
		elif self.level == 2: parent.exploreColumnsCreator = slots
		parent.Enable()
		self.Destroy()

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()


# Say status panel.
# Houses options such as announcing cart names.
class SayStatusPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure various status announcements such as announcing listener count.
	title = _("Status announcements")

	def makeSettings(self, settingsSizer):
		sayStatusHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: the label for a setting in SPL add-on settings to announce scheduled time.
		self.scheduledForCheckbox = sayStatusHelper.addItem(wx.CheckBox(self, label=_("Announce &scheduled time for the selected track")))
		self.scheduledForCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayScheduledFor"])
		# Translators: the label for a setting in SPL add-on settings to announce listener count.
		self.listenerCountCheckbox = sayStatusHelper.addItem(wx.CheckBox(self, label=_("Announce &listener count")))
		self.listenerCountCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayListenerCount"])
		# Translators: the label for a setting in SPL add-on settings to announce currently playing cart.
		self.cartNameCheckbox = sayStatusHelper.addItem(wx.CheckBox(self, label=_("&Announce name of the currently playing cart")))
		self.cartNameCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"])
		# Translators: the label for a setting in SPL add-on settings to announce player position for the current and next tracks.
		self.playerPositionCheckbox = sayStatusHelper.addItem(wx.CheckBox(self, label=_("Include track player &position when announcing current and next track information")))
		self.playerPositionCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"])

	def onSave(self):
		splconfig.SPLConfig["SayStatus"]["SayScheduledFor"] = self.scheduledForCheckbox.Value
		splconfig.SPLConfig["SayStatus"]["SayListenerCount"] = self.listenerCountCheckbox.Value
		splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"] = self.cartNameCheckbox.Value
		splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"] = self.playerPositionCheckbox.Value


# Advanced options
# This panel houses advanced options such as using SPL Controller command to invoke SPL Assistant.
class AdvancedOptionsPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure advanced SPL add-on options such as update checking.
	title = _("Advanced")

	def makeSettings(self, settingsSizer):
		advOptionsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: A checkbox to toggle if SPL Controller command can be used to invoke Assistant layer.
		self.splConPassthroughCheckbox = advOptionsHelper.addItem(wx.CheckBox(self, label=_("Allow SPL C&ontroller command to invoke SPL Assistant layer")))
		self.splConPassthroughCheckbox.SetValue(splconfig.SPLConfig["Advanced"]["SPLConPassthrough"])
		# Translators: The label for a setting in SPL add-on dialog to set keyboard layout for SPL Assistant.
		labelText = _("SPL Assistant command &layout:")
		self.compatibilityLayouts = [
			("off", "NVDA"),
			("jfw", "JAWS for Windows")
		]
		self.compatibilityList = advOptionsHelper.addLabeledControl(labelText, wx.Choice, choices=[x[1] for x in self.compatibilityLayouts])
		selection = next((x for x, y in enumerate(self.compatibilityLayouts) if y[0] == splconfig.SPLConfig["Advanced"]["CompatibilityLayer"]))
		try:
			self.compatibilityList.SetSelection(selection)
		except:
			pass

	def onSave(self):
		splconfig.SPLConfig["Advanced"]["SPLConPassthrough"] = self.splConPassthroughCheckbox.Value
		splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] = self.compatibilityLayouts[self.compatibilityList.GetSelection()][0]


# A dialog to reset add-on config including encoder settings and others.
class ResetDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: Title of the dialog to reset various add-on settings.
		super(ResetDialog, self).__init__(parent, title=_("Reset settings"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		resetHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: the label for resetting profile triggers.
		self.resetInstantProfileCheckbox = resetHelper.addItem(wx.CheckBox(self, label=_("Reset instant switch profile")))
		# Translators: the label for resetting encoder settings.
		self.resetEncodersCheckbox = resetHelper.addItem(wx.CheckBox(self, label=_("Remove encoder settings")))
		# Translators: the label for resetting track comments.
		self.resetTrackCommentsCheckbox = resetHelper.addItem(wx.CheckBox(self, label=_("Erase track comments")))

		resetHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(resetHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.resetInstantProfileCheckbox.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		if gui.messageBox(
			# Translators: A message to warn about resetting SPL config settings to factory defaults.
			_("Are you sure you wish to reset SPL add-on settings to defaults?"),
			# Translators: The title of the warning dialog.
			_("Warning"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING, self
		) != wx.YES:
			parent.Enable()
			self.Destroy()
			return
		# Reset all profiles.
		# 7.0: Only a priveleged thread should do this, otherwise unexpected things may happen.
		with threading.Lock():
			global _configDialogOpened
			# #96 (19.03/18.09.7-LTS): call the reset handler instead of reset method directly so the additional confirmation message can be shown.
			# Without an exception, reset will continue.
			try:
				splconfig.SPLConfig.handlePostConfigReset(factoryDefaults=True, resetViaConfigDialog=True)
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
					import appModules.splengine.encoders
					appModules.splengine.encoders.resetEncoderConfig(factoryDefaults=True)
			_configDialogOpened = False
			wx.CallAfter(
				# Translators: A dialog message shown when settings were reset to defaults.
				gui.messageBox, _("Successfully applied default add-on settings."),
				# Translators: Title of the reset config dialog.
				_("Reset configuration"), wx.OK | wx.ICON_INFORMATION)
		self.Destroy()
		# #6: because the parent isn't add-on settings but the categories/panel sizer, fetch its ancestor.
		parent.Parent.Parent.Destroy()

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()


# Reset panel.
class ResetSettingsPanel(gui.SettingsPanel):
	# Translators: title of a panel to reset add-on settings.
	title = _("Reset settings")

	def makeSettings(self, settingsSizer):
		resetHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: Help text explaijning what will happen when settings are reset.
		labelText = _("Warning! Selecting Reset button and choosing various reset options will reset add-on settings to defaults.")
		resetHelper.addItem(wx.StaticText(self, label=labelText))

		# Translators: The label of a button to open reset dialog.
		resetButton = resetHelper.addItem(wx.Button(self, label=_("Reset settings...")))
		resetButton.Bind(wx.EVT_BUTTON, self.onResetConfig)

	def onSave(self):
		# Without this, not implemented error is raised by the superclass.
		pass

	def onResetConfig(self, evt):
		self.Disable()
		ResetDialog(self).Show()


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
		AdvancedOptionsPanel,
		ResetSettingsPanel,
	]

	def makeSettings(self, settingsSizer):
		super(SPLConfigDialog, self).makeSettings(settingsSizer)
		global _configDialogOpened
		# #40 (17.12): respond to app terminate notification by closing this dialog.
		# All top-level dialogs will be affected by this, and apart from this one, others will check for flags also.
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)
		# 20.02: let everyone know add-on settings is opened.
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
def _configDialogOpenError():
	gui.messageBox(translate("An NVDA settings dialog is already open. Please close it first."), translate("Error"), style=wx.OK | wx.ICON_ERROR)


# #125 (20.05): open any settings panel from main add-on settings, also checking if other dialogs are open.
def openAddonSettingsPanel(panel):
	# 5.2: Guard against alarm dialogs.
	# #129 (20.04): also check for broadcast profiles dialog.
	# #125 (20.05): checking for instance of base settings dialog class isn't enough - Python will look at actual class being instantiated, so keep the global flag.
	if _configDialogOpened:
		wx.CallAfter(_configDialogOpenError)
	else: gui.mainFrame._popupSettingsDialog(SPLConfigDialog, panel)


# Main add-on settings screen.
def onConfigDialog(evt):
	wx.CallAfter(openAddonSettingsPanel, None)


# Open broadcast profiles dialog and its friends upon request.
def onBroadcastProfilesDialog(evt):
	if _configDialogOpened:
		wx.CallAfter(_configDialogOpenError)
		return
	# Present an error message if only normal profile is in use.
	if splconfig.SPLConfig.configInMemory or splconfig.SPLConfig.normalProfileOnly:
		# Translators: presented when only normal profile is in use.
		wx.CallAfter(gui.messageBox, _("Normal profile is in use, cannot open broadcast profiles dialog."), _("SPL Broadcast Profiles"), wx.OK | wx.ICON_ERROR)
		return
	gui.mainFrame.prePopup()
	BroadcastProfilesDialog(gui.mainFrame).Show()
	gui.mainFrame.postPopup()
