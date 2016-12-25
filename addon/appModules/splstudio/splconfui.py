# SPL Studio Configuration user interfaces
# An app module and global plugin package for NVDA
# Copyright 2016-2017 Joseph Lee and others, released under GPL.
# Split from SPL config module in 2016.
# Provides the configuration management UI package for SPL Studio app module.
# For code which provides foundation for code in this module, see splconfig module.

import os
import weakref
import datetime
import calendar
import ui
import api
import gui
import wx
from winUser import user32
import tones
import splupdate
import splconfig


# Configuration dialog.
_configDialogOpened = False

class SPLConfigDialog(gui.SettingsDialog):
	# Translators: This is the label for the StationPlaylist Studio configuration dialog.
	title = _("Studio Add-on Settings")

	def makeSettings(self, settingsSizer):

		# Broadcast profile controls were inspired by Config Profiles dialog in NVDA Core.
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to select a broadcast profile.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Broadcast &profile:"))
		# Sort profiles for display purposes (the config pool might not be sorted).
		sortedProfiles = [profile.name for profile in splconfig.SPLConfigPool]
		# No need to sort if the only living profile is the normal configuration or there is one other profile besides this.
		# Optimization: Only sort if config pool itself isn't  - usually after creating, renaming or deleting profile(s).
		if len(sortedProfiles) > 2 and not splconfig.isConfigPoolSorted():
			firstProfile = splconfig.SPLConfigPool[0].name
			sortedProfiles = [firstProfile] + sorted(sortedProfiles[1:])
		# 7.0: Have a copy of the sorted profiles so the actual combo box items can show profile flags.
		self.profileNames = list(sortedProfiles)
		self.profiles = wx.Choice(self, wx.ID_ANY, choices=self.displayProfiles(sortedProfiles))
		self.profiles.Bind(wx.EVT_CHOICE, self.onProfileSelection)
		try:
			self.profiles.SetSelection(self.profileNames.index(splconfig.SPLActiveProfile))
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.profiles)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Profile controls code credit: NV Access (except copy button).
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label of a button to create a new broadcast profile.
		item = newButton = wx.Button(self, label=_("&New"))
		item.Bind(wx.EVT_BUTTON, self.onNew)
		sizer.Add(item)
		# Translators: The label of a button to copy a broadcast profile.
		item = copyButton = wx.Button(self, label=_("Cop&y"))
		item.Bind(wx.EVT_BUTTON, self.onCopy)
		sizer.Add(item)
		# Translators: The label of a button to rename a broadcast profile.
		item = self.renameButton = wx.Button(self, label=_("&Rename"))
		item.Bind(wx.EVT_BUTTON, self.onRename)
		sizer.Add(item)
		# Translators: The label of a button to delete a broadcast profile.
		item = self.deleteButton = wx.Button(self, label=_("&Delete"))
		item.Bind(wx.EVT_BUTTON, self.onDelete)
		sizer.Add(item)
		# Have a copy of the triggers dictionary.
		self._profileTriggersConfig = dict(splconfig.profileTriggers)
		# Translators: The label of a button to manage show profile triggers.
		item = self.triggerButton = wx.Button(self, label=_("&Triggers..."))
		item.Bind(wx.EVT_BUTTON, self.onTriggers)
		sizer.Add(item)

		self.switchProfile = splconfig.SPLSwitchProfile
		self.activeProfile = splconfig.SPLActiveProfile
		# Used as sanity check in case switch profile is renamed or deleted.
		self.switchProfileRenamed = False
		self.switchProfileDeleted = False
		# Translators: The label for a setting in SPL Add-on settings to configure countdown seconds before switching profiles.
		self.triggerThresholdLabel = wx.StaticText(self, wx.ID_ANY, label=_("Countdown seconds before switching profiles"))
		sizer.Add(self.triggerThresholdLabel)
		self.triggerThreshold = wx.SpinCtrl(self, wx.ID_ANY, min=10, max=60)
		self.triggerThreshold.SetValue(long(splconfig.SPLConfig["Advanced"]["ProfileTriggerThreshold"]))
		self.triggerThreshold.SetSelection(-1, -1)
		sizer.Add(self.triggerThreshold)
		if splconfig.SPLConfig["ActiveIndex"] == 0:
			self.renameButton.Disable()
			self.deleteButton.Disable()
			self.triggerButton.Disable()
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to set status announcement between words and beeps.
		self.beepAnnounceCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Beep for status announcements"))
		self.beepAnnounceCheckbox.SetValue(splconfig.SPLConfig["General"]["BeepAnnounce"])
		settingsSizer.Add(self.beepAnnounceCheckbox, border=10,flag=wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to set message verbosity.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Message &verbosity:"))
		# Translators: One of the message verbosity levels.
		self.verbosityLevels=[("beginner",_("beginner")),
		# Translators: One of the message verbosity levels.
		("advanced",_("advanced"))]
		self.verbosityList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.verbosityLevels])
		currentVerbosity=splconfig.SPLConfig["General"]["MessageVerbosity"]
		selection = (x for x,y in enumerate(self.verbosityLevels) if y[0]==currentVerbosity).next()
		try:
			self.verbosityList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.verbosityList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		self.outroSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Check box hiding method comes from Alberto Buffolino's Columns Review add-on.
		# Translators: Label for a check box in SPL add-on settings to notify when end of track (outro) is approaching.
		self.outroCheckBox=wx.CheckBox(self,wx.NewId(),label=_("&Notify when end of track is approaching"))
		self.outroCheckBox.SetValue(splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"])
		self.outroCheckBox.Bind(wx.EVT_CHECKBOX, self.onOutroCheck)
		self.outroSizer.Add(self.outroCheckBox, border=10,flag=wx.BOTTOM)

		# Translators: The label for a setting in SPL Add-on settings to specify end of track (outro) alarm.
		self.outroAlarmLabel = wx.StaticText(self, wx.ID_ANY, label=_("&End of track alarm in seconds"))
		self.outroSizer.Add(self.outroAlarmLabel)
		self.endOfTrackAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=1, max=59)
		self.endOfTrackAlarm.SetValue(long(splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"]))
		self.endOfTrackAlarm.SetSelection(-1, -1)
		self.outroSizer.Add(self.endOfTrackAlarm)
		self.onOutroCheck(None)
		settingsSizer.Add(self.outroSizer, border=10, flag=wx.BOTTOM)

		self.introSizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: Label for a check box in SPL add-on settings to notify when end of intro is approaching.
		self.introCheckBox=wx.CheckBox(self,wx.NewId(),label=_("&Notify when end of introduction is approaching"))
		self.introCheckBox.SetValue(splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"])
		self.introCheckBox.Bind(wx.EVT_CHECKBOX, self.onIntroCheck)
		self.introSizer.Add(self.introCheckBox, border=10,flag=wx.BOTTOM)

		# Translators: The label for a setting in SPL Add-on settings to specify track intro alarm.
		self.introAlarmLabel = wx.StaticText(self, wx.ID_ANY, label=_("&Track intro alarm in seconds"))
		self.introSizer.Add(self.introAlarmLabel)
		self.songRampAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=1, max=9)
		self.songRampAlarm.SetValue(long(splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"]))
		self.songRampAlarm.SetSelection(-1, -1)
		self.introSizer.Add(self.songRampAlarm)
		self.onIntroCheck(None)
		settingsSizer.Add(self.introSizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control braille timer.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Braille timer:"))
		self.brailleTimerValues=[("off",_("Off")),
		# Translators: One of the braille timer settings.
		("outro",_("Track ending")),
		# Translators: One of the braille timer settings.
		("intro",_("Track intro")),
		# Translators: One of the braille timer settings.
		("both",_("Track intro and ending"))]
		self.brailleTimerList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.brailleTimerValues])
		brailleTimerCurValue=splconfig.SPLConfig["General"]["BrailleTimer"]
		selection = (x for x,y in enumerate(self.brailleTimerValues) if y[0]==brailleTimerCurValue).next()
		try:
			self.brailleTimerList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.brailleTimerList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL Add-on settings to change microphone alarm setting.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Microphone alarm in seconds"))
		sizer.Add(label)
		self.micAlarm = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=7200)
		self.micAlarm.SetValue(long(splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"]))
		self.micAlarm.SetSelection(-1, -1)
		sizer.Add(self.micAlarm)
		# Translators: The label for a setting in SPL Add-on settings to specify mic alarm interval.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Microphone alarm &interval in seconds"))
		sizer.Add(label)
		self.micAlarmInterval = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=60)
		self.micAlarmInterval.SetValue(long(splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"]))
		self.micAlarmInterval.SetSelection(-1, -1)
		sizer.Add(self.micAlarmInterval)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control alarm announcement type.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Alarm notification:"))
		# Translators: One of the alarm notification options.
		self.alarmAnnounceValues=[("beep",_("beep")),
		# Translators: One of the alarm notification options.
		("message",_("message")),
		# Translators: One of the alarm notification options.
		("both",_("both beep and message"))]
		self.alarmAnnounceList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.alarmAnnounceValues])
		alarmAnnounceCurValue=splconfig.SPLConfig["General"]["AlarmAnnounce"]
		selection = (x for x,y in enumerate(self.alarmAnnounceValues) if y[0]==alarmAnnounceCurValue).next()
		try:
			self.alarmAnnounceList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.alarmAnnounceList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to control library scan announcement.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Library scan announcement:"))
		self.libScanValues=[("off",_("Off")),
		# Translators: One of the library scan announcement settings.
		("ending",_("Start and end only")),
		# Translators: One of the library scan announcement settings.
		("progress",_("Scan progress")),
		# Translators: One of the library scan announcement settings.
		("numbers",_("Scan count"))]
		self.libScanList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.libScanValues])
		libScanCurValue=splconfig.SPLConfig["General"]["LibraryScanAnnounce"]
		selection = (x for x,y in enumerate(self.libScanValues) if y[0]==libScanCurValue).next()
		try:
			self.libScanList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.libScanList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce time including hours.
		self.hourAnnounceCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Include &hours when announcing track or playlist duration"))
		self.hourAnnounceCheckbox.SetValue(splconfig.SPLConfig["General"]["TimeHourAnnounce"])
		settingsSizer.Add(self.hourAnnounceCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to toggle track dial mode on and off.
		self.trackDialCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Track Dial mode"))
		self.trackDialCheckbox.SetValue(splconfig.SPLConfig["General"]["TrackDial"])
		settingsSizer.Add(self.trackDialCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to toggle category sound announcement.
		self.categorySoundsCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Beep for different track categories"))
		self.categorySoundsCheckbox.SetValue(splconfig.SPLConfig["General"]["CategorySounds"])
		settingsSizer.Add(self.categorySoundsCheckbox, border=10,flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label for a setting in SPL add-on settings to set how track comments are announced.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Track comment announcement:"))
		self.trackCommentValues=[("off",_("Off")),
		# Translators: One of the track comment notification settings.
		("message",_("Message")),
		# Translators: One of the track comment notification settings.
		("beep",_("Beep")),
		# Translators: One of the track comment notification settings.
		("both",_("Both"))]
		self.trackCommentList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.trackCommentValues])
		trackCommentCurValue=splconfig.SPLConfig["General"]["TrackCommentAnnounce"]
		selection = (x for x,y in enumerate(self.trackCommentValues) if y[0]==trackCommentCurValue).next()
		try:
			self.trackCommentList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.trackCommentList)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to toggle top and bottom notification.
		self.topBottomCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Notify when located at &top or bottom of playlist viewer"))
		self.topBottomCheckbox.SetValue(splconfig.SPLConfig["General"]["TopBottomAnnounce"])
		settingsSizer.Add(self.topBottomCheckbox, border=10,flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label for a setting in SPL add-on settings to be notified that metadata streaming is enabled.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Metadata streaming notification and connection"))
		self.metadataValues=[("off",_("Off")),
		# Translators: One of the metadata notification settings.
		("startup",_("When Studio starts")),
		# Translators: One of the metadata notification settings.
		("instant",_("When instant switch profile is active"))]
		self.metadataList = wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.metadataValues])
		metadataCurValue=splconfig.SPLConfig["General"]["MetadataReminder"]
		selection = (x for x,y in enumerate(self.metadataValues) if y[0]==metadataCurValue).next()
		try:
			self.metadataList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.metadataList)
		self.metadataStreams = list(splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"])
		# Translators: The label of a button to manage column announcements.
		item = manageMetadataButton = wx.Button(self, label=_("Configure metadata &streaming connection options..."))
		item.Bind(wx.EVT_BUTTON, self.onManageMetadata)
		sizer.Add(item)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label for a setting in SPL add-on settings to toggle custom column announcement.
		self.columnOrderCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce columns in the &order shown on screen"))
		self.columnOrderCheckbox.SetValue(splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"])
		self.columnOrder = splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"]
		# Without manual conversion below, it produces a rare bug where clicking cancel after changing column inclusion causes new set to be retained.
		self.includedColumns = set(splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"])
		sizer.Add(self.columnOrderCheckbox, border=10,flag=wx.BOTTOM)
		# Translators: The label of a button to manage column announcements.
		item = manageColumnsButton = wx.Button(self, label=_("&Manage track column announcements..."))
		item.Bind(wx.EVT_BUTTON, self.onManageColumns)
		sizer.Add(item)
		# Translators: The label of a button to configure columns explorer slots (SPL Assistant, number row keys to announce specific columns).
		item = columnsExplorerButton = wx.Button(self, label=_("Columns E&xplorer..."))
		item.Bind(wx.EVT_BUTTON, self.onColumnsExplorer)
		self.exploreColumns = splconfig.SPLConfig["General"]["ExploreColumns"]
		sizer.Add(item)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Say status flags to be picked up by the dialog of this name.
		self.scheduledFor = splconfig.SPLConfig["SayStatus"]["SayScheduledFor"]
		self.listenerCount = splconfig.SPLConfig["SayStatus"]["SayListenerCount"]
		self.cartName = splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"]
		self.playingTrackName = splconfig.SPLConfig["SayStatus"]["SayPlayingTrackName"]

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label of a button to open status announcement options such as announcing listener count.
		item = sayStatusButton = wx.Button(self, label=_("&Status announcements..."))
		item.Bind(wx.EVT_BUTTON, self.onStatusAnnouncement)
		sizer.Add(item)

		# Translators: The label of a button to open advanced options such as using SPL Controller command to invoke Assistant layer.
		item = advancedOptButton = wx.Button(self, label=_("&Advanced options..."))
		item.Bind(wx.EVT_BUTTON, self.onAdvancedOptions)
		self.splConPassthrough = splconfig.SPLConfig["Advanced"]["SPLConPassthrough"]
		self.compLayer = splconfig.SPLConfig["Advanced"]["CompatibilityLayer"]
		self.autoUpdateCheck = splconfig.SPLConfig["Update"]["AutoUpdateCheck"]
		self.updateInterval = splconfig.SPLConfig["Update"]["UpdateInterval"]
		self.updateChannel = splupdate.SPLUpdateChannel
		self.pendingChannelChange = False
		sizer.Add(item)
		settingsSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# Translators: The label for a button in SPL add-on configuration dialog to reset settings to defaults.
		item = resetButton = wx.Button(self, label=_("Reset settings..."))
		item.Bind(wx.EVT_BUTTON,self.onResetConfig)
		settingsSizer.Add(item)

	def postInit(self):
		global _configDialogOpened
		_configDialogOpened = True
		self.profiles.SetFocus()

	def onOk(self, evt):
		global _configDialogOpened
		selectedProfile = self.profiles.GetStringSelection().split(" <")[0]
		profileIndex = splconfig.getProfileIndexByName(selectedProfile)
		splconfig.SPLConfig["General"]["BeepAnnounce"] = self.beepAnnounceCheckbox.Value
		splconfig.SPLConfig["General"]["MessageVerbosity"] = self.verbosityLevels[self.verbosityList.GetSelection()][0]
		splconfig.SPLConfig["IntroOutroAlarms"]["SayEndOfTrack"] = self.outroCheckBox.Value
		splconfig.SPLConfig["IntroOutroAlarms"]["EndOfTrackTime"] = self.endOfTrackAlarm.Value
		splconfig.SPLConfig["IntroOutroAlarms"]["SaySongRamp"] = self.introCheckBox.Value
		splconfig.SPLConfig["IntroOutroAlarms"]["SongRampTime"] = self.songRampAlarm.Value
		splconfig.SPLConfig["General"]["BrailleTimer"] = self.brailleTimerValues[self.brailleTimerList.GetSelection()][0]
		splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarm"] = self.micAlarm.Value
		splconfig.SPLConfig["MicrophoneAlarm"]["MicAlarmInterval"] = self.micAlarmInterval.Value
		splconfig.SPLConfig["General"]["AlarmAnnounce"] = self.alarmAnnounceValues[self.alarmAnnounceList.GetSelection()][0]
		splconfig.SPLConfig["General"]["LibraryScanAnnounce"] = self.libScanValues[self.libScanList.GetSelection()][0]
		splconfig.SPLConfig["General"]["TimeHourAnnounce"] = self.hourAnnounceCheckbox.Value
		splconfig.SPLConfig["General"]["TrackDial"] = self.trackDialCheckbox.Value
		splconfig.SPLConfig["General"]["CategorySounds"] = self.categorySoundsCheckbox.Value
		splconfig.SPLConfig["General"]["TrackCommentAnnounce"] = self.trackCommentValues[self.trackCommentList.GetSelection()][0]
		splconfig.SPLConfig["General"]["TopBottomAnnounce"] = self.topBottomCheckbox.Value
		splconfig.SPLConfig["General"]["MetadataReminder"] = self.metadataValues[self.metadataList.GetSelection()][0]
		splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"] = self.metadataStreams
		splconfig.SPLConfig["ColumnAnnouncement"]["UseScreenColumnOrder"] = self.columnOrderCheckbox.Value
		splconfig.SPLConfig["ColumnAnnouncement"]["ColumnOrder"] = self.columnOrder
		splconfig.SPLConfig["ColumnAnnouncement"]["IncludedColumns"] = self.includedColumns
		splconfig.SPLConfig["General"]["ExploreColumns"] = self.exploreColumns
		splconfig.SPLConfig["SayStatus"]["SayScheduledFor"] = self.scheduledFor
		splconfig.SPLConfig["SayStatus"]["SayListenerCount"] = self.listenerCount
		splconfig.SPLConfig["SayStatus"]["SayPlayingCartName"] = self.cartName
		splconfig.SPLConfig["SayStatus"]["SayPlayingTrackName"] = self.playingTrackName
		splconfig.SPLConfig["Advanced"]["SPLConPassthrough"] = self.splConPassthrough
		splconfig.SPLConfig["Advanced"]["CompatibilityLayer"] = self.compLayer
		splconfig.SPLConfig["Update"]["AutoUpdateCheck"] = self.autoUpdateCheck
		splconfig.SPLConfig["Update"]["UpdateInterval"] = self.updateInterval
		self.pendingChannelChange = splupdate.SPLUpdateChannel != self.updateChannel
		splupdate.SPLUpdateChannel = self.updateChannel
		splconfig.SPLConfig["ActiveIndex"] = profileIndex
		# Reverse of merge: save profile specific sections to individual config dictionaries.
		splconfig.applySections(profileIndex)
		splconfig.SPLActiveProfile = selectedProfile
		splconfig.SPLSwitchProfile = self.switchProfile
		# Make sure to nullify prev profile if instant switch profile is gone.
		# 7.0: Don't do the following in the midst of a broadcast.
		if self.switchProfile is None and not splconfig._triggerProfileActive:
			splconfig.SPLPrevProfile = None
		_configDialogOpened = False
		# 7.0: Perform extra action such as restarting auto update timer.
		self.onCloseExtraAction()
		# Apply changes to profile triggers.
		splconfig.profileTriggers = dict(self._profileTriggersConfig)
		self._profileTriggersConfig.clear()
		self._profileTriggersConfig = None
		splconfig.triggerStart(restart=True)
		super(SPLConfigDialog,  self).onOk(evt)

	def onCancel(self, evt):
		global _configDialogOpened
		# 6.1: Discard changes to included columns set.
		if self.includedColumns is not None: self.includedColumns.clear()
		self.includedColumns = None
		# Apply profile trigger changes if any.
		splconfig.profileTriggers = dict(self._profileTriggersConfig)
		self._profileTriggersConfig.clear()
		self._profileTriggersConfig = None
		splconfig.triggerStart(restart=True)
		# 7.0: No matter what happens, merge appropriate profile.
		try:
			prevActive = self.profileNames.index(self.activeProfile)
		except ValueError:
			prevActive = 0
		splconfig.mergeSections(prevActive)
		if self.switchProfileRenamed or self.switchProfileDeleted:
			splconfig.SPLSwitchProfile = self.switchProfile
		if self.switchProfileDeleted:
			splconfig.SPLActiveProfile = splconfig.SPLConfigPool[prevActive].name
		_configDialogOpened = False
		super(SPLConfigDialog,  self).onCancel(evt)

	# Perform extra action when closing this dialog such as restarting update timer.
	def onCloseExtraAction(self):
		# Change metadata streaming.
		hwnd = user32.FindWindowA("SPLStudio", None)
		if hwnd:
			for url in xrange(5):
				dataLo = 0x00010000 if splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"][url] else 0xffff0000
				user32.SendMessageW(hwnd, 1024, dataLo | url, 36)
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

	# Check events for outro and intro alarms, respectively.
	def onOutroCheck(self, evt):
		if not self.outroCheckBox.IsChecked():
			self.outroSizer.Hide(self.outroAlarmLabel)
			self.outroSizer.Hide(self.endOfTrackAlarm)
		else:
			self.outroSizer.Show(self.outroAlarmLabel)
			self.outroSizer.Show(self.endOfTrackAlarm)
		self.Fit()

	def onIntroCheck(self, evt):
		if not self.introCheckBox.IsChecked():
			self.introSizer.Hide(self.introAlarmLabel)
			self.introSizer.Hide(self.songRampAlarm)
		else:
			self.introSizer.Show(self.introAlarmLabel)
			self.introSizer.Show(self.songRampAlarm)
		self.Fit()

	# Include profile flags such as instant profile string for display purposes.
	def displayProfiles(self, profiles):
		for index in xrange(len(profiles)):
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
		curProfile = splconfig.getProfileByName(selectedProfile)
		self.outroCheckBox.SetValue(curProfile["IntroOutroAlarms"]["SayEndOfTrack"])
		self.endOfTrackAlarm.SetValue(long(curProfile["IntroOutroAlarms"]["EndOfTrackTime"]))
		self.onOutroCheck(None)
		self.introCheckBox.SetValue(curProfile["IntroOutroAlarms"]["SaySongRamp"])
		self.songRampAlarm.SetValue(long(curProfile["IntroOutroAlarms"]["SongRampTime"]))
		self.onIntroCheck(None)
		self.micAlarm.SetValue(long(curProfile["MicrophoneAlarm"]["MicAlarm"]))
		self.micAlarmInterval.SetValue(long(curProfile["MicrophoneAlarm"]["MicAlarmInterval"]))
		# 6.1: Take care of profile-specific column and metadata settings.
		self.metadataStreams = curProfile["MetadataStreaming"]["MetadataEnabled"]
		self.columnOrderCheckbox.SetValue(curProfile["ColumnAnnouncement"]["UseScreenColumnOrder"])
		self.columnOrder = curProfile["ColumnAnnouncement"]["ColumnOrder"]
		# 6.1: Again convert list to set.
		self.includedColumns = set(curProfile["ColumnAnnouncement"]["IncludedColumns"])

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
		configPos = splconfig.getProfileIndexByName(oldName)
		profilePos = self.profileNames.index(oldName)
		# Translators: The label of a field to enter a new name for a broadcast profile.
		with wx.TextEntryDialog(self, _("New name:"),
				# Translators: The title of the dialog to rename a profile.
				_("Rename Profile"), defaultValue=oldName) as d:
			if d.ShowModal() == wx.ID_CANCEL:
				return
			newName = api.filterFileName(d.Value)
		if oldName == newName: return
		newNamePath = newName + ".ini"
		newProfile = os.path.join(SPLProfiles, newNamePath)
		if oldName.lower() != newName.lower() and os.path.isfile(newProfile):
			# Translators: An error displayed when renaming a configuration profile
			# and a profile with the new name already exists.
			gui.messageBox(_("That profile already exists. Please choose a different name."),
				_("Error"), wx.OK | wx.ICON_ERROR, self)
			return
		oldNamePath = oldName + ".ini"
		oldProfile = os.path.join(SPLProfiles, oldNamePath)
		try:
			os.rename(oldProfile, newProfile)
		except WindowsError:
			pass
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
		splconfig.SPLConfigPool[configPos].name = newName
		splconfig.SPLConfigPool[configPos].filename = newProfile
		splconfig._SPLCache[newName] = splconfig._SPLCache[oldName]
		del splconfig._SPLCache[oldName]
		if len(state) > 1: newName = " <".join([newName, state[1]])
		self.profiles.SetString(index, newName)
		self.profiles.Selection = index
		self.profiles.SetFocus()

	def onDelete(self, evt):
		# Prevent profile deletion while a trigger is active (in the midst of a broadcast), otherwise flags such as instant switch and time-based profiles become inconsistent.
		# 6.4: This was seen after deleting a profile one positoin before the previsouly active profile.
		# 7.0: One should never delete the currently active time-based profile.
		# 7.1: Find a way to safely proceed via two-step verification if trying to delete currently active time-based profile.
		if (splconfig._SPLTriggerEndTimer is not None and splconfig._SPLTriggerEndTimer.IsRunning()) or splconfig._triggerProfileActive or splconfig.SPLPrevProfile is not None:
			# Translators: Message reported when attempting to delete a profile while a profile is triggered.
			gui.messageBox(_("An instant switch profile might be active or you are in the midst of a broadcast. If so, please press SPL Assistant, F12 to switch back to a previously active profile before opening add-on settings to delete a profile."),
				# Translators: Title of a dialog shown when profile cannot be deleted.
				_("Profile delete error"), wx.OK | wx.ICON_ERROR, self)
			return
		index = self.profiles.Selection
		name = self.profiles.GetStringSelection().split(" <")[0]
		configPos = splconfig.getProfileIndexByName(name)
		profilePos = self.profileNames.index(name)
		if gui.messageBox(
			# Translators: The confirmation prompt displayed when the user requests to delete a broadcast profile.
			_("Are you sure you want to delete this profile? This cannot be undone."),
			# Translators: The title of the confirmation dialog for deletion of a profile.
			_("Confirm Deletion"),
			wx.YES | wx.NO | wx.ICON_QUESTION, self
		) == wx.NO:
			return
		path = splconfig.SPLConfigPool[configPos].filename
		del splconfig.SPLConfigPool[configPos]
		try:
			os.remove(path)
		except WindowsError:
			pass
		if name == self.switchProfile or name == self.activeProfile:
			self.switchProfile = None
			splconfig.SPLPrevProfile = None
			self.switchProfileDeleted = True
		self.profiles.Delete(index)
		del self.profileNames[profilePos]
		del splconfig._SPLCache[name]
		if name in self._profileTriggersConfig:
			del self._profileTriggersConfig[name]
		# 6.3: Select normal profile if the active profile is gone.
		# 7.0: Consult profile names instead.
		try:
			self.profiles.Selection = self.profileNames.index(self.activeProfile)
		except ValueError:
			self.activeProfile = splconfig.SPLConfigPool[0].name
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
	if splconfig._alarmDialogOpened or _metadataDialogOpened:
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

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label of a field to enter the name of a new broadcast profile.
		sizer.Add(wx.StaticText(self, label=_("Profile name:")))
		item = self.profileName = wx.TextCtrl(self)
		sizer.Add(item)
		mainSizer.Add(sizer)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to select a base  profile for copying.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Base profile:"))
		self.baseProfiles = wx.Choice(self, wx.ID_ANY, choices=[profile.split(" <")[0] for profile in parent.profiles.GetItems()])
		try:
			self.baseProfiles.SetSelection(self.baseProfiles.GetItems().index(parent.profiles.GetStringSelection().split(" <")[0]))
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.baseProfiles)
		if not self.copy:
			sizer.Hide(label)
			sizer.Hide(self.baseProfiles)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.profileName.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		profileNames = [profile.name for profile in splconfig.SPLConfigPool]
		name = api.filterFileName(self.profileName.Value)
		if not name:
			return
		if name in profileNames:
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
			baseConfig = splconfig.getProfileByName(self.baseProfiles.GetStringSelection())
			baseProfile = {sect:key for sect, key in baseConfig.iteritems() if sect in splconfig._mutatableSettings7}
		else: baseProfile = None
		splconfig.SPLConfigPool.append(splconfig.unlockConfig(newProfilePath, profileName=name, parent=baseProfile))
		# Make the cache know this is a new profile.
		# If nothing happens to this profile, the newly created profile will be saved to disk.
		splconfig._SPLCache[name]["___new___"] = True
		parent = self.Parent
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

		sizer = wx.BoxSizer(wx.VERTICAL)
		# Translators: The label of a checkbox to toggle if selected profile is an instant switch profile.
		self.instantSwitchCheckbox=wx.CheckBox(self,wx.NewId(),label=_("This is an &instant switch profile"))
		self.instantSwitchCheckbox.SetValue(parent.switchProfile == parent.profiles.GetStringSelection().split(" <")[0])
		sizer.Add(self.instantSwitchCheckbox, border=10,flag=wx.TOP)

		# Translators: The label of a checkbox to toggle if selected profile is a time-based profile.
		self.timeSwitchCheckbox=wx.CheckBox(self,wx.NewId(),label=_("This is a &time-based switch profile"))
		self.timeSwitchCheckbox.SetValue(profile in self.Parent._profileTriggersConfig)
		self.timeSwitchCheckbox.Bind(wx.EVT_CHECKBOX, self.onTimeSwitch)
		sizer.Add(self.timeSwitchCheckbox, border=10,flag=wx.TOP)
		mainSizer.Add(sizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		daysSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Day")), wx.HORIZONTAL)
		self.triggerDays = []
		for day in xrange(len(calendar.day_name)):
			triggerDay=wx.CheckBox(self, wx.NewId(),label=calendar.day_name[day])
			value = (64 >> day & self.Parent._profileTriggersConfig[profile][0]) if profile in self.Parent._profileTriggersConfig else 0
			triggerDay.SetValue(value)
			self.triggerDays.append(triggerDay)
		for day in self.triggerDays:
			daysSizer.Add(day)
			if not self.timeSwitchCheckbox.IsChecked(): daysSizer.Hide(day)
		mainSizer.Add(daysSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		timeSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Time")), wx.HORIZONTAL)
		self.hourPrompt = wx.StaticText(self, wx.ID_ANY, label=_("Hour"))
		timeSizer.Add(self.hourPrompt)
		self.hourEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=23)
		self.hourEntry.SetValue(self.Parent._profileTriggersConfig[profile][4] if profile in self.Parent._profileTriggersConfig else 0)
		self.hourEntry.SetSelection(-1, -1)
		timeSizer.Add(self.hourEntry)
		self.minPrompt = wx.StaticText(self, wx.ID_ANY, label=_("Minute"))
		timeSizer.Add(self.minPrompt)
		self.minEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.minEntry.SetValue(self.Parent._profileTriggersConfig[profile][5] if profile in self.Parent._profileTriggersConfig else 0)
		self.minEntry.SetSelection(-1, -1)
		timeSizer.Add(self.minEntry)
		self.durationPrompt = wx.StaticText(self, wx.ID_ANY, label=_("Duration in minutes"))
		timeSizer.Add(self.durationPrompt)
		self.durationEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=1440)
		self.durationEntry.SetValue(self.Parent._profileTriggersConfig[profile][6] if profile in self.Parent._profileTriggersConfig else 0)
		self.durationEntry.SetSelection(-1, -1)
		timeSizer.Add(self.durationEntry)
		if not self.timeSwitchCheckbox.IsChecked():
			timeSizer.Hide(self.hourPrompt)
			timeSizer.Hide(self.hourEntry)
			timeSizer.Hide(self.minPrompt)
			timeSizer.Hide(self.minEntry)
			timeSizer.Hide(self.durationPrompt)
			timeSizer.Hide(self.durationEntry)
		mainSizer.Add(timeSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
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
			prompt.Show() if self.timeSwitchCheckbox.IsChecked() else prompt.Hide()
		self.Fit()

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

	def __init__(self, parent, func=None):
		inst = MetadataStreamingDialog._instance() if MetadataStreamingDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		MetadataStreamingDialog._instance = weakref.ref(self)

		# Translators: Title of a dialog to configure metadata streaming status for DSP encoder and four additional URL's.
		super(MetadataStreamingDialog, self).__init__(parent, title=_("Metadata streaming options"))
		self.func = func

		# WX's CheckListBox isn't user friendly.
		# Therefore use checkboxes laid out across the top.
		self.checkedStreams = []
		# Add the DSP encoder checkbox first before adding other URL's.
		checkedDSP=wx.CheckBox(self,wx.NewId(),label="DSP encoder")
		if func:
			streaming = func(0, 36, ret=True)
			if streaming == -1: streaming += 1
			checkedDSP.SetValue(streaming)
		else: checkedDSP.SetValue(self.Parent.metadataStreams[0])
		self.checkedStreams.append(checkedDSP)
		# Now the rest.
		for url in xrange(1, 5):
			checkedURL=wx.CheckBox(self,wx.NewId(),label="URL {URL}".format(URL = url))
			if func:
				streaming = func(url, 36, ret=True)
				if streaming == -1: streaming += 1
				checkedURL.SetValue(streaming)
			else: checkedURL.SetValue(self.Parent.metadataStreams[url])
			self.checkedStreams.append(checkedURL)

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		if func is None: labelText=_("Select the URL for metadata streaming upon request.")
		else: labelText=_("Check to enable metadata streaming, uncheck to disable.")
		label = wx.StaticText(self, wx.ID_ANY, label=labelText)
		mainSizer.Add(label,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedStream in self.checkedStreams:
			sizer.Add(checkedStream)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		if self.func is not None:
			# Translators: A checkbox to let metadata streaming status be applied to the currently active broadcast profile.
			self.applyCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Apply streaming changes to the selected profile"))
			self.applyCheckbox.SetValue(True)
			mainSizer.Add(self.applyCheckbox, border=10,flag=wx.TOP)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedStreams[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global _metadataDialogOpened
		if self.func is None: parent = self.Parent
		metadataEnabled = []
		for url in xrange(5):
			if self.func is None: parent.metadataStreams[url] = self.checkedStreams[url].Value
			else:
				dataLo = 0x00010000 if self.checkedStreams[url].Value else 0xffff0000
				self.func(dataLo | url, 36)
				if self.applyCheckbox.Value: metadataEnabled.append(self.checkedStreams[url].Value)
		if self.func is None:
			parent.profiles.SetFocus()
			parent.Enable()
		else:
			# 6.1: Store just toggled settings to profile if told to do so.
			if len(metadataEnabled): splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"] = metadataEnabled
		self.Destroy()
		_metadataDialogOpened = False
		return

	def onCancel(self, evt):
		global _metadataDialogOpened
		if self.func is None: self.Parent.Enable()
		self.Destroy()
		_metadataDialogOpened = False

# Column announcement manager.
# Select which track columns should be announced and in which order.
class ColumnAnnouncementsDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: Title of a dialog to configure column announcements (order and what columns should be announced).
		super(ColumnAnnouncementsDialog, self).__init__(parent, title=_("Manage column announcements"))

		# Same as metadata dialog (wx.CheckListBox isn't user friendly).
		# Gather values for checkboxes except artist and title.
		# 6.1: Split these columns into rows.
		self.checkedColumns = []
		for column in ("Duration", "Intro", "Category", "Filename"):
			checkedColumn=wx.CheckBox(self,wx.NewId(),label=column)
			checkedColumn.SetValue(column in self.Parent.includedColumns)
			self.checkedColumns.append(checkedColumn)
		self.checkedColumns2 = []
		for column in ("Outro","Year","Album","Genre","Mood","Energy"):
			checkedColumn=wx.CheckBox(self,wx.NewId(),label=column)
			checkedColumn.SetValue(column in self.Parent.includedColumns)
			self.checkedColumns2.append(checkedColumn)
		self.checkedColumns3 = []
		for column in ("Tempo","BPM","Gender","Rating","Time Scheduled"):
			checkedColumn=wx.CheckBox(self,wx.NewId(),label=column)
			checkedColumn.SetValue(column in self.Parent.includedColumns)
			self.checkedColumns3.append(checkedColumn)


		mainSizer = wx.BoxSizer(wx.VERTICAL)
		# Translators: Help text to select columns to be announced.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Select columns to be announced (artist and title are announced by default"))
		mainSizer.Add(label,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedColumn in self.checkedColumns:
			sizer.Add(checkedColumn)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedColumn in self.checkedColumns2:
			sizer.Add(checkedColumn)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for checkedColumn in self.checkedColumns3:
			sizer.Add(checkedColumn)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to select column announcement order.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Column &order:"))
		# WXPython Phoenix contains RearrangeList to allow item orders to be changed automatically.
		# Because WXPython Classic doesn't include this, work around by using a variant of list box and move up/down buttons.
		self.trackColumns= wx.ListBox(self, wx.ID_ANY, choices=parent.columnOrder)
		self.trackColumns.Bind(wx.EVT_LISTBOX,self.onColumnSelection)
		try:
			self.trackColumns.SetSelection(0)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.trackColumns)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

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
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.checkedColumns[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.columnOrder = self.trackColumns.GetItems()
		# Make sure artist and title are always included.
		parent.includedColumns.add("Artist")
		parent.includedColumns.add("Title")
		for checkbox in self.checkedColumns + self.checkedColumns2 + self.checkedColumns3:
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

# Columns Explorer.
# Configure which column will be announced when SPL Assistnat, number keys are pressed.
class ColumnsExplorerDialog(wx.Dialog):

	def __init__(self, parent):
		# Translators: The title of Columns Explorer configuration dialog.
		super(ColumnsExplorerDialog, self).__init__(parent, title=_("Columns Explorer"))

		# Gather column slots.
		# 7.0: First six slots are reserved for Studio 5.0x columns.
		self.columnSlots = []

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		# 7.0: Studio 5.0x columns.
		# 8.0: Remove the below code.
		oldStudioColumns = ["Artist", "Title", "Duration", "Intro", "Category", "Filename"]
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		for slot in xrange(6):
			# Translators: The label for a setting in SPL add-on dialog to select column for this column slot.
			label = wx.StaticText(self, wx.ID_ANY, label=_("Slot {position}").format(position = slot+1))
			columns = wx.Choice(self, wx.ID_ANY, choices=oldStudioColumns)
			try:
				columns.SetSelection(oldStudioColumns.index(parent.exploreColumns[slot]))
			except:
				pass
			sizer.Add(label)
			sizer.Add(columns)
			self.columnSlots.append(columns)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# For Studio 5.10 and later.
		if splconfig.SPLConfig["ColumnExpRange"] == (0, 10):
			sizer = wx.BoxSizer(wx.HORIZONTAL)
			for slot in xrange(6, 10):
				label = wx.StaticText(self, wx.ID_ANY, label=_("Slot {position}").format(position = slot+1))
				columns = wx.Choice(self, wx.ID_ANY, choices=splconfig._SPLDefaults7["ColumnAnnouncement"]["ColumnOrder"])
				try:
					columns.SetSelection(splconfig._SPLDefaults7["ColumnAnnouncement"]["ColumnOrder"].index(parent.exploreColumns[slot]))
				except:
					pass
				sizer.Add(label)
				sizer.Add(columns)
				self.columnSlots.append(columns)
			mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.columnSlots[0].SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		for slot in xrange(len(self.columnSlots)):
			parent.exploreColumns[slot] = self.columnSlots[slot].GetStringSelection()
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

		# Translators: the label for a setting in SPL add-on settings to announce scheduled time.
		self.scheduledForCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce &scheduled time for the selected track"))
		self.scheduledForCheckbox.SetValue(parent.scheduledFor)
		mainSizer.Add(self.scheduledForCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce listener count.
		self.listenerCountCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Announce &listener count"))
		self.listenerCountCheckbox.SetValue(parent.listenerCount)
		mainSizer.Add(self.listenerCountCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for a setting in SPL add-on settings to announce currently playing cart.
		self.cartNameCheckbox=wx.CheckBox(self,wx.NewId(),label=_("&Announce name of the currently playing cart"))
		self.cartNameCheckbox.SetValue(parent.cartName)
		mainSizer.Add(self.cartNameCheckbox, border=10,flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: the label for a setting in SPL add-on settings to announce currently playing track name.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Track name announcement:"))
		# Translators: One of the track name announcement options.
		self.trackAnnouncements=[("auto",_("automatic")),
		# Translators: One of the track name announcement options.
		("background",_("while using other programs")),
		# Translators: One of the track name announcement options.
		("off",_("off"))]
		self.trackAnnouncementList= wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.trackAnnouncements])
		selection = (x for x,y in enumerate(self.trackAnnouncements) if y[0]==parent.playingTrackName).next()
		try:
			self.trackAnnouncementList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.trackAnnouncementList)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.scheduledForCheckbox.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.scheduledFor = self.scheduledForCheckbox.Value
		parent.listenerCount = self.listenerCountCheckbox.Value
		parent.cartName = self.cartNameCheckbox.Value
		parent.playingTrackName = self.trackAnnouncements[self.trackAnnouncementList.GetSelection()][0]
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

	def __init__(self, parent):
		# Translators: The title of a dialog to configure advanced SPL add-on options such as update checking.
		super(AdvancedOptionsDialog, self).__init__(parent, title=_("Advanced options"))

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		sizer = wx.BoxSizer(wx.VERTICAL)
		# Translators: A checkbox to toggle automatic add-on updates.
		self.autoUpdateCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Automatically check for add-on &updates"))
		self.autoUpdateCheckbox.SetValue(self.Parent.autoUpdateCheck)
		sizer.Add(self.autoUpdateCheckbox, border=10,flag=wx.TOP)
		# Translators: The label for a setting in SPL add-on settings/advanced options to select automatic update interval in days.
		label = wx.StaticText(self, wx.ID_ANY, label=_("Update &interval in days"))
		sizer.Add(label)
		self.updateInterval= wx.SpinCtrl(self, wx.ID_ANY, min=1, max=30)
		self.updateInterval.SetValue(long(parent.updateInterval))
		self.updateInterval.SetSelection(-1, -1)
		sizer.Add(self.updateInterval)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		# LTS and 8.x only.
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a combo box to select update channel.
		label = wx.StaticText(self, wx.ID_ANY, label=_("&Add-on update channel:"))
		self.channels= wx.Choice(self, wx.ID_ANY, choices=["stable", "longterm"])
		self.updateChannels = ("stable", "lts")
		self.channels.SetSelection(self.updateChannels.index(self.Parent.updateChannel))
		sizer.Add(label)
		sizer.Add(self.channels)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: A checkbox to toggle if SPL Controller command can be used to invoke Assistant layer.
		self.splConPassthroughCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Allow SPL C&ontroller command to invoke SPL Assistant layer"))
		self.splConPassthroughCheckbox.SetValue(self.Parent.splConPassthrough)
		sizer.Add(self.splConPassthroughCheckbox, border=10,flag=wx.TOP)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: The label for a setting in SPL add-on dialog to set keyboard layout for SPL Assistant.
		label = wx.StaticText(self, wx.ID_ANY, label=_("SPL Assistant command &layout:"))
		self.compatibilityLayouts=[("off","NVDA"),
		("jfw","JAWS for Windows"),
		("wineyes","Window-Eyes")]
		self.compatibilityList= wx.Choice(self, wx.ID_ANY, choices=[x[1] for x in self.compatibilityLayouts])
		selection = (x for x,y in enumerate(self.compatibilityLayouts) if y[0]==self.Parent.compLayer).next()
		try:
			self.compatibilityList.SetSelection(selection)
		except:
			pass
		sizer.Add(label)
		sizer.Add(self.compatibilityList)
		mainSizer.Add(sizer, border=10, flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.autoUpdateCheckbox.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		parent = self.Parent
		parent.splConPassthrough = self.splConPassthroughCheckbox.Value
		parent.compLayer = self.compatibilityLayouts[self.compatibilityList.GetSelection()][0]
		parent.autoUpdateCheck = self.autoUpdateCheckbox.Value
		parent.updateInterval = self.updateInterval.Value
		parent.updateChannel = ("stable", "lts")[self.channels.GetSelection()]
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

		# Translators: the label for resetting profile triggers.
		self.resetInstantProfileCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Reset instant switch profile"))
		self.resetInstantProfileCheckbox.SetValue(False)
		mainSizer.Add(self.resetInstantProfileCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for resetting profile triggers.
		self.resetTimeProfileCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Delete time-based profile database"))
		self.resetTimeProfileCheckbox.SetValue(False)
		mainSizer.Add(self.resetTimeProfileCheckbox, border=10,flag=wx.BOTTOM)

				# Translators: the label for resetting encoder settings.
		self.resetEncodersCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Remove encoder settings"))
		self.resetEncodersCheckbox.SetValue(False)
		mainSizer.Add(self.resetEncodersCheckbox, border=10,flag=wx.BOTTOM)

		# Translators: the label for resetting track comments.
		self.resetTrackCommentsCheckbox=wx.CheckBox(self,wx.NewId(),label=_("Erase track comments"))
		self.resetTrackCommentsCheckbox.SetValue(False)
		mainSizer.Add(self.resetTrackCommentsCheckbox, border=10,flag=wx.BOTTOM)

		mainSizer.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
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
			parent.profiles.SetFocus()
			parent.Enable()
			self.Destroy()
			return
		import threading, sys, globalVars
		# Reset all profiles.
		# LTS: Only a priveleged thread should do this, otherwise unexpected things may happen.
		# Save some flags from death.
		with threading.Lock() as resetting:
			global _configDialogOpened
			colRange = splconfig.SPLConfig["ColumnExpRange"]
			splconfig.resetAllConfig()
			splconfig.SPLConfig = dict(splconfig._SPLDefaults7)
			splconfig.SPLConfig["ActiveIndex"] = 0
			splconfig.SPLActiveProfile = splconfig.SPLConfigPool[0].name
			splconfig.SPLConfig["ColumnExpRange"] = colRange
			if self.resetInstantProfileCheckbox.Value:
				if splconfig.SPLSwitchProfile is not None:
					splconfig.SPLSwitchProfile = None
					splconfig.SPLPrevProfile = None
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
				if "globalPlugins.SPLStudioUtils.encoders" in sys.modules:
					import globalPlugins.SPLStudioUtils.encoders
					globalPlugins.SPLStudioUtils.encoders.cleanup()
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
