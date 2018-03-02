# StationPlaylist Studio #

* مطورو الإضافة: Geoff Shang, Joseph Lee وآخرون
* تحميل [الإصدار النهائي][1]
* تحميل [الإصدار التجريبي][2]

تقوم هذه الإضافة البرمجية بتحسين استخدام الكفيف لتطبيق Station Playlist
Studio, فضلا عن إضافة أدوات للتحكم في الأستوديو من أي مكان.

For more information about the add-on, read the [add-on guide][4]. For
developers seeking to know how to build the add-on, see
buildInstructions.txt located at the root of the add-on source code
repository.

IMPORTANT NOTES:

* This add-on requires NVDA 2017.4 or later and StationPlaylist Studio 5.10
  or later.
* If using Windows 8 or later, for best experience, disable audio ducking
  mode.
* add-on 8.0/16.10 requires Studio 5.10 or later. For broadcasters using
  Studio 5.0x and/or Windows XP, Vista or 7 without Service Pack 1, a
  [long-term support version][3] (15.x) is available. The last stable
  version to support Windows releases prior to 7 Service Pack 1 is 17.11.2.
* Starting from 2018, [changelogs for old add-on releases][5] will be found
  on GitHub. This add-on readme will list changes from version 5.0 (2015
  onwards).
* Certain add-on features (notably add-on updating) won't work under some
  conditions, including running NVDA in secure mode.
* Due to tecnical limitations, you cannot install or use this add-on on
  Windows Store version of NVDA.

## مفاتيح الاختصار

* Alt+Shift+T من نافذة الاستوديو: للإعلان عن الوقت المنقضي للمسار أو التراك
  المشغل حاليا.
* Control+Alt+T (مسح بإصبعين لأسفل بنمط SPL) من نافذة الاستوديو: للإعلان عن
  الوقت المتبقي للمسار أو التراك المشغل حاليا.
* NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window:
  announces broadcaster time such as 5 minutes to top of the hour. Pressing
  this command twice will announce minutes and seconds till top of the hour.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  end of track setting dialog.
* Alt+NVDA+2 (مسح بأصبعين يسار بنمطSPL) من نافذة الاستوديو: لفتح محاورة
  إعدادات التنبيه بمقدمة الأغنية.
* Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart
  assignments.
* Alt+NVDA+4 from Studio window: Opens microphone alarm dialog.
* اضغط ctrl+NVDA+F من نافذة الأستديو لفتح محاورة اختيار المسارات بحسب المطرب
  أو الأغنية. اضغط NVDA+f3 للبحث نحو التالي واضغط Shift+NVDA+f3 للبحث نحو
  السابق. 
* Alt+NVDA+R من نافذة الاستوديو: لخطوات إعدادات الإعلان عن البحث في المكتبة
* Control+Shift+X من نافذة الاستوديو: لخطوات إعدادات ميقات البرايل.
* Control+Alt+left/right arrow (while focused on a track): Announce
  previous/next track column.
* Control+Alt+up/down arrow (while focused on a track): Move to previous or
  next track and announce specific columns (unavailable in add-on 15.x).
* Control+NVDA+1 through 0 (6 for Studio 5.0x): Announce column content for
  a specified column.
* Alt+NVDA+C while focused on a track: announces track comments if any.
* Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration
  dialog.
* Control+NVDA+- (hyphen) من نافذة الاستوديو: إرسال الاستفسارات لمطور
  الإضافة باستخدام منظم البريد الافتراضي لديك.
* Alt+NVDA+F1: Open welcome dialog.

## الأوامر غير المعينة

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands.

* التحول إلى نافذة الأستديو من أي برنامج آخر. 
* نمط التحكم في تطبيق SPL. 
* Announcing Studio status such as track playback from other programs.
* نمط SPL المساعد من الأستوديو. 
* الإعلان عن الوقت متضمن الثواني من SPL Studio.
* الإعلان عن درجة الحرارة
* الإعلان عن عنوان المسار التالي إذا كان مجدول.
* الإعلان عن عنوان المسار المشغل حاليا
* تحديد المسار الحالي لبدأ تحليل وقت المسار
* إجراء تحليل وقت المسار
* Take playlist snapshots.
* البحث عن نص بأعمدة محددة
* البحث عن مسارات تقع بين معدل وقت معين عبر باحث عن معدلات الوقت.
* تشغيل أو تعطيل حالة بث البيانات بسرعة

## أوامر إضافية عند استخدام Sam encoder أو SPL.

تتوفر المفاتيح التالية عند استخدام Sam encoder أو SPL:

* F9: الاتصال بالخادم الذي سيتم بث الملفات من خلاله.
* F10: (SAM encoder فقط) قطع الاتصال بالخادم.
* Control+F9/Control+F10 (تشفير SAM فقط): اتصال أو قطع اتصال كل التشفيرات,
  على التوالي.
* F11: ينتقل بين تشغيل وتعطيل الرجوع لنافذة الاستوديو بعد الاتصال بالخادم.
* shift+F11: ينتقل بين تشغيل وتعطيل إمكانية تشغيل أول مسار بعد الاتصال
  بالخادم.
* Control+F11: التبديل بين تشغيل وتعطيل المراقبة الخلفية للتشفير المحدد.
* F12: Opens a dialog to enter custom label for the selected encoder or
  stream.
* Control+F12: يفتح محاورة لاختيار التشفير الذي قمت بحذفه (لإعادة ترتيب
  أسماء الفيديوهات التي ستبث وإعدادات التشفير).
* Alt+NVDA+0: Opens encoder settings dialog to configure options such as
  stream label.

فضلا عن ذلك, إتاحة أوامر لمراجعة الأعمدة وتشمل:

* Control+NVDA+1: موقع التشفير
* Control+NVDA+2: البث
* Control+NVDA+3 من sam encoder: تنسيق التشفير.
* Control+NVDA+3 (من نافذة التشفير): إعدادات التشفير
* control+nvda+4 (من نافذة تشفير sam) حالة اتصال التشفير.
* control+nvda+4 من تشفير spl: معدل النقل أو حالة الاتصال.
* control+nvda+5 من تشفير SAM: وصف حالة الاتصال

## مساعد نمط أوامر SPL 

