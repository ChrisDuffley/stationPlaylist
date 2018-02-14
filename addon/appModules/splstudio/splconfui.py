# SPL Studio Configuration user interfaces
# An app module and global plugin package for NVDA
# Copyright 2016-2018 Joseph Lee and others, released under GPL.
# Split from SPL config module in 2016.
# Provides the configuration management UI package for SPL Studio app module.
# For code which provides foundation for code in this module, see splconfig module.

import sys
py3 = sys.version.startswith("3")
import os
import weakref
import api
import gui
import wx
from winUser import user32
import tones
try:
	from . import splupdate
except RuntimeError:
	splupdate = None
from . import splconfig
from . import splactions

# Python 3 preparation (a compatibility layer until Six module is included).
rangeGen = range if py3 else xrange

# Until wx.CENTER_ON_SCREEN returns...
CENTER_ON_SCREEN = wx.CENTER_ON_SCREEN if hasattr(wx, "CENTER_ON_SCREEN") else 2

# Configuration dialog.
_configDialogOpened = False

class SPLConfigDialog(gui.SettingsDialog):
	# Translators: This is the label for the StationPlaylist Studio configuration dialog.
	title = _("Studio Add-on Settings")

	def makeSettings(self, settingsSizer):
		SPLConfigHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# #40 (17.12): respond to app terminate notification by closing this dialog.
		# All top-level dialogs will be affected by this, and apart from this one, others will check for flags also.
		splactions.SPLActionAppTerminating.register(self.onAppTerminate)

		# Broadcast profile controls were inspired by Config Profiles dialog in NVDA Core.
		# 7.0: Have a copy of the sorted profiles so the actual combo box items can show profile flags.
		# 8.0: No need to sort as profile names from ConfigHub knows what to do.
		# 17.10: skip this if only normal profile is in use.
		if not (splconfig.SPLConfig.configInMemory or splconfig.SPLConfig.normalProfileOnly):
			self.profileNames = list(splconfig.SPLConfig.profileNames)
			self.profileNames[0] = _("Normal profile")
			# Translators: The label for a setting in SPL add-on dialog to select a broadcast profile.
			self.profiles = SPLConfigHelper.addLabeledControl(_("Broadcast &profile:"), wx.Choice, choices=self.displayProfiles(list(self.profileNames)))
			self.profiles.Bind(wx.EVT_CHOICE, self.onProfileSelection)
			try:
				self.profiles.SetSelection(self.profileNames.index(splconfig.SPLConfig.activeProfile))
			except:
				pass

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
			SPLConfigHelper.addItem(sizer.sizer)
		self.switchProfile = splconfig.SPLConfig.instantSwitch
		self.activeProfile = splconfig.SPLConfig.activeProfile
		# Used as sanity check in case switch profile is renamed or deleted.
		self.switchProfileRenamed = False
		self.switchProfileDeleted = False

		self.beepAnnounce = splconfig.SPLConfig["General"]["BeepAnnounce"]
		self.messageVerbosity = splconfig.SPLConfig["General"]["MessageVerbosity"]
		self.brailleTimer = splconfig.SPLConfig["General"]["BrailleTimer"]
		self.libScan = splconfig.SPLConfig["General"]["LibraryScanAnnounce"]
		self.hourAnnounce = splconfig.SPLConfig["General"]["TimeHourAnnounce"]
		self.verticalColumn = splconfig.SPLConfig["General"]["VerticalColumnAnnounce"]
		self.categorySounds = splconfig.SPLConfig["General"]["CategorySounds"]
		self.trackComments = splconfig.SPLConfig["General"]["TrackCommentAnnounce"]
		self.topBottom = splconfig.SPLConfig["General"]["TopBottomAnnounce"]
		self.requestsAlert = splconfig.SPLConfig["General"]["RequestsAlert"]
		# Translators: The label of a button to open a dialog to configure general add-on settings such as beep announcement and top and bottom notifications.
		self.generalSettingsButton = SPLConfigHelper.addItem(wx.Button(self, label=_("&General add-on settings...")))
		self.generalSettingsButton.Bind(wx.EVT_BUTTON, self.onGeneralSettings)

		self.endOfTrackTime = splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"]
		self.sayEndOfTrack = splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"]
		self.songRampTime = splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"]
		self.saySongRamp = splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"]
		self.micAlarm = splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]
		self.micAlarmInterval = splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"]
		# Translators: The label of a button to open a dialog to configure various alarms.
		alarmsCenterButton = SPLConfigHelper.addItem(wx.Button(self, label=_("&Alarms Center...")))
		alarmsCenterButton.Bind(wx.EVT_BUTTON, self.onAlarmsCenter)

		# Translators: One of the alarm notification options.
		self.alarmAnnounceValues=[("beep",_("beep")),
		# Translators: One of the alarm notification options.
		("message",_("message")),
		# Translators: One of the alarm notification options.
		("both",_("both beep and message"))]
		# Translators: The label for a setting in SPL add-on dialog to control alarm announcement type.
		self.alarmAnnounceList = SPLConfigHelper.addLabeledControl(_("&Alarm notification:"), wx.Choice, choices=[x[1] for x in self.alarmAnnounceValues])
		alarmAnnounceCurValue=splconfig.SPLConfig["General"]["AlarmAnnounce"]
		selection = (x for x,y in enumerate(self.alarmAnnounceValues) if y[0]==alarmAnnounceCurValue).next()
		try:
			self.alarmAnnounceList.SetSelection(selection)
		except:
			pass

		# Translators: The label of a button to manage playlist snapshot flags.
		playlistSnapshotFlagsButton = SPLConfigHelper.addItem(wx.Button(self, label=_("&Playlist snapshots...")))
		playlistSnapshotFlagsButton.Bind(wx.EVT_BUTTON, self.onPlaylistSnapshotFlags)
		# Playlist snapshot flags to be manipulated by the configuration dialog.
		self.playlistDurationMinMax = splconfig.SPLConfig["PlaylistSnapshots"]["DurationMinMax"]
		self.playlistDurationAverage = splconfig.SPLConfig["PlaylistSnapshots"]["DurationAverage"]
		self.playlistArtistCount = splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCount"]
		self.playlistArtistCountLimit = splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"]
		self.playlistCategoryCount = splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCount"]
		self.playlistCategoryCountLimit = splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"]
		self.playlistGenreCount = splconfig.SPLConfig["PlaylistSnapshots"]["GenreCount"]
		self.playlistGenreCountLimit = splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"]
		self.resultsWindowOnFirstPress = splconfig.SPLConfig["PlaylistSnapshots"]["ShowResultsWindowOnFirstPress"]

		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		self.metadataValues=[("off",_("Off")),
		# Translators: One of the metadata notification settings.
		("startup",_("When Studio starts")),
		# Translators: One of the metadata notification settings.
		("instant",_("When instant switch profile is active"))]
		# Translators: the label for a setting in SPL add-on settings to be notified that metadata streaming is enabled.
		self.metadataList = sizer.addLabeledControl(_("&Metadata streaming notification and connection"), wx.Choice, choices=[x[1] for x in self.metadataValues])
		metadataCurValue=splconfig.SPLConfig["General"]["MetadataReminder"]
		selection = (x for x,y in enumerate(self.metadataValues) if y[0]==metadataCurValue).next()
		try:
			self.metadataList.SetSelection(selection)
		except:
			pass
		self.metadataStreams = list(splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"])
		# Translators: The label of a button to manage column announcements.
		manageMetadataButton = sizer.addItem(wx.Button(self, label=_("Configure metadata &streaming connection options...")))
		manageMetadataButton.Bind(wx.EVT_BUTTON, self.onManageMetadata)
		SPLConfigHelper.addItem(sizer.sizer)

		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		# Translators: the label for a setting in SPL add-on settings to toggle custom column announcement.
		self.columnOrderCheckbox=sizer.addItem(wx.CheckBox(self,wx.NewId(),label=_("Announce columns in the &order shown on screen")))
		self.columnOrderCheckbox.SetValue(splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"])
		self.columnOrder = splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"]
		# Without manual conversion below, it produces a rare bug where clicking cancel after changing column inclusion causes new set to be retained.
		self.includedColumns = set(splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"])
		# Translators: The label of a button to manage column announcements.
		manageColumnsButton = sizer.addItem(wx.Button(self, label=_("&Manage track column announcements...")))
		manageColumnsButton.Bind(wx.EVT_BUTTON, self.onManageColumns)
		SPLConfigHelper.addItem(sizer.sizer)

		# Translators: the label for a setting in SPL add-on settings to toggle whether column headers should be included when announcing track information.
		self.columnHeadersCheckbox = SPLConfigHelper.addItem(wx.CheckBox(self, label=_("Include column &headers when announcing track information")))
		self.columnHeadersCheckbox.SetValue(splconfig.SPLConfig["ColumnAnnouncement"]["IncludeColumnHeaders"])

		sizer = gui.guiHelper.ButtonHelper(wx.HORIZONTAL)
		# Translators: The label of a button to configure columns explorer slots (SPL Assistant, number row keys to announce specific columns).
		columnsExplorerButton = sizer.addButton(self, label=_("Columns E&xplorer..."))
		columnsExplorerButton.Bind(wx.EVT_BUTTON, self.onColumnsExplorer)
		self.exploreColumns = splconfig.SPLConfig["General"]["ExploreColumns"]
		# Translators: The label of a button to configure columns explorer slots for Track Tool (SPL Assistant, number row keys to announce specific columns).
		columnsExplorerTTButton = sizer.addButton(self, label=_("Columns Explorer for &Track Tool..."))
		columnsExplorerTTButton.Bind(wx.EVT_BUTTON, self.onColumnsExplorerTT)
		self.exploreColumnsTT = splconfig.SPLConfig["General"]["ExploreColumnsTT"]
		SPLConfigHelper.addItem(sizer.sizer)

		sizer = gui.guiHelper.ButtonHelper(wx.HORIZONTAL)
		# Translators: The label of a button to open status announcement dialog such as announcing listener count.
		sayStatusButton = sizer.addButton(self, label=_("&Status announcements..."))
		sayStatusButton.Bind(wx.EVT_BUTTON, self.onStatusAnnouncement)
		# Say status flags to be picked up by the dialog of this name.
		self.scheduledFor = splconfig.SPLConfig["SayStatus"]["SayScheduledFor"]
		self.listenerCount = splconfig.SPLConfig["SayStatus"]["SayListenerCount"]
		self.cartName = splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"]
		self.playingTrackName = splconfig.SPLConfig["SayStatus"]["SayPlayingTrackName"]
		self.studioPlayerPosition = splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"]
		# Translators: The label of a button to open advanced options such as using SPL Controller command to invoke Assistant layer.
		advancedOptButton = sizer.addButton(self, label=_("&Advanced options..."))
		advancedOptButton.Bind(wx.EVT_BUTTON, self.onAdvancedOptions)
		self.splConPassthrough = splconfig.SPLConfig["Advanced"]["SPLConPassthrough"]
		self.compLayer = splconfig.SPLConfig["Advanced"]["CompatibilityLayer"]
		self.autoUpdateCheck = splconfig.SPLConfig["Update"]["AutoUpdateCheck"]
		self.updateInterval = splconfig.SPLConfig["Update"]["UpdateInterval"]
		self.updateChannel = splupdate.SPLUpdateChannel
		self.pendingChannelChange = False
		SPLConfigHelper.addItem(sizer.sizer)

		# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		resetButton = SPLConfigHelper.addItem(wx.Button(self, label=_("Reset settings...")))
		resetButton.Bind(wx.EVT_BUTTON,self.onResetConfig)

	def postInit(self):
		global _configDialogOpened
		_configDialogOpened = True
		self.profiles.SetFocus() if hasattr(self, "profiles") else self.generalSettingsButton.SetFocus()

	def onOk(self, evt):
		global _configDialogOpened
		if hasattr(self, "profiles"):
			selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
			if splconfig.SPLConfig.activeProfile != selectedProfile:
				splconfig.SPLConfig.swapProfiles(splconfig.SPLConfig.activeProfile, selectedProfile)
		splconfig.SPLConfig["General"]["BeepAnnounce"] = self.beepAnnounce
		splconfig.SPLConfig["General"]["MessageVerbosity"] = self.messageVerbosity
		splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"] = self.endOfTrackTime
		splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"] = self.sayEndOfTrack
		splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"] = self.songRampTime
		splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"] = self.saySongRamp
		splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"] = self.micAlarm
		splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] = self.micAlarmInterval
		splconfig.SPLConfig["General"]["AlarmAnnounce"] = self.alarmAnnounceValues[self.alarmAnnounceList.GetSelection()][0]
		splconfig.SPLConfig["General"]["BrailleTimer"] = self.brailleTimer
		splconfig.SPLConfig["General"]["LibraryScanAnnounce"] = self.libScan
		splconfig.SPLConfig["General"]["TimeHourAnnounce"] = self.hourAnnounce
		splconfig.SPLConfig["General"]["CategorySounds"] = self.categorySounds
		splconfig.SPLConfig["General"]["TrackCommentAnnounce"] = self.trackComments
		splconfig.SPLConfig["General"]["TopBottomAnnounce"] = self.topBottom
		splconfig.SPLConfig["General"]["RequestsAlert"] = self.requestsAlert
		splconfig.SPLConfig["PlaylistSnapshots"]["DurationMinMax"] = self.playlistDurationMinMax
		splconfig.SPLConfig["PlaylistSnapshots"]["DurationAverage"] = self.playlistDurationAverage
		splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCount"] = self.playlistArtistCount
		splconfig.SPLConfig["PlaylistSnapshots"]["ArtistCountLimit"] = self.playlistArtistCountLimit
		splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCount"] = self.playlistCategoryCount
		splconfig.SPLConfig["PlaylistSnapshots"]["CategoryCountLimit"] = self.playlistCategoryCountLimit
		splconfig.SPLConfig["PlaylistSnapshots"]["GenreCount"] = self.playlistGenreCount
		splconfig.SPLConfig["PlaylistSnapshots"]["GenreCountLimit"] = self.playlistGenreCountLimit
		splconfig.SPLConfig["PlaylistSnapshots"]["ShowResultsWindowOnFirstPress"] = self.resultsWindowOnFirstPress
		splconfig.SPLConfig["General"]["MetadataReminder"] = self.metadataValues[self.metadataList.GetSelection()][0]
		splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"] = self.metadataStreams
		splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"] = self.columnOrderCheckbox.Value
		splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"] = self.columnOrder
		splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"] = self.includedColumns
		splconfig.SPLConfig["ColumnAnnouncement"]["IncludeColumnHeaders"] = self.columnHeadersCheckbox.Value
		splconfig.SPLConfig["General"]["ExploreColumns"] = self.exploreColumns
		splconfig.SPLConfig["General"]["ExploreColumnsTT"] = self.exploreColumnsTT
		splconfig.SPLConfig["General"]["VerticalColumnAnnounce"] = self.verticalColumn
		splconfig.SPLConfig["SayStatus"]["SayScheduledFor"] = self.scheduledFor
		splconfig.SPLConfig["SayStatus"]["SayListenerCount"] = self.listenerCount
		splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"] = self.cartName
		splconfig.SPLConfig["SayStatus"]["SayPlayingTrackName"] = self.playingTrackName
		splconfig.SPLConfig["SayStatus"]["SayStudioPlayerPosition"] = self.studioPlayerPosition
		splconfig.SPLConfig["Advanced"]["SPLConPassthrough"] = self.splConPassthrough
		splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] = self.compLayer
		splconfig.SPLConfig["Update"]["AutoUpdateCheck"] = self.autoUpdateCheck
		splconfig.SPLConfig["Update"]["UpdateInterval"] = self.updateInterval
		self.pendingChannelChange = splupdate.SPLUpdateChannel != self.updateChannel
		splupdate.SPLUpdateChannel = self.updateChannel
		splconfig.SPLConfig.instantSwitch = self.switchProfile
		# Make sure to nullify prev profile if instant switch profile is gone.
		# 7.0: Don't do the following in the midst of a broadcast.
		if self.switchProfile is None and not splconfig._triggerProfileActive:
			splconfig.SPLConfig.prevProfile = None
		_configDialogOpened = False
		# 7.0: Perform extra action such as restarting auto update timer.
		self.onCloseExtraAction()
		# Apply changes to profile triggers.
		splconfig.profileTriggers = dict(self._profileTriggersConfig)
		self._profileTriggersConfig.clear()
		self._profileTriggersConfig = None
		splconfig.triggerStart(restart=True)
		# 8.0: Make sure NVDA knows this must be cached (except for normal profile).
		# 17.10: but not when config is volatile.
		try:
			if selectedProfile != _("Normal profile") and selectedProfile not in splconfig._SPLCache:
				splconfig._cacheConfig(splconfig.SPLConfig.profileByName(selectedProfile))
		except NameError:
			pass
		super(SPLConfigDialog,  self).onOk(evt)

	def onCancel(self, evt):
		global _configDialogOpened
		# 6.1: Discard changes to included columns set.
		if self.includedColumns is not None: self.includedColumns.clear()
		self.includedColumns = None
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
			prevActive = _("Normal profile")
		if self.switchProfileRenamed or self.switchProfileDeleted:
			splconfig.SPLConfig.instantSwitch = self.switchProfile
		_configDialogOpened = False
		super(SPLConfigDialog,  self).onCancel(evt)

	# Perform extra action when closing this dialog such as restarting update timer.
	def onCloseExtraAction(self):
		# Coordinate auto update timer restart routine if told to do so.
		if not splconfig.SPLConfig["Update"]["AutoUpdateCheck"] or self.pendingChannelChange:
			if splupdate._SPLUpdateT is not None and splupdate._SPLUpdateT.IsRunning(): splupdate._SPLUpdateT.Stop()
			splupdate._SPLUpdateT = None
			if self.pendingChannelChange:
				splupdate._pendingChannelChange = True
				# Translators: A dialog message shown when add-on update channel has changed.
				wx.CallAfter(gui.messageBox, _("You have changed the add-on update channel. You must restart NVDA for the change to take effect. Be sure to answer yes when you are asked to install the new version when prompted after restarting NVDA."),
				# Translators: Title of the update channel dialog.
				_("Add-on update channel changed"), wx.OK|wx.ICON_INFORMATION)
		else:
			if splupdate._SPLUpdateT is None: splconfig.updateInit()
		# Change metadata streaming.
		# 17.11: call the metadata connector directly, reducing code duplication from previous releases.
		# 17.12: replaced by an action, with config UI active flag set.
		splactions.SPLActionProfileSwitched.notify(configDialogActive=True)

	def onAppTerminate(self):
		# Call cancel function when the app terminates so the dialog can be closed.
		self.onCancel(None)

	# Include profile flags such as instant profile string for display purposes.
	def displayProfiles(self, profiles):
		for index in rangeGen(len(profiles)):
			profiles[index] = splconfig.getProfileFlags(profiles[index])
		return profiles

	# Load settings from profiles.
	def onProfileSelection(self, evt):
		# Don't rely on SPLConfig here, as we don't want to interupt the show.
		selection = self.profiles.GetSelection()
		# No need to look at the profile flag.
		selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
		# Play a tone to indicate active profile.
		if self.activeProfile == selectedProfile:
			tones.beep(512, 40)
		if selection == 0:
			self.renameButton.Disable()
			self.deleteButton.Disable()
			self.triggerButton.Disable()
		else:
			self.renameButton.Enable()
			self.deleteButton.Enable()
			self.triggerButton.Enable()
		curProfile = splconfig.SPLConfig.profileByName(selectedProfile)
		self.endOfTrackTime = curProfile["IntroOutroAlarms"]["EndOfTrackTime"]
		self.sayEndOfTrack = curProfile["IntroOutroAlarms"]["SayEndOfTrack"]
		self.songRampTime = curProfile["IntroOutroAlarms"]["SongRampTime"]
		self.saySongRamp = curProfile["IntroOutroAlarms"]["SaySongRamp"]
		self.micAlarm = curProfile["MicrophoneAlarm"]["MicAlarm"]
		self.micAlarmInterval = curProfile["MicrophoneAlarm"]["MicAlarmInterval"]
		# 6.1: Take care of profile-specific column and metadata settings.
		self.metadataStreams = curProfile["MetadataStreaming"]["MetadataEnabled"]
		self.columnOrderCheckbox.SetValue(curProfile["ColumnAnnouncement"]["UseScreenColumnOrder"])
		self.columnOrder = curProfile["ColumnAnnouncement"]["ColumnOrder"]
		# 6.1: Again convert list to set.
		self.includedColumns = set(curProfile["ColumnAnnouncement"]["IncludedColumns"])
		self.columnHeadersCheckbox.SetValue(curProfile["ColumnAnnouncement"]["IncludeColumnHeaders"])

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
		# Translators: The label of a field to enter a new name for a broadcast profile.
		with wx.TextEntryDialog(self, _("New name:"),
				# Translators: The title of the dialog to rename a profile.
				_("Rename Profile"), defaultValue=oldName) as d:
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
			self.activeProfile = _("Normal profile")
			self.profiles.Selection = 0
		self.onProfileSelection(None)
		self.profiles.SetFocus()

	def onTriggers(self, evt):
		self.Disable()
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

	# Various general add-on settings.
	def onGeneralSettings(self, evt):
		self.Disable()
		GeneralSettingsDialog(self).Show()

	# Alarms Center.
	def onAlarmsCenter(self, evt):
		self.Disable()
		AlarmsCenter(self).Show()

	# Configure playlist snapshot flags.
	def onPlaylistSnapshotFlags(self, evt):
		self.Disable()
		PlaylistSnapshotsDialog(self).Show()

	# Manage metadata streaming.
	def onManageMetadata(self, evt):
		self.Disable()
		MetadataStreamingDialog(self).Show()

	# Manage column announcements.
	def onManageColumns(self, evt):
		self.Disable()
		ColumnAnnouncementsDialog(self).Show()

	# Columns Explorer configuration.
	def onColumnsExplorer(self, evt):
		self.Disable()
		ColumnsExplorerDialog(self).Show()

	# Track Tool Columns Explorer configuration.
	def onColumnsExplorerTT(self, evt):
		self.Disable()
		ColumnsExplorerDialog(self, tt=True).Show()

		# Status announcement dialog.
	def onStatusAnnouncement(self, evt):
		self.Disable()
		SayStatusDialog(self).Show()

	# Advanced options.
	# See advanced options class for more details.
	def onAdvancedOptions(self, evt):
		self.Disable()
		AdvancedOptionsDialog(self).Show()

	# Reset settings to defaults.
	# This affects the currently selected profile.
	def onResetConfig(self, evt):
		self.Disable()
		ResetDialog(self).Show()


# Open the above dialog upon request.
def onConfigDialog(evt):
	# 5.2: Guard against alarm dialogs.
	if _alarmDialogOpened or _metadataDialogOpened:
		# Translators: Presented when an alarm dialog is opened.
		wx.CallAfter(gui.messageBox, _("Another add-on settings dialog is open. Please close the previously opened dialog first."), _("Error"), wx.OK|wx.ICON_ERROR)
	else: gui.mainFrame._popupSettingsDialog(SPLConfigDialog)

# Helper dialogs for add-on settings dialog.

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
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

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
			baseProfile = {sect:key for sect, key in baseConfig.iteritems() if sect in splconfig._mutatableSettings}
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
		for day in rangeGen(len(calendar.day_name)):
			triggerDay=wx.CheckBox(self, wx.NewId(),label=calendar.day_name[day])
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
		self.Center(wx.BOTH | CENTER_ON_SCREEN)
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
class GeneralSettingsDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: Title of a dialog to configure various status announcements such as announcing listener count.
		super(GeneralSettingsDialog, self).__init__(parent, title=_("General add-on settings"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		generalSettingsHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: the label for a setting in SPL add-on settings to set status announcement between words and beeps.
		self.beepAnnounceCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("&Beep for status announcements")))
		self.beepAnnounceCheckbox.SetValue(parent.beepAnnounce)

		# Translators: One of the message verbosity levels.
		self.verbosityLevels=[("beginner",_("beginner")),
		# Translators: One of the message verbosity levels.
		("advanced",_("advanced"))]
		# Translators: The label for a setting in SPL add-on dialog to set message verbosity.
		self.verbosityList = generalSettingsHelper.addLabeledControl(_("Message &verbosity:"), wx.Choice, choices=[x[1] for x in self.verbosityLevels])
		currentVerbosity=parent.messageVerbosity
		selection = (x for x,y in enumerate(self.verbosityLevels) if y[0]==currentVerbosity).next()
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
		brailleTimerCurValue=parent.brailleTimer
		selection = (x for x,y in enumerate(self.brailleTimerValues) if y[0]==brailleTimerCurValue).next()
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
		libScanCurValue=parent.libScan
		selection = (x for x,y in enumerate(self.libScanValues) if y[0]==libScanCurValue).next()
		try:
			self.libScanList.SetSelection(selection)
		except:
			pass

		# Translators: the label for a setting in SPL add-on settings to announce time including hours.
		self.hourAnnounceCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("Include &hours when announcing track or playlist duration")))
		self.hourAnnounceCheckbox.SetValue(parent.hourAnnounce)

		# Translators: The label for a setting in SPL add-on dialog to set vertical column.
		verticalColLabel = _("&Vertical column navigation announcement:")
		# Translators: One of the options for vertical column navigation denoting NVDA will announce current column positoin (e.g. second column position from the left).
		self.verticalColumnsList = generalSettingsHelper.addLabeledControl(verticalColLabel, wx.Choice, choices=[_("whichever column I am reviewing"), "Status"] + splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"])
		verticalColumn = parent.verticalColumn
		selection = self.verticalColumnsList.FindString(verticalColumn) if verticalColumn is not None else 0
		try:
			self.verticalColumnsList.SetSelection(selection)
		except:
			pass

		# Translators: the label for a setting in SPL add-on settings to toggle category sound announcement.
		self.categorySoundsCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("&Beep for different track categories")))
		self.categorySoundsCheckbox.SetValue(parent.categorySounds)

		self.trackCommentValues=[("off",_("Off")),
		# Translators: One of the track comment notification settings.
		("message",_("Message")),
		# Translators: One of the track comment notification settings.
		("beep",_("Beep")),
		# Translators: One of the track comment notification settings.
		("both",_("Both"))]
		# Translators: the label for a setting in SPL add-on settings to set how track comments are announced.
		self.trackCommentList = generalSettingsHelper.addLabeledControl(_("&Track comment announcement:"), wx.Choice, choices=[x[1] for x in self.trackCommentValues])
		trackCommentCurValue=parent.trackComments
		selection = (x for x,y in enumerate(self.trackCommentValues) if y[0]==trackCommentCurValue).next()
		try:
			self.trackCommentList.SetSelection(selection)
		except:
			pass

		# Translators: the label for a setting in SPL add-on settings to toggle top and bottom notification.
		self.topBottomCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("Notify when located at &top or bottom of playlist viewer")))
		self.topBottomCheckbox.SetValue(parent.topBottom)

		# Translators: the label for a setting in SPL add-on settings to enable requests alert.
		self.requestsAlertCheckbox = generalSettingsHelper.addItem(wx.CheckBox(self, label=_("Play a sound when listener &requests arrive")))
		self.requestsAlertCheckbox.SetValue(parent.requestsAlert)

		generalSettingsHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(generalSettingsHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.beepAnnounceCheckbox.SetFocus()
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.beepAnnounce = self.beepAnnounceCheckbox.Value
		parent.messageVerbosity = self.verbosityLevels[self.verbosityList.GetSelection()][0]
		parent.brailleTimer = self.brailleTimerValues[self.brailleTimerList.GetSelection()][0]
		parent.libScan = self.libScanValues[self.libScanList.GetSelection()][0]
		parent.hourAnnounce = self.hourAnnounceCheckbox.Value
		parent.verticalColumn = self.verticalColumnsList.GetStringSelection() if self.verticalColumnsList.GetSelection() != 0 else None
		parent.categorySounds = self.categorySoundsCheckbox.Value
		parent.trackComments = self.trackCommentValues[self.trackCommentList.GetSelection()][0]
		parent.topBottom = self.topBottomCheckbox.Value
		parent.requestsAlert = self.requestsAlertCheckbox.Value
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

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
		self.Center(wx.BOTH | CENTER_ON_SCREEN)
		if level in (0, 1): self.outroAlarmEntry.SetFocus()
		elif level == 2: self.introAlarmEntry.SetFocus()
		elif level == 3: self.micAlarmEntry.SetFocus()

	def onOk(self, evt):
		global _alarmDialogOpened
		# Optimization: don't bother if Studio is dead and if the same value has been entered (only when standalone versions are opened).
		if self.level > 0 and user32.FindWindowA("SPLStudio", None):
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
				studioWindow = getNVDAObjectFromEvent(user32.FindWindowA("TStudioForm", None), OBJID_CLIENT, 0)
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

# Playlist snapshot flags
# For things such as checkboxes for average duration and top category count.
class PlaylistSnapshotsDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: Title of a dialog to configure playlist snapshot information.
		super(PlaylistSnapshotsDialog, self).__init__(parent, title=_("Playlist snapshots"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		playlistSnapshotsHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: Help text for playlist snapshots dialog.
		labelText = _("""Select information to be included when obtaining playlist snapshots.
		Track count and total duration are always included.""")
		playlistSnapshotsHelper.addItem(wx.StaticText(self, label=labelText))

		# Translators: the label for a setting in SPL add-on settings to include shortest and longest track duration in playlist snapshots window.
		self.playlistDurationMinMaxCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Shortest and longest tracks")))
		self.playlistDurationMinMaxCheckbox.SetValue(parent.playlistDurationMinMax)
		# Translators: the label for a setting in SPL add-on settings to include average track duration in playlist snapshots window.
		self.playlistDurationAverageCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Average track duration")))
		self.playlistDurationAverageCheckbox.SetValue(parent.playlistDurationAverage)
		# Translators: the label for a setting in SPL add-on settings to include track artist count in playlist snapshots window.
		self.playlistArtistCountCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Artist count")))
		self.playlistArtistCountCheckbox.SetValue(parent.playlistArtistCount)
		self.playlistArtistCountLimit=playlistSnapshotsHelper.addLabeledControl(_("Top artist count (0 displays all artists)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=parent.playlistArtistCountLimit)
		# Translators: the label for a setting in SPL add-on settings to include track category count in playlist snapshots window.
		self.playlistCategoryCountCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Category count")))
		self.playlistCategoryCountCheckbox.SetValue(parent.playlistCategoryCount)
		self.playlistCategoryCountLimit=playlistSnapshotsHelper.addLabeledControl(_("Top category count (0 displays all categories)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=parent.playlistCategoryCountLimit)
		# Translators: the label for a setting in SPL add-on settings to include track genre count in playlist snapshots window.
		self.playlistGenreCountCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("Genre count")))
		self.playlistGenreCountCheckbox.SetValue(parent.playlistGenreCount)
		self.playlistGenreCountLimit=playlistSnapshotsHelper.addLabeledControl(_("Top genre count (0 displays all genres)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=parent.playlistGenreCountLimit)
		# Translators: the label for a setting in SPL add-on settings to show playlist snaphsots window when the snapshots command is pressed once.
		self.resultsWindowOnFirstPressCheckbox=playlistSnapshotsHelper.addItem(wx.CheckBox(self, label=_("&Show results window when playlist snapshots command is performed once")))
		self.resultsWindowOnFirstPressCheckbox.SetValue(parent.resultsWindowOnFirstPress)

		playlistSnapshotsHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(playlistSnapshotsHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.playlistDurationMinMaxCheckbox.SetFocus()
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.playlistDurationMinMax = self.playlistDurationMinMaxCheckbox.Value
		parent.playlistDurationAverage = self.playlistDurationAverageCheckbox.Value
		parent.playlistArtistCount = self.playlistArtistCountCheckbox.Value
		parent.playlistArtistCountLimit = self.playlistArtistCountLimit.GetValue()
		parent.playlistCategoryCount = self.playlistCategoryCountCheckbox.Value
		parent.playlistCategoryCountLimit = self.playlistCategoryCountLimit.GetValue()
		parent.playlistGenreCount = self.playlistGenreCountCheckbox.Value
		parent.playlistGenreCountLimit = self.playlistGenreCountLimit.GetValue()
		parent.resultsWindowOnFirstPress = self.resultsWindowOnFirstPressCheckbox.Value
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

# Metadata reminder controller.
# Select notification/streaming URL's for metadata streaming.
_metadataDialogOpened = False

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

		# WX's CheckListBox isn't user friendly.
		# Therefore use checkboxes laid out across the top.
		# 17.04: instead of two loops, just use one loop, with labels deriving from the below tuple.
		# Only one loop is needed as helper.addLabelControl returns the checkbox itself and that can be appended.
		streamLabels = ("DSP encoder", "URL 1", "URL 2", "URL 3", "URL 4")
		self.checkedStreams = []
		# Add checkboxes for each stream, beginning with the DSP encoder.
		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		from . import splmisc
		streams = splmisc.metadataList()
		for stream in rangeGen(5):
			self.checkedStreams.append(sizer.addItem(wx.CheckBox(self, label=streamLabels[stream])))
			if not configDialogActive: self.checkedStreams[-1].SetValue(streams[stream])
			else: self.checkedStreams[-1].SetValue(self.Parent.metadataStreams[stream])
		metadataSizerHelper.addItem(sizer.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

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
		self.checkedStreams[0].SetFocus()
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		global _metadataDialogOpened
		# Prepare checkbox values first for various reasons.
		metadataEnabled = [self.checkedStreams[url].Value for url in rangeGen(5)]
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

# Column announcement manager.
# Select which track columns should be announced and in which order.
class ColumnAnnouncementsDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: Title of a dialog to configure column announcements (order and what columns should be announced).
		super(ColumnAnnouncementsDialog, self).__init__(parent, title=_("Manage column announcements"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		colAnnouncementsHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: Help text to select columns to be announced.
		labelText = _("Select columns to be announced (artist and title are announced by default")
		colAnnouncementsHelper.addItem(wx.StaticText(self, label=labelText))

		# Same as metadata dialog (wx.CheckListBox isn't user friendly).
		# Gather values for checkboxes except artist and title.
		# 6.1: Split these columns into rows.
		# 17.04: Gather items into a single list instead of three.
		self.checkedColumns = []
		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for column in ("Duration", "Intro", "Category", "Filename"):
			self.checkedColumns.append(sizer.addItem(wx.CheckBox(self, label=column)))
			self.checkedColumns[-1].SetValue(column in self.Parent.includedColumns)
		colAnnouncementsHelper.addItem(sizer.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for column in ("Outro","Year","Album","Genre","Mood","Energy"):
			self.checkedColumns.append(sizer.addItem(wx.CheckBox(self, label=column)))
			self.checkedColumns[-1].SetValue(column in self.Parent.includedColumns)
		colAnnouncementsHelper.addItem(sizer.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for column in ("Tempo","BPM","Gender","Rating","Time Scheduled"):
			self.checkedColumns.append(sizer.addItem(wx.CheckBox(self, label=column)))
			self.checkedColumns[-1].SetValue(column in self.Parent.includedColumns)
		colAnnouncementsHelper.addItem(sizer.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		# WXPython Phoenix contains RearrangeList to allow item orders to be changed automatically.
		# Because WXPython Classic doesn't include this, work around by using a variant of list box and move up/down buttons.
		# 17.04: The label for the list below is above the list, so move move up/down buttons to the right of the list box.
		# Translators: The label for a setting in SPL add-on dialog to select column announcement order.
		self.trackColumns = colAnnouncementsHelper.addLabeledControl(_("Column &order:"), wx.ListBox, choices=parent.columnOrder)
		self.trackColumns.Bind(wx.EVT_LISTBOX,self.onColumnSelection)
		self.trackColumns.SetSelection(0)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		self.upButton = wx.Button(self, wx.ID_ANY, label=_("Move &up"))
		self.upButton.Bind(wx.EVT_BUTTON,self.onMoveUp)
		self.upButton.Disable()
		sizer.Add(self.upButton)
				# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
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
		self.checkedColumns[0].SetFocus()
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.columnOrder = self.trackColumns.GetItems()
		# Make sure artist and title are always included.
		parent.includedColumns.add("Artist")
		parent.includedColumns.add("Title")
		for checkbox in self.checkedColumns:
			action = parent.includedColumns.add if checkbox.Value else parent.includedColumns.discard
			action(checkbox.Label)
		parent.profiles.SetFocus()
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

# Columns Explorer for both Studio and Track Tool
# Configure which column will be announced when Control+NVDA+number row keys are pressed.
class ColumnsExplorerDialog(wx.Dialog):

	def __init__(self, parent, tt=False):
		self.trackTool = tt
		if not tt:
			# Translators: The title of Columns Explorer configuration dialog.
			actualTitle = _("Columns Explorer")
			cols = splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"]
		else:
			# Translators: The title of Columns Explorer configuration dialog.
			actualTitle = _("Columns Explorer for Track Tool")
			cols = ("Artist","Title","Duration","Cue","Overlap","Intro","Segue","Filename","Album","CD Code","Outro","Year","URL 1","URL 2","Genre")
		# Gather column slots.
		self.columnSlots = []

		super(ColumnsExplorerDialog, self).__init__(parent, title=actualTitle)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		colExplorerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# 7.0: Studio 5.0x columns.
		# 17.04: Five by two grid layout as 5.0x is no longer supported.
		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for slot in rangeGen(5):
			# Translators: The label for a setting in SPL add-on dialog to select column for this column slot.
			columns = sizer.addLabeledControl(_("Slot {position}").format(position = slot+1), wx.Choice, choices=cols)
			try:
				columns.SetSelection(cols.index(parent.exploreColumns[slot] if not tt else parent.exploreColumnsTT[slot]))
			except:
				pass
			self.columnSlots.append(columns)
		colExplorerHelper.addItem(sizer.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)

		sizer = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
		for slot in rangeGen(5, 10):
			columns = sizer.addLabeledControl(_("Slot {position}").format(position = slot+1), wx.Choice, choices=cols)
			try:
				columns.SetSelection(cols.index(parent.exploreColumns[slot] if not tt else parent.exploreColumnsTT[slot]))
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
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		slots = parent.exploreColumns if not self.trackTool else parent.exploreColumnsTT
		for slot in rangeGen(len(self.columnSlots)):
			slots[slot] = self.columnSlots[slot].GetStringSelection()
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

# Say status dialog.
# Houses options such as announcing cart names.
class SayStatusDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: Title of a dialog to configure various status announcements such as announcing listener count.
		super(SayStatusDialog, self).__init__(parent, title=_("Status announcements"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sayStatusHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# Translators: the label for a setting in SPL add-on settings to announce scheduled time.
		self.scheduledForCheckbox=sayStatusHelper.addItem(wx.CheckBox(self, label=_("Announce &scheduled time for the selected track")))
		self.scheduledForCheckbox.SetValue(parent.scheduledFor)
		# Translators: the label for a setting in SPL add-on settings to announce listener count.
		self.listenerCountCheckbox=sayStatusHelper.addItem(wx.CheckBox(self, label=_("Announce &listener count")))
		self.listenerCountCheckbox.SetValue(parent.listenerCount)
		# Translators: the label for a setting in SPL add-on settings to announce currently playing cart.
		self.cartNameCheckbox=sayStatusHelper.addItem(wx.CheckBox(self, label=_("&Announce name of the currently playing cart")))
		self.cartNameCheckbox.SetValue(parent.cartName)
		# Translators: the label for a setting in SPL add-on settings to announce currently playing track name.
		labelText = _("&Track name announcement:")
		# Translators: One of the track name announcement options.
		self.trackAnnouncements=[("auto",_("automatic")),
		# Translators: One of the track name announcement options.
		("background",_("while using other programs")),
		# Translators: One of the track name announcement options.
		("off",_("off"))]
		self.trackAnnouncementList=sayStatusHelper.addLabeledControl(labelText, wx.Choice, choices=[x[1] for x in self.trackAnnouncements])
		selection = (x for x,y in enumerate(self.trackAnnouncements) if y[0]==parent.playingTrackName).next()
		try:
			self.trackAnnouncementList.SetSelection(selection)
		except:
			pass
		# Translators: the label for a setting in SPL add-on settings to announce player position for the current and next tracks.
		self.playerPositionCheckbox=sayStatusHelper.addItem(wx.CheckBox(self, label=_("Include track player &position when announcing current and next track information")))
		self.playerPositionCheckbox.SetValue(parent.studioPlayerPosition)

		sayStatusHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(sayStatusHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.scheduledForCheckbox.SetFocus()
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.scheduledFor = self.scheduledForCheckbox.Value
		parent.listenerCount = self.listenerCountCheckbox.Value
		parent.cartName = self.cartNameCheckbox.Value
		parent.playingTrackName = self.trackAnnouncements[self.trackAnnouncementList.GetSelection()][0]
		parent.studioPlayerPosition = self.playerPositionCheckbox.Value
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

# Advanced options
# This dialog houses advanced options such as using SPL Controller command to invoke SPL Assistant.
# More options will be added in 7.0.
# 7.0: Auto update check will be configurable from this dialog.
class AdvancedOptionsDialog(wx.Dialog):

	# Available channels (if there's only one, channel selection list will not be shown).
	# Prepare for a day when channels list is NULL.
	_updateChannels = ["try", "dev", "stable"]

	def __init__(self, parent):
		# Translators: The title of a dialog to configure advanced SPL add-on options such as update checking.
		super(AdvancedOptionsDialog, self).__init__(parent, title=_("Advanced options"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		advOptionsHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		# #48 (18.02): do not show auto-update checkbox and interval options if not needed.
		# The exception will be custom try builds.
		if splupdate.isAddonUpdatingSupported() == splupdate.SPLUpdateErrorNone:
			# Translators: A checkbox to toggle automatic add-on updates.
			self.autoUpdateCheckbox=advOptionsHelper.addItem(wx.CheckBox(self,label=_("Automatically check for add-on &updates")))
			self.autoUpdateCheckbox.SetValue(self.Parent.autoUpdateCheck)
			# Translators: The label for a setting in SPL add-on settings/advanced options to select automatic update interval in days.
			self.updateInterval=advOptionsHelper.addLabeledControl(_("Update &interval in days"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=180, initial=self.Parent.updateInterval)
		else: self._updateChannels = [None]
		# For releases that support channel switching.
		if len(self._updateChannels) > 1:
			# Translators: The label for a combo box to select update channel.
			labelText = _("&Add-on update channel:")
			self.channels=advOptionsHelper.addLabeledControl(labelText, wx.Choice, choices=["Test Drive Fast", "Test Drive Slow", "stable"])
			self.channels.SetSelection(self._updateChannels.index(self.Parent.updateChannel))
		# Translators: A checkbox to toggle if SPL Controller command can be used to invoke Assistant layer.
		self.splConPassthroughCheckbox=advOptionsHelper.addItem(wx.CheckBox(self, label=_("Allow SPL C&ontroller command to invoke SPL Assistant layer")))
		self.splConPassthroughCheckbox.SetValue(self.Parent.splConPassthrough)
		# Translators: The label for a setting in SPL add-on dialog to set keyboard layout for SPL Assistant.
		labelText = _("SPL Assistant command &layout:")
		self.compatibilityLayouts=[("off","NVDA"),
		("jfw","JAWS for Windows"),
		("wineyes","Window-Eyes")]
		self.compatibilityList=advOptionsHelper.addLabeledControl(labelText, wx.Choice, choices=[x[1] for x in self.compatibilityLayouts])
		selection = (x for x,y in enumerate(self.compatibilityLayouts) if y[0]==self.Parent.compLayer).next()
		try:
			self.compatibilityList.SetSelection(selection)
		except:
			pass

		advOptionsHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Add(advOptionsHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		try:
			self.autoUpdateCheckbox.SetFocus()
		except AttributeError:
			self.splConPassthroughCheckbox.SetFocus()
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		addonUpdatingSupported = splupdate.isAddonUpdatingSupported() == splupdate.SPLUpdateErrorNone
		# The try (fast ring) builds aren't for the faint of heart.
		# 17.10: nor for old Windows releases anymore.
		if len(self._updateChannels) > 1:
			channel = self._updateChannels[self.channels.GetSelection()]
			# 17.09: present this dialog if and only if switching to fast ring from other rings.
			if self.Parent.updateChannel != "try" and channel == "try":
				if gui.messageBox(
					# Translators: The confirmation prompt displayed when changing to the fastest development channel (with risks involved).
					_("You are about to switch to the Test Drive Fast (try) builds channel, the fastest and most unstable development channel. Please note that the selected channel may come with updates that might be unstable at times and should be used for testing and sending feedback to the add-on developer. If you prefer to use stable releases, please answer no and switch to a more stable update channel. Are you sure you wish to switch to Test Drive Fast channel?"),
					# Translators: The title of the channel switch confirmation dialog.
					_("Switching to unstable channel"),
					wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self
				) == wx.NO:
					return
		if addonUpdatingSupported:
			# If update interval is set to zero, update check will happen every time the app module loads, so warn users.
			updateInterval = self.updateInterval.Value
			if self.Parent.updateInterval > 0 and updateInterval == 0 and gui.messageBox(
				# Translators: The confirmation prompt displayed when changing update interval to zero days (updates will be checked every time Studio app module loads).
				_("Update interval has been set to zero days, so updates to the Studio add-on will be checked every time NVDA and/or Studio starts. Are you sure you wish to continue?"),
				# Translators: The title of the update interval dialog.
				_("Confirm update interval"),
				wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self
			) == wx.NO:
				return
		parent = self.Parent
		parent.splConPassthrough = self.splConPassthroughCheckbox.Value
		parent.compLayer = self.compatibilityLayouts[self.compatibilityList.GetSelection()][0]
		if addonUpdatingSupported:
			parent.autoUpdateCheck = self.autoUpdateCheckbox.Value
			parent.updateInterval = updateInterval
		if len(self._updateChannels) > 1: parent.updateChannel = self._updateChannels[self.channels.GetSelection()]
		parent.profiles.SetFocus()
		parent.Enable()
		self.Destroy()
		return

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()

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
		self.Center(wx.BOTH | CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		if gui.messageBox(
		# Translators: A message to warn about resetting SPL config settings to factory defaults.
		_("Are you sure you wish to reset SPL add-on settings to defaults?"),
		# Translators: The title of the warning dialog.
		_("Warning"),wx.YES_NO|wx.NO_DEFAULT|wx.ICON_WARNING,self
		)!=wx.YES:
			parent.profiles.SetFocus()
			parent.Enable()
			self.Destroy()
			return
		import threading, sys, globalVars
		# Reset all profiles.
		# LTS: Only a priveleged thread should do this, otherwise unexpected things may happen.
		with threading.Lock() as resetting:
			global _configDialogOpened
			splconfig.SPLConfig.reset()
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
		parent.Destroy()

	def onCancel(self, evt):
		self.Parent.Enable()
		self.Destroy()
