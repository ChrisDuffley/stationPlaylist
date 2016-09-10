# StationPlaylist Studio #

* مطورو الإضافة: Geoff Shang, Joseph Lee وآخرون
* تحميل [الإصدار النهائي][1]
* تحميل [الإصدار التجريبي][2]

تقوم هذه الإضافة البرمجية بتحسين استخدام الكفيف لتطبيق Station Playlist
Studio, فضلا عن إضافة أدوات للتحكم في الأستوديو من أي مكان.

للاطلاع على المزيد حول هذه الإضافة, يرجى قراءة [دليل الإضافات البرمجية][3].

ملحوظة هامة: تتطلب هذه الإضافة NVDA2015.3 وما بعده وإصدار spl 5.00 وما
بعده. إذا قمت بتثبيت nvda2016.1 وما بعده على نظام ويندوز 8 وما بعده, يرجى
تعطيل دعم خفض الأصوات الأخرى.

## مفاتيح الاختصار

* Alt+Shift+T من نافذة الاستوديو: للإعلان عن الوقت المنقضي للمسار أو التراك
  المشغل حاليا.
* Control+Alt+T (مسح بإصبعين لأسفل بنمط SPL) من نافذة الاستوديو: للإعلان عن
  الوقت المتبقي للمسار أو التراك المشغل حاليا.
* NVDA+Shift+F12 (مسح بإصبعين لأعلى بنمط SPL) من نافذة الاستوديو: للإعلان عن
  وقت المذيع.
* Control+NVDA+1 من نافذة الاستوديو: التنقل بين كيفية الإعلان عن الرسائل
  (كرسائل الآلية ورسائل نهاية البحث في المكتبة) بالصفير أو بالكلمات.
* Control+NVDA+2 (مسح بإصبعين يمين بنمط SPL) من نافذة الاستوديو: لفتح محاورة
  نهاية المسار أو التراك.
* Alt+NVDA+2 (مسح بأصبعين يسار بنمطSPL) من نافذة الاستوديو: لفتح محاورة
  إعدادات التنبيه بمقدمة الأغنية.
* Control+NVDA+3 من نافذة الاستوديو: لفتح نمط استكشاف التنويهات والمفاتيح
  المنوطة بكل تنويه أو إعلان
* Control+NVDA+4 من نافذة الاستوديو: لفتح محاورة تنبيه الميكروفون.
* اضغط ctrl+NVDA+F من نافذة الأستديو لفتح محاورة اختيار المسارات بحسب المطرب
  أو الأغنية. اضغط NVDA+f3 للبحث نحو التالي واضغط Shift+NVDA+f3 للبحث نحو
  السابق. 
* Alt+NVDA+R من نافذة الاستوديو: لخطوات إعدادات الإعلان عن البحث في المكتبة
* Control+Shift+X من نافذة الاستوديو: لخطوات إعدادات ميقات البرايل.
* Control+Alt+right/left arrow (while focused on a track): Announce
  next/previous track column.
* Control+NVDA+0 or Alt+NVDA+0 from Studio window: Opens the Studio add-on
  configuration dialog.
* Control+NVDA+- (hyphen) من نافذة الاستوديو: إرسال الاستفسارات لمطور
  الإضافة باستخدام منظم البريد الافتراضي لديك.

## الأوامر غير المعينة

الأوامر التالية لا يتم تعيينها افتراضيا. وإذا أردت تعيينها فعليك الذهاب إلى
محاورة اختصارات NVDA لإضافة الاختصارات المخصصة. 

* التحول إلى نافذة الأستديو من أي برنامج آخر. 
* نمط التحكم في تطبيق SPL. 
* نمط SPL المساعد من الأستوديو. 
* الإعلان عن الوقت متضمن الثواني من SPL Studio.
* التبديل بين تشغيل وتعطيل إدارة المسار (تعمل بشكل جيد عند تنشيط أحد
  المسارات، لتعيين اختصار لهذه الخاصية, اختر مسار, ثم افتح محاورة تخصيص
  اختصارات NVDA).