This layer command set allows you to obtain various status on SPL Studio,
such as whether a track is playing, total duration of all tracks for the
hour and so on. From any SPL Studio window, press the SPL Assistant layer
command, then press one of the keys from the list below (one or more
commands are exclusive to playlist viewer). You can also configure NvDA to
emulate commands from other screen readers.

The available commands are:

* A: التشغيل الآلي.
* C (Shift+C in JAWS and Window-Eyes layouts): Title for the currently
  playing track.
* C (JAWS and Window-Eyes layouts): Toggle cart explorer (playlist viewer
  only).
* D (R in JAWS layout): Remaining duration for the playlist (if an error
  message is given, move to playlist viewer and then issue this command).
* E (G in Window-Eyes layout): Metadata streaming status.
* Shift+1 through Shift+4, Shift+0: Status for individual metadata streaming
  URL's (0 is for DSP encoder).
* E (Window-Eyes layout): Elapsed time for the currently playing track.
* F: Find track (playlist viewer only).
* H: مدة الموسيقى للساعة الحالية.
* Shift+H: Remaining track duration for the hour slot.
* I (L in JAWS or Window-Eyes layouts): Listener count.
* K: Move to the marked track (playlist viewer only).
* Control+K: Set the current track as the place marker track (playlist
  viewer only).
* L (Shift+L in JAWS and Window-Eyes layouts): Line in.
* M:  الميكروفون
* N: لتشغيل المسار التالي.
* P: حالة التشغيل (المسار يعمل أم متوقف).
* shift+P: حدة المسار الحالي.
* R (Shift+E in JAWS and Window-Eyes layouts): Record to file
  enabled/disabled.
* shift+r: مراقبة حالة التقدم في البحث بالمكتبة.
* S: Track starts (scheduled).
* Shift+S: Time until selected track will play (track starts in).
* T: Cart edit/insert mode on/off.
* U: وقت الاستوديو
* Control+Shift+U: Check for add-on updates.
* W: حالة التقس ودرجة الحرارة إذا كانت معدة.
* y: حالة قائمة التشغيل المعدلة.
* 1 through 0 (6 for Studio 5.0x): Announce column content for a specified
  column.
* F8: Take playlist snapshots (number of tracks, longest track, etc.).
* F9: Mark current track for track time analysis (playlist viewer only).
* F10: Perform track time analysis (playlist viewer only).
* f12: الانتقال بين الملف الحالي وملف لم يتم تعريفه من قبل.
* F1: نمط المساعدة
* shift+f1: فتح دليل المستخدم على الإنترنت

## نمط التحكم في تطبيق SPL 

هو عبارة عن نمط يزودك بمجموعة من المفاتيح كي تتمكن من التحكم في التطبيق من
أي مكان. اضغط أمر نمط التحكم في SPL وسينطق NVDA, "نمط التحكم في Station
PlayList Studio." اضغط أي من الأوامر التي سيلي ذكرها للتحكم في مختلف إعدادات
الاستوديو بالتطبيق كالتحكم في تشغيل أو تعطيل الميكروفون, أو تشغيل المسار
التالي.

والأوامر التي يتيحها هذا النمط هي:

* اضغط P لتشغيل المسار التالي.
* اضغط U لعمل توقف مؤقت أو إعادة التشغيل مرة أخرى.
* اضغط S لوقف تشغيل المسار بطريقة التلاشي (fade out), أو اضغط حرف T لتوقف
  المسار فورا.
* اضغط M أو Shift+M لتشغيل أو تعطيل الميكروفون, على التوالي, أو N لتشغيل
  الميكروفون دون التلاشي
* اضغط a لتفعيل خاصية التشغيل الآلي, واضغط Shift+A لتعطيلها.
* اضغط L لتفعيل مدخل الصوت واضغط shift+l لتعطيله.
* Press R to hear remaining time for the currently playing track.
* اضغط Shift+R للإعلان عن مدى التقدم في البحث في المكتبة.
* Press C to let NVDA announce name and duration of the currently playing
  track.
* Press Shift+C to let NVDA announce name and duration of the upcoming track
  if any.
* اضغط E للحصول على عدد وأسماء التشفيرات الجاري مراقبتها.
* Press I to obtain listener count.
* Press Q to obtain various status information about Studio including
  whether a track is playing, microphone is on and others.
* Press cart keys (F1, Control+1, for example) to play assigned carts from
  anywhere.
* Press H to show a help dialog which lists available commands.

## تنبيهات المسار

By default, NvDA will play a beep if five seconds are left in the track
(outro) and/or intro. To configure this value as well as to enable or
disable them, press Alt+NVDA+1 or Alt+NVDA+2 to open end of track and song
ramp dialogs, respectively. In addition, use Studio add-on settings dialog
to configure if you'll hear a beep, a message or both when alarms are turned
on.

## تنبيه الميكروفون

You can ask NVDA to play a sound when microphone has been active for a
while. Press Alt+NVDA+4 to configure alarm time in seconds (0 disables it).

## الباحث عن المسارات

If you wish to quickly find a song by an artist or by song name, from track
list, press Control+NVDA+F. Type or choose the name of the artist or the
song name. NVDA will either place you at the song if found or will display
an error if it cannot find the song you're looking for. To find a previously
entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or
backward.

ملحوظة: الباحث عن المسارات حساس لحالة الأحرف. 

## مستكشف التنويهات

وفقا لإصدار البرنامج, يتيح لك برنامج SPL تعيين مفتاح ل96 تنويه. يتيح لك NVDA
سماع أي تنويه معين لهذه الأوامر.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the
cart command once will tell you which jingle is assigned to the
command. Pressing the cart command twice will play the jingle. Press
Alt+NvDA+3 to exit cart explorer. See the add-on guide for more information
on cart explorer.

## تحليل وقت المسار

للحصول على مدة المسارات المحددة لتشغيلها, قم بتحديد المسار الحالي لبدأ عملية
تحليل الوقت (من مساعد spl اضغط على f9), ثم اضغط على f10 بعد الانتهاء من
التحديد.

## Columns Explorer

By pressing Control+NVDA+1 through 0 (6 for Studio 5.0x) or SPL Assistant, 1
through 0 (6 for Studio 5.01 and earlier), you can obtain contents of
specific columns. By default, these are artist, title, duration, intro,
category and filename (Studio 5.10 adds year, album, genre and time
scheduled). You can configure which columns will be explored via columns
explorer dialog found in add-on settings dialog.

## Playlist snapshots

