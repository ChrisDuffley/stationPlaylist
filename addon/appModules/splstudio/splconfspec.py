# SPL Studio Configuration Specifications
# An app module and global plugin package for NVDA
# Copyright 2020 Joseph Lee, released under GPL.
# Provides configuration specifications (confspec) for SPL add-on settings.
# Split from SPL config module in 2020.
# Idea borrowed from NVDA Core's configspec module (credit: NV Access).

from io import StringIO
from configobj import ConfigObj

# StationPlaylist add-on settings spec.
confspec = ConfigObj(StringIO("""
[General]
BeepAnnounce = boolean(default=false)
MessageVerbosity = option("beginner", "advanced", default="beginner")
BrailleTimer = option("off", "intro", "outro", "both", default="off")
AlarmAnnounce = option("beep", "message", "both", default="beep")
TrackCommentAnnounce = option("off", "beep", "message", "both", default="off")
LibraryScanAnnounce = option("off", "ending", "progress", "numbers", default="off")
CategorySounds = boolean(default=false)
TopBottomAnnounce = boolean(default=true)
RequestsAlert = boolean(default=true)
MetadataReminder = option("off", "startup", "instant", default="off")
TimeHourAnnounce = boolean(default=true)
ExploreColumns = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood"))
ExploreColumnsTT = string_list(default=list("Artist","Title","Duration","Cue","Overlap","Intro","Segue","Filename","Album","CD Code"))
ExploreColumnsCreator = string_list(default=list("Artist","Title","Position","Cue","Intro","Outro","Segue","Duration","Last Scheduled","7 Days"))
VerticalColumnAnnounce = option(None,"Status","Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled",default=None)
[PlaylistSnapshots]
DurationMinMax = boolean(default=true)
DurationAverage = boolean(default=true)
ArtistCount = boolean(default=true)
ArtistCountLimit = integer(min=0, max=10, default=5)
CategoryCount = boolean(default=true)
CategoryCountLimit = integer(min=0, max=10, default=5)
GenreCount = boolean(default=true)
GenreCountLimit = integer(min=0, max=10, default=5)
ShowResultsWindowOnFirstPress = boolean(default=false)
[IntroOutroAlarms]
SayEndOfTrack = boolean(default=true)
EndOfTrackTime = integer(min=1, max=59, default=5)
SaySongRamp = boolean(default=true)
SongRampTime = integer(min=1, max=9, default=5)
[MicrophoneAlarm]
MicAlarm = integer(min=0, max=7200, default="0")
MicAlarmInterval = integer(min=0, max=60, default=0)
[MetadataStreaming]
MetadataEnabled = bool_list(default=list(false,false,false,false,false))
[ColumnAnnouncement]
UseScreenColumnOrder = boolean(default=true)
ColumnOrder = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
IncludedColumns = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
[PlaylistTranscripts]
ColumnOrder = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
IncludedColumns = string_list(default=list("Artist","Title","Duration","Intro","Outro","Category","Year","Album","Genre","Mood","Energy","Tempo","BPM","Gender","Rating","Filename","Time Scheduled"))
[SayStatus]
SayScheduledFor = boolean(default=true)
SayListenerCount = boolean(default=true)
SayPlayingCartName = boolean(default=true)
SayStudioPlayerPosition = boolean(default=false)
[Advanced]
SPLConPassthrough = boolean(default=false)
CompatibilityLayer = option("off", "jfw", default="off")
[Startup]
WelcomeDialog = boolean(default=true)
"""), encoding="UTF-8", list_values=False)
confspec.newlines = "\r\n"