* الإعلان عن درجة الحرارة
* الإعلان عن عنوان المسار التالي إذا كان مجدول.
* الإعلان عن عنوان المسار المشغل حاليا
* تحديد المسار الحالي لبدأ تحليل وقت المسار
* إجراء تحليل وقت المسار
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
* Control+NVDA+0 or Alt+NVDA+0: Opens encoder settings dialog to configure
  options such as stream label.

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
* s: موعد بداية تشغيل المسار (إذا كان في جدول).
* Shift+S: Time until selected track will play.
* T: تعطيل أو تشغيل نمط تعيين مفاتيح للتنويهات.
* U: وقت الاستوديو
* Control+Shift+U: Check for add-on updates.
* W: حالة التقس ودرجة الحرارة إذا كانت معدة.
* y: حالة قائمة التشغيل المعدلة.
* 1 through 0 (6 for Studio 5.0x): Announce column content for a specified
  column.
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
* اضغط E للحصول على عدد وأسماء التشفيرات الجاري مراقبتها.
* Press I to obtain listener count.
* اضغط f1 لإظهار محاورة مساعدة بقائمة بالأوامر المتاحة.

## تنبيهات المسار

افتراضيا, سيصدر NVDA صوت صفير قرب نهاية المسار بخمس ثواني (النهاية) أو/و
المقدمة. لتغيير هذه القيمة من خمس ثواني أو لتعطيل هذا الإعداد, اضغط على
Control+NVDA+2  أو Alt+NVDA+2 لفتح محاورة نهاية المسار أو نهاية الأغنية على
التوالي. كما يمكنك استخدام إعدادات الإضافة لإعداد ما إذا كنت ستسمع صفير, أم
رسالة أو كلاهما عند تشغيل التنبيهات.

## تنبيه الميكروفون

يمكنك إعداد NVDA كي يصدر صوت عندما يكون الميكروفون مشغل لفترة. اضغط
NVDA+control+4 لإعداد وقت إصدار الصوت بالثوان (الرقم 0 يعطل إصدار الصوت).

## الباحث عن المسارات

إذا أردت البحث عن أغنية باسم المطرب أو باسم الأغنية, من قائمة المسارات, اضغط
Control+NVDA+ F. اكتب اسم المطرب أو اسم الأغنية وسوف يضعك NVDA عندها إن وجدت
أو سيظهر رسالة خطأ إن لم يجد الأغنية التي تبحث عنها. وللبحث عن مطرب أو أغنية
سابقا اضغط NVDA+f3 أو اضغط NVDA+Shift+f3 للبحث في التالي أو السابق. 

ملحوظة: الباحث عن المسارات حساس لحالة الأحرف. 

## مستكشف التنويهات

وفقا لإصدار البرنامج, يتيح لك برنامج SPL تعيين مفتاح ل96 تنويه. يتيح لك NVDA
سماع أي تنويه معين لهذه الأوامر.

لمعرفة المفتاح المنوط بكل تنويه, من نافذة SPL, اضغط Control+NVDA+3. بالضغط
على هذا الاختصار مرة واحدة سيخبرك بالمفتاح المنوط بالتنويه وبالضغط عليه
مرتين سيقوم بتشغيل التنويه. اضغط Control+NvDA+3 للخروج من نمط مستكشف
التنويهات. انظر دليل الإضافة لمعرفة المزيد عن مستكشف التنويهات.

## طلب المسار

You can use arrow keys to review various information about a track. To turn
Track Dial on, while a track is focused in the main playlist viewer, press
the command you assigned for toggling Track Dial. Then use left and right
arrow keys to review information such as artist, duration and so
on. Alternatively, press Control+Alt+left or right arrows to navigate
between columns without invoking Track Dial.

## تحليل وقت المسار

للحصول على مدة المسارات المحددة لتشغيلها, قم بتحديد المسار الحالي لبدأ عملية
تحليل الوقت (من مساعد spl اضغط على f9), ثم اضغط على f10 بعد الانتهاء من
التحديد.

## Columns Explorer

By pressing SPL Assistant, 1 through 0 (6 for Studio 5.01 and earlier), you
can obtain contents of specific columns. By default, these are artist,
title, duration, intro, category and filename (Studio 5.10 adds year, album,
genre and time scheduled). You can configure which columns will be explored
via columns explorer dialog found in add-on settings dialog.

## محاورة الإعدادات

From studio window, you can press Control+NVDA+0 or Alt+NVDA+0 to open the
add-on configuration dialog. Alternatively, go to NVDA's preferences menu
and select SPL Studio Settings item. This dialog is also used to manage
broadcast profiles.

## نمط اللمس لتطبيق SPL

إذا كنت تستخدم الاستوديو من حاسوب بشاشة لمس يعمل بنظام التشغيل ويندوز 8 وما
بعده ولديك NVDA 2012.3 وما بعده, يمكنك أداء بعض الأوامر من شاشة اللمس. أولا
استخدم لمسة ب3 أصابع للانتقال لنمط اللمس, ثم استخدم أوامر اللمس المسرودة
أعلاه لأداء المهام.

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

## مستجدات الإصدار 4.4/3.9