You can press SPL Assistant, F8 while focused on a playlist in Studio to
obtain various statistics about a playlist, including number of tracks in
the playlist, longest track, top artists and so on. After assigning a custom
command for this feature, pressing the custom command twice will cause NVDA
to present playlist snapshot information as a webpage so you can use browse
mode to navigate (press escape to close).

## محاورة الإعدادات

From studio window, you can press Alt+NVDA+0 to open the add-on
configuration dialog. Alternatively, go to NVDA's preferences menu and
select SPL Studio Settings item. This dialog is also used to manage
broadcast profiles.

## نمط اللمس لتطبيق SPL

إذا كنت تستخدم الاستوديو من حاسوب بشاشة لمس يعمل بنظام التشغيل ويندوز 8 وما
بعده ولديك NVDA 2012.3 وما بعده, يمكنك أداء بعض الأوامر من شاشة اللمس. أولا
استخدم لمسة ب3 أصابع للانتقال لنمط اللمس, ثم استخدم أوامر اللمس المسرودة
أعلاه لأداء المهام.

## Version 18.03/15.14-LTS

* If NVDA is configured to announce metadata streaming status when Studio
  starts, NVDA will honor this setting and no longer announce streaming
  status when switching to and from instant switch profiles.
* If switching to and from an instant switch profile and NVDA is configured
  to announce metadata streaming status whenever this happens, NVDA will no
  longer announce this information multiple times when switching profiles
  quickly.
* NVDA will remember to switch to the appropriate time-based profile (if
  defined for a show) after NVDA restarts multiple times during broadcasts.
* If a time-based profile with profile duration set is active and when
  add-on settings dialog is opened and closed, NVDA will still switch back
  to the original profile once the time-based profile is finished.
* If a time-based profile is active (particularly during broadcasts),
  changing broadcast profile triggers via add-on settings dialog will not be
  possible.

## Version 18.02/15.13-LTS

* 18.02: Due to internal changes made to support extension points and other
  features, NVDA 2017.4 is required.
* Add-on updating won't be possible under some cases. These include running
  NVDA from source code or with secure mode turned on. Secure mode check is
  applicable to 15.13-LTS as well.
* If errors occur while checking for updates, these will be logged and NVDA
  will advise you to read the NVDA log for details.
* In add-on settings, various update settings in advanced settings section
  such as update interval will not be displayed if add-on updating is not
  supported.
* NVDA will no longer appear to freeze or do nothing when switching to an
  instant switch profile or a time-based profile and NVDA is configured to
  announce metadata streaming status.

## Version 18.01/15.12-LTS

* When using JAWS layout for SPL Assistant, update check command
  (Control+Shift+U) now works correctly.
* When changing microphone alarm settings via the alarm dialog (Alt+NVDA+4),
  changes such as enabling alarm and changes to microphone alarm interval
  are applied when closing the dialog.

## Version 17.12

* Windows 7 Service Pack 1 or later is required.
* Several add-on features were enhanced with extension points. This allows
  microphone alarm and metadata streaming feature to respond to changes in
  broadcast profiles. This requires NvDA 2017.4.
* When Studio exits, various add-on dialogs such as add-on settings, alarm
  dialogs and others will close automatically. This requires NVDA 2017.4.
* Added a new command in SPL Controller layer to announce name of the
  upcoming track if any (Shift+C).
* You can now press cart keys (F1, for example) after entering SPl
  Controller layer to play assigned carts from anywhere.
* Due to changes introduced in wxPython 4 GUI toolkit, stream label eraser
  dialog is now a combo box instead of a number entry field.

## Version 17.11.2

This is the last stable version to support Windows XP, Vista and 7 without
Service Pack 1. The next stable version for these Windows releases will be a
15.x LTS release.

* If using Windows releases prior to Windows 7 Service Pack 1, you cannot
  switch to development channels.

## Version 17.11.1/15.11-LTS

* NVDA will no longer play error tones or appear to do nothing when using
  Control+Alt+left or right arrow keys to navigate columns in Track Tool
  5.20 with a track loaded. Because of this change, when using Studio 5.20,
  build 48 or later is required.

## Version 17.11/15.10-LTS

* Initial support for StationPlaylist Studio 5.30.
* If microphone alarm and/or interval timer is turned on and if Studio exits
  while microphone is on, NVDA will no longer play microphone alarm tone
  from everywhere.
* When deleting broadcast profiles and if another profile happens to be an
  instant switch profile, instant switch flag won't be removed from the
  switch profile.
* If deleting an active profile that is not an instant switch or a
  time-based profile, NVDA will ask once more for confirmation before
  proceeding.
* NVDA will apply correct settings for microphone alarm settings when
  switching profiles via add-on settings dialog.
* You can now press SPL Controller, H to obtain help for SPL Controller
  layer.

## Version 17.10

* If using Windows releases prior to Windows 7 Service Pack 1, you cannot
  switch to Test Drive Fast update channel. A future release of this add-on
  will move users of old Windows versions to a dedicated support channel.
* Several general settings such as status announcement beeps, top and bottom
  of playlist notification and others are now located in the new general
  add-on settings dialog (accessed from a new button in add-on settings).
* It is now possible to make add-on options read-only, use only the normal
  profile, or not load settings from disk when Studio starts. These are
  controlled by new command-line switches specific to this add-on.
* When running NVDA from Run dialog (Windows+R), you can now pass in
  additional command-line switches to change how the add-on works. These
  include "--spl-configvolatile" (read-only settings),
  "--spl-configinmemory" (do not load settings from disk), and
  "--spl-normalprofileonly" (only use normal profile).
* If exitting Studio (not NVDA) while an instant switch profile is active,
  NVDA will no longer give misleading announcement when switching to an
  instant switch profile when using Studio again.

## Version 17.09.1

* As a result of announcement from NV Access that NVDA 2017.3 will be the
  last version to support Windows versions prior to windows 7 Service Pack
  1, Studio add-on will present a reminder message about this if running
  from old Windows releases. End of support for old Windows releases from
  this add-on (via long-term support release) is scheduled for April 2018.
* NVDA will no longer display startup dialogs and/or announce Studio version
  if started with minimal (nvda -rm) flag set. The sole exception is the old
  Windows release reminder dialog.

## Version 17.09

* If a user enters advanced options dialog under add-on settings while the
  update channel and interval was set to Test Drive Fast and/or zero days,
  NVDA will no longer present the channel and/or interval warning message
  when exitting this dialog.
