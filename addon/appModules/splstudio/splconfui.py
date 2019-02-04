# SPL Studio Configuration user interfaces
# An app module and global plugin package for NVDA
# Copyright 2016-2019 Joseph Lee and others, released under GPL.
# Split from SPL config module in 2016.
# Provides the configuration management UI package for SPL Studio app module.
# For code which provides foundation for code in this module, see splconfig module.

# #6 (18.09-LTS): completely changed to use multi-page screen (requires NVDA 2018.2).
import gui
if not hasattr(gui, "MultiCategorySettingsDialog"):
	raise RuntimeError("no multi-category settings dialog")
# #76 (18.09-LTS): support NVDA releases with or without checkable list.
# 19.01/18.09.6-LTS: strictly use native checkable list box that ships with NVDA.
from gui.nvdaControls import CustomCheckListBox
import os
import weakref
import api
import wx
from winUser import user32
import tones
try:
	from . import splupdate
except RuntimeError:
	splupdate = None
import addonHandler
addonHandler.initTranslation()
from . import splconfig
from . import splactions
import six

# Due to syntax/variable name issues, the actual add-on settings class can be found at the end of this module.

# Helper panels/dialogs for add-on settings dialog.

# Broadcast profiles category
_selectedProfile = None
_configApplyOnly = False

class BroadcastProfilesPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure broadcast profiles.
	title = _("Broadcast profiles")

	def makeSettings(self, settingsSizer):
		broadcastProfilesHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Broadcast profile controls were inspired by Config Profiles dialog in NVDA Core.
		# 7.0: Have a copy of the sorted profiles so the actual combo box items can show profile flags.
		# 8.0: No need to sort as profile names from ConfigHub knows what to do.
		# 17.10: skip this if only normal profile is in use.
		# #6: display a read-only explanatory text.
		if not (splconfig.SPLConfig.configInMemory or splconfig.SPLConfig.normalProfileOnly):
			self.profileNames = list(splconfig.SPLConfig.profileNames)
			self.profileNames[0] = splconfig.defaultProfileName
			# Translators: The label for a setting in SPL add-on dialog to select a broadcast profile.
			self.profiles = broadcastProfilesHelper.addLabeledControl(_("Broadcast &profile:"), wx.Choice, choices=self.displayProfiles(list(self.profileNames)))
			self.profiles.Bind(wx.EVT_CHOICE, self.onProfileSelection)
			try:
				self.profiles.SetSelection(self.profileNames.index(splconfig.SPLConfig.activeProfile))
			except:
				pass
		else:
			# Borrowed logic from NVDA Core's speech panel (although there is no label for this read-only text).
			broadcastProfilesHelper.addItem(wx.lib.expando.ExpandoTextCtrl(self, size=(self.scaleSize(250), -1), value=_("Normal profile is in use."), style=wx.TE_READONLY))

		# Profile controls code credit: NV Access (except copy button).
		# 17.10: if restrictions such as volatile config are applied, disable this area entirely.
		if not (splconfig.SPLConfig.volatileConfig or splconfig.SPLConfig.normalProfileOnly or splconfig.SPLConfig.configInMemory):
			sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
			# Translators: The label of a button to create a new broadcast profile.
			newButton = wx.Button(self, label=_("&New"))
			newButton.Bind(wx.EVT_BUTTON, self.onNew)
			# Translators: The label of a button to copy a broadcast profile.
			copyButton = wx.Button(self, label=_("Cop&y"))
			copyButton.Bind(wx.EVT_BUTTON, self.onCopy)
			# Translators: The label of a button to rename a broadcast profile.
			self.renameButton = wx.Button(self, label=_("&Rename"))
			self.renameButton.Bind(wx.EVT_BUTTON, self.onRename)
			# Translators: The label of a button to delete a broadcast profile.
			self.deleteButton = wx.Button(self, label=_("&Delete"))
			self.deleteButton.Bind(wx.EVT_BUTTON, self.onDelete)
			# Have a copy of the triggers dictionary.
			self._profileTriggersConfig = dict(splconfig.profileTriggers)
			# Translators: The label of a button to manage show profile triggers.
			self.triggerButton = wx.Button(self, label=_("&Triggers..."))
			self.triggerButton.Bind(wx.EVT_BUTTON, self.onTriggers)
			sizer.sizer.AddMany((newButton, copyButton, self.renameButton, self.deleteButton, self.triggerButton))
			# Translators: The label for a setting in SPL Add-on settings to configure countdown seconds before switching profiles.
			self.triggerThreshold = sizer.addLabeledControl(_("Countdown seconds before switching profiles"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=10, max=60, initial=splconfig.SPLConfig["Advanced"]["ProfileTriggerThreshold"])
			if self.profiles.GetSelection() == 0:
				self.renameButton.Disable()
				self.deleteButton.Disable()
				self.triggerButton.Disable()
			broadcastProfilesHelper.addItem(sizer.sizer)
		self.switchProfile = splconfig.SPLConfig.instantSwitch
		self.activeProfile = splconfig.SPLConfig.activeProfile
		# Used as sanity check in case switch profile is renamed or deleted.
		self.switchProfileRenamed = False
		self.switchProfileDeleted = False

	def onSave(self):
		if hasattr(self, "profiles"):
			selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
			if splconfig.SPLConfig.activeProfile != selectedProfile:
				if _configApplyOnly:
					gui.messageBox(_("The selected profile is different from currently active broadcast profile. Settings will be applied to the selected profile instead."),
						_("Apply settings"), wx.OK | wx.ICON_INFORMATION, self)
				else:
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
		if self.switchProfile is None and not splconfig._triggerProfileActive:
			splconfig.SPLConfig.prevProfile = None
		# Apply changes to profile triggers.
		# #6: but only if OK button is clicked.
		if not _configApplyOnly:
			splconfig.profileTriggers = dict(self._profileTriggersConfig)
			self._profileTriggersConfig.clear()
			self._profileTriggersConfig = None

	def onDiscard(self):
		# Apply profile trigger changes if any.
		try:
			splconfig.profileTriggers = dict(self._profileTriggersConfig)
			self._profileTriggersConfig.clear()
			self._profileTriggersConfig = None
		except AttributeError:
			pass
		splconfig.triggerStart(restart=True)
		# 7.0: No matter what happens, merge appropriate profile.
		try:
			prevActive = self.activeProfile
		except ValueError:
			prevActive = splconfig.defaultProfileName
		if self.switchProfileRenamed or self.switchProfileDeleted:
			splconfig.SPLConfig.instantSwitch = self.switchProfile

	# Include profile flags such as instant profile string for display purposes.
	def displayProfiles(self, profiles):
		for index in six.moves.range(len(profiles)):
			profiles[index] = splconfig.getProfileFlags(profiles[index])
		return profiles

	# Load settings from profiles.
	# #6: set selected profile flag so other panels can pull in appropriate settings.
	def onProfileSelection(self, evt):
		global _selectedProfile
		# Don't rely on SPLConfig here, as we don't want to interupt the show.
		selection = self.profiles.GetSelection()
		# No need to look at the profile flag.
		selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
		# Play a tone to indicate active profile.
		if self.activeProfile == selectedProfile:
			tones.beep(512, 40)
			_selectedProfile = None
		else:
			_selectedProfile = selectedProfile
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
		# Translators: The label of a field to enter a new name for a broadcast profile.
		with wx.TextEntryDialog(self, _("New name:"),
				# Translators: The title of the dialog to rename a profile.
				_("Rename Profile"), value=oldName) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
			newName = api.filterFileName(d.Value)
		if oldName == newName: return
		try:
			splconfig.SPLConfig.renameProfile(oldName, newName)
		except RuntimeError:
			# Translators: An error displayed when renaming a configuration profile
			# and a profile with the new name already exists.
			gui.messageBox(_("That profile already exists. Please choose a different name."),
				_("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		if self.switchProfile == oldName:
			self.switchProfile = newName
			self.switchProfileRenamed = True
		# Be sure to update profile triggers.
		if oldName in self._profileTriggersConfig:
			self._profileTriggersConfig[newName] = self._profileTriggersConfig[oldName]
			del self._profileTriggersConfig[oldName]
		if self.activeProfile == oldName:
			self.activeProfile = newName
		self.profileNames[profilePos] = newName
		if oldName in splconfig._SPLCache:
			splconfig._SPLCache[newName] = splconfig._SPLCache[oldName]
			del splconfig._SPLCache[oldName]
		if len(state) > 1: newName = " <".join([newName, state[1]])
		self.profiles.SetString(index, newName)
		self.profiles.Selection = index
		self.profiles.SetFocus()
		# Don't forget to update selected profile name.
		global _selectedProfile
		if _selectedProfile == oldName:
			_selectedProfile = newName

	def onDelete(self, evt):
		# Prevent profile deletion while a trigger is active (in the midst of a broadcast), otherwise flags such as instant switch and time-based profiles become inconsistent.
		# 6.4: This was seen after deleting a profile one position before the previously active profile.
		# 7.0: One should never delete the currently active time-based profile.
		# 7.1: Find a way to safely proceed via two-step verification if trying to delete currently active time-based profile.
		if (splconfig._SPLTriggerEndTimer is not None and splconfig._SPLTriggerEndTimer.IsRunning()) or splconfig._triggerProfileActive or splconfig.SPLConfig.prevProfile is not None:
			# Translators: Message reported when attempting to delete a profile while a profile is triggered.
			gui.messageBox(_("An instant switch profile might be active or you are in the midst of a broadcast. If so, please press SPL Assistant, F12 to switch back to a previously active profile before opening add-on settings to delete a profile."),
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
		if name in self._profileTriggersConfig:
			del self._profileTriggersConfig[name]
		# 6.3: Select normal profile if the active profile is gone.
		# 7.0: Consult profile names instead.
		try:
			self.profiles.Selection = self.profileNames.index(self.activeProfile)
		except ValueError:
			self.activeProfile = splconfig.defaultProfileName
			self.profiles.Selection = 0
		self.onProfileSelection(None)
		self.profiles.SetFocus()
		# Don't forget other settings panels.
		global _selectedProfile
		if _selectedProfile == name:
			_selectedProfile = None

	def onTriggers(self, evt):
		self.Disable()
		if splconfig._triggerProfileActive:
			# Translators: Message reported when attempting to change profile switch trigger while broadcasting.
			gui.messageBox(_("You cannot change profile switch triggers in the midst of a broadcast."),
				# Translators: Title of a dialog shown when profile trigger cannot e changd.
				_("Profile triggers"), wx.OK | wx.ICON_ERROR, self)
			self.Enable()
			return
		TriggersDialog(self, self.profileNames[self.profiles.Selection]).Show()

	# Obtain profile flags for a given profile.
	# This is a proxy to the splconfig module level profile flag retriever with custom strings/maps as arguments.
	def getProfileFlags(self, name):
		return splconfig.getProfileFlags(name, active=self.activeProfile, instant=self.switchProfile, triggers=self._profileTriggersConfig, contained=True)

	# Handle flag modifications such as when toggling instant switch.
	# Unless given, flags will be queried.
	# This is a sister function to profile flags retriever.
	def setProfileFlags(self, index, action, flag, flags=None):
		profile = self.profileNames[index]
		if flags is None: flags = self.getProfileFlags(profile)
		action = getattr(flags, action)
		action(flag)
		self.profiles.SetString(index, profile if not len(flags) else "{0} <{1}>".format(profile, ", ".join(flags)))

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
			self.baseProfiles = newProfileSizerHelper.addLabeledControl(_("&Base profile:"), wx.Choice, choices=[profile.split(" <")[0] for profile in parent.profiles.GetItems()])
			try:
				self.baseProfiles.SetSelection(self.baseProfiles.GetItems().index(parent.profiles.GetStringSelection().split(" <")[0]))
			except:
				pass

		newProfileSizerHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(newProfileSizerHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
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
			# Translators: An error displayed when the user attempts to create a profile which already exists.
			gui.messageBox(_("That profile already exists. Please choose a different name."),
				_("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		namePath = name + ".ini"
		if not os.path.exists(splconfig.SPLProfiles):
			os.mkdir(splconfig.SPLProfiles)
		newProfilePath = os.path.join(splconfig.SPLProfiles, namePath)
		# LTS optimization: just build base profile dictionary here if copying a profile.
		if self.copy:
			baseConfig = splconfig.SPLConfig.profileByName(self.baseProfiles.GetStringSelection())
			baseProfile = {sect:key for sect, key in baseConfig.items() if sect in splconfig._mutatableSettings}
		else: baseProfile = None
		splconfig.SPLConfig.createProfile(newProfilePath, profileName=name, parent=baseProfile)
		parent.profileNames.append(name)
		parent.profiles.Append(name)
		parent.profiles.Selection = parent.profiles.Count - 1
		parent.onProfileSelection(None)
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

# Broadcast profile triggers dialog.
# This dialog is similar to NVDA Core's profile triggers dialog and allows one to configure when to trigger this profile.
class TriggersDialog(wx.Dialog):

	def __init__(self, parent, profile):
		# Translators: The title of the broadcast profile triggers dialog.
		super(TriggersDialog, self).__init__(parent, title=_("Profile triggers for {profileName}").format(profileName = profile))
		self.profile = profile
		self.selection = parent.profiles.GetSelection()
		# When referencing profile triggers, use the dictionary stored in the main add-on settings.
		# This is needed in order to discard changes when cancel button is clicked from the parent dialog.
		# 7.0: Remove this text for now (may return in 7.1 if requested).
		"""if profile in self.Parent._profileTriggersConfig:
			t = self.Parent._profileTriggersConfig[profile]
			d = "-".join([str(t[1]), str(t[2]).zfill(2), str(t[3]).zfill(2)])
			t = ":".join([str(t[4]).zfill(2), str(t[5]).zfill(2)])
			triggerText = "The next trigger is scheduled on {0} at {1}.".format(d, t)
		else:
			triggerText = "No triggers defined."
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		label = wx.StaticText(self, wx.ID_ANY, label=triggerText)
		sizer.Add(label)"""

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		triggersHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: The label of a checkbox to toggle if selected profile is an instant switch profile.
		self.instantSwitchCheckbox=triggersHelper.addItem(wx.CheckBox(self, label=_("This is an &instant switch profile")))
		self.instantSwitchCheckbox.SetValue(parent.switchProfile == parent.profiles.GetStringSelection().split(" <")[0])

		# Translators: The label of a checkbox to toggle if selected profile is a time-based profile.
		self.timeSwitchCheckbox=triggersHelper.addItem(wx.CheckBox(self, label=_("This is a &time-based switch profile")))
		self.timeSwitchCheckbox.SetValue(profile in self.Parent._profileTriggersConfig)
		self.timeSwitchCheckbox.Bind(wx.EVT_CHECKBOX, self.onTimeSwitch)

		daysSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Day")), wx.HORIZONTAL)
		self.triggerDays = []
		import calendar
		for day in six.moves.range(len(calendar.day_name)):
			triggerDay=wx.CheckBox(self, wx.ID_ANY,label=calendar.day_name[day])
			triggerDay.SetValue((64 >> day & self.Parent._profileTriggersConfig[profile][0]) if profile in self.Parent._profileTriggersConfig else 0)
			if not self.timeSwitchCheckbox.IsChecked(): triggerDay.Disable()
			self.triggerDays.append(triggerDay)
			daysSizer.Add(triggerDay)
		triggersHelper.addItem(daysSizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		timeSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Time")), wx.HORIZONTAL)
		self.hourPrompt = wx.StaticText(self, wx.ID_ANY, label=_("Hour"))
		self.hourEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=23)
		self.hourEntry.SetValue(self.Parent._profileTriggersConfig[profile][4] if profile in self.Parent._profileTriggersConfig else 0)
		self.hourEntry.SetSelection(-1, -1)
		self.minPrompt = wx.StaticText(self, wx.ID_ANY, label=_("Minute"))
		self.minEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.minEntry.SetValue(self.Parent._profileTriggersConfig[profile][5] if profile in self.Parent._profileTriggersConfig else 0)
		self.minEntry.SetSelection(-1, -1)
		self.durationPrompt = wx.StaticText(self, wx.ID_ANY, label=_("Duration in minutes"))
		self.durationEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=1440)
		self.durationEntry.SetValue(self.Parent._profileTriggersConfig[profile][6] if profile in self.Parent._profileTriggersConfig else 0)
		self.durationEntry.SetSelection(-1, -1)
		if not self.timeSwitchCheckbox.IsChecked():
			self.hourPrompt.Disable()
			self.hourEntry.Disable()
			self.minPrompt.Disable()
			self.minEntry.Disable()
			self.durationPrompt.Disable()
			self.durationEntry.Disable()
		timeSizer.AddMany((self.hourPrompt, self.hourEntry, self.minPrompt, self.minEntry, self.durationPrompt, self.durationEntry))
		triggersHelper.addItem(timeSizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		triggersHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(triggersHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
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
		# Now time-based profile checkbox.
		if self.timeSwitchCheckbox.Value:
			bit = 0
			for day in self.triggerDays:
				if day.Value: bit+=64 >> self.triggerDays.index(day)
			if bit:
				hour, min = self.hourEntry.GetValue(), self.minEntry.GetValue()
				duration = self.durationEntry.GetValue()
				if splconfig.duplicateExists(parent._profileTriggersConfig, self.profile, bit, hour, min, duration):
					# Translators: Presented if another profile occupies a time slot set by the user.
					gui.messageBox(_("A profile trigger already exists for the entered time slot. Please choose a different date or time."),
						_("Error"), wx.OK | wx.ICON_ERROR, self)
					return
				# Change display name if there is no profile of this name registered.
				# This helps in preventing unnecessary calls to profile flags retriever, a huge time and memory savings.
				# Otherwise trigger flag will be added each time this is called (either this handler or the add-on settings' flags retriever must retrieve the flags set).
				if not self.profile in parent._profileTriggersConfig:
					parent.setProfileFlags(self.selection, "add", _("time-based"))
				import datetime
				parent._profileTriggersConfig[self.profile] = splconfig.setNextTimedProfile(self.profile, bit, datetime.time(hour, min))
				parent._profileTriggersConfig[self.profile][6] = duration
			else:
				# Er, did you specify a date?
				gui.messageBox(_("The time-based profile checkbox is checked but no switch dates are given. Please either specify switch date(s) or uncheck time-based profile checkbox."),
					_("Error"), wx.OK | wx.ICON_ERROR, self)
				return
		elif not self.timeSwitchCheckbox.Value and self.profile in self.Parent._profileTriggersConfig:
			del parent._profileTriggersConfig[self.profile]
			# Calling set profile flags with discard argument is always safe here.
			parent.setProfileFlags(self.selection, "discard", _("time-based"))
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

	# Disable date and time sizers when time switch checkbox is cleared and vice versa.
	def onTimeSwitch(self, evt):
		# Hack: Somehow, NVDA is not notified of state change for this checkbox, so force NVDA to report the new state.
		import eventHandler
		eventHandler.executeEvent("stateChange", api.getFocusObject())
		for prompt in self.triggerDays + [self.hourPrompt, self.hourEntry, self.minPrompt, self.minEntry, self.durationPrompt, self.durationEntry]:
			prompt.Enable() if self.timeSwitchCheckbox.IsChecked() else prompt.Disable()
		self.Fit()

# A collection of general settings for the add-on.
class GeneralSettingsPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure various general add-on settings such as top and bottom announcement for playlists.
	title = _("General")

	def makeSettings(self, settingsSizer):
		generalSettingsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# Translators: the label for a setting in SPL add-on settings to set status announcement between words and beeps.
		self.beepAnnounceCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("&Beep for status announcements")))
		self.beepAnnounceCheckbox.SetValue(splconfig.SPLConfig["General"]["BeepAnnounce"])

		# Translators: One of the message verbosity levels.
		self.verbosityLevels=[("beginner",_("beginner")),
		# Translators: One of the message verbosity levels.
		("advanced",_("advanced"))]
		# Translators: The label for a setting in SPL add-on dialog to set message verbosity.
		self.verbosityList = generalSettingsHelper.addLabeledControl(_("Message &verbosity:"), wx.Choice, choices=[x[1] for x in self.verbosityLevels])
		currentVerbosity=splconfig.SPLConfig["General"]["MessageVerbosity"]
		selection = next((x for x,y in enumerate(self.verbosityLevels) if y[0]==currentVerbosity))
		try:
			self.verbosityList.SetSelection(selection)
		except:
			pass

		self.brailleTimerValues=[("off",_("Off")),
		# Translators: One of the braille timer settings.
		("outro",_("Track ending")),
		# Translators: One of the braille timer settings.
		("intro",_("Track intro")),
		# Translators: One of the braille timer settings.
		("both",_("Track intro and ending"))]
		# Translators: The label for a setting in SPL add-on dialog to control braille timer.
		self.brailleTimerList = generalSettingsHelper.addLabeledControl(_("&Braille timer:"), wx.Choice, choices=[x[1] for x in self.brailleTimerValues])
		brailleTimerCurValue=splconfig.SPLConfig["General"]["BrailleTimer"]
		selection = next((x for x,y in enumerate(self.brailleTimerValues) if y[0]==brailleTimerCurValue))
		try:
			self.brailleTimerList.SetSelection(selection)
		except:
			pass

		self.libScanValues=[("off",_("Off")),
		# Translators: One of the library scan announcement settings.
		("ending",_("Start and end only")),
		# Translators: One of the library scan announcement settings.
		("progress",_("Scan progress")),
		# Translators: One of the library scan announcement settings.
		("numbers",_("Scan count"))]
		# Translators: The label for a setting in SPL add-on dialog to control library scan announcement.
		self.libScanList = generalSettingsHelper.addLabeledControl(_("&Library scan announcement:"), wx.Choice, choices=[x[1] for x in self.libScanValues])
		libScanCurValue=splconfig.SPLConfig["General"]["LibraryScanAnnounce"]
		selection = next((x for x,y in enumerate(self.libScanValues) if y[0]==libScanCurValue))
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

		self.trackCommentValues=[("off",_("Off")),
		# Translators: One of the track comment notification settings.
		("message",_("Message")),
		# Translators: One of the track comment notification settings.
		("beep",_("Beep")),
		# Translators: One of the track comment notification settings.
		("both",_("Both"))]
		# Translators: the label for a setting in SPL add-on settings to set how track comments are announced.
		self.trackCommentList = generalSettingsHelper.addLabeledControl(_("&Track comment announcement:"), wx.Choice, choices=[x[1] for x in self.trackCommentValues])
		trackCommentCurValue=splconfig.SPLConfig["General"]["TrackCommentAnnounce"]
		selection = next((x for x,y in enumerate(self.trackCommentValues) if y[0]==trackCommentCurValue))
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

# A common alarm dialog (Alarms Center)
# Based on NVDA core's find dialog code (implemented by the author of this add-on).
# Extended in 2016 to handle microphone alarms.
# Only one instance can be active at a given moment (code borrowed from GUI's exit dialog routine).
_alarmDialogOpened = False

# A common alarm error dialog.
def _alarmError():
	# Translators: Text of the dialog when another alarm dialog is open.
	gui.messageBox(_("Another alarm dialog is open."),_("Error"),style=wx.OK | wx.ICON_ERROR)

class AlarmsCenter(wx.Dialog):
	"""A dialog providing common alarm settings.
	This dialog contains a number entry field for alarm duration and a check box to enable or disable the alarm.
	For one particular case, it consists of two number entry fields.
	"""

	# The following comes from exit dialog class from GUI package (credit: NV Access and Zahari from Bulgaria).
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _alarmDialogOpened:
			raise RuntimeError("An instance of alarm dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, level=0):
		inst = AlarmsCenter._instance() if AlarmsCenter._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		import weakref
		AlarmsCenter._instance = weakref.ref(self)

		# Now the actual alarm dialog code.
		# 8.0: Apart from level 0 (all settings shown), levels change title.
		titles = (_("Alarms Center"), _("End of track alarm"), _("Song intro alarm"), _("Microphone alarm"))
		super(AlarmsCenter, self).__init__(parent, wx.ID_ANY, titles[level])
		self.level = level
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		alarmsCenterHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		if level in (0, 1):
			timeVal = parent.endOfTrackTime if level == 0 else splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"]
			self.outroAlarmEntry = alarmsCenterHelper.addLabeledControl(_("&End of track alarm in seconds"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=1, max=59, initial=timeVal)
			self.outroToggleCheckBox=alarmsCenterHelper.addItem(wx.CheckBox(self, label=_("&Notify when end of track is approaching")))
			self.outroToggleCheckBox.SetValue(parent.sayEndOfTrack if level == 0 else splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"])

		if level in (0, 2):
			rampVal = parent.songRampTime if level == 0 else splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"]
			self.introAlarmEntry = alarmsCenterHelper.addLabeledControl(_("&Track intro alarm in seconds"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=1, max=9, initial=rampVal)
			self.introToggleCheckBox=alarmsCenterHelper.addItem(wx.CheckBox(self, label=_("&Notify when end of introduction is approaching")))
			self.introToggleCheckBox.SetValue(parent.saySongRamp if level == 0 else splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"])

		if level in (0, 3):
			micAlarm = splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"] if level == 3 else parent.micAlarm
			micAlarmInterval = splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] if level == 3 else parent.micAlarmInterval
			# Translators: A dialog message to set microphone active alarm.
			self.micAlarmEntry = alarmsCenterHelper.addLabeledControl(_("&Microphone alarm in seconds (0 disables the alarm)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=7200, initial=micAlarm)
			self.micIntervalEntry = alarmsCenterHelper.addLabeledControl(_("Microphone alarm &interval in seconds"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=60, initial=micAlarmInterval)

		alarmsCenterHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(alarmsCenterHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		if level in (0, 1): self.outroAlarmEntry.SetFocus()
		elif level == 2: self.introAlarmEntry.SetFocus()
		elif level == 3: self.micAlarmEntry.SetFocus()

	def onOk(self, evt):
		global _alarmDialogOpened
		# Optimization: don't bother if Studio is dead and if the same value has been entered (only when standalone versions are opened).
		if self.level > 0 and user32.FindWindowW(u"SPLStudio", None):
			# Gather settings to be applied in section/key format.
			if self.level == 1:
				splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"] = self.outroAlarmEntry.GetValue()
				splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"] = self.outroToggleCheckBox.GetValue()
			elif self.level == 2:
				splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"] = self.introAlarmEntry.GetValue()
				splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"] = self.introToggleCheckBox.GetValue()
			elif self.level == 3:
				splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"] = self.micAlarmEntry.GetValue()
				splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] = self.micIntervalEntry.GetValue()
				# #42 (18.01/15.12-LTS): don't forget to restart microphone alarm timer.
				# 18.02: do it here at once.
				# It is fine to import something from winUser again as this will be traversed if and only if microphone alarm dialog is open with Studio active.
				from winUser import OBJID_CLIENT
				from NVDAObjects.IAccessible import getNVDAObjectFromEvent
				studioWindow = getNVDAObjectFromEvent(user32.FindWindowW(u"TStudioForm", None), OBJID_CLIENT, 0)
				studioWindow.appModule.actionProfileSwitched()
		elif self.level == 0:
			parent = self.Parent
			parent.endOfTrackTime = self.outroAlarmEntry.GetValue()
			parent.sayEndOfTrack = self.outroToggleCheckBox.GetValue()
			parent.songRampTime = self.introAlarmEntry.GetValue()
			parent.saySongRamp = self.introToggleCheckBox.GetValue()
			parent.micAlarm = self.micAlarmEntry.GetValue()
			parent.micAlarmInterval = self.micIntervalEntry.GetValue()
			self.Parent.profiles.SetFocus()
			self.Parent.Enable()
		self.Destroy()
		_alarmDialogOpened = False

	def onCancel(self, evt):
		if self.level == 0:
			self.Parent.Enable()
		self.Destroy()
		global _alarmDialogOpened
		_alarmDialogOpened = False

	def onAppTerminate(self):
		self.onCancel(None)

class AlarmsPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure various alarms and related settings.
	title = _("Alarms")

	def makeSettings(self, settingsSizer):
		alarmsCenterHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# #77 (18.09-LTS): record temporary settings.
		self._curProfileSettings = {}
		self.outroAlarmEntry = alarmsCenterHelper.addLabeledControl(_("&End of track alarm in seconds"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=1, max=59, initial=splconfig._SPLDefaults["IntroOutroAlarms"]["EndOfTrackTime"])
		self.outroToggleCheckBox=alarmsCenterHelper.addItem(wx.CheckBox(self, label=_("&Notify when end of track is approaching")))
		self.outroToggleCheckBox.SetValue(splconfig._SPLDefaults["IntroOutroAlarms"]["SayEndOfTrack"])

		self.introAlarmEntry = alarmsCenterHelper.addLabeledControl(_("&Track intro alarm in seconds"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=1, max=9, initial=splconfig._SPLDefaults["IntroOutroAlarms"]["SongRampTime"])
		self.introToggleCheckBox=alarmsCenterHelper.addItem(wx.CheckBox(self, label=_("&Notify when end of introduction is approaching")))
		self.introToggleCheckBox.SetValue(splconfig._SPLDefaults["IntroOutroAlarms"]["SaySongRamp"])

		self.micAlarmEntry = alarmsCenterHelper.addLabeledControl(_("&Microphone alarm in seconds (0 disables the alarm)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=7200, initial=splconfig._SPLDefaults["MicrophoneAlarm"]["MicAlarm"])
		self.micIntervalEntry = alarmsCenterHelper.addLabeledControl(_("Microphone alarm &interval in seconds"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=60, initial=splconfig._SPLDefaults["MicrophoneAlarm"]["MicAlarmInterval"])

		# Translators: One of the alarm notification options.
		self.alarmAnnounceValues=[("beep",_("beep")),
		# Translators: One of the alarm notification options.
		("message",_("message")),
		# Translators: One of the alarm notification options.
		("both",_("both beep and message"))]
		# Translators: The label for a setting in SPL add-on dialog to control alarm announcement type.
		self.alarmAnnounceList = alarmsCenterHelper.addLabeledControl(_("&Alarm notification:"), wx.Choice, choices=[x[1] for x in self.alarmAnnounceValues])
		alarmAnnounceCurValue=splconfig.SPLConfig["General"]["AlarmAnnounce"]
		selection = next((x for x,y in enumerate(self.alarmAnnounceValues) if y[0]==alarmAnnounceCurValue))
		try:
			self.alarmAnnounceList.SetSelection(selection)
		except:
			pass

	def onPanelActivated(self):
		selectedProfile = _selectedProfile
		if selectedProfile is None: selectedProfile = splconfig.SPLConfig.activeProfile
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		if selectedProfile not in self._curProfileSettings: settings = dict(curProfile)
		else: settings = dict(self._curProfileSettings[selectedProfile])
		self.outroAlarmEntry.SetValue(settings["IntroOutroAlarms"]["EndOfTrackTime"])
		self.outroToggleCheckBox.SetValue(settings["IntroOutroAlarms"]["SayEndOfTrack"])
		self.introAlarmEntry.SetValue(settings["IntroOutroAlarms"]["SongRampTime"])
		self.introToggleCheckBox.SetValue(settings["IntroOutroAlarms"]["SaySongRamp"])
		self.micAlarmEntry.SetValue(settings["MicrophoneAlarm"]["MicAlarm"])
		self.micIntervalEntry.SetValue(settings["MicrophoneAlarm"]["MicAlarmInterval"])
		super(AlarmsPanel, self).onPanelActivated()

	def onPanelDeactivated(self):
		selectedProfile = _selectedProfile
		if selectedProfile is None: selectedProfile = splconfig.SPLConfig.activeProfile
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		currentSettings = {"IntroOutroAlarms": {}, "MicrophoneAlarm": {}}
		currentSettings["IntroOutroAlarms"]["EndOfTrackTime"] = self.outroAlarmEntry.GetValue()
		currentSettings["IntroOutroAlarms"]["SayEndOfTrack"] = self.outroToggleCheckBox.GetValue()
		currentSettings["IntroOutroAlarms"]["SongRampTime"] = self.introAlarmEntry.GetValue()
		currentSettings["IntroOutroAlarms"]["SaySongRamp"] = self.introToggleCheckBox.GetValue()
		currentSettings["MicrophoneAlarm"]["MicAlarm"] = self.micAlarmEntry.GetValue()
		currentSettings["MicrophoneAlarm"]["MicAlarmInterval"] = self.micIntervalEntry.GetValue()
		if currentSettings != {sect:key for sect, key in curProfile.items() if sect in ("IntroOutroAlarms", "MicrophoneAlarm")}:
			self._curProfileSettings[selectedProfile] = dict(currentSettings)
		super(AlarmsPanel, self).onPanelDeactivated()

	def onSave(self):
		# Save global settings first, and then record profile-specific settings in appropriate profile.
		splconfig.SPLConfig["General"]["AlarmAnnounce"] = self.alarmAnnounceValues[self.alarmAnnounceList.GetSelection()][0]
		selectedProfile = _selectedProfile
		if selectedProfile is None: selectedProfile = splconfig.SPLConfig.activeProfile
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		curProfile["IntroOutroAlarms"]["EndOfTrackTime"] = self.outroAlarmEntry.GetValue()
		curProfile["IntroOutroAlarms"]["SayEndOfTrack"] = self.outroToggleCheckBox.GetValue()
		curProfile["IntroOutroAlarms"]["SongRampTime"] = self.introAlarmEntry.GetValue()
		curProfile["IntroOutroAlarms"]["SaySongRamp"] = self.introToggleCheckBox.GetValue()
		curProfile["MicrophoneAlarm"]["MicAlarm"] = self.micAlarmEntry.GetValue()
		curProfile["MicrophoneAlarm"]["MicAlarmInterval"] = self.micIntervalEntry.GetValue()
		self._curProfileSettings.clear()
		# #80 (18.10.2/18.09.4-LTS): don't just nullify profile setings, otherwise attribute and type error excpetions may arise.
		if not _configApplyOnly: self._curProfileSettings = None

	def onDiscard(self):
		self._curProfileSettings.clear()
		self._curProfileSettings = None

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
		self.playlistDurationMinMaxCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Shortest and longest tracks")))
		self.playlistDurationMinMaxCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["DurationMinMax"])
		# Translators: the label for a setting in SPL add-on settings to include average track duration in playlist snapshots window.
		self.playlistDurationAverageCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Average track duration")))
		self.playlistDurationAverageCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["DurationAverage"])
		# Translators: the label for a setting in SPL add-on settings to include track artist count in playlist snapshots window.
		self.playlistArtistCountCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Artist count")))
		self.playlistArtistCountCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCount"])
		# Translators: the label for a setting in SPL add-on settings to set top artist count limit in playlist snapshots window.
		self.playlistArtistCountLimit=playlistSnapshotsHelper.addLabeledControl(_("Top artist count (0 displays all artists)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"])
		# Translators: the label for a setting in SPL add-on settings to include track category count in playlist snapshots window.
		self.playlistCategoryCountCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Category count")))
		self.playlistCategoryCountCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCount"])
		# Translators: the label for a setting in SPL add-on settings to set top track category count limit in playlist snapshots window.
		self.playlistCategoryCountLimit=playlistSnapshotsHelper.addLabeledControl(_("Top category count (0 displays all categories)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"])
		# Translators: the label for a setting in SPL add-on settings to include track genre count in playlist snapshots window.
		self.playlistGenreCountCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Genre count")))
		self.playlistGenreCountCheckbox.SetValue(splconfig.SPLConfig["PlaylistSnapshots"]["GenreCount"])
		# Translators: the label for a setting in SPL add-on settings to set top track genre count limit in playlist snapshots window.
		self.playlistGenreCountLimit=playlistSnapshotsHelper.addLabeledControl(_("Top genre count (0 displays all genres)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"])
		# Translators: the label for a setting in SPL add-on settings to show playlist snaphsots window when the snapshots command is pressed once.
		self.resultsWindowOnFirstPressCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("&Show results window when playlist snapshots command is performed once")))
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
_metadataDialogOpened = False
metadataStreamLabels = ("DSP encoder", "URL 1", "URL 2", "URL 3", "URL 4")

class MetadataStreamingDialog(wx.Dialog):
	"""A dialog to toggle metadata streaming quickly and from add-on settings dialog.
	"""
	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _metadataDialogOpened:
			raise RuntimeError("An instance of metadata streaming dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, configDialogActive=True):
		inst = MetadataStreamingDialog._instance() if MetadataStreamingDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		MetadataStreamingDialog._instance = weakref.ref(self)

		# Translators: Title of a dialog to configure metadata streaming status for DSP encoder and four additional URL's.
		super(MetadataStreamingDialog, self).__init__(parent, title=_("Metadata streaming options"))
		# #44 (18.02): Config dialog flag controls how stream value will be gathered and set (if true, this is part of add-on settings, otherwise use Studio API).
		self.configDialogActive = configDialogActive
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		metadataSizerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		if configDialogActive: labelText=_("Select the URL for metadata streaming upon request.")
		else: labelText=_("Check to enable metadata streaming, uncheck to disable.")
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
		for stream in six.moves.range(5):
			if not configDialogActive: self.checkedStreams.Check(stream, check=streams[stream])
			else: self.checkedStreams.Check(stream, check=self.Parent.metadataStreams[stream])
		self.checkedStreams.SetSelection(0)

		if not configDialogActive:
			# Translators: A checkbox to let metadata streaming status be applied to the currently active broadcast profile.
			self.applyCheckbox = metadataSizerHelper.addItem(wx.CheckBox(self, label=_("&Apply streaming changes to the selected profile")))
			self.applyCheckbox.SetValue(True)

		metadataSizerHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(metadataSizerHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedStreams.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global _metadataDialogOpened
		# Prepare checkbox values first for various reasons.
		# #76 (18.09-LTS): traverse check list box and build boolean list accordingly.
		metadataEnabled = [self.checkedStreams.IsChecked(url) for url in six.moves.range(5)]
		if self.configDialogActive:
			parent = self.Parent
			parent.metadataStreams = metadataEnabled
			parent.profiles.SetFocus()
			parent.Enable()
		else:
			from . import splmisc
			splmisc.metadataConnector(servers=metadataEnabled)
			# 6.1: Store just toggled settings to profile if told to do so.
			if self.applyCheckbox.Value: splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"] = metadataEnabled
		self.Destroy()
		_metadataDialogOpened = False

	def onCancel(self, evt):
		global _metadataDialogOpened
		if self.configDialogActive: self.Parent.Enable()
		self.Destroy()
		_metadataDialogOpened = False

	def onAppTerminate(self):
		self.onCancel(None)

class MetadataStreamingPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure metadata streaming status for DSP encoder and four additional URL's.
	title = _("Metadata streaming")

	def makeSettings(self, settingsSizer):
		metadataSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		self.metadataValues=[("off",_("Off")),
		# Translators: One of the metadata notification settings.
		("startup",_("When Studio starts")),
		# Translators: One of the metadata notification settings.
		("instant",_("When instant switch profile is active"))]
		# Translators: the label for a setting in SPL add-on settings to be notified that metadata streaming is enabled.
		self.metadataList = metadataSizerHelper.addLabeledControl(_("&Metadata streaming notification and connection"), wx.Choice, choices=[x[1] for x in self.metadataValues])
		metadataCurValue=splconfig.SPLConfig["General"]["MetadataReminder"]
		selection = next((x for x,y in enumerate(self.metadataValues) if y[0]==metadataCurValue))
		try:
			self.metadataList.SetSelection(selection)
		except:
			pass

		# Profile specific: have a map of current profile settings.
		self._curProfileSettings = {}
		# WX's native CheckListBox isn't user friendly.
		# Therefore use checkboxes laid out across the top.
		# 17.04: instead of two loops, just use one loop, with labels deriving from a stream labels tuple.
		# Only one loop is needed as helper.addLabelControl returns the checkbox itself and that can be appended.
		# Add checkboxes for each stream, beginning with the DSP encoder.
		# #76 (18.09-LTS): completely changed to use custom check list box (NVDA Core issue 7491).
		from . import splmisc
		self.checkedStreams = metadataSizerHelper.addLabeledControl(_("&Select the URL for metadata streaming upon request:"), CustomCheckListBox, choices=metadataStreamLabels)
		for stream in six.moves.range(5):
			self.checkedStreams.Check(stream, check=splconfig._SPLDefaults["MetadataStreaming"]["MetadataEnabled"][stream])
		self.checkedStreams.SetSelection(0)

	def onPanelActivated(self):
		selectedProfile = _selectedProfile
		if selectedProfile is None: selectedProfile = splconfig.SPLConfig.activeProfile
		# Load settings from a temp map first.
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		if selectedProfile not in self._curProfileSettings: settings = list(curProfile["MetadataStreaming"]["MetadataEnabled"])
		else: settings = self._curProfileSettings[selectedProfile]
		for stream in six.moves.range(5):
			self.checkedStreams.Check(stream, check=settings[stream])
		super(MetadataStreamingPanel, self).onPanelActivated()

	def onPanelDeactivated(self):
		selectedProfile = _selectedProfile
		if selectedProfile is None: selectedProfile = splconfig.SPLConfig.activeProfile
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		currentSettings = [self.checkedStreams.IsChecked(url) for url in six.moves.range(5)]
		if currentSettings != curProfile["MetadataStreaming"]["MetadataEnabled"]:
			self._curProfileSettings[selectedProfile] = currentSettings
		super(MetadataStreamingPanel, self).onPanelDeactivated()

	def onSave(self):
		splconfig.SPLConfig["General"]["MetadataReminder"] = self.metadataValues[self.metadataList.GetSelection()][0]
		selectedProfile = _selectedProfile
		if selectedProfile is None: selectedProfile = splconfig.SPLConfig.activeProfile
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		# #76 (18.09-LTS): traverse check list box and build boolean list accordingly.
		curProfile["MetadataStreaming"]["MetadataEnabled"] = [self.checkedStreams.IsChecked(url) for url in six.moves.range(5)]
		self._curProfileSettings.clear()
		if not _configApplyOnly: self._curProfileSettings = None

	def onDiscard(self):
		self._curProfileSettings.clear()
		self._curProfileSettings = None

# Column announcement manager.
# Select which track columns should be announced and in which order.
# 18.08: also serves as a base dialog for Playlist Transcripts/column selector setting.
class ColumnAnnouncementsDialog(wx.Dialog):

	def __init__(self, parent, playlistTranscripts=False):
		self.playlistTranscripts = playlistTranscripts
		if not self.playlistTranscripts:
			# Translators: Title of a dialog to configure column announcements (order and what columns should be announced).
			dialogTitle = _("Manage column announcements")
		else:
			# Translators: Title of a dialog to configure columnn seleciton for Playlist Transcripts.
			dialogTitle = _("Playlist transcript columns")
		super(ColumnAnnouncementsDialog, self).__init__(parent, title=dialogTitle)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		colAnnouncementsHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		if not self.playlistTranscripts:
			# Translators: Help text to select columns to be announced.
			labelText = _("&Select columns to be announced\n(artist and title are announced by default):")
		else:
			# Translators: Help text to select columns to be announced.
			labelText = _("&Select columns to be included in playlist transcripts\n(artist and title are always included):")

		# Same as metadata dialog (wx.CheckListBox isn't user friendly).
		# Gather values for checkboxes except artist and title.
		# 6.1: Split these columns into rows.
		# 17.04: Gather items into a single list instead of three.
		# #76 (18.09-LTS): completely changed to use custom check list box (NVDA Core issue 7491).
		# For this one, remove Artist and Title.
		self.Parent.includedColumns.discard("Artist")
		self.Parent.includedColumns.discard("Title")
		checkableColumns = ("Duration","Intro","Category","Filename","Outro","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Time Scheduled")
		self.checkedColumns = colAnnouncementsHelper.addLabeledControl(labelText, CustomCheckListBox, choices=checkableColumns)
		self.checkedColumns.SetCheckedStrings(self.Parent.includedColumns)
		self.checkedColumns.SetSelection(0)

		# wxPython 4 contains RearrangeList to allow item orders to be changed automatically.
		# Because wxPython 3 doesn't include this, work around by using a variant of list box and move up/down buttons.
		# 17.04: The label for the list below is above the list, so move move up/down buttons to the right of the list box.
		# Translators: The label for a setting in SPL add-on dialog to select column announcement order.
		self.trackColumns = colAnnouncementsHelper.addLabeledControl(_("Column &order:"), wx.ListBox, choices=parent.columnOrder)
		self.trackColumns.Bind(wx.EVT_LISTBOX,self.onColumnSelection)
		self.trackColumns.SetSelection(0)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a button in column announcement dialog to change column position for the selected column.
		self.upButton = wx.Button(self, wx.ID_ANY, label=_("Move &up"))
		self.upButton.Bind(wx.EVT_BUTTON,self.onMoveUp)
		self.upButton.Disable()
		sizer.Add(self.upButton)
		# Translators: The label for a button in column announcement dialog to change column position for the selected column.
		self.dnButton = wx.Button(self, wx.ID_ANY, label=_("Move &down"))
		self.dnButton.Bind(wx.EVT_BUTTON,self.onMoveDown)
		sizer.Add(self.dnButton)
		colAnnouncementsHelper.addItem(sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		colAnnouncementsHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(colAnnouncementsHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedColumns.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.columnOrder = self.trackColumns.GetItems()
		parent.includedColumns = set(self.checkedColumns.GetCheckedStrings())
		# Make sure artist and title are always included.
		parent.includedColumns.add("Artist")
		parent.includedColumns.add("Title")
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

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

class ColumnAnnouncementsPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure column announcements (order and what columns should be announced).
	title = _("Column announcements")

	def makeSettings(self, settingsSizer):
		colAnnouncementsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self.columnOrder = splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
		# Without manual conversion below, it produces a rare bug where clicking cancel after changing column inclusion causes new set to be retained.
		self.includedColumns = set(splconfig._SPLDefaults["ColumnAnnouncement"]["IncludedColumns"])
		# #77 (18.09-LTS): record temporary settings.
		self._curProfileSettings = {}

		# Translators: the label for a setting in SPL add-on settings to toggle custom column announcement.
		self.columnOrderCheckbox=colAnnouncementsHelper.addItem(wx.CheckBox(self,wx.ID_ANY,label=_("Announce columns in the &order shown on screen")))
		self.columnOrderCheckbox.SetValue(splconfig._SPLDefaults["ColumnAnnouncement"]["UseScreenColumnOrder"])

		# Translators: The label of a button to manage column announcements.
		manageColumnsButton = colAnnouncementsHelper.addItem(wx.Button(self, label=_("&Manage track column announcements...")))
		manageColumnsButton.Bind(wx.EVT_BUTTON, self.onManageColumns)

		# Translators: the label for a setting in SPL add-on settings to toggle whether column headers should be included when announcing track information.
		self.columnHeadersCheckbox = colAnnouncementsHelper.addItem(wx.CheckBox(self, label=_("Include column &headers when announcing track information")))
		self.columnHeadersCheckbox.SetValue(splconfig._SPLDefaults["ColumnAnnouncement"]["IncludeColumnHeaders"])

	def onPanelActivated(self):
		selectedProfile = _selectedProfile
		if selectedProfile is None: selectedProfile = splconfig.SPLConfig.activeProfile
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		if selectedProfile not in self._curProfileSettings: settings = dict(curProfile)
		else: settings = dict(self._curProfileSettings[selectedProfile])
		self.columnOrderCheckbox.SetValue(settings["ColumnAnnouncement"]["UseScreenColumnOrder"])
		self.columnOrder = list(settings["ColumnAnnouncement"]["ColumnOrder"])
		# 6.1: Again convert list to set.
		self.includedColumns = set(settings["ColumnAnnouncement"]["IncludedColumns"])
		self.columnHeadersCheckbox.SetValue(settings["ColumnAnnouncement"]["IncludeColumnHeaders"])
		super(ColumnAnnouncementsPanel, self).onPanelActivated()

	def onPanelDeactivated(self):
		selectedProfile = _selectedProfile
		if selectedProfile is None: selectedProfile = splconfig.SPLConfig.activeProfile
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		currentSettings = {"ColumnAnnouncement": {}}
		currentSettings["ColumnAnnouncement"]["UseScreenColumnOrder"] = self.columnOrderCheckbox.GetValue()
		currentSettings["ColumnAnnouncement"]["ColumnOrder"] = list(self.columnOrder)
		currentSettings["ColumnAnnouncement"]["IncludedColumns"] = set(self.includedColumns)
		currentSettings["ColumnAnnouncement"]["IncludeColumnHeaders"] = self.columnHeadersCheckbox.GetValue()
		if currentSettings["ColumnAnnouncement"] != curProfile["ColumnAnnouncement"]:
			self._curProfileSettings[selectedProfile] = dict(currentSettings)
		super(ColumnAnnouncementsPanel, self).onPanelDeactivated()

	def onSave(self):
		selectedProfile = _selectedProfile
		if selectedProfile is None: selectedProfile = splconfig.SPLConfig.activeProfile
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		curProfile["ColumnAnnouncement"]["UseScreenColumnOrder"] = self.columnOrderCheckbox.Value
		curProfile["ColumnAnnouncement"]["ColumnOrder"] = self.columnOrder
		curProfile["ColumnAnnouncement"]["IncludedColumns"] = self.includedColumns
		curProfile["ColumnAnnouncement"]["IncludeColumnHeaders"] = self.columnHeadersCheckbox.Value
		self._curProfileSettings.clear()
		if not _configApplyOnly: self._curProfileSettings = None

	def onDiscard(self):
		# 6.1: Discard changes to included columns set.
		if self.includedColumns is not None: self.includedColumns.clear()
		self.includedColumns = None
		self._curProfileSettings.clear()
		self._curProfileSettings = None

	def onManageColumns(self, evt):
		self.Disable()
		ColumnAnnouncementsDialog(self).Show()

class PlaylistTranscriptsPanel(gui.SettingsPanel):
	# Translators: Title of a panel to configure playlsit transcripts options.
	title = _("Playlist transcripts")

	def makeSettings(self, settingsSizer):
		playlistTranscriptsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		from . import splmisc
		#self.transcriptFormat = splconfig.SPLConfig["PlaylistTranscripts"]["TranscriptFormat"]
		self.columnOrder = splconfig.SPLConfig["PlaylistTranscripts"]["ColumnOrder"]
		# Again manually create a new set.
		self.includedColumns = set(splconfig.SPLConfig["PlaylistTranscripts"]["IncludedColumns"])
		#self.availableTranscriptFormats = [output[0] for output in splmisc.SPLPlaylistTranscriptFormats]
		#self.availableTranscriptFormats.insert(0, "")

		# Translators: the label for a setting in SPL add-on settings to select preferred playlist transcript format.
		#labelText = _("&Prefered transcript format:")
		# Translators: one of the transcript format options.
		#self.transcriptFormatsList = playlistTranscriptsHelper.addLabeledControl(labelText, wx.Choice, choices=[_("ask me every time")]+[output[2] for output in splmisc.SPLPlaylistTranscriptFormats])
		#self.transcriptFormatsList.SetSelection(self.availableTranscriptFormats.index(splconfig.SPLConfig["PlaylistTranscripts"]["TranscriptFormat"]))

		# Translators: The label of a button to configure columns for playlist transcripts.
		transcriptColumnsButton = playlistTranscriptsHelper.addItem(wx.Button(self, label=_("Manage transcript columns...")))
		transcriptColumnsButton.Bind(wx.EVT_BUTTON, self.onTranscriptColumns)

	def onSave(self):
		#splconfig.SPLConfig["PlaylistTranscripts"]["TranscriptFormat"] = self.availableTranscriptFormats[self.transcriptFormatsList.GetSelection()]
		splconfig.SPLConfig["PlaylistTranscripts"]["ColumnOrder"] = list(self.columnOrder)
		splconfig.SPLConfig["PlaylistTranscripts"]["IncludedColumns"] = set(self.includedColumns)

	def onDiscard(self):
		# 6.1: Discard changes to included columns set.
		if self.includedColumns is not None: self.includedColumns.clear()
		self.includedColumns = None

	def onTranscriptColumns(self, evt):
		self.Disable()
		ColumnAnnouncementsDialog(self, playlistTranscripts=True).Show()

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
			cols = ("Artist","Title","Duration","Cue","Overlap","Intro","Segue","Filename","Album","CD Code","Outro","Year","URL 1","URL 2","Genre")
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
		for slot in six.moves.range(5):
			# Translators: The label for a setting in SPL add-on dialog to select column for this column slot.
			columns = sizer.addLabeledControl(_("Slot {position}").format(position = slot+1), wx.Choice, choices=cols)
			try:
				columns.SetSelection(cols.index(slots[slot]))
			except:
				pass
			self.columnSlots.append(columns)
		colExplorerHelper.addItem(sizer.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for slot in six.moves.range(5, 10):
			columns = sizer.addLabeledControl(_("Slot {position}").format(position = slot+1), wx.Choice, choices=cols)
			try:
				columns.SetSelection(cols.index(slots[slot]))
			except:
				pass
			self.columnSlots.append(columns)
		colExplorerHelper.addItem(sizer.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		colExplorerHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(colExplorerHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.columnSlots[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		# #62 (18.06): manually build a list so changes won't be retained when Cancel button is clicked from main settings, caused by reference problem.
		# Note that item count is based on how many column combo boxes are present in this dialog.
		# #63 (18.06): use levels instead due to introduction of Columns Explorer for SPL Creator.
		slots = [self.columnSlots[slot].GetStringSelection() for slot in six.moves.range(10)]
		if self.level == 0: parent.exploreColumns = slots
		elif self.level == 1: parent.exploreColumnsTT = slots
		elif self.level == 2: parent.exploreColumnsCreator = slots
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

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
		self.scheduledForCheckbox=sayStatusHelper.addItem(wx.CheckBox(self, label=_("Announce &scheduled time for the selected track")))
		self.scheduledForCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayScheduledFor"])
		# Translators: the label for a setting in SPL add-on settings to announce listener count.
		self.listenerCountCheckbox=sayStatusHelper.addItem(wx.CheckBox(self, label=_("Announce &listener count")))
		self.listenerCountCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayListenerCount"])
		# Translators: the label for a setting in SPL add-on settings to announce currently playing cart.
		self.cartNameCheckbox=sayStatusHelper.addItem(wx.CheckBox(self, label=_("&Announce name of the currently playing cart")))
		self.cartNameCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"])
		# Translators: the label for a setting in SPL add-on settings to announce currently playing track name.
		labelText = _("&Track name announcement:")
		# Translators: One of the track name announcement options.
		self.trackAnnouncements=[("auto",_("automatic")),
		# Translators: One of the track name announcement options.
		("background",_("while using other programs")),
		# Translators: One of the track name announcement options.
		("off",_("off"))]
		self.trackAnnouncementList=sayStatusHelper.addLabeledControl(labelText, wx.Choice, choices=[x[1] for x in self.trackAnnouncements])
		selection = next((x for x,y in enumerate(self.trackAnnouncements) if y[0]==splconfig.SPLConfig["SayStatus"]["SayPlayingTrackName"]))
		try:
			self.trackAnnouncementList.SetSelection(selection)
		except:
			pass
		# Translators: the label for a setting in SPL add-on settings to announce player position for the current and next tracks.
		self.playerPositionCheckbox=sayStatusHelper.addItem(wx.CheckBox(self, label=_("Include track player &position when announcing current and next track information")))
		self.playerPositionCheckbox.SetValue(splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"])

	def onSave(self):
		splconfig.SPLConfig["SayStatus"]["SayScheduledFor"] = self.scheduledForCheckbox.Value
		splconfig.SPLConfig["SayStatus"]["SayListenerCount"] = self.listenerCountCheckbox.Value
		splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"] = self.cartNameCheckbox.Value
		splconfig.SPLConfig["SayStatus"]["SayPlayingTrackName"] = self.trackAnnouncements[self.trackAnnouncementList.GetSelection()][0]
		splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"] = self.playerPositionCheckbox.Value

# Advanced options
# This panel houses advanced options such as using SPL Controller command to invoke SPL Assistant.
# More options will be added in 7.0.
# 7.0: Auto update check will be configurable from this panel.
# #6: this is one of a few panels that will make sure changes are okay to be saved (isValid).
# It is also one of two panels (the other one being broadcast profiles) that will perform extra actions if OK or Apply is clicked from add-on settings dialog (postSave).
class AdvancedOptionsPanel(gui.SettingsPanel):
	# Translators: title of a panel to configure advanced SPL add-on options such as update checking.
	title = _("Advanced")

	def makeSettings(self, settingsSizer):
		advOptionsHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# #48 (18.02): do not show auto-update checkbox and interval options if not needed.
		# The exception will be custom try builds.
		# #50 (18.04): made simpler because the update module won't be present if updating isn't supported.
		if splupdate and splupdate.isAddonUpdatingSupported() == splupdate.SPLUpdateErrorNone:
			# Translators: A checkbox to toggle automatic add-on updates.
			self.autoUpdateCheckbox=advOptionsHelper.addItem(wx.CheckBox(self,label=_("Automatically check for add-on &updates")))
			self.autoUpdateCheckbox.SetValue(splconfig.SPLConfig["Update"]["AutoUpdateCheck"])
			# Translators: The label for a setting in SPL add-on settings/advanced options to select automatic update interval in days.
			self.updateInterval=advOptionsHelper.addLabeledControl(_("Update &interval in days"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=180, initial=splconfig.SPLConfig["Update"]["UpdateInterval"])
		# Translators: A checkbox to toggle if SPL Controller command can be used to invoke Assistant layer.
		self.splConPassthroughCheckbox=advOptionsHelper.addItem(wx.CheckBox(self, label=_("Allow SPL C&ontroller command to invoke SPL Assistant layer")))
		self.splConPassthroughCheckbox.SetValue(splconfig.SPLConfig["Advanced"]["SPLConPassthrough"])
		# Translators: The label for a setting in SPL add-on dialog to set keyboard layout for SPL Assistant.
		labelText = _("SPL Assistant command &layout:")
		self.compatibilityLayouts=[("off","NVDA"),
		("jfw","JAWS for Windows"),
		("wineyes","Window-Eyes")]
		self.compatibilityList=advOptionsHelper.addLabeledControl(labelText, wx.Choice, choices=[x[1] for x in self.compatibilityLayouts])
		selection = next((x for x,y in enumerate(self.compatibilityLayouts) if y[0]==splconfig.SPLConfig["Advanced"]["CompatibilityLayer"]))
		try:
			self.compatibilityList.SetSelection(selection)
		except:
			pass
		# 18.09: allow some dev snapshot users to test pilot features.
		# Translators: A checkbox to enable pilot features (with risks involved).
		self.pilotBuildCheckbox=advOptionsHelper.addItem(wx.CheckBox(self, label=_("Pilot features: I want to test and provide early &feedback on features under development")))
		self.pilotBuildCheckbox.SetValue(splconfig.SPLConfig["Advanced"]["PilotFeatures"])
		if not splconfig.SPLConfig.canEnablePilotFeatures: self.pilotBuildCheckbox.Disable()

	# Check update channel and interval here.
	# The onSave method will just assume that it is okay to apply update channel switches and other advanced options.
	# 18.09: no op if something other than Studio add-on is used to check for updates.
	def isValid(self):
		if splupdate and splupdate.isAddonUpdatingSupported() == splupdate.SPLUpdateErrorNone:
			# If update interval is set to zero, update check will happen every time the app module loads, so warn users.
			if (splconfig.SPLConfig["Update"]["UpdateInterval"] > 0 and self.updateInterval.Value == 0 and gui.messageBox(
				# Translators: The confirmation prompt displayed when changing update interval to zero days (updates will be checked every time Studio app module loads).
				_("Update interval has been set to zero days, so updates to the Studio add-on will be checked every time NVDA and/or Studio starts. Are you sure you wish to continue?"),
				# Translators: The title of the update interval dialog.
				_("Confirm update interval"),
				wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self
			) == wx.NO):
				return False
		if (splconfig.SPLConfig.canEnablePilotFeatures and not splconfig.SPLConfig["Advanced"]["PilotFeatures"] and self.pilotBuildCheckbox.IsChecked() and gui.messageBox(
			# Translators: The confirmation prompt displayed when about to enable pilot flag (with risks involved).
			_("You are about to enable pilot features. Please note that pilot features may include functionality that might be unstable at times and should be used for testing and sending feedback to the add-on developer. If you prefer to use stable features, please answer no and uncheck pilot features checkbox. Are you sure you wish to enable pilot features?"),
			# Translators: The title of the channel switch confirmation dialog.
			_("Enable pilot features"),
			wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self
		) == wx.NO):
			return False
		return True

	def onSave(self):
		# Pilot features flag will be checked in post-save method below.
		# 18.09: but only if add-on update feature is usable from Studio add-on.
		splconfig.SPLConfig["Advanced"]["SPLConPassthrough"] = self.splConPassthroughCheckbox.Value
		splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] = self.compatibilityLayouts[self.compatibilityList.GetSelection()][0]
		if splupdate and splupdate.isAddonUpdatingSupported() == splupdate.SPLUpdateErrorNone:
			splconfig.SPLConfig["Update"]["AutoUpdateCheck"] = self.autoUpdateCheckbox.Value
			splconfig.SPLConfig["Update"]["UpdateInterval"] = self.updateInterval.Value

	def postSave(self):
		# Coordinate auto update timer restart routine if told to do so.
		# #50 (18.03): but only if add-on update facility is alive.
		if splupdate and splupdate.isAddonUpdatingSupported() == splupdate.SPLUpdateErrorNone:
			if not splconfig.SPLConfig["Update"]["AutoUpdateCheck"]:
				splupdate.updateCheckTimerEnd()
			else:
				if splupdate._SPLUpdateT is None: splupdate.updateInit()
		if splconfig.SPLConfig.canEnablePilotFeatures and self.pilotBuildCheckbox.Value != splconfig.SPLConfig["Advanced"]["PilotFeatures"]:
			# Translators: A dialog message shown when pilot features is turned on or off.
			wx.CallAfter(gui.messageBox, _("You have toggled pilot features checkbox. You must restart NVDA for the change to take effect."),
			# Translators: Title of the pilot features dialog.
			_("Pilot features"), wx.OK|wx.ICON_INFORMATION)
			splconfig.SPLConfig["Advanced"]["PilotFeatures"] = self.pilotBuildCheckbox.Value
			splconfig.SPLConfig._pendingPilotFeaturesToggle = True

# A dialog to reset add-on config including encoder settings and others.
class ResetDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: Title of the dialog to reset various add-on settings.
		super(ResetDialog, self).__init__(parent, title=_("Reset settings"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		resetHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: the label for resetting profile triggers.
		self.resetInstantProfileCheckbox=resetHelper.addItem(wx.CheckBox(self,label=_("Reset instant switch profile")))
		# Translators: the label for resetting profile triggers.
		self.resetTimeProfileCheckbox=resetHelper.addItem(wx.CheckBox(self,label=_("Delete time-based profile database")))
		# Translators: the label for resetting encoder settings.
		self.resetEncodersCheckbox=resetHelper.addItem(wx.CheckBox(self,label=_("Remove encoder settings")))
		# Translators: the label for resetting track comments.
		self.resetTrackCommentsCheckbox=resetHelper.addItem(wx.CheckBox(self,label=_("Erase track comments")))

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
		_("Warning"),wx.YES_NO|wx.NO_DEFAULT|wx.ICON_WARNING,self
		)!=wx.YES:
			parent.Enable()
			self.Destroy()
			return
		import threading, sys, globalVars
		# Reset all profiles.
		# LTS: Only a priveleged thread should do this, otherwise unexpected things may happen.
		with threading.Lock() as resetting:
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
			if self.resetTimeProfileCheckbox.Value:
				splconfig.profileTriggers.clear()
				if splconfig.triggerTimer is not None and splconfig.triggerTimer.IsRunning():
					splconfig.triggerTimer.Stop()
					splconfig.triggerTimer = None
			if self.resetTrackCommentsCheckbox.Value:
				splconfig.trackComments.clear()
			if self.resetEncodersCheckbox.Value:
				if os.path.exists(os.path.join(globalVars.appArgs.configPath, "splStreamLabels.ini")):
					os.remove(os.path.join(globalVars.appArgs.configPath, "splStreamLabels.ini"))
				if "globalPlugins.splUtils.encoders" in sys.modules:
					import globalPlugins.splUtils.encoders
					globalPlugins.splUtils.encoders.cleanup()
			_configDialogOpened = False
			# Translators: A dialog message shown when settings were reset to defaults.
			wx.CallAfter(gui.messageBox, _("Successfully applied default add-on settings."),
			# Translators: Title of the reset config dialog.
			_("Reset configuration"), wx.OK|wx.ICON_INFORMATION)
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
	# Translators: This is the label for the StationPlaylist Studio configuration dialog.
	title = _("Studio Add-on Settings")
	categoryClasses=[
		BroadcastProfilesPanel,
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
		# #40 (17.12): respond to app terminate notification by closing this dialog.
		# All top-level dialogs will be affected by this, and apart from this one, others will check for flags also.
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

	def onOk(self, evt):
		super(SPLConfigDialog,  self).onOk(evt)
		# But because of issues encountered while saving some settings, settings dialog might still be active, as well as selected profile flag not being cleared.
		global _configDialogOpened, _selectedProfile
		_configDialogOpened = False
		_selectedProfile = None

	def onCancel(self, evt):
		super(SPLConfigDialog,  self).onCancel(evt)
		global _configDialogOpened, _selectedProfile
		_configDialogOpened = False
		_selectedProfile = None

	def onApply(self,evt):
		# Let profile sensitive panels (such as broadcast profiles) know that settings should be applied.
		global _configApplyOnly
		_configApplyOnly = True
		super(SPLConfigDialog,  self).onApply(evt)
		_configApplyOnly = False

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)


# Open the above dialog upon request.
def onConfigDialog(evt):
	# 5.2: Guard against alarm dialogs.
	if _alarmDialogOpened or _metadataDialogOpened:
		# Translators: Presented when an alarm dialog is opened.
		wx.CallAfter(gui.messageBox, _("Another add-on settings dialog is open. Please close the previously opened dialog first."), _("Error"), wx.OK|wx.ICON_ERROR)
	else: gui.mainFrame._popupSettingsDialog(SPLConfigDialog)