* وظيفة البحث في المكتبة تعمل الآن في الإصدار 5.10 (مطلوب آخر نسخة من
  الإصدار 5.10).

## مستجدات الإصدار 4.3/3.8

* عند الانتقال إلى جزء آخر من التطبيق كالانتقال إلى محاورة إدراج مسارات
  أثناء تنشيط مستكشف التنويهات, فإن NVDA لم يعد يعلن عن رسائل التنويهات عند
  ضغط المفاتيح الخاصة بذلك (على سبيل المثال, تحديد مكان مسار من محاورة إدراج
  المسارات).
* مفاتيح اختصارات مساعدة جديدة, تشمل التنقل بين الإعلان عن الأوقات المجدولة
  وعدد المستمعين (Shift+S و Shift+i بالترتيب, لم يتم حفظها عبر الجلسات).
* عند الخروج من التطبيق أثناء فتح أكثر من محاورة تحذير, فسيعلم NVDA بأنه قد
  تم الخروج من التطبيق ولم يقم بحفظ أية تعديلات على المحاورات التحذيرية
  المفتوحة.
* ترجمة الإضافة لمزيد من اللغات

## مستجدات الإصدار 4.2/3.7

* لم يعد ينسى NVDA الاحتفاظ بتعريفات encoder الجديدة والتي تم تغييرها عندما
  يقوم المستخدم بتسجيل الخروج من ويندوز أو عند إعادة تشغيل الجهاز.
* عند حدوث خلل في ملف إعدادات الإضافة عند بدأ تشغيل NVDA, فسيسترجع NVDA
  الإعدادات الافتراضية وستظهر رسالة تخبر المستخدم بذلك.
* في الإصدار 3.7, تم تصحيح الخطأ الذي كان يحدث عند حزف المسارات بالإصدار
  4.33 من الاستوديو (نفس الإصلاح تم لمستخدمي الإصدار 5.0x بالإصدار 4.1 من
  الإضافة).

## مستجدات الإصدار 4.1

* في استوديو 5.0x, حزف مسار من عارض قائمة التشغيل الرئيسية لم يعد يتسبب في
  إعلان NVDA عن المسار الموجود أسفل المسار الجديد النشط (تلاحظ هذه المشكلة
  بوضوح إذا تم حزف المسار السابق للمسار الأخير حيث كان NVDA يقول في هذه
  الحالة "مجهول").
* معالجة العديد من قضايا البحث في المكتبة في إستوديو 5.10, ومن بين هذه
  القضايا الإعلان عن مجموع العناصر بالمكتبة أثناء التحرك بمفتاح الانتقال
  بمحاورة إدراج المسارات والقول "جاري البحث" عند محاولة ملاحظة البحث في
  المكتبة عبر مساعد SPL 
* عند استخدام سطر إلكتروني مع الإصدار 5.10 من SPL وعندما يكون المسار محدد,
  فإن الضغط على المسافة لتحديد مسار آخر لم يعد يتسبب في عدم انعكاس حالة
  المسار الجديد على السطر الإلكتروني.

## مستجدات الإصدار 4.0/3.6

الإصدار 4.0 من الإضافة يدعم الإصدار SPL Studio 5.00 وما بعدها, مع الإصدار
3.x والذي صمم لتوفير بعض الخصائص الجديدة من إصدار الإضافة 4.0 للمستخدمين
الذين يثبتون إصدار قديم من تطبيق SPL.

* مفاتيح مساعدة جديدة لتطبيق SPL, وقت محدد للمسار (S), الوقت المتبقي لقائمة
  التشغيل (D) ودرجة الحرارة (W إذا كانت ضمن الإعدادات).
* مفاتيح اختصار جديدة بمساعد أوامر SPL, وتشمل شريط التقدم للبحث في المكتبة
  (Shift+R) وتشغيل الميكروفون دون التلاشي (N). 
* عند تشغيل أو تعطيل الميكروفون عبر مساعد أوامر SPL, فسيصدر صوت للتنبيه
  بحالة تعطيل أو تشغيل الميكروفون.
* الإعدادات مثل وقت نهاية المسار سيتم حفظها في ملف إعدادات صنع خصيصا لهذا
  الغرض يوجد بمجلدك الشخصي وستحفظ الإعدادات مع ترقية الإضافة (4.0 وما
  بعدها).