* Playlist remainder and trakc time analysis commands will now require that
  a playlist be loaded, and a more accurate error message will be presented
  otherwise.

## Version 17.08.1

* NVDA will no longer fail to cause Studio to play the first track when an
  encoder is connected.

## Version 17.08

* Changes to update channel labels: try build is now Test Drive Fast,
  development channel is Test Drive Slow. The true "try" builds will be
  reserved for actual try builds that require users to manually install a
  test version.
* Update interval can now be set to 0 (zero) days. This allows the add-on to
  check for updates when NVDA and/or SPL Studio starts. A confirmation will
  be required to change update interval to zero days.
* NVDA will no longer fail to check for add-on updates if update interval is
  set to 25 days or longer.
* In add-on settings, added a checkbox to let NvDA play a sound when
  listener requests arrive. To use this fully, requests window must pop up
  when requests arrive.
* Pressing broadcaster time command (NVDA+Shift+F12) twice will now cause
  NVDA to announce minutes and seconds remaining in the current hour.
* It is now possible to use Track Finder (Control+NVDA+F) to search for
  names of tracks you've searched before by selecting a search term from a
  history of terms.
* When announcing title of current and next track via SPL Assistant, it is
  now possible to include information about which Studio internal player
  will play the track (e.g. player 1).
* Added a setting in add-on settings under status announcements to include
  player information when announcing title of the current and the next
  track.
* Fixed an issue in temporary cue and other dialogs where NVDA would not
  announce new values when manipulating time pickers.
* NVDA can suppress announcement of column headers such as Artist and
  Category when reviewing tracks in playlist viewer. This is a broadcast
  profile specific setting.
* Added a checkbox in add-on settings dialog to suppress announcement of
  column headers when reviewing tracks in playlist viewer.
* Added a command in SPL Controller layer to announce name and duration of
  the currently playing track from anywhere (C).
* When obtaining status information via SPL Controller (Q) while using
  Studio 5.1x, information such as microphone status, cart edit mode and
  others will also be announced in addition to playback and automation.

## Version 17.06

* You can now perform Track Finder command (Control+NVDA+F) while a playlist
  is loaded but the first track isn't focused.
* NVDA will no longer play error tones or do nothing when searching for a
  track forward from the last track or backward from the first track,
  respectively.
* Pressing NVDA+Numpad Delete (NVDA+Delete in laptop layout) will now
  announce track position followed by number of items in a playlist.

## Version 17.05.1

* NVDA will no longer fail to save changes to alarm settings from various
  alarm dialogs (for example, Alt+NVDA+1 for end of track alarm).

## Version 17.05/15.7-LTS

* Update interval can now be set up to 180 days. For default installations,
  update check interval will be 30 days.
* Fixed an issue where NVDA may play error tone if Studio exits while a
  time-based profile is active.

## Version 17.04

* Added a basic add-on debugging support by logging various information
  while the add-on is active with NVDA set to debug logging (requires NVDA
  2017.1 and later). To use this, after installing NVDA 2017.1, from Exit
  NVDA dialog, choose "restart with debug logging enabled" option.
* Improvements to presentation of various add-on dialogs thanks to NVDA
  2016.4 features.
* NVDA will download add-on updates in the background if you say "yes" when
  asked to update the add-on. Consequently, file download notifications from
  web browsers will no longer be shown.
* NVDA will no longer appear to freeze when checking for update at startup
  due to add-on update channel change.
* Added ability to press Control+Alt+up or down arrow keys to move between
  tracks (specifically, track columns) vertically just as one is moving to
  next or previous row in a table.
* Added a combo box in add-on settings dialog to set which column should be
  announced when moving through columns vertically.
* Moved end of track , intro and microphone alarm controls from add-on
  settings to the new Alarms Center.
* In Alarms Center, end of track and track intro edit fields are always
  shown regardless of state of alarm notification checkboxes.
* Added a command in SPL Assistant to obtain playlist snapshots such as
  number of tracks, longest track, top artists and so on (F8). You can also
  add a custom command for this feature.
* Pressing the custom gesture for playlist snapshots command once will let
  NVDA speak and braile a short snapshot information. Pressing the command
  twice will cause NVDA to open a webpage containing a fuller playlist
  snapshot information. Press escape to close this webpage.
* Removed Track Dial (NVDA's version of enhanced arrow keys), replaced by
  Columns explorer and Column Navigator/table navigation commands). This
  affects Studio and Track Tool.
* After closing Insert Tracks dialog while a library scan is in progress, it
  is no longer required to press SPL Assistant, Shift+R to monitor scan
  progress.
* Improved accuracy of detecting and reporting completion of library scans
  in Studio 5.10 and later. This fixes a problem where library scan monitor
  will end prematurely when there are more tracks to be scanned,
  necessitating restarting library scan monitor.
* Improved library scan status reporting via SPL Controller (Shift+R) by
  announcing scan count if scan is indeed happening.
* In studio Demo, when registration screen appears when starting Studio,
  commands such as remaining time for a track will no longer cause NVDA to
  do nothing, play error tones, or give wrong information. An error message
  will be announced instead. Commands such as these will require Studio's
  main window handle to be present.
* Initial support for StationPlaylist Creator.
* Added a new command in SPL Controller layer to announce Studio status such
  as track playback and microphone status (Q).

## Version 17.03

* NVDA will no longer appear to do anything or play an error tone when
  switching to a time-based broadcast profile.
* ترجمة الإضافة لمزيد من اللغات

## Version 17.01/15.5-LTS

Note: 17.01.1/15.5A-LTS replaces 17.01 due to changes to location of new
add-on files.

* 17.01.1/15.5A-LTS: Changed where updates are downloaded from for long-term
  support releases. Installing this version is mandatory.
* Improved responsiveness and reliability when using the add-on to switch to
  Studio, either using focus to Studio command from other programs or when
  an encoder is connected and NVDA is told to switch to Studio when this
  happens. If Studio is minimized, Studio window will be shown as
  unavailable. If so, restore Studio window from system tray.
* If editing carts while Cart Explorer is active, it is no longer necessary
  to reenter Cart Explorer to view updated cart assignments when Cart Edit
  mode is turned off. Consequently, Cart Explorer reentry message is no
  longer announced.
* In add-on 15.5-LTS, corrected user interface presentation for SPL add-on
  settings dialog.

## Version 16.12.1

* Corrected user interface presentation for SPL add-on settings dialog.
* ترجمة الإضافة لمزيد من اللغات

## Version 16.12/15.4-LTS

* More work on supporting Studio 5.20, including announcing cart insert mode
  status (if turned on) from SPL Assistant layer (T).
* Cart edit/insert mode toggle is no longer affected by message verbosity
  nor status announcement type settings (this status will always be
  announced via speech and/or braille).
* It is no longer possible to add comments to timed break notes.
* Support for Track Tool 5.20, including fixed an issue where wrong
  information is announced when using Columns Explorer commands to announce
  column information.

## Version 16.11/15.3-LTS

* Initial support for StationPlaylist Studio 5.20, including improved
  responsiveness when obtaining status information such as automation status
  via SPL Assistant layer.
* Fixed issues related to searching for tracks and interacting with them,
  including inability to check or uncheck place marker track or a track
  found via time range finder dialog.
* Column announcement order will no longer revert to default order after
  changing it.
* 16.11: If broadcast profiles have errors, error dialog will no longer fail
  to show up.

## Version 16.10.1/15.2-LTS

* You can now interact with the track that was found via Track Finder
  (Control+NVDA+F) such as checking it for playback.
* ترجمة الإضافة لمزيد من اللغات

## Version 8.0/16.10/15.0-LTS

Version 8.0 (also known as 16.10) supports SPL Studio 5.10 and later, with
15.0-LTS (formerly 7.x) designed to provide some new features from 8.0 for
users using earlier versions of Studio. Unless otherwise noted, entries
below apply to both 8.0 and 7.x. A warning dialog will be shown the first
time you use add-on 8.0 with Studio 5.0x installed, asking you to use 15.x
LTS version.

* Version scheme has changed to reflect release year.month instead of
  major.minor. During transition period (until mid-2017), version 8.0 is
  synonymous with version 16.10, with 7.x LTS being designated 15.0 due to
  incompatible changes.