* إضافة مفتاح الاختصار (Alt+NvDA+2 لضبط وقت التنبيه بمقدمة الأغنية وهو ما
  بين 1 إلى 9 ثوان.
* في محاورات نهاية المسار والتنبيه بالمقدمة, يمكنك استخدام السهم الأعلى
  والأسفل لتغيير إعدادات التنبيه. إذا قمت بإدخال قيمة خاطئة, فسيضبط وقت
  التنبيه على أقصى قيمة.
* إضافة الأمر (Control+NVDA+4) لضبط الوقت الذي سيصدر بعده NVDA يخبرك به إن
  الميكروفون مشغل لفترة.
* إضافة خاصية للإعلان عن الوقت بالساعات, والدقائق والثوان (لم يتم توفير
  مفتاح اختصار بعد)
* أصبح بالإمكان تتبع البحث في المكتبة من خلال محاورة إدراج مسار أو من أي
  مكان, مع وضع أمر لخيارات الإعلان عن البحث في المكتبة (Alt+NVDA+R) 
* دعم أداة المسار, ويشمل ذلك إصدار صوت إذا كان للمسار بداية محددة وأوامر
  للإعلان عن المعلومات المتوفرة على المسار مثل الإعلان عن مدة المسار ومكانه
  بقائمة المسارات.
* دعم StationPlaylist Encoder (Studio 5.00 وما بعده), مع توفير نفس الدعم
  الذي نقدمه ل SAM Encoder.
* في نوافذ encoder, لم يعد يصدر NVDA نغمات الخطأ عند إخبار NVDA بالانتقال
  إلى نافذة الستوديو على الاتصال بالخادم أثناء تصغير نافذة الاستوديو.
* لم تعد تسمع أخطاء عند حزف مواد معرفة.
* أصبح بالإمكان مراقبة بداية ونهاية الأغنية بالبرايل وذلك باستخدام خيارات
  ميقات البرايل (Control+Shift+X).
* معالجة مشكلة كانت تحدث عند محاولة الانتقال لنافذة التطبيق من أي برنامج آخر
  بعد تصغير كافة النوافذ مما كان يتسبب في ظهور شيء آخر.
* عند استخدام الإصدار 5.01 من SPL أو ما قبله, فإن NVDA لم يعد يعلن عن بعض
  معلومات الحالة لمرات متعددة, من أمثلة ذلك الوقت المحدد.

## مستجدات الإصدار 3.4

* التعامل بشكل صحيح مع التنويهات التي تم تعيين اختصار لها يشمل مفتاح التحكم
  على سبيل المثال (control+f1) بنمط استكشاف التنويهات.
* معالجة خطأ كان يحدث عند قراءة NVDA معلومات خاطئة عندما كنت تريد الحصول على
  معلومات عن الوقت المتبقي والمنقضي في الإصدار 5.10 من SPL Studio 
* ترجمة الإضافة لمزيد من اللغات

## مستجدات الإصدار 3.0

* في نمط استكشاف التنويهات, التعامل مع الاختصارات التي تشمل مفتاح التحكم
  بشكل صحيح.
* ترجمة الإضافة لمزيد من اللغات

## مستجدات الإصدار 3.3

* لم يعد من الضروري البقاء بنافذة sam encoder حتى إجراء الاتصال بخادم البث
  باستخدام sam encoder.
* معالجة مشكلة عدم عمل بعض اختصارات encoder عند الانتقال لنافذة sam من
  البرامج الأخرى على سبيل المثال (أوامر تعريف البث).

## مستجدات الإصدار 3.2

* إضافة اختصار للإعلان عن الوقت المتبقي من المسار الحالي (r).
* تصحيح رسالة المساعدة التفاعلية لاختصار shift+f11 بنافذة sam encoder.
* إذا تم استخدام الاستوديو القياسي بنمط استكشاف التنويهات, سيقوم NVDA بتنبيه
  المستخدم عن عدم إتاحة مفاتيح صف الأرقام العلوي لتعيين اختصارات للتنويهات.
* في الإصدار 5.10, عدم صدور صوت الخطأ أثناء البحث عن المسارات.
* ترجمة الإضافة لمزيد من اللغات وتحديث الترجمة.

## مستجدات الإصدار 3.1

* في نافذة sam encoder, وضع اختصار (shift+f11) لتشغيل أول مسار بعد الاتصال
  بالخادم.
* معالجة العديد من الأخطاء عند الاتصال بخادم ب sam encoder, ومن بين هذه
  المشكلات عدم القدرة على تنفيذ أوامر NVDA, وصمت NVDA بعد إجراء الاتصال
  بالخادم, إصدار صوت الخطء بدلا من صوت الصفير للإعلان عن إتمام الاتصال.

## مستجدات الإصدار 3.0

* تم إضافة مستكشف التنويهات للتعرف على المفتاح المنوط بتشغيل كل تنويه (يمكن
  تعيين مفاتيح ل96 تنويه).
* تمت إضافة أوامر جديدة, بما في ذلك وقت المذيع (NVDA+Shift+F12) وعدد
  المستمعين (i) وعنوان المسار التالي (n) في وضع مساعد أوامر SPL.
* سيتم الإعلان عن الرسائل ذات الحالتين على السطر الإلكتروني بغض النظر عن وضع
  الإعلان عن تلك الرسائل سواء كان صفير أم نطق.
* عندما تقوم بتصغير نافذة StationPlaylist وتريد الانتقال إلى نافذة البرنامج
  من أي مكان, فإن NVDA سيخبرك بأن النافذة مصغرة.
* لم تعد تسمع صوت الخطأ عندما يكون الإعلان عن الحالة في وضع الصفير وعندما
  تكون رسائل الحالة رسائل أخرى غير تشغيل وتعطيل (مثال: تشغيل التنويهات أو
  الإعلانات).
* لم تعد تسمع صوت الخطأ عند رغبتك في الحصول على معلومات مثل الوقت المتبقي
  أثناء تنشيط نوافذ الاستوديو الأخرى غير نافذة قائمة المسارات (مثل محاورة
  الخيارات). إذا تعذر الحصول على المعلومات المطلوبة, فإن NVDA سيخبرك بهذا.
* أصبح من الممكن البحث عن مسار باسم المطرب حيث كنت في السابق لا تتمكن إلا من
  البحث بعنوان المسار فقط.
* دعم إضافة SAM Encoder الموجودة بتطبيق Winamp, بما في ذلك إمكانية تسمية
  الملف الذي يبث عبر الخادم والتنقل بين تشغيل وتعطيل خاصية الرجوع لنافذة
  الاستوديو بعد الاتصال بالخادم.
* يتوفر ملف المساعدة للإضافة من مدير الإضافات البرمجية.

## مستجدات الإصدار 2.1

* معالجة خطأ كان يحدث عندما يكون المستخدم غير قادر على الحصول على معلومات
  مثل تلك التي تعبر عن حالة الآلية وذلك عند تشغيل SPL Studio لأول مرة أثناء
  تشغيل NVDA.

## مستجدات الإصدار 2.0

* قد تم إلغاء بعض الاختصارات العامة والخاصة بالبرنامج حتى يتسنى للمستخدم
  تخصيص الأوامر من محاورة اختصارات NVDA (يحتاج الإصدار 2.0 من الإضافة
  استخدام إصدار NVDA 2013.3 أو أعلى). 
* إضافة المزيد من مساعد أوامر SPL كالإعلان عن حالة نمط التحرير
* الآن يمكنك التحول إلى SPL أستديو حتى وإن كانت جميع النوافذ مصغرة (قد لا
  يعمل أحيانا). 
* امتداد وقت التحذير بنهاية المسار إلى 59 ثانية
* يمكنك الآن البحث عن مسار في قائمة التشغيل بالضغط على Control+NVDA+F وكل من
  NVDA+f3 أو NVDA+Shift+F3 للتنقل بين المسار التالي أو السابق على التوالي. 
* أصبح NVDA يعلن أسماء مربعات التحرير والسرد الصحيحة (مثل محاورة الخيارات
  وشاشة تنزيل البرنامج الأولى). 
* معالجة خطأ كان يحدث عند قراءة NVDA معلومات خاطئة عندما كنت تريد الحصول على
  معلومات عن الوقت المتبقي في الإصدار الخامس من SPL Studio 

## مستجدات الإصدار 1.2

* عند تثبيت الإصدار 4.x من تطبيق StationPlayList على أنظمة التشغيل 8/8.1 على
  بعض الحواسيب, أصبح من الممكن الاستماع مرة أخرى إلى الوقت المنقضي والوقت
  المتبقي للمسار.
* ترجمة الإضافة لمزيد من اللغات

## مستجدات الإصدار 1.1

* إضافة مفتاح الاختصار (Control+NvDA+2) لوضع صوت تنبيهي لمعرفة نهاية المسار.
* إصلاح خطأ برمجي يتعلق بعدم الإعلان عن بعض أسماء مربعات التحرير (وبخاصة
  حقول التحرير بمحاورة الخيارات).
* ترجمة الإضافة لمزيد من اللغات


## مستجدات الإصدار 1.0

* إصدار أولي

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=spl

[2]: http://addons.nvda-project.org/files/get.php?file=spl-dev [2]: 

[3]: http://addons.nvda-project.org/files/get.php?file=spl-dev [2]: 