* Add-on source code is now hosted on GitHub (repository located at
  https://github.com/josephsl/stationPlaylist).
* Added a welcome dialog that launches when Studio starts after installing
  the add-on. A command (Alt+NvDA+F1) has been added to reopen this dialog
  once dismissed.
* Changes to various add-on commands, including removal of status
  announcement toggle (Control+NvDA+1), reassigned end of track alarm to
  Alt+NVDA+1, Cart Explorer toggle is now Alt+NvDA+3, microphone alarm
  dialog is Alt+NVDA+4 and add-on/encoder settings dialog is
  Alt+NvDA+0. This was done to allow Control+NVDA+number row to be assigned
  to Columns Explorer.
* 8.0: Relaxed Columns Explorer restriction in place in 7.x so numbers 1
  through 6 can be configured to announce Studio 5.1x columns.
* 8.0: Track Dial toggle command and the corresponding setting in add-on
  settings are deprecated and will be removed in 9.0. This command will
  remain available in add-on 7.x.
* Added Control+Alt+Home/End to move Column Navigator to first or last
  column in Playlist Viewer.
* You can now add, view, change or delete track comments (notes). Press
  Alt+NVDA+C from a track in the playlist viewer to hear track comments if
  defined, press twice to copy comment to clipboard or three times to open a
  dialog to edit comments.
* Added ability to notify if a track comment exists, as well as a setting in
  add-on settings to control how this should be done.
* Added a setting in add-on settings dialog to let NVDA notify you if you've
  reached top or bottom of playlist viewer.
* When resetting add-on settings, you can now specify what gets reset. By
  default, add-on settings will be reset, with checkboxes for resetting
  instant switch profile, time-based profile, encoder settings and erasing
  track comments added to reset settings dialog.
* In Track Tool, you can obtain information on album and CD code by pressing
  Control+NVDA+9 and Control+NVDA+0, respectively.
* Performance improvements when obtaining column information for the first
  time in Track Tool.
* 8.0: Added a dialog in add-on settings to configure Columns Explorer slots
  for Track Tool.
* You can now configure microphone alarm interval from microphone alarm
  dialog (Alt+NvDA+4).

## Version 7.5/16.09

* NVDA will no longer pop up update progress dialog if add-on update channel
  has just changed.
* NVDA will honor the selected update channel when downloading updates.
* ترجمة الإضافة لمزيد من اللغات

## Version 7.4/16.08

Version 7.4 is also known as 16.08 following the year.month version number
for stable releases.

* It is possible to select add-on update channel from add-on
  settings/advanced options, to be removed later in 2017. For 7.4, available
  channels are beta, stable and long-term.
* Added a setting in add-on settings/Advanced options to configure update
  check interval between 1 and 30 days (default is 7 or weekly checks).
* SPL Controller command and the command to focus to Studio will not be
  available from secure screens.
* New and updated translations and added localized documentation in various
  languages.

## Changes for 7.3

* Slight performance improvements when looking up information such as
  automation via some SPL Assistant commands.
* ترجمة الإضافة لمزيد من اللغات

## Changes for 7.2

* Due to removal of old-style internal configuration format, it is mandatory
  to install add-on 7.2. Once installed, you cannot go back to an earlier
  version of the add-on.
* Added a command in SPL Controller to report listener count (I).
* You can now open SPL add-on settings and encoder settings dialogs by
  pressing Alt+NVDA+0. You can still use Control+NVDA+0 to open these
  dialogs (to be removed in add-on 8.0).
* In Track Tool, you can use Control+Alt+left or right arrow keys to
  navigate between columns.
* Contents of various Studio dialogs such as About dialog in Studio 5.1x are
  now announced.
* In SPL Encoders, NVDA will silence connection tone if auto-connect is
  enabled and then turned off from encoder context menu while the selected
  encoder is connecting.
* ترجمة الإضافة لمزيد من اللغات

## Changes for 7.1

* Fixed erorrs encountered when upgrading from add-on 5.5 and below to 7.0.
* When answering "no" when resetting add-on settings, you'll be returned to
  add-on settings dialog and NVDA will remember instant switch profile
  setting.
* NVDA will ask you to reconfigure stream labels and other encoder options
  if encoder configuration file becomes corrupted.

## Changes for 7.0

* Added add-on update check feature. This can be done manually (SPL
  Assistant, Control+Shift+U) or automatically (configurable via advanced
  options dialog from add-on settings).
* It is no longer required to stay in the playlist viewer window in order to
  invoke most SPL Assistant layer commands or obtain time announcements such
  as remaining time for the track and broadcaster time.
* Changes to SPL Assistant commands, including playlist duration (D),
  reassignment of hour selection duration from Shift+H to Shift+S and
  Shift+H now used to announce duration of remaining tracks for the current
  hour slot, metadata streaming status command reassigned (1 through 4, 0 is
  now Shift+1 through Shift+4, Shift+0).
* It is now possible to invoke track finder via SPL Assistant (F).
* SPL Assistant, numbers 1 through 0 (6 for Studio 5.01 and earlier) can be
  used to announce specific column information. These column slots can be
  changed under Columns Explorer item in add-on settings dialog.
* Fixed numerous errors reported by users when installing add-on 7.0 for the
  first time when no prior version of this add-on was installed.
* Improvements to Track Dial, including improved responsiveness when moving
  through columns and tracking how columns are presented on screen.
* Added ability to press Control+Alt+left or right arrow keys to move
  between track columns.
* It is now possible to use a different screen reader command layout for SPL
  Assistant commands. Go to advanced options dialog from add-on settings to
  configure this option between NVDA, JAWS and Window-Eyes layouts. See the
  SPL Assistant commands above for details.
* NVDA can be configured to switch to a specific broadcast profile at a
  specific day and time. Use the new triggers dialog in add-on settings to
  configure this.
* NVDA will report name of the profile one is switching to via instant
  switch (SPL Assistant, F12) or as a result of time-based profile becoming
  active.
* Moved instant switch toggle (now a checkbox) to the new triggers dialog.
* Entries in profiles combo box in add-on settings dialog now shows profile
  flags such as active, whether it is an instant switch profile and so on.
* If a serious problem with reading broadcast profile files are found, NVDA
  will present an error dialog and reset settings to defaults instead of
  doing nothing or sounding an error tone.
* Settings will be saved to disk if and only if you change settings. This
  prolongs life of SSD's (solid state drives) by preventing unnecessary
  saves to disk if no settings have changed.
* In add-on settings dialog, the controls used to toggle announcement of
  scheduled time, listener count, cart name and track name has been moved to
  a dedicated status announcements dialog (select status announcement button
  to open this dialog).
* Added a new setting in add-on settings dialog to let NVDA play beep for
  different track categories when moving between tracks in playlist viewer.
* Attempting to open metadata configuration option in add-on settings dialog
  while quick metadata streaming dialog is open will no longer cause NVDA to
  do nothing or play an error tone. NvDA will now ask you to close metadata
  streaming dialog before you can open add-on settings.
* When announcing time such as remaining time for the playing track, hours
  are also announced. Consequently, the hour announcement setting is enabled
  by default.
* Pressing SPL Controller, R now causes NVDA to announce remaining time in
  hours, minutes and seconds (minutes and seconds if this is such a case).
* In encoders, pressing Control+NVDA+0 will present encoder settings dialog
  for configuring various options such as stream label, focusing to Studio
  when connected and so on.
* In encoders, it is now possible to turn off connection progress tone
  (configurable from encoder settings dialog).

## Changes for 6.4

* Fixed a major problem when switching back from an instant switch profile
  and the instant switch profile becomes active again, seen after deleting a
  profile that was positioned right before the previously active
  profile. When attempting to delete a profile, a warning dialog will be
  shown if an instant switch profile is active.

## مستجدات الإصدار 6.3

* تحسينات أمنية داخلية
* عند بدأ تشغيل الإصدار 6.3 وما بعده من الإضافة لأول مرة على نظام ويندوز 8
  وما بعده مع NVDA2016.1 وما بعده, ستظهر محاورة تطلب منك تعطيل نمط خفض
  الأصوات الأخرى وذلك بالضغط على NVDA+shift+d ويمكنك تحديد المربع الذي يمنع
  ظهور هذا التنبيه في المرات القادمة.
* إضافة اختصار لإرسال الأخطاء البرمجية, والاقتراحات والاستفسارات الأخرى
  لمطور الإضافة (Control+NVDA+dash (hyphen, "-")).
* ترجمة الإضافة لمزيد من اللغات

## مستجدات الإصدار 6.2

* معالجة مشكلة كانت تحدث مع اختصار بقية قائمة التشغيل (D من مساعد spl (r في
  النمط التوافقي)) حيث كان يتم الإعلان عن مدة الساعة الحالية بدلا من الإعلان
  عن مدة قائمة التشغيل كلها (حيث يمكن تعديل ذلك من الإعدادات المتقدمة
  بمحاورة إعدادات الإضافة).
* يمكن ل NVDA الآن الإعلان عن المسار المشغل حاليا من أي برنامج (يمكن إعداد
  ذلك من إعدادات الإضافة).
* أصبح الإعداد المستخدم في في جعل أمر المتحكم في spl يستدعي مساعد Spl مقدم
  (حيث كان ذلك الإعداد مفعل في كل الأوقات).
* في تشفير sam, سيعمل الاختصاران Control+F9 و Control+F10 الآن بشكل صحيح.
* في التشفيرات, عند تنشيط تشفير معين وكان هذا التشفير معد كي تتم مراقبته في
  الخلفية, فسيبدأ NVDA عملية المراقبة آليا.

## مستجدات الإصدار 6.1

* من الآن ستكون إعدادات بيانات البث وتضمين ترتيب إعلان الأعمدة في أوضاع.
* عند تغير الوضع, سيعلن عن بيانات البث الصحيحة.
* عند فتح محاورة إعدادات بيانات البث السريعة (لم يعين لها مفتاح), سيتم تطبيق
  التعديلاتللوضع النشط.
* عند بدأ تشغيل البرنامج, تغيرت طريقة عرض الأخطاء إذا كان الوضع الذي به خطأ
  هو الوضع العادي.
* عند تغيير اختصارات إعدادات معينة كاختصار الإعلان عن الحالة, تمت معالجة خطأ
  عدم الاحتفاظ بالإعدادات المعدلة عند الانتقال لوضع آخر.
* عند استخدام أي من الأوامر المساعدة ل SPL باختصار مخصص (كاختصار المسار
  التالي), لم يعد يتطلب منك أن تبقى في عارض قائمة التشغيل لاستخدام هذه
  الأوامر (يمكن تنفيذهم من أي مكان من نوافذ أخرى).

## مستجدات الإصدار 5.0

* أوامر جديدة بمساعد spl, وتشمل تلك الأوامر الإعلان عن عنوان المسار المشغل
  حاليا (c), الإعلان عن حالة بث البيانات (e, من 1 إلى 4 و 0) وفتح دليل
  المستخدم على الإنترنت (Shift+F1).
* إمكانية عمل حزمة من الإعدادات المفضلة كملفات شخصية لاستخدامها أثناء العرض
  وللانتقال إلى ملف شخصي لم يعرف من قبل. انظر دليل الإضافة للمزيد من
  التفاصيل عن ملفات النشرات الصوتية.
* إضافة إعداد جديد للتحكم في طول الرسالة (سيتم تقليل بعض الرسائل عند تشغيل
  مستوى متقدم من الإطناب).
* إضافة إعداد جديد للسماح ل NVDA بالإعلان عن الساعات, والدقائق, والثواني
  لأوامر مدة المسار أو قائمة التشغيل (الخصائص المندرجة تحت هذا الإعداد تشمل
  الإعلان عن الوقت المنقضي والوقت المتبقي للمسار المشغل حاليا, وتحليل وقت
  المسار وخصائص أخرى).
* يمكن ل NVDA إخبارك بالوقت الإجمالي لنطاق من المسارات عبر خاصية تحليل وقت
  المسار. اضغط على f9 بمساعد spl لتحديد المسار الحالي كبداية للتحديد, انتقل
  إلى نهاية المسارات المراد وضعها في نطاق ثم اضغط الأمر f10. يمكن إعادة
  تخصيص هذه الأوامر فلا يجب على المستخدم استدعاء نمط مساعد أوامر spl لإجراء
  تحليل وقت المسار.
* إضافة محاورة للبحث عن عمود (لم يتم تعيين أمر له) للبحث عن نص بأعمدة محددة
  مثل المطرب أو جزء من اسم ملف.
* إضافة محاورة جديدة للبحث عن الوقت الإجمالي لنطاق من المسارات (لم يتم تعيين
  أمر له) وهذا الأمر مفيد عندما تريد ملء وقت متبقي بالساعة فستبحث عن مسار
  بمدة الوقت المتبقي.
* إضافة إمكانية إعادة ترتيب الإعلان عن أعمدة المسار وللإيجاز في الإعلان عن
  بعض الأعمدة إذا كان مربع التحديد"استخدام ترتيب الشاشة" غير محدد من محاورة
  إعدادات الإضافة. استخدم محاورة "إدارة الإعلان عن الأعمدة" لإعادة ترتيب
  الأعمدة.
* إضافة محاورة (لم يتم تعيين أمر لها) لتنقل بين تعطيل وتشغيل الإعلان عن حالة
  بث البيانات بسرعة.
* إضافة إعداد لتحديد متى يتم الإعلان عن حالة بث البيانات ولتشغيل الإعلان عن
  حالة بث البيانات.
* إضافة إمكانية تحديد مسار كعلامة مرجعية للعودة إليه فيما بعد (control+k
  بمساعد spl لتحديد المسار كعلامة مرجعية و k بمساعد spl للانتقال إلى المسار
  المحدد).
* تحسين الأداء عند البحث عن مسار تالي أو سابق يحتوي على نص البحث.
* إضافة إعداد للإعلان عن تنشيط الميكروفون ويكون ما بين الصفير أو الرسائل أو
  كلاهما.
* أصبح من الممكن إعداد تنبيه الميكروفون بين 0 (للتعطيل) وساعتين (7200 ثانية)
  واستخدام الأسهم للتنقل بين قيم هذا الإعداد.
* إضافة إعداد لإتاحة إعلان بتنشيط الميكروفون يسمع كل فترة.
* يمكنك الآن استخدام أمر تشغيل وتعطيل إدارة المسارات بنافذة الاستوديو لإدارة
  مسار لم تقم بتعيين أمر لإدارته.
* إضافة إمكانية استخدام نمط أوامر SPL لاستدعاء مساعد SPL (والذي يمكن العثور
  عليه بمحاورة الإعدادات المتقدمة للإضافة بمحاورة إعدادات الإضافة).
* إضافة إمكانية استخدام NVDA لبعض الأوامر التي يستخدمها SPL مع بعض قارآت
  الشاشة الأخرى. لإعداد ذلك, اذهب إلى إعدادات الإضافة, اختر إعدادات متقدمة
  وقم بتحديد نمط التوافق مع قارآت الشاشة.
* في التشفيرات, سيتم تذكر الإعدادات مثل إعداد تنشيط التطبيق عند الاتصال.
* أصبح من الممكن عرض أعمدة متعددة من نافذة التشفير (مثل حالة اتصال التشفير)
  عبر الضغط على Control+NVDa زائد رقم الأمر, عد إلى أوامر التشفير المذكورة
  أعلاه.
* معالجة خطأ برمجي نادر كان يحدث عند الانتقال للتطبيق أو إغلاق إحدى محاورات
  NVDA (مثل محاورات الإضافة) وهو منع أوامر المسارات من العمل بشكل جيد (مثل
  أمر إدارة المسارات).

## مستجدات الإصدار 5.6

* في studio 5.10 وما بعده, لم يعد يعلن NVDA عن رسالة "غير محدد" عند تشغيل
  المسار المحدد.
* نظرا لوجود مشكلة في تطبيق studio نفسه, سيعلن NVDA الآن عن اسم التراك
  المشغل حاليا آليا. تمت إضافة خيار لتعطيل وتشغيل هذا الإعداد بمحاورة
  إعدادات الإضافة.

## مستجدات الإصدار 3.0

* سيتم تذكر إعداد التشغيل بعد الاتصال عند البعد عن نافذة التشفير.

## مستجدات الإصدار 5.4

* إجراء فحص للمكتبة من محاورة إدراج المسارات لم يعد ينتج عنه عدم إعلان NVDA
  عن حالة الفحص أو تشغيل نغمات الخطأ إذا كان NVDA معد للإعلان عن مدى التقدم
  في فحص المكتبة أو عدد الفحص.
* ترجمة الإضافة لمزيد من اللغات

## مستجدات الإصدار 5.3

* توفير حل لمشكلة تشفير SAM (عدم تشغيل المسار التالي إذا كان يوجد مسار مشغل
  بالفعل وعندما يكون التشفير متصل(.
* لم يعد NVDA يصدر صوت الخطأ أو لم يفعل شيء إذا تم ضغط F1 المنوط بتشغيل نمط
  المساعدة ل SPL.

## مستجدات الإصدار 5.2

* لم يعد يسمح NVDA بفتح محاورتي الإعدادات والتنبيهات. ستظهر رسالة تحذيرية
  تخبرك بضرورة إغلاق المحاورة المفتوحة أولا قبل الشروع في فتح محاورة أخرى.
* عند مراقبة تشفير أو أكثر, فإن الضغط على E سيعلن الآن عن عدد التشفير ومعرف
  التشفير واسم ملف التشغيل إن وجد.
* يدعم NVDA كل أوامر الاتصال وقطع الاتصال (Control+F9/Control+F10) بتشفيرات
  سام SAM encoders.
* لم يعد يقوم NVDA بتشغيل المسار التالي إذا كان أحد التشفيرات متصل أثناء
  تشغيل مسار من الاستوديو وأنه تم إخبار الاستوديو بتشغيل مسارات أثناء اتصال
  التشفيرات.
* ترجمة الإضافة لمزيد من اللغات

## مستجدات الإصدار 5.1

* أصبح من الممكن مراجعة الأعمدة الفردية بأداة المسار عبر خاصية إدارة المسار
  (بضغط المفتاح المخصص لهذا الغرض). لاحظ أنه يجب تنشيط الاستوديو قبل الشروع
  في استخدام هذا النمط.
* إضافة مربع تحديد بإعدادات الإضافة للتبديل بين تشغيل وتعطيل الإعلان عن اسم
  التنويه الجاري تشغيله.
* تشغيل أو تعطيل الميكروفون عبر نمط أوامر SPL لم يعد يتسبب في إصدار نغمات
  خطأ أو عدم إصدار صوت تشغيل أو تعطيل الميكروفون.
* إذا تم تخصيص أمر لمساعد نمط أوامر SPL وتم ضغط هذا الأمر مباشرة بعد الدخول
  في نمط المساعدة, فسيخرج NVDA من هذا النمط.

## مستجدات الإصدار 5.0

* إضافة محاورة لإعدادات إضافة SPL, والتي يمكن الوصول إليها من قائمة
  التفضيلات ب NVDA أو بالضغط على Control+NVDA+0 من نافذة التطبيق.
* إضافة إمكانية العودة بكافة الإعدادات للوضع الافتراضي من محاورة الإعدادات.
* إذا وجد خطأ ببعض الإعدادات, فستعود الإعدادات التي بها الخطأ إلى الوضع
  الافتراضي.
* إضافة نمط شاشة لمس لتطبيق SPL وأوامر لمس لأداء مهام مختلفة.
* تعديلات بمساعد نمط أوامر SPL ويشمل ذلك التعديل إضافة أمر للمساعدة (F1)
  وحذف الأوامر المنوطة بتعطيل أو تشغيل الإعلان عن عدد المستمعين (Shift+I)
  والإعلان عن الوقت المجدول (Shift+S). 
* إعادة تسمية "التبديل بين تعطيل وتشغيل الحالة" إلى "الإعلان عن الحالة" حيث
  أن الصفير يستخدم في الإعلان عن معلومات أخرى للحالة كالانتهاء من فحص
  المكتبة.
* الاحتفاظ من الآن بإعداد الإعلان عن الحالة عبر الجلسات. حيث كنت من قبل
  تحتاج إلى تشغيل هذا الإعداد يدويا عند بدأ الاستوديو.
* يمكنك الآن استخدام خاصية إدارة المسارات لمراجعة الأعمدة بمدخل أحد المسارات
  بعارض قائمة التشغيل الرئيسي بالاستوديو (لتعطيل أو تشغيل هذه الخاصية قم
  بالضغط على الاختصار الذي قمت بتعيينه لذلك الأمر).
* يمكنك الآن تخصيص اختصارات للإعلان عن درجة الحرارة أو للإعلان عن عنوان
  المسار التالي إذا كان مجدول.
* إضافة مربع تحديد بمحاورتي نهاية المسار والتنبيه بمقدمة الأغنية لتفعيل أو
  تعطيل هذه التنبيهات (قم بالتحديد للتشغيل). يمكن "إعداد" هذه التنبيهات من
  إعدادات الإضافة.
* معالجة مشكلة فتح محاورة التنبيه أو أمر البحث عن مسار أثناء وجود أي من هذه
  المحاورات مفتوحة والتي كانت تتسبب في ظهور هذه المحاورات أكثر من مرة. الآن
  سيطلب منك إغلاق المحاورة المفتوحة مسبقا أولا.
* تعديلات وإصلاحات بمستكشف التنويهات, استكشاف بنوك تنويهات خاطئة عندما يكون
  المستخدم غير موجود بعارض قائمة التشغيل. من الآن سيعمل مستكشف التنويهات على
  التأكد من أن المستخدم موجود بعارض قائمة التشغيل.
* إضافة إمكانية استخدام نمط أوامر SPL لاستدعاء مساعد SPL (تجريبي, انظر ملف
  المساعدة الخاص بالإضافة لمعرفة كيفية تفعيل هذه الخاصية).
* في نوافذ التشفير, سيعلن أمر الوقتوالتاريخ ب NVDA (افتراضيا nvda+f12) عن
  الوقت بالثواني.
* يمكنك الآن مراقبة التشفيرات الفردية لحالة الاتصال والرسائل الأخرى بالضغط
  على Control+F11 وذلك أثناء تنشيط التشفير الذي تود مراقبته (يعمل أفضفل عند
  استخدام SAM encoders).
* إضافة اختصار بنمط spl controller للإعلان عن حالة مراقبة التشفير (E).
* جاري العمل على معالجة مشكلة نطق NVDA أسماء ملفات تشغيل للتشفير الخطأ,
  وخاصة بعد حذف أحد التشفيرات (لإعادة ترتيب أسماء ملفات التشغيل, اضغط على
  Control+F12, ثم قم باختيار موضع التشفير الذي قمت بحذفه).

## Older releases

Please see changelog link for release notes for old add-on releases.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: http://www.josephsl.net/files/nvdaaddons/getupdate.php?file=spl-lts16

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
