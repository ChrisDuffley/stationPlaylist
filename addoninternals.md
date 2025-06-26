# NVDA Add-on internals: StationPlaylist

Author: Joseph Lee

Based on StationPlaylist Add-on for NVDA 25.07

## 2021 Preface and notes

This guide has gone through many revisions, style changes, and updated to include features in latest add-on releases. When first published in 2015, it was done as a series of blog posts. Now in 2021, edits were made to remove traces of old style and update this guide to reflect add-on features as of 2021 and beyond.

In 2018, the scope of the add-on has expanded to cover StationPlaylist Creator and Track Tool. For the most part, this guide will still cover StationPlaylist Studio alone, but there are important changes made in recent releases that'll ask us to consider other programs in StationPlaylist suite. In particular, trakc item class inheritance hierarchy has changed so many column navigation commands are available when dealing with tracks across SPL apps. As a result, the add-on itself was renamed in 2019 to just "StationPlaylist".

Later in 2018, add-on update feature was removed in favor of Add-on Updater add-on. Although the source code for this feature is gone, information pertaining to it will be documented here for sake of completeness (after all, Add-on Updater's update checking mechanism can trace its roots to Studio add-on).

Then came 2019, and so did Python 3, abstract classes, and new encoder types. The old days of just dealing with SAM and SPL encoders is over, and encoder support has been redesigned from ground up in 2020. Compared to old add-on releases, the scope of SPL Utilities global plugin has been reduced in favor of giving more autonomy to encoder support app modules (mostly SPL Engine). Along with this, the add-on has been updated to be powered strictly by Python 3.

In 2020, the add-on has gone through another major change: removal of unnecessary features and splitting broadcast profiles management from add-on settings dialog. In the old days, add-on settings management was intimately tied to broadcast profiles, and that was the reason why broadcast profiles panel was an integral part of add-on settings dialog. In early 2020, several bugs stemming from design decisions years ago came to light such as applying settings changes to wrong profile. Together with a need to make add-on settings panels independent of each other in order to allow users to open alarms panel from anywhere (described later), it was decided to split broadcast profiles panel into its own dialog.

Another big change in 2020 was removing unnecessary and problematic features. For years, Window-Eyes users were supported by having a dedicated command layout in SPL Assistant layer. As Window-Eyes usage has declined, the dedicated command layout was removed. Another removed feature is time-based (triggered) broadcast profiles as it became clear that defining instant switch profiles were enough, coupled with design problems in the feature itself that showed up in recent years. Just like add-on update feature, time-based profiles feature will be described to provide historical overview.

2021 may turn out to be a turning point for the add-on. I (Joseph Lee) will be stepping down from maintaining this add-on, effective January 1, 2022. My hope is that new maintainers (whoever might be) will step up and improve this add-on greatly.

## 2025 preface and notes

It's been four years since last editing this document. There is now a new maintainer (Chris Duffley), some life changes, and the ad-on source code was edited to take advantage of more recent NVDA features. In particular, since 2025, the add-on internals document is now part of the main Studio add-on repository instead of being a wiki document.

While the add-on source code has gone through major changes and refactoring including adopting Python 3.11 syntax, the overall add-on design remains: one global plugin, multiple app modules, a common services module, with Studio app module at the center. In earlier add-on releases, this design was not enforced often, but with 25.06 and enhanced in 25.07, the global plugin (finally) imports parts of the Studio app module to perform some of its tasks. This and other refactoring work throughout 2025 gave me an opportunity to revise parts of this document to reflect what is happening in 2025, notably no more add-on update feature from this add-on (now done via add-on store).

## Introduction

If you are a radio broadcaster, you might be accustomed to activities involved when producing a show. This may include playlist selection, scheduling break notes, responding to requests, monitoring listener count and encoding status and so on. To assist a broadcaster, a broadcast automation program is used, and one of the popular apps is called StationPlaylist Studio.

In NVDA Add-on Internals: StationPlaylist, we'll learn about what StationPlaylist Studio (and other StationPlaylist (SPL) suite of apps) is and how the NVDA add-on works. You don't have to install or use the NVDA add-on to understand the ins and outs of this powerful add-on (using the add-on might help you better appreciate the defth of this material; for fuller experience, it is handy to have the add-on source code in front of you as you read this document). So let's get started by learning more about SPL suite of applications.

Note: throughout this guide, unless specified otherwise, the terms "StationPlaylist", "SPL", and "Studio" refer to the same thing.

### Introducing StationPlaylist app suite and the NVDA add-on

[StationPlaylist suite](www.stationplaylist.com) is a collection of programs to help broadcasters plan, run, and do related activities around broadcasting. The apps consist of Studio, Creator, Track Tool, Streamer and others.

StationPlaylist Studio is a broadcast automation software that helps broadcasters schedule trakcs, play jingles and more. It includes support for break notes, hourly playlist, track tagging and comes with tools to manage track playback such as setting track intros. In studio 5.00 and later, it includes its own stream encoder.

StationPlaylist Creator and Remote Voice Track (VT) are mostly used for planning a show and designing playlists to be used by Studio. It can be used to define spot groups, custom track categories and more. Whereas Creator is limited to local playlists, Remote VT is used to manage playlists stored on a remote computer.

StationPlaylist Track Tool is mainly used for managing tracks. It is often employed to define introductions, cue points and other properties of tracks.

StationPlaylist Streamer is useful for broadcasting a show with something other than Studio. As such, it comes with support for various encoders and digital signal processing (DSP) modules.

In addition to the components above, StationPlaylist suite includes additional tools such as VT Recorder, and a host of internal support modules such as SPL Engine used for DSP processing and other tasks.

Is Studio suite accessible? Surprisingly, yes. It is possible to use app features without using screen reader scripts and add-ons. However, there are times when a broadcaster would use scripts, such as announcing status changes, monitoring track intros and endings, enhanced support for encoders and so on, and NVDA add-on for StationPlaylist (usually refered to as SPL) accomplishes this well.

### StationPlaylist add-on: a history

In 2011, Geoff Shang, a seasoned blind broadcaster, started working on SPL Studio add-on. This early version (numbered 0.01) was developed to let NVDA announce various status changes such as automation toggle and so on. This initial version, co-developed by James Teh (a former lead developer of NVDA screen reader) was considered a quick project, and further development ceased until 2013.

In 2013, I (Joseph Lee) received several emails regarding NVDA's support for SPL Studio with a request for someone to write an add-on for it. As I was still new to add-on development then (this was after I developed Control Usage Assistant and GoldWave), I decided to take on this challenge in order to learn more Python and to practice what I learned in computer science labs at UC Riverside. I first downloaded the existing add-on (0.01) and installed Studio 5.01 on my computer to learn more about this program and to gather suggestions from SPL users. After little over a month of development and preview releases, I released Studio add-on 1.0 in January 2014.

Most of the early versions (1.x, 2.x, 3.x, released throughout 2014) were mostly quick projects that bridged the gap between NVDA and other screen readers (Brian Hartgen's JAWS scripts were my inspiration and have studied documentation for Jeff Bishop's Window-Eyes scripts). These early versions, supporting Studio 4.33 and later, were also used to fix bugs encountered by Studio users - for instance, a broadcaster posted  a YouTube video explaining how NVDA was not reading edit fields, which was fixed early on. Later releases (4.x, 5.x, 6.x, released throughout 2015), further bridged the gap with other screen readers and introduced unique features (for instance, add-on 5.0 introduced a configuration dialog, and 6.0 introduced concept of a broadcast profile). In late 2016, seeing that some of my add-ons were using year.month scheme for versioning, I decided to switch SPL to follow this model after receiving comments from the NVDA community.

2018 is a memorable year in the ad-on history. Notably, a preliminary add-on update feature became its own add-on, aptly called Add-on Updater. While the add-on update feature was part of another add-on called Windows App Essentials, its potential was realized with StationPlaylist add-on such as choosing different update channels and testing preview features. Besides this change, the add-on went through a major refactor to expand columns explorer (described below) to places other than Studio, and this, together with other code changes, became part of the next LTS release (18.09.x).

But the most significant change happened a year later. Throughout 2019, NV Access and other NVDA contributors (including I) embarked on Python 2 to 3 transition, resulting in NVDA 2019.3 in early 2020. The Python 2 to 3 transition affected this add-on as well, with changes made to features such as metadata streaming, add-on settings, to name a few. Building on top of Python 3 work, 2020 and 2021 saw the implementation of code linting while navigating the worst phases of the COVID-19 pandemic. All this work was also backported to the fourth LTS releases (20.09.x).

Just like 2019, 2023 was another significant year. As I entered a doctoral program, it became clear that I will not be able to maintain the add-on, thus I asked the NVDA add-ons community to maintain this add-on. Thankfully, Chris Duffley, a broadcaster and user of the add-on, agreed to maintain the add-on since March 2023. Chris and I continue to discuss the add-on maintenance, with both of us agreeing to review Python 3.7 to 3.11 transition work in 2024 and working on major refactoring work in 2025. All of these changes will be packaged into the next LTS release (25.06.x), ending more than a decade's long journey on supporting Studio 5.x.

Highlights of past major releases and subsequent maintenance releases include:

* 1.x: Initial release, added end of track alarm and other features.
* 2.x: Track Finder and better routines to recognize Studio versions.
* 3.x: first long-term support (LTS) release, Cart Explorer, support for SAM Encoder and no need to stay on the encoder window during connection attempts. This was the last version to support Studio 4.33.
* 4.x: Library scan, support for SPL encoder and studio 5.10.
* 5.x: Track Dial, dedicated configuration dialog.
* 6.x: Broadcast profiles, metadata streaming, column search and announcement reordering.
* 7.x: second LTS release, add-on updates, time-based profile switching, Track Columns Explorer and others. This is the last version to support Studio 5.01. Renamed to 15.x in late 2016.
* 16.10 (formerly 8.0): Columns explorer for Track Tool, selective data resets.
* 17.04 (formerly 9.0: vertical column navigation, playlist snapshots, support for Studio 5.20.
* 17.08 (10.0: listener request notification, column header announcement suppression. This is the last major version, with subsequent versions using continuous delivery.
* 17.12: end of support for old Windows releases, add-on settings reorganization, extension points.
* 18.06: responding to recent NVDA features, playlist transcripts, wxPython 4 support, partial playlist snapshots, expanding the scope of the add-on.
* 18.09: third LTS release, add-on settings panels, checkable list, wxPython 4.
* 19.01: add-on update feature removed, compatibility flags with future NVDA releases.
* 19.07: renaming the add-on, settings reload/reset.
* 20.02: Python 3, restructured encoders support and new encoders, Creator's Playlist Editor support.
* 20.06: removed Window-Eyes support, time-based broadcast profiles facility removed, support for Remote VT client.
* 20.09: fourth LTS release, pilot features removed, connecting to individual encoders in SPL encoders, background encoder monitor registry.
* 21.01: track property announcement changes, more lint fixes.
* 21.06: compatibility with newer NVDA releases, type annotations and more robust source code. This is the last version with planned new features and bug fixes from me.
* 22.01: control types refactor, internal refinements to configuration management, remove profile caching mechanism as SSD technology has matured. This was the last planned release from me for some time.
* 22.03: feature changes and removals to improve add-on security.
* 23.02: dropped support for Windows 7, 8, 8.1, and unsupported Windows 10 releases. This was the last version actively developed by me (Joseph Lee).
* 23.05: new maintainer (Chris Duffley).
* 24.03: initial support for speech on demand mode, encoder support enhancements.
* 25.01: dropped 32-bit Windows releases support, linter updates, Add-on Updater support removed with the introduction of NV Access add-on store.
* 25.06: fifth LTS release, restored partial support for Windows 8.1 and older Windows 10 releases, code refactoring including Python 3.11 syntax.
* 25.07: major code restructuring with the introduction of SPL common services module (housed along with app modules).

Throughout this document, you'll get a chance to see how the add-on works, design philosophy and how the add-on is being developed, with glimpses into the past and future. My hope is that this add-on internals document would be a valuable reference for users and developers - for users to see the inner workings of this add-on, and for developers to use this add-on as an example of how an add-on is planned, implemented, tested, released and maintained.

To download the add-on, visit NV Access add-on store.

## Design, code layout, layer sets and importance of Studio API and Studio window handle

### Overall design and source code layout

StationPlaylist add-on for NVDA consists of seven app modules (including two app module packages), a common services module (housed along with app modules), and a global plugin. Because Studio and Creator come with Track Tool for managing tracks, the add-on includes an app module for Track Tool in addition to the main app module package for Studio, as well as an app module for StationPlaylist Creator. A fourth app module for Voice Track Recorder is present which is used for event tracking purposes. Remote VT client is the fifth app module and is mainly used to support remote playlist editor. The other two app modules deal with Streamer and SPL DSP Engine, with SPL Engine being an app module package due to inclusion of encoders support module which is also used by Streamer. The seventh module, Streamer, does not exist - it is an alias of SPL Engine app module.

The overall design is that of a partnership between the main Studio app module and the Studio Utilities (SPLUtils) global plugin. Studio app module performs things expected from scripts such as responding to key presses, announcing status information, configuration management and so forth, while the global plugin is responsible for running Studio commands from anywhere, and in older add-on releases, for encoder support (the add-on supports SAM, SPL, and AltaCast encoders). In reality, the global plugin is subordinate to the app module, as the app module controls overall functionality of the add-on and because the global plugin requires Studio to be running to unlock some features (here, unlock means using layer commands and parts of encoder support).

As part of the app modules, a common services module (splcommon) is included to house functions and constants common across the ap modules and the global plugin. Contents include Studio API wrapper, cart key definitions, configuration management, and status messages colection. The common services module resembles Studio app module package in prior add-on releases as majority of its contents indeed come from the Studio app module package, thus the common services serves as an extension of the Studio app module.

When it comes to hierarchy of app modules, Studio app module package is ranked first. This is because Studio app module is the oldest part of the add-on, and it provides base services and blueprints for other app modules. For instance, Creator and Track Tool rely on configuration facility provided by Studio app module package for Columns Explorer (explained later), and Voice Track (VT) Recorder app module cannot function properly without Studio app module running. Even though SPL Engine and Streamer are independent of Studio app module, they still require Studio app module to function (this is especially the case with SPL Engine, as Studio loads splengine.exe, the DSP Engine executable).

In short, all components of StationPlaylist add-on emphasize studio app module - although many components are independent of Studio, they still reference it for various reasons. Thus, Studio serves as the bridge that connects various add-on features together.

The source code consists of:

* appModules: This folder contains the main splstudio (app module) package and the app modules for Track Tool, Creator, VT Recorder, Remote VT client, and SPL DSP Engine app module package to support SPL Engine, Streamer, and encoders. The common services module is also stored in this folder.
* The SPL Studio package consists of various modules, which include __init__ (main app module and track item classes), configuration manager and user interfaces (splconfig and splconfui) and miscellaneous services (splmisc) as well as support modules and various wave files used by the add-on.
* The SPL Engine package consists of main Engine module and encoder support module.
* The SPL common services package includes the add-on base services (splbase) and constants collection (splconsts).
* The Studio main app module file is divided into sections. First, the overlay classes for track items are defined, then comes the app module, further divided into four sections: fundamental methods (constructor, events and others), time commands (end of track, broadcaster time, etc.), other commands (track Finder, cart explorer and others) and SPL Assistant layer. This allows me to identify where a bug is coming from and to add features in appropriate sections.
* globalPlugins: This folder contains SPLUtils module, consisting of main global plugin code and SPL Controller layer.

Note: until 2019, encoder support was part of SPL Utils. In 2020, it is part of SPL DSP Engine app module package.

### Design philosophy

When I set out to write the add-on in 2013, I put forth certain things the add-on should adhere to, including:

* Consistency: The add-on should have a consistent interface and command structure. Interface includes various GUI's such as add-on configuration dialog. For layer commands, I tried using native Studio command assignments.
* Extensibility: The add-on should be organized and written in such a way that permits easy extensibility, hence the app module and the global plugin were divided into submodules, with each of them being a specialist of some kind (such as configuration management).
* Separation of concerns: Coupled with extensibility, this allowed me to provide just needed commands at the right time, which resulted in two layer command sets (explained below).
* Easy to follow source code: Although some may say excessive documentation is a noise, I believe it is important for a developer to understand how a function or a module came about. Also, I have used and read user guides for other screen reader scripts to better understand how a feature worked and come up with some enhancements to a point where I found some major bugs with JAWS scripts (one of them, which I hope Brian patched by now is microphone alarm where the alarm would go off despite the fact that microphone was turned off before alarm timeout has expired).
* Unique feature labels: One way to stand out was to give features interesting names. For instance, during add-on 3.0 development, I decided to give cart learn mode a name that better reflects what the feature does: Cart Explorer to explore cart assignments. Same could be set about NVDA's implementation of enhanced arrow keys (called Track Dial, as the feature is similar to flipping a dial on a remote control).
* Extensive collaboration and feedback cycle between users and developers: I believed that the real stars of the show were not the add-on code files, but broadcasters who'll use various add-on features. Because of this, I worked with users early on, and their continued feedback shapes future add-on releases. This collaboration and feedback cycle also helped me (the add-on author) understand how the add-on was used and to plan future features to meet the needs of broadcasters who may use this add-on in various scenarios (a good example is broadcast profiles, as you'll see in add-on configuration section).

### Why two layer sets?

When I first sat down to design the add-on, I knew I had to write both an app module and a global plugin (to perform Studio commands from anywhere), which led to defining two layer command sets for specific purposes:

* SPL Assistant: This layer command set is available in the app module and is intended to obtain status information and to manage app module features. I called this Assistant because this layer serves as an assistant to a broadcaster in reading various status information. More details can be found later in this article.
* SPL Controller: This layer is for the global plugin and performs Studio commands from anywhere. I called this "controller" because it controls various functions of Studio from other programs. More details will be provided below.

In the early days, I enforced this separation, but in add-on 6.0, it is possible to invoke SPL Assistant layer by pressing the command used to invoke SPL Controller. In add-on 7.0, it is possible for SPL Assistant to emulate commands from other screen reader scripts, and the mechanics of it is covered later in this article.

### The "magic" behind layer commands

In order for layer commands to work, I borrowed code from another add-on: Toggle and ToggleX by Tyler Spivey. Toggle/ToggleX allows one to toggle various formatting announcement settings via a layer command set. It works like this:

* Dynamic Command:script binding and removal: It is possible to bind gestures dynamically via bindGesture/bindGestures method for an app module or a global plugin (bindGesture binds a single command to a script, whereas bindGestures binds commands to scripts from a gestures map or another container). To remove gesture map dynamically, the main/layer gestures combo was cleared, then the main gestures were bound.
* Defining extra gesture maps in the app module/global plugin: Normally, an app module or a global plugin that accepts keyboard input uses a single gestures map (called __gestures; a map is another term for dictionaries or associative array where there is a value tied to a key). But in order for layers to work, a second gestures map was provided to store layer commands (command and the bound script of the form "command":"script"). In recent NVDA releases, script decorator is used for main commands while gestures map is used for layer commands.
* Wrapped functions: Tyler used "wraps" decorator from functools to wrap how "finally" function is called from within the layer set (this was needed to remove bindings for layer commands after they are done). Also, a custom implementation of getScript function (app module/global plugin) was used to return either the main script of the layer version depending on context.

A typical layer command execution is as follows:

1. First, assign a command to a layer (entry) command (add-on 2.0 and later; add-on 1.x used NVDA+Grave for SPL Controller and Control+NVDA+Grave for the Assistant layer; removed in 2.0 to prevent conflicts with language-specific gestures).
2. You press the layer entry command. This causes the app module/global plugin to perform the following:
	1. Layer conditions are checked. Until add-on 6.x, the app module wanted to see if you are in the Playlist Viewer (relaxed in add-on 7.0), and for the global plugin, checks if Studio is running.
	2. Sets a flag telling NVDA that the Assistant/Controller layer is active.
	3. Adds gestures for the layer set to the main gestures map via bindGestures function. In case of screen reader emulation in SPL Assistant, the appropriate gestures map is selected.
3. You press a command in the layer set (such as A from Assistant to hear automation status, or press A to turn automation on if using SPL Controller layer). Depending on how the layer script is implemented, it either calls Studio API (for SPL Controller layer and for some Assistant commands) or simulates object navigation to fetch needed information (Assistant layer). In the app module, for performance reasons, the object is cached. More details on mechanics of this procedure in subsequent sections.
4. After the layer command is done, it calls "finish" function (app module/global plugin) to perform clean up actions such as:
	* Clears layer flags.
	* Removes the "current" gestures (main gestures and layer commands) and reassigns it to the main gestures map (this is dynamic binding removal).
	* Performs additional actions depending on context (for example, if Cart Explorer was in use).

### The importance of Studio window handle and Studio API

In order to use services offered by Studio, one has to use Studio API, which in turn requires one to keep an eye on window handle to Studio (in Windows API, a window handle (just called handle) is a reference to something, such as a window, a file, connection routines and so on). This is important if one wishes to perform Studio commands from other programs (Studio uses messages to communicate with the outside program in question via user32.dll's SendMessage function).

Starting from add-on 7.0, one of the activities the app module performs at startup (besides announcing the version of Studio you are using) is to look for the handle to Studio's main window until it is found (this is done via a thread which calls user32.dll's FindWindowW (FindWindowA until late 2018 as explained below) function every second), and once found, the app module caches this information for later use. A similar check is performed by SPL Controller command, as without this, SPL Controller is useless (as noted earlier). Because of the prominence of the Studio API and the window handle, one of the first things I do whenever new versions of Studio is released is to ask for the latest Studio API and modify the app module and/or global plugin accordingly.

#### FindWindowA versus FindWindowW

In the old days of Windows (1990's), programs were not ready to support Unicode when Windows itself did. To support programs that are not Unicode-aware, Microsoft defined two versions of a given Windows API function. For example, there were two versions of FindWindow function, the difference being the final character as follows:

* A: ANSI version meant for legacy programs (e.g. FindWindowA).
* W: Wide char (Unicode) character version (e.g. FindWindowW).

In reality, programs call FindWindow function, and the appropriate "version" was chosen based on overall character representation macro as specified by the program. For example, if the program was unicode-aware, when FindWindow is called, Windows internally calls FindWindowW.

Until 2018, Studio app module and other components of the add-on called FindWindowA due to the fact that, in Python 2, a string is a read-only array of ANSI characters. Python 3 (and if a string is prefixed with "u" in Python 2) uses immutable array of Unicode characters for strings. Internally, NVDA expects Unicode strings for the function that wraps FindWindow function (located in winUser module), thus mimicking Python 3 behavior. StationPlaylist add-on adopted FindWindowW behavior in late 2018, but the wrapper provided by NVDA is not used due to incorrect error checking behavior in NVDA (if window handle is 0 (NULL), success error is raised, which goes against specifications from Windows API; no longer the case in NVDA 2019.3/Python 3).

## Life of the SPL app module

Note: For the rest of this article, you'll see some portions of the source code to let you better understand how something works (mostly pseudo code will be provided). Also, certain things will require explaining how NVDA Core (the screen reader itself) works (so you'll learn several things at once).

### SPL Studio app module and friends: design and code overview

As noted previously, the SPL Studio app module (splstudio/__init__.py) and friends (other app modules) consists of several sections. These include (from top to bottom):

* Imports: Many modules from Python packages and from NVDA screen reader are imported here, including IAccessible controls support, configuration manager and so on.
* Layer command wrapper: I talked about how layer commands work in a previous section, and the "finally" function at the top is the one that makes this possible.
* Few helper functions and checks: This includes a flag specifying minimum version of Studio needed, the cached value for Studio window handle (SPLWin) and place holders for threads such as microphone alarm timer (more on this in threads section). This section also includes helper functions such as "messageSound" (displays a message on a braille display and plays a wave file) and other helper functions.
* Track item overlay classes: three classes are defined for various purposes. The first is a base class that provides commands and services across Studio and other apps, while other two classes provide support for tracks found throughout Studio (one is a general track items class, the other is specific to playlist viewer). We'll come back to these objects later.
* App module class: This is the core of not only the app module, but the entire add-on package. The app module class (appModules.splstudio.AppModule) is further divided into sections as described in add-on design chapter.

For Studio's colleagues (Creator, Track Tool, Remote VT client), they consist of sections listed above except layer command wrapper, and track item classes are simplified. For VT Recorder, because it controls certain internal behaviors of Studio app module when it starts, only the constructor and terminate methods (see below) are provided. For Streamer and DSP Engine, encoder specific workarounds are present.

Let's now tour the lifecycle of the app module object in question: before and during app module initialization, activities performed while the app module is active, death and (until 2018) add-on updates.

Note: although standalone add-on update feature is gone and later became part of the add-on store, the mechanism behind add-on update feature will be documented for sake of completeness.

### Before birth: NVDA's app module import routines

Before we go any further, it is important for you to understand how NVDA loads various app modules. This routine, available from source/appModuleHandler.py (NVDA Core), can be summarized as follows:

1. If a new process (program) runs, NVDA will try to obtain the process ID (PID) for the newly loaded process.
2. Next, NVDA will look for an app module matching the name of the executable for the newly created process. It looks in various places, including source/appModules, userConfigDirectory/appModules and addonname/appModules, then resorting to the default app module if no app module with the given name is found.
3. Next, NVDA will attempt to use Python's built-in __import__ function to load the app module, raising errors if necessary. No errors means the app module is ready for use.
4. Once the newly loaded module is ready, NVDA will instantiate appModule.AppModule class (make it available). If a constructor (__init__ method) is defined, Python (not NVDA) will call the app module constructor (more on this below).

In case the app module's AppModule class has a constructor defined, Python will follow directions specified in the constructor. Just prior to performing app module specific constructor routines, it is important to call the constructor for the default app module first as in the following code:

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

This is a must because the default app module constructor performs important activities, including:

1. The default app module constructor will call another base constructor (this time, it is baseObject.ScriptableObject, containing gestures support among other important properties).
2. Initializes various properties, such as PID (process ID), app module name (if defined), application name and the handle to the app in question via kernel32.dll's OpenProcess function (XP/Server 2003 and Vista/Server 2008 and later requires different arguments).
3. Lastly, the constructor initializes process injection handle and helper binding handle in case such routines are required.

### Birth: app module construction

Certain app module add-ons shipt with an app module with a constructor define, and SPL Studio is one of them; in 2018, constructors were added to Creator and Track Tool for various purposes, and Remote VT client ships with a constructor similar to Creator app module. After calling the base constructor as described above, SPL app module's constructor (__init__ method that runs when the app module starts) does the following:

1. Checks whether a supported version of Studio is running, and if not, raises RuntimeError exception, preventing you from using the app module while an unsupported version of Studio is in use (as of add-on 25.07, you need to use Studio 6.0 and later).
2. Unless silenced by `globalVars.appArgs.minimal` being True, NVDA announces, "Using SPL Studio version 5.01" if Studio 5.01 is in use (of course, NVDA will say 5.10 when Studio 5.10 is in use). This is done via ui.message function (part of NVDA Core) which lets you hear spoken messages or read the message on a braille display. In reality, ui.message function calls two functions serially (one after the other): speech.speakMessage (speaking something via a synthesizer) and braille.handler.message (brailling messages on a braille display if connected).
3. Next, add-on settings and related subsystems are initialized by calling splconfig.initialize(). For add-on 6.x and 7.x, the first four steps are performed by the init (formerly initConfig) function itself, while in 8.0 it is handled by SPLConfig ConfigHub class constructor. Add-on 17.10 changes this significantly, and in 18.07 and later, some steps are skipped if another Studio app is in use (see the next few sections). This is done as follows:
	1. For add-on 6.x and 7.x, loads a predefined configuration file named userConfigPath/splstudio.ini. In add-on 6.0 and later, this is known as "normal profile). In add-on 6.x and 7.x, this is done by calling splconfig.unlockConfig() function that handles configuration validation via ConfigObj and Validator, and in 8.0 and later, this is part of SPLConfig constructor. In add-on 17.10 and later, this step will not take place if NVDA is told to use an in-memory config, and in 18.07 and later, any SPL app module that opens SPLConfig (splconfig.openConfig) will register its app name to indicate which app is starting.
	2. For add-on 6.0 and later, loads broadcast profiles from addonDir/profiles folder. These are .ini files and are processed just like the normal profile except that global settings are pulled in from the normal profile. In add-on 8.0, just like normal profile, this is done when constructing SPLConfig object. In add-on 17.10 and later, if the add-on is told to use normal profile only, this step will not occur.
	3. Each profile is then appended to a record keeper container (splconfig.SPLConfigPool for 6.x and 7.x, splconfig.SPLConfig.profiles in 8.0 and later). Then the active profile is set and splconfig.SPLConfig (user configuration map) is set to the first profile in the configuration pool (normal profile; for add-on 5.x and earlier or if only normal profile is to be used (17.10 and later), there is (or will be) just one profile so append step is skipped).
	4. Between add-on 7.0 and 21.10 (enhanced in 17.10 and relaxed in 20.09), unless in-memory config is requested, Normal profile dictionary (not others) is cached. This is useful in keeping a record of settings loaded from disk versus run-time configuration and is employed when comparing values when saving profiles. See profile caching section in broadcast profiles for details and reasons which is documented for historical reasons.
	5. Starting from add-on 18.08,. if NVDA supports it, SPLConfig will listen to config save action so add-on settings can be saved when config save command (Control+NVDA+C) is invoked. Add-on 19.03 added support for config reload/reset action so add-on settings can be reloaded or reset to defaults if Control+NVDA+R is pressed once or three times, respectively.
	6. If an instant profile is defined (a cached instant profile name is present), the instant profile variable is set accordingly.
	7. If errors were found, NVDA either displays an error dialog (5.x and earlier) or a status dialog (6.0 and later) detailing the error in question and what NVDA has done to faulty profiles. This can range from applying default values to some settings to resetting everything to defaults (the latter will occur if validator reports that all settings in the normal profile are invalid or ConfigObj threw parse errors, commonly seen when file content doesn't make sense).
	8. Between add-on 7.0 and 18.12, add-on update facility is initialized (splupdate.initialize). among other things, the initialization routine loads update check metadata. In 2018, prior to being removed, update initialization was moved to app module constructor. Although no longer included, we'll meet add-on update routines (housed in splstudio/splupdate.py) later in this article to provide context.
	9. In add-on 8.0, track comments are loaded (if any). See track items section for details.
	10. Although not part of the init routine, starting from 17.12, various modules register one or more functions for action notifications. See extension points section for details.
4. Starting with NVDA 2015.3, it became possible for an app module to request NVDA to monitor certain events for certain controls even if the app is not being used. This is done by calling eventHandler.requestEvents function with three arguments: process ID, window class for the control in question and the event to be monitored. For earlier versions of NVDA (checked via built-in hasattr function), this step is skipped, and background status monitor flag is then set accordingly. We'll discuss event handling throughout this article.
5. Next, GUI subsystem is initialized (NVDA uses wxPython). This routine adds an entry in NVDA's preferences menu entitled "SPL Studio Settings", the add-on configuration dialog.
6. As described above, the app module will look for the window handle for the Studio app. In order to avoid this routine consuming resources and making NVDA not responsive, this is done in a separate thread. The thread performs the following:
	1. Studio window handle is searched via a loop. If Studio exits for whatever reason, an event flag is raised by the app module, causing this thread to exit.
	2. If the handle is found, its value is recorded in a flag found in base services module (splbase).
	3. If the app module is told to announce status of metadata streaming and connect to predefined URL's, NVDA will do it at this point provided that Studio's playlist viewer (discussed later) is loaded. In order to announce status messages as the last announcement after connecting to metadata servers, Studio app module places ui.message in the event queue to be handled by NVDA (queueHandler.queueFunction). More on internals of metadata announcement and related components in the SPL Assistant chapter.
7. Between add-on 7.0 and 18.12, if automatic update check is enabled, update check timer is started.

#### Changes introduced in 17.10 due to volatile configuration flags

In add-on 17.10, several internal flags and associated command-line switches are introduced to control how the add-on settings are loaded and treated. Presence of these flags will significantly alter the way settings are loaded and saved. These flags should be used when instructed by the add-on developer, as they are used for troubleshooting or experimenting purposes.

The flags are as follows:

1. Do not save changes to disk (configVolatile/--spl-configvolatile, removed in 20.09): all profiles (including broadcast profiles) will be loaded from disk but changes will not be saved. With this flag turned on, profile caching will not occur if supported, including normal profile.
2. Load normal profile only (normalProfileOnly/--spl-normalprofileonly): broadcast profiles will not be used i.e. cannot create and switch amongst broadcast profiles. Combining this with NVDA setting to not have configuration to disk on exit effectively makes normal profile a read-only config store.
3. Use in-memory config (configInMemory/--spl-configinmemory): only normal profile will be used, but instead of loading settings from disk, an in-memory version with default settings applied will be used (and no profile caching if supported).

Using flags that specify the use of normal profile only will restrict ability to create new broadcast profiles.

#### Changes introduced in 18.07 to handle add-on settings from apps other than Studio

Because Columns Explorer (see the corresponding section below) is used in Studio, Creator, Remote VT, and Track Tool, it became necessary to change how add-on settings are loaded and managed outside of Studio. Instead of splconfig.initialize calling SPLConfig constructor directly, it will call splconfig.openConfig function that will call the constructor (if needed) and add the app name to a list of active SPL components. If this is done with add-on settings already loaded, no construction activity will take place.

In app modules for Creator, Remote VT, and Track Tool, the constructor will call splconfig.openConfig to perform the above activity. When the app module terminates (see below), splconfig.closeConfig will be called to unregister the component that is being terminated, and if no SPL components are active, add-on settings will be gone from memory.

### Life of the app module: events, commands and output

Once the Studio app module is ready, you can then move to Studio window and perform activities such as:

* Press commands, and NVDA will respond by either opening a dialog or speaking what it did.
* Announce status changes such as microphone status. The length and format of these messages (and other add-on messages) are controlled by message verbosity flag (in case verbosity is set to advanced, NVDA will shorten these announcements, which comes from a messages pool). A special case is announcing artist and title of the currently playing track automatically, for which object navigation is employed. This is necessary due to a broken option in Studio itself.
* Find tracks.
* Examine information in columns via Track Dial and/or Columns Explorer (Track Dial was removed in 2017).
* Listen to progress of a library scan in the background.
* Perform SPL Assistant gestures.
* For 6.0 and later, manage broadcast profiles (we'll talk about broadcast profiles in configuration management section).
* For 17.12 and later, respond to actions such as broadcast profile switches.

For Creator, Remote VT, and Track Tool, it will let you review column data, including playlist editor content in Creator and Remote VT.

#### Extension points

Introduced in NVDA 2017.4, an extension point is a notification system from NVDA that tells modules and functions to perform tasks when something happens. For example, the braille subsystem will load a different braille display if different configuration profiles specify this change, or a speech synthesizer can filter certain text from spoken messages before announcing it to users.

There are four extension point types:

* Action: a function can wait for something to happen, such as change of profiles, loading and saving settings and others, and act accordingly once an action takes place.
* Decider: A data processor inside a script or a function can tell NVDA to continue processing data, such as passing a keystroke to remote system. A specialized version, called accumulating decider, is used to let all deciders participate in data processing such as handling command-line switches.
* Filter: a speech processor can add, change, or remove texts before letting synthesizers announce the would-be spoken text.

In SPL add-on, actions are used to notify modules of some action such as when Studio exits, broadcast profile switches and so on. There are two actions defined (in splactions module):

* Broadcast profile switch: notifies microphone alarm thread and metadata streaming configuration to switch streams or turn off the alarm (see below for details).
* Studio exiting: tells add-on dialogs to close without saving settings.

### Death: termination routines

While using the add-on, you can stop using it in various ways, including exiting or restarting NVDA, turning off your computer or logging off or closing Studio or other SPL app. Just like initialization routines, the Studio app module has specific directions to follow when add-on is closed.

Here is a list of steps Studio app module performs when it is about to leave this world:

1. The "terminate" method is called. Just like the startup (constructor) routine, this method first calls the terminate method defined in the default app module, which closes handles and performs other closing routines.
2. Calls splconfig.terminate() function to save add-on settings and perform shutdown routines for some features. This function goes through following steps:
	1. In add-on 7.0, if update check timer is running, the timer is told to stop, and update metadata is copied back to normal profile. This step is gone in 19.01.
	2. Starting with add-on 18.07, active SPL component is unregistered via splconfig.closeConfig function. If there are other components running, the below steps will not occur, otherwise add-on settings will be closed.
	3. Unless disabled through flags in 17.10, profiles are saved (beginning with normal profile) to disk if and only if profile-specific settings were changed (an online cache used for storing profile settings when they are loaded is kept for this purpose). This step will not occur if an in-memory version of normal profile is in use or other SPL components are active. The online profile cache is gone in 21.10.
	4. If there is an instant switch profile defined, this is recorded in the normal profile, otherwise it is removed from the profile database.
	5. Once all profiles are saved, various flags, active profile and config pool is cleared.
	6. For add-on 5.x and earlier, there is only one broadcast profile to worry about, and this profile is saved at this point.
	7. These steps are part of splconfig.SPLConfig.save method in add-on 8.0 and later.
3. In 17.12 and later, NVDA notifies registered handlers for app terminate action. As noted above, this will cause add-on dialogs to close without saving settings.
4. NVDA then attempts to remove StationPlaylist Add-on Settings entry from NVDA's preferences menu, then various maps used by Studio app module (such as Cart Explorer map) are cleared.
5. An important task is cleaning up objects cache used by some SPL Assistant commands, as cached information (specifically, objects) will point to something else next time Studio starts (without restarting NVDA), which is dangerous.
6. As the app module is laid to rest, the window handle value for Studio window is cleared. This is a must, as the handle will be different next time Studio runs. At this point, NVDA removes splstudio (Studio app module) from list of app modules in use.

### Historical: add-on updates: updating to latest and greatest version

Note: this feature, dubbed "standalone add-on update", is gone in 19.01, although the mechanism behind it is documented here for sake of completeness. Standalone add-on update refers to using SPL Assistant to check for updates from Studio. Since 2023, add-on updates are performed by add-on store.

In add-on 7.0 and later (until 18.12), it is possible to update to the latest version of the add-on by using add-on update check facility. This is done by connecting to a server where the update add-on files are stored.

The SPL add-on uses a combination of urllib library and update channels (explained later) to fetch the needed update metadata. The user can tell the add-on to check for updates automatically or one can perform this check manually.

The update check is performed as follows:

1. If the add-on is told to check for updates, the Studio app module constructor will start a timer whose purpose is to call a function when it is time to check for an update.
2. If automatic update check is enabled, the update manager (splconfig.updateInit) will determine when the update was checked last. This is done in order to perform update checks every 24 hours.
3. Once the timer kicks in (automatic update check is on), the update check function (splupdate.updateChecker) will be called. This function uses two parameters to determine if a status progress tone should be played and to schedule the next update check.
4. The update check function first connects to the URL for the current update channel (more on channels at the end of this article) and compares the filename returned by the server. If the file names does not match, the add-on will interpret this as presence of an update and will return a dictionary containing current add-on version, new version (parsed as a regular expression) and URL for the file, and if not, it returns nothing.
5. If a new version is available and if the user said "yes" to update prompt, the update metadata (update timestamp) will be cached to be retrieved by the app module later.
6. This process repeats if automatic check is enabled (a timer will be set to call this function again after 24 hours).

In case of a manual update check (described in SPL Assistant layer section), apart from not using a timer and stopping an update check timer temporarily (if needed), it will go through steps 3 through 5 from above.

## Time announcements, alarms and adjusting basic settings

Now that we know how Studio app module is born and dies, it is time for us to look at what happens while Studio is in use, and we'll start with how the add-on announces time, work with alarms and uses basic settings.

### Time announcement routines: a tale of four brothers

SPL Studio app module for NVDA comes with four time announcement commands. These are elapsed time, remaining time, broadcaster time and complete time including seconds. The first two uses Studio API to obtain needed information, while others use a combination of Python routines and Windows API functions.

Three of these routines are assigned to commands (sometimes termed gestures). These are:

* Control+Alt+T: Remaining time
* Alt+Shift+T: Elapsed time
* NVDA+Shift+F12: Broadcaster time

One can then use Input Gestures dialog (part of NVDA screen reader) to change them or assign a command to complete time routine.

### A step sideways with studioAPI function: A central Studio API handler and dispatcher

Before going any further, it is important to mention a function that not only is used by the first two time routines, but also comes in handy in SPL Assistant and other methods. This function, called studioAPI (defined in splcommon.splbase module), sends messages to Studio window and retrieves the value returned. The signature is:

	studioAPI(arg, command)

With the arguments being the message to be sent to studio window (arg and command). At first glance, it may seem similar to user32's SendMessage function (in fact, that's what the studioAPI function will call), but unlike a typical SendMessage function routine, the Studio handle and message type is automatically filled in, hence only argument (WParem) and command (LParem) are needed.

In older versions of the add-on, studioAPI did more than return results. It called a callback with or without an offset, as well as not return anything. However, the only callback passed in was time announcer (next section), thus in 2018, studioAPI function has been relegated to a thin wrapper around SendMessage function with Studio window handle and message typed filled in.

### First applications of studioAPI function: Announcing elapsed and remaining times

When you press Control+Alt+T or Alt+Shift+T to hear remaining or elapsed time, the script will first check if you are in the main Playlist Viewer, and if so, will call studioAPI function with correct arguments and commands, the result then being fed to announceTime function. In fact, the only differences are argument that is used and the error message.

### Broadcaster time: Simulating Studio's broadcaster clock

When you listen to radio shows, you may hear messages such as, "five minutes to two" or "ten minutes past five". This announcement is called broadcaster time.

Studio does display broadcaster clock. However, because it is in the middle of the screen, one has to use object navigation commands to locate it, and this method was used in older add-on releases. This involved locating the foreground window (api.getForegroundObject()) and navigating through a preset direction to arrive at the clock object, and this is still used in some places. However, this was prone to a critical problem: sometimes, the object we're interested in changed positions (a good example was when different builds of Studio 5.10 were released).

Recently, this method was abandoned in favor of using Python's time module to obtain current time and convert it into a format that is familiar to broadcasters, thus removing the need to use object navigation. When you press NVDA+Shift+F12, NVDA first fetches local time (time.localtime), then converts this into a format suitable for output. Along the way NVDA tries to emulate how Studio displays broadcaster clock. Recently, a slight modification was made so this process can be used to obtain time left to top of the hour when NVDA+Shift+F12 is pressed twice, with the difference being subtracting local time from top of the next hour. When processing is complete for both cases, NVDA announces the output text.

### Complete time: Windows API to the rescue

Here, complete time refers to time including seconds. Normally, when you press NVDA+F12, NVDA excludes seconds when announcing time. All that is needed to announce seconds is to change the format argument for kernel32.dll's GetTimeFormatEx (formerly GetTimeFormat) function. With this change, NVDA can announce time including seconds, but in order to use it, you need to assign a command to this feature (some app module commands are not assigned by default).

### Setting alarms

Studio app module comes with three alarms: song outro (ending), intro/ramp,  and microphone active alarm. Because we need to talk about some important things when talking about microphone alarm, we'll just tour the routine used when setting up the intro and outro alarms.

Prior to 2020, separate dialogs were used to configure song outro and intro alarm settings. In 2020, these have been combined into one command that opens Alarms category in SPL add-on settings. The mechanism behind the former method is documented for completeness.

The following two controls are used to configure song outro and intro settings from Alarms settings (Alt+NVDA+1):

* Alarm setting: a spin box (a sping control) is used to adjust alarm values. You can type the alarm value or use up or down arrow to change the value. If an incorrect value is entered, the maximum value (59 for end of track, 9 for song intro) will be used.
* Notification check box: This sets whether alarm will play or not.

We'll learn how the alarm values are stored and retrieved in the configuration management section, and you'll get to meet how intro and outro alarms work in the next chapter.

#### Alarms Center

Prior to introduction of Alarms category in SPL add-on settings, separate dialogs were used to configure various alarm settings. In reality, it was really one dialog class called Alarms Center that presented different settings based on an internal flag.

True to its name and function, Alarms Center not only housed end of track and track intro alarms, it included microphone alarm controls, and all that was needed to change its appearance was a single integer that specified which portion of the dialog was shown. In case of Alarms Center dialog presented from an older version of add-on settings (see a later chapter on add-on configuration), all alarm controls were shown (level = 0), with different levels controlling what controls were shown as follows:

* 0: Alarms Center, displays all controls.
* 1: End of track alarm.
* 2: Track intro alarm.
* 3: Microphone alarm controls.

Alarms Center was removed in 2020 in favor of standardizing around alarm settings category.

### Toggle settings

StationPlaylist add-on comes with some toggle settings that affect the operation of the app module. These include library scan announcement (Alt+NVDA+R) and braille timer (Control+Shift+X). For each setting script, NVDA will first check the current value, change the value and announce the new value.

## Event handling: announcing status changes, activating alarms and more

When you are producing a live show, it is important for your screen reader to announce various status changes and happenings such as number of listeners, outro notification, playback status, alerting you of listener requests and so on. NVDA is an expert when it comes to handling status changes, activating alarms and more. In this section, we'll learn the magic behind this expertise: handling events.

### NVDA is event-driven

Windows applications (especially those using Windows API) are event-driven programs. Somewhere in the application is an event loop that responds to various events, such as when a check box is clicked, computer is shutting down and so on. NVDA, being a Windows screen reader, does use events for various purposes, ranging from announcing new chat notification in Skype to ignoring it completely.

To handle various events, NVDA uses an event queue (queue handler) and an event handler for event processing. When an event is fired by itself or from other programs, NVDA first checks if the given event is worthy of its attention. Then it performs actions associated with the event, such as announcing changes to a control (name, value, etc.), playing beeps and sounds (progress bar updates) and so on. For add-ons (mostly global plugins and app modules), NVDA is eager to listen to certain events and let controls fire events.

Typically, an event handling routine is declared like this:

	event_eventname(module, object in question, next handler)

For example, for Studio app module, one event handler declared is gain focus (you have moved to a different control), and is written as follows:

	event_gainFocus(self, obj, nextHandler)

The routine is just like any other function (callable) except that the routine called nextHandler function at the end to allow other controls to respond to events.

### What does events have to do with Studio app module?

Events and event handlers are crucial to the operation of the Studio app module, described as "heartbeat" of the add-on. Events and their handlers are used to perform bulk of the work required to allow the app module to function. These include:

* Announcing status changes such as when microphone is turned on or off.
* Alarm notification, such as when end of intro is approaching.
* Activating certain announcement and background tasks such as activating microphone alarm, announcing library scan progress and more.
* Perform workarounds for issues such as focus problems when deleting a track.

Of all the event handlers declared, the most important one is name change event. It is declared as follows:

	event_nameChange(self, obj, nextHandler)

When this event is fired by Studio, NVDA performs following operations:

1. Various checks are performed. These include, but are not limited to:
	1. Make sure there is something to announce.
	2. If using another app, NVDA will ensure that background monitor flag is set (see the discussion on app module constructor in previous sections for more details).
	3. If the status to be announced is a common one such as listener count, schedule and cart playback status, NVDA will check if it is permited to announce them.
2. Depending on the type of control (mostly window class name), NVDA performs different operations (see below).
3. Lastly, NVDA calls nextHandler() to let other controls respond to name change event.

### Status announcements versus alarm notification

There are two groups of controls NVDA is interested in: status bar and status text with window class name of TStatusBar and TStaticText, respectively (Studio is a Delphi application). Depending on which control fired the event, NVDA will respond differently.

For status announcements (TStatusBar), NVDA:

1. Checks IAccessible child ID (position of the control relative to the parent control as exposed by MSAA (Microsoft Active Accessibility)/IAccessible).
2. If IAccessible child ID is 1, it either announces library scan progress or playback status.
3. For other status bar objects (controls or windows), NVDA first checks if it is a toggle change (ends with "On" or "Off"), and if so, it does the following:
	1. If you set status announcement to words, NVDA announces toggle change notification via speech.
	2. If status announcement is set to beeps, an appropriate wave file is selected for playback via NVWave module (nvwave.playWaveFile; this is done via messageSound function).
	3. Braille output is not affected - it'll announce toggle changes.
	4. For cart edit mode or microphone toggle, extra steps are performed, (by calling extraAction method with the status string as the argument) such as activating microphone alarm or announcing that you are using Cart Explorer (if this is the case). We'll come back to how this works in future installments.
4. For all other announcements, NVDA announces them. In case of schedule announcement, to prevent itself from repeating the same message, NVDA checks if a cached name is the same as the just changed name.

For static text controls (mostly used for alarm notifications):

1. Checks whether NVDA is looking at remaining time for the intro or the whole track.
2. For both cases, NVDA checks if it can braille this (braille timer is not off).
3. If NVDA is told to play or announce alarms (for outro and intro), NVDA plays appropriate tones (middle A (440 hertz) for outro, an octave above middle C (512 hertz) for intro), or if told to do so, warns you that end of track or intro is approaching (add-on 6.0 and later).

The structure of event_nameChange function defined in the Studio app module is such that it can be extended to handle name change event for other controls (it is a tree structure, with the root being the event and two subtrees, one for the status bar and another for static text). Just like other add-ons that define event handling routines, name change event calls nextHandler().

### Other events defined in the Studio app module

There are five more events defined in the Studio app module. They are:

* Gain focus: performs focus-related routines such as checking if you are in Insert Tracks dialog in order to turn off background library scanning (more on background library scan in a future installment).
* App module gain focus: Used to handle touchscreens (yes, Studio app module has a dedicated SPL touch mode) such as assigning additional commands.
* App module lose focus: opposite of the event above.
* Show: this event is specifically designed to respond to listener requests, discussed below.
* Foreground: this is used to coordinate status bar content announcement when Studio starts.

#### Listener requests

A seldom talked about component of StationPlaylist Studio is the ability to host a website with a PHP script to allow listeners to request tracks to be played by a broadcaster. When a request is made, Studio pops up a listener request dialog that lists requested tracks.

Due to limitations of old NVDA releases, Studio app module did not have an easy way to detect the appearance of this dialog and notify you of listener requests. This is no longer the case, as NVDA allows show events to be registered for background event tracking. However, because anything can fire show events, tracking show events is not recommended. Knowing this, the Studio app module keeps an eye on show events for one and only one window: listener requests, represented by window class name of TRequests, with the only job assigned for this event handler being playing a sound when requests arrive provided that the requests pop-up option is set in Studio.

So far, we have covered things that the app module performs wherever you are in Studio. the next few sections will cover how the app module handles specific situations, such as working with items in the playlist viewer, finding tracks, library scans and so on.

## Track items, overlay classes and Track Finder

While using the add-on, you may have noticed that you can perform certain commands while focused on track items, and that the command to find tracks is same as that of find command in web browsers. If you are curious about these, then this section will let you see how it works. But first, we need to go over some more facts about NVDA screen reader, this time we'll talk about objects.

### Important facts about NVDA's use of objects

One of the questions I and other add-on authors and NVDA developers received was, "what exactly are objects and how are they used in NVDA?" In programming, an object is instance of the object definition coming to life (this definition, called a "class", defines how certain things behave and how information can be retrieved from this object by other parts of the program; the programming paradigm that uses classes and related concepts is termed "object-oriented programming"). For example, someone may say, "build me a phone book", and a programmer will think about how phone book entries are stored and come up with a "phone book" (an array of phone entries), all done via objects.

In graphical user interfaces (GUI's), an object is a more technical term for controls (sometimes called widgets). This includes windows, form fields, links, documents and so on. A control (object) can convey information such as state of the control, location, color and so on (the control contains both visible and internal attributes that can be used by other programs).

In NVDA world, all screen elements (controls) are objects. As such, when dealing with objects, NVDA uses accessibility API's to obtain needed information. To provide a consistent user experience, differences between accessibility API's (IAccessible, UI Automation, Java Access Bridge and so on) are abstracted and provides a mechanism to announce same information across controls implemented using different frameworks. For example, when a check box is checked, NVDA will say "checked"" - NVDA will know if you checked this box because the underlying accessibility API informs NVDA of this change, and the same information is spoken regardless of whether it is dealing with IAccessible, UIA and so on.

Currently, NVDA can work with IAccessible, User Interface Automation (UIA), Java Access Bridge (JAB) and others (WAI ARIA is supported). Support modules for these API's lives in source/NVDAObjects directory of the NVDA Core source code.

### Overlay classes: Customizing built-in objects

If NVDA was limited to using its own object handlers, we would be limited to information that is correctly exposed by accessibility API's (no app modules at all). But why is that NVDA can announce extra information for some controls and comes with various app modules for different applications? This is done through overlay classes - custom objects and their handlers built on top of API classes (built-in objects).

In essence, overlay classes are subclasses of stable API classes (subclasses are specialist classes deriving (inheriting) from one or more parent classes). This allows custom (overlay) objects to provide extra properties, ranging from control-specific commands to removing certain properties. For example, here's how NVDA's way of announcing toast notifications (Windows 8.x and 10) works:

1. Toasts are notifications from apps, and they are UIA objects (NVDAObjects.UIA.Toast).
2. When events fired by toasts are received by NVDA, it'll check to make sure it is dealing with toast notifications.
3. When NVDA is dealing with toasts, it'll perform what it is told to do by toast objects (announce toasts provided by "report help balloons" is checked from Object Presentation dialog).

### Why do objects and overlay classes matter in Studio app module?

Some readers might ask this question after reading the above section on overlay classes. I had to introduce overlay classes because they are important in Studio app module: track items in playlist Viewer are overlay classes. In fact, there are at least three of them: an abstract base class representing track items for studio and other apps (appModules.splstudio.SPLTrackItem), a generic representation of Studio track item (appModules.splstudio.SPLStudioTrackItem), and a playlist viewer (main window) track item (appModules.splstudio.StudioPlaylistViewerItem; in case of playlist viewer item class, it derives its power from track item class for Studio, which in turn is powered by abstract SPL track item powered by IAccessible).

These classes were born when I started working on Studio 5.10 support in 2014. Because Studio 5.10 uses a different way of showing track properties, I had to come up with a way to take care of them. Adding to the urgency was the fact that Studio 5.10 uses check marks to indicate whether a track is selected for playback (Studio 5.0x and earlier uses check boxes), and when check marks are checked in Studio 5.10, NVDA would not announce newly checked state, fixed by defining a routine to be used when SPACE is pressed (via an overlay class). In addition, initial version of Track Finder (see below) was sensitive to object description changes, I modified it to account for differences between Studio versions.

Then in 2015, when I was designing Track Dial (next section), I thought about scope of this feature. I thought, "if I let this be invoked from everywhere, it could lead to issues such as errors and attempting to use Track Dial from somewhere other than track items". Then I thought, "perhaps I should limit this feature to main playlist viewer at the cost of making sure I identify track items correctly". Given that I had experience with overlay classes and since there was already an overlay class for Studio 5.10 track items, I decided to go with the latter option, which led to defining a new overlay class for Studio 5.0x track items and letting 5.10 track items inherit from this new class.

In 2018, as support for Columns Explorer was being worked on for Creator and Track Tool, I decided to overhaul the entire track item class hierarchy. Since track items would use same column navigation routines, it was decided to split SPL 5.0x track item class into two classes: the old track item class, and a new abstract class providing basic services for Studio, Creator and Track Tool track items. Also, in order to support column reordering, SysListView32 class was employed, as it provides a handy routine to retrieve column content for the correct column when columns were rearranged on screen.

In 2020, SPL track item overlay classes were reworked. Because base SPL track item class was meant to serve as a blueprint, it became an abstract base class in 2019. What was formerly Studio 5.10 track item class became a specialist class for playlist viewer items, and old Studio 5.0x item class was revived to represent track items found in other parts of Studio such as Insert Tracks dialog. At the same time, column navigation services provided by the SPL track item base class was eliminated in favor of using facilities provided by SysListView32 list item class to provide consistency with NVDA itself and to add column navigation commands for Creator's playlist editor and Remote VT client (prior to this, SPL track item base provided customized column navigation commands). Later, track name and description routines were revised to use SysListView32 routines (see the section on custom column announcement order), which resolved a long-standing problem where track information would not be announced unless "report object descriptions" setting was enabled from NVDA.

### Track items overview

Each track item in Studio (including playlist viewer), and in extension, tracks found in Creator, Track Tool, and Remote VT client, consists of a row of columns (6 for Studio 5.0x and earlier, 18 for playlist viewer in Studio 5.10 and later, may vary on other track lists). As far as NVDA is concerned, it is an overlay class that provides a number of services, including:

* Routines for navigating and announcing various columns (most were eliminated in favor of using SysListView32 list item routines directly in 2020).
* Announcing columns in specific order (see the next chapter on importance of column navigation).
* For Studio, obtaining track comments if defined (see track comments section below).
* For studio 5.10 and later, a routine to handle when check marks are checked (when you check a track by pressing SPACE, NVDA will announce the newly checked state and will update the braille display accordingly).

We'll come back to track items when talking about columns later. For now, let's move onto two related features in Studio app module that works with track items: Track Finder and track comments. There is a second feature that deals with Track Finder, and we'll meet this feature in the next section.

### Track Finder: Locating tracks given a search string

Track Finder allows you to search for tracks with the given artist or song title. This is done by performing a "linear search" - examining one track item to the next until the search term is found. This feature was partly inspired by similar features in other screen readers and NVDA's own find facility (cursorManager.FindDialog and its friends).

Track finder is not limited to searching for artist or title: a variation of this dialog (called Column Search) allows you to search for text in specific columns such as duration, file name and so on. Another variation of this dialog, called Time Range Finder (which is a separate dialog of its own (splmisc.SPLTimeRangeDialog) but modeled after Track Finder) uses Studio API to locate tracks with duration between minimum and maximum specified by a user.

In reality, Track Finder and Column Search are a single dialog (splmisc.SPLFindDialog) that presents two dialogs (does this sound familiar?). For now, we'll talk about how the original Track Finder (add-on 2.x to 5.x) works (stay tuned for the next section to learn more about Column Search and the complete refactoring of track finder and its applications).

#### Original track Finder: commands, routines and controls

To use Track Finder, press Control+NVDA+F (wait, I saw this command before). For anyone who are accustomed to NVDA's browse mode, this command would be familiar: find text in webpages. This command performs activities similar to alarm dialogs (see sections above): after conditions are checked (making sure you are in playlist viewer and you have added at least one track) and setting required flags, NVDA opens Track Finder dialog where you can enter a search term and press ENTER. NVDA will call track finder function (trackFinder) to locate the track with the given search term, and depending on search results, NVDA will move focus to the track or open a dialog saying results were not found.

Two other commands are used as part of Track Finder: Find next and previous, assigned to NVDA+F3 and NVDA+Shift+F3, respectively (they also come from browse mode). When these commands are invoked, it'll check if you have searched for a term before, and if not, it'll open Track Finder dialog. If you have searched for a term before, NVDA will perform linear search with search direction specified (trackFinder method in the app module takes various parameters, and one of them is search direction).

#### Track Finder 1.0 versus 2.0

In add-on version 2.0 to 5.x, when told to find tracks, NVDA will look for search term in track descriptions (in case you are searching for artist in Studio 5.0x, NVDA will also check the name of the check box, as this holds artist name). Although this was simple to implement, it had some issues:

1. Because of track item changes in Studio 5.10, I had to spend some time adjusting the track finder formula.
2. When finding a track in a playlist with hundreds of tracks loaded, finding a track at the end of the playlist took several seconds, and this wasn't acceptable to users.

In add-on 6.0, thanks to column search, Track Finder's performance was improved. Also, track finder was split into two functions: trackFinder still manages moving focus or showing the error dialog, while the linear search now lives in a private function. This design allows track finder routine to be used by more than one feature (in this case, place marker feature uses this, as you'll see in the next section.

For both versions, the signature of trackFinder method (linear search routine in 1.0, search results manager in 2.0) in the Studio app module is:

	trackFinder(self, text, obj, directionForward=True, column=None)

Text is the search term, obj is where the search should begin, direction specifies search direction and column is used if Column Search is used (searching for text in specific columns). In Track Finder 2.0 (add-on 6.0), add an "s" to column keyword, and since 2021, columns argument expects a list of column position integers.

## Method resolution  order and importance of column navigation in track items, Track Tool and other features

In the previous section, you saw how overlay classes work, as well as how track items in Studio are defined and used. We'll continue our tour of track items by looking at column navigation feature and how it is used in various places. But before we get into that, we need to talk about how NVDA knows how certain commands apply in specific situations via method resolution order.

### Method resolution order: locating commands and defining command scope

If multiple classes (objects) are defined, especially if inheritance is involved, it becomes hard to determine which method is which and where various methods are defined. This becomes complicated when two or more classes inherit from a single parent, or multiple inheritance is in use (Python supports both scenarios).

One way Python solves this is through Method Resolution Order (MRO). Simply put, when a method is to be used, it first looks at whether this method is defined in the object it is dealing with, and if not, will consult the parent of this object.

For example, suppose we have a list box that defines a scroll method, and a custom list box widget inherits from this list box (in effect, custom list box is a list box). To make matters slightly complicated, let's say the scroll method is not defined (not really defined) in the custom list box. Then when the user scrolls through the custom list box, Python will see that the custom list box does not have the scroll method, so it'll look at the parent (original list box) and use its scroll method (in this case, yes, Python will use the parent's scroll method).

In terms of NVDA, method resolution order comes in handy when dealing with overlay classes. This has wide ranging consequences, including ability to limit where certain commands can be used to not defining a command (setting the script bound to gesture to None), effectively forcing NVDA to look up a given gesture from the base class (parent). If NVDA cannot locate the command in question, it'll pass this to Windows, which then sends the command to the active program.

### Finishing the puzzle: MRO and Studio's track items

As described in the previous section, Studio app module defines three classes for track items: abstract base class for tracks found in Studio and other apps, a class representing track items found throughout Studio, and another for representing playlist viewer track items. In reality, all that matters is the first two, with the playlist viewer item class providing custom routines on top of the Studio track item class. In case of MRO, playlist viewer item class will be consulted if playlist viewer is in use, otherwise main Studio track item class will be consulted, which in turn will consult SPL track item base class. Other apps such as Track Tool and Remote VT client have their own MRO, ultimately consulting SPL track item base class defined in Studio app module.

The most important job of appModules.splstudio.SPLTrackItem class is announcing column data. Prior to 2020, it also housed column navigation commands and routines such as next and previous column, handler for Track Dial (historical), and a dedicated routine to announce column information given column number and optional header. In 2020, only Columns Explorer remains.

On top of the base SPL track item class is general Studio track item class, which does nothing, as it is meant to represent tracks in places such as Insert Tracks dialog. However the class that represents playlist viewer items (appModules.splstudio.StudioPlaylistViewerItem) adds routines and scripts for use from playlist viewer. These include:

* reportFocus: This is called when reporting track items to you (broadcaster). It's main job is to see if custom column order is defined (see below) and builds needed pieces if column order is specified. Later in 2020, column order handling was moved to track name getter.
* Track comments: Routines related to working with comments for traks (see the previous section for details).
* Announcing toggle state of tracks when Space is pressed.
* Toggling column announcement inclusion and order between screen order and custom order (see column announcement order section for details).

### Birth of Track Dial: from hesitation to possibilities

Note: Information on Track Dial is kept for reference purposes. Track Dial was removed in 2017 with the release of add-on 17.04.

As I was writing the add-on, one of the top suggestions I received was ability to use enhanced arrow keys feature to review columns. This feature allows broadcasters using screen reader scripts to use arrow keys to review column information such as artist, duration and so on. As of time of this writing, all three screen reader scripts support this feature.

At first, I told broadcasters that this wasn't possible. My impression back then (summer 2014) was that I had to manipulate track description text (obj.description) to enable this possibility. But seeing how other screen readers implement this convinced me that it might be possible to implement this for NVDA users, thus I started researching this in fall 2014.

I started by looking for patterns in description text that could be used to give users an impression that column navigation was active (when it was not). I studied how Python handles regular expressions and manipulated substrings (str.find and slicing) with no satisfactory results. Then in 2015, while working on improving support for Studio's own stream encoder, I noticed that the encoder entries were SysListView32 objects (NVDAObjects.IAccessible.SysListView32). Careful study of this object, especially a method to retrieve column content, gave me an idea as to how to bring Track Dial to life.

### The magic behind Track Dial: SysListView32 controls

SysListView32 controls are lists with items organized into columns. For example, certain apps use these controls to arrange entries into columns, such as in certain table-based apps, and in case of studio, displaying various status about encoders.

When these controls are encountered, NVDA allows you to use table navigation commands (Control+Alt+arrows) to navigate between columns, provided that there are child objects (columns) exposed by the accessibility API implementation in use. Table navigation commands are supplied by another class (behaviors.RowWithFakeNavigation; the behaviors mix-in includes things NVDA should perform in various scenarios, including terminal input and output, editable text handling (via a dedicated module) and so on). This is all possible thanks to a method in SysListView32 class (NVDA Core) that allows one to retrieve column text, and this became the engine for Track Dial, Columns Explorer and other column navigation facilities in this add-on (I say "add-on" because column navigation is used by both Studio and Track Tool). This was further solidified in 2018 and later when all track item classes (including Creator track items and SAM encoder entries) were repowered by SysListView32.ListItem class.

Until 2018, the column text retrieval routine (which lives in SysListView32 and a copy lives in splstudio.splmisc module) was as follows:

1. Features requiring text from a specific column will call a private function in splstudio.splmisc module, which will take the current object and the column index as parameters.
2. The column retriever first looks up the handle for the process where the control lives, then creates a place holder for the buffer to hold the column content.
3. Next, it looks at the size of the underlying sysListView32 control (ctypes.sizeof) and asks Windows to allocate storage for an internal SysListView32 control via kernel32.dll's VirtualAllocEx. This is needed to store the resulting column text. Same is done for another place holder to store the actual column text by calling VirtualAllocEx.
4. The retriever then creates an internal SysListView32 control used as a place holder to store column text, then asks Windows to tell the process where the column text lives to reveal the column text for the specified column (first calls WriteProcessMemory, sens a message via user32.dll's SendMessage to retrieve text length, then uses ReadProcessMemory to retrieve the actual column text if there is something to read). Once the column text is revealed, the retriever stores the text inside the text buffer (ctypes.create_unicode_buffer, allocated to store the resulting text).
5. Lastly, the retriever frees resources (VirtualFreeEx) and returns the just retrieved column text, which can be used by routines requesting this.

In 2018, this was simplified by use of SysListView32 routines directly. In 2020, almost the entire table navigation routines are performed by the base SysListView32 item class (the only exception being row navigation in playlist viewer).

### Column retrieval and navigation routines: from hesitation to a cornerstone

Column content retrieval routine has become one of the cornerstones of this add-on. In addition to Track Dial, ten other routines rely on it: Column Search, track place marker, column announcement order, Track Columns Explorer, vertical column navigation, playlist snapshots, playlist transcripts, Creator and Track Tool app modules, playlist editor found in Creator and Remote VT client, and when working with SAM encoder entries. Let's find out how seven of these work in more detail (playlist snapshots and transcripts are described under SPL Assistant section, as they deserve sections of their own).

#### Historical: track Dial: Navigating columns in track items

Note: no longer applicable since 17.04, included here for completeness.

The column retriever routine is just one of the activities performed during Track Dial, and to see the beauty of this feature, assign a command to toggle Track Dial (you need to focus on the track item before opening Input Gestures dialog, as Track Dial is used by track items alone). Once you assign a command to toggle Track Dial and toggle this on, Studio will set a flag indicating that Track Dial is on, which causes left and right arrow keys to be assigned to column navigation commands (this flag is stored as part of the add-on configuration database). If you tell NVDA to play beeps for status announcements (see previous chapter), NVDA will play a high beep. Once you are done with Track Dial, press the just assigned command to turn off Track Dial, at which point left and right arrow keys return to their original functions, a low beep will be heard (if told to do so) and Track Dial flag will be cleared.

When navigating columns, NVDA will check if you are at the edge of the track row, and if so, it will play a beep and repeat the last column text. If not, NVDA will look at the column you wish to navigate to (stored in the app module), then it'll call the column text retriever to retrieve the column text.

To handle differences between Studio 5.0x and 5.1x, each track item class informs NVDA as to how leftmost column should be handled. For Studio 5.0x, leftmost column is artist field (obj.name will be checked), while track checked status is "shown" in Studio 5.10 (obj.name will be announced).

#### Custom column announcement order: What to announce and how

Track Dial routine also allowed another top request to come to life: column announcement order. This allows you (broadcaster) to hear columns in specific order and to exclude certain columns from being announced.

Until 2020, custom column announcement order handler resided in reportFocus method in the main track item class. In late 2020, this was split into a custom track name getter, as track name announcement was revised to use SysListView32 routines directly (prior to this, track item class relied on default IAccessible implementation).

In order to use this, you must tell NVDA to not use screen order (add-on settings dialog's column announcement panel, or in 21.01 and later, press NVDA+V while focused on playlist viewer item to toggle this). Then from the same settings panel (column announcement), check the columns you wish to hear and/or use the columns list to set column announcement order. The column announcement order is a list box with two buttons: move up and down.

Once column order and included columns are defined, NVDA will use this information to build track property text. Prior to 2021, this was track description, later shifting to building track name text. This is done by repeatedly calling the column retriever routine for columns you wish to hear, then using the column order you defined to build parts of the property text (a combination of a list and str.join is used).

For example, if NVDA is told to announce title and artist (in that specific order), NVDA will first locate title, then will add artist information. This is then presented as, "Title: some title, Artist: some artist".

It is also possible to suppress announcement of column headers. Until 2020, add-on settings shipped with a dedicated checkbox to toggle header announcement. From 2021 onwards, NVDA's table row/column header setting is used to set column header announcement for Studio track columns.

##### Track name versus description?

Until 2020, because Studio's track item class relied mostly on default IAccessible implementation, track description recorded trakc properties. For this reason, whenever custom column order or inclusion were defined, reportFocus method would construct a custom track description text based on the custom column order. This changed in add-on 20.11 when SysListView32 routines took a greater role in defining track items, and since NVDA builds custom text for item names based on column information, Studio's track item class will also construct custom item name based on custom column order and inclusion if defined. Because of this, from late 2020, column builder was split into a different method, namely a custom item name getter which is the method used by NVDA to retrieve name text for a control.

#### Track Columns Explorer: Retrieve information from specific columns

In add-on 7.0, it became possible to let NVDA announce information from specific columns. This is done by letting NVDA assign SPL Assistant, 1 through 0 (6 for Studio 5.0x) to a function to obtain information from specific column (slot); add-on 8.0 changed these commands to use Control+NVDA+number row, and SPL Assistant, number row commands were removed in 2020. This is called Track Columns Explorer (usually termed Coloumns Explorer).

In addition to using column retriever routine in Track Dial, Columns Explorer needs to know Studio version in use, as Studio 5.1x shows columns not found in Studio 5.0x (this is checked when entering SPL Assistant as discussed later). In addition, since not all track items expose more than ten columns or column slots cannot be configured for some items (notably Creator's Playlist Editor), Columns Explorer needs to know how many columns can be retrieved and take action if no column slot can be defined.

Once column slots are defined (for items allowing configuring column slots, which are Studio's Playlist Viewer, Track Tool, Creator's main tracks list, and playlist editor in Creator and Remote VT, Columns Explorer performs the following:

1. Checks if you are indeed focused on a track item, and if not, it'll say "not a track". With the removal of SPL Assistant, number row commands in 2020, this is no longer checked as track items themselves will define Columns Explorer commands.
2. Consults a list of column slots and locates corresponding column index for the slot in question.
3. Uses column retriever routine to announce column header and content for the selected column slot.

##### Optimization bonus: I've rearranged columns in studio 5.10...

Due to a different control data structure in use, one can rearrange columns in Studio 5.10 and later. But how does NVDA know exactly which column is which? This is thanks to the fact that internal column position doesn't change. When you rearrange columns, you are changing the way columns are presented on screen. When column retriever function (described above) is invoked, Studio returns column content for a column index regardless of where this column is located on screen. Not only this makes Columns Explorer simpler to implement, it allows Track Dial to track (after manual intervention) column presentation changes on screen.

##### What about items where column slots cannot be configured?

For items other than Studio's Playlist Viewer, Track Tool, Creator's main tracks list, and playlist editor in Creator and Remote VT, Columns Explorer slots cannot be configured (hence absence of "exploreColumns" property, notably in Studio's insert tracks dialog). If so, Columns Explorer will resort to displaying data for columns shown in display order (as it appears on screen). As a bonus, if a track item does not show more than ten columns, Columns Explorer will announce an error message if current column position is out of bounds (beyond column count for the track item). These were done in order to support older Playlist Editor properly as track items in there only shows eight columns.

#### Column Search: Finding text in specific columns

In the previous section, I mentioned that a single dialog performs double duty when talking about Track Finder. We'll now tour the other side of the coin: Column Search.

Column Search dialog adds a second control to Track Finder: a list of columns. Once text is entered to be searched in a column, NVDA will use trackFinder routine (discussed earlier) to locate text in specific columns (I mentioned that trackFinder routine takes column(s) as the argument, and this is where this argument comes in handy). In fact, both regular Track Finder and Column Search uses the above column retriever routine to locate column text (the private linear search function introduced in Track Finder 2.0 locates text from specified columns, and for regular track finder, artist and title columns are examined). Just like the regular Track Finder, once search is done, it'll either move you to a track item or present an error dialog.

So what causes one dialog to present both Track Finder and Column Search dialog? It's all thanks to the arguments passed into the find dialog constructor. The signature is:

	splmisc.SPLFindDialog(parent, obj, text, title, columnSearch=False)

The last argument (columnSearch) determines which version of the dialog to present. The object (obj) is needed to tell NVDA where to begin the search and to call the track finder routine defined in the object's app module.

#### Track Place Marker: A variation of column search for finding filenames

Another feature that uses column routines is track place marker. You would drop a place marker at the current track (SPL Assistant, Control+K), move around the playlist, then move to the track with the marker set on it (SPL Assistant, K).

Once you drop a place marker, Studio app module will record the filename of the currently focused track, and when you wish to move to the marked track, NVDA will use column search routine to locate it. Unlike a typical column search, NVDA will call the private linear search routine directly and will select the column where filename is stored (in effect, you are asking NVDA to do a column search after choosing filename as the data you are looking for).

#### Vertical column navigation: just announce the column I want

Ever since implementing Track Dial, some broadcasters requested adding support for moving through tracks vertically (as in reading specific columns just like moving to a different row in a table). This also resolved an issue where pressing Control+Alt+up/down arrow keys caused the monitor to flip upside down. This is achieved by asking SPLTrackItem.reportFocus to announce just the column the user wants when Control+Alt+up/down arrow is pressed, all controlled by a hidden class variable. This feature not only works for vertical column navigation - it is also used when a broadcaster requests only one column be announced, and the column to be announced can be customized (not to be confused with column announcement order routine discussed above).

Vertical column navigation was simplified in 2020 by using routines found in SysListView32 list item class directly. Prior to 2020, custom vertical navigation routines were used, and for places other than playlist viewer, vertical column navigation was impossible. In 2020, vertical column navigation routines from SysListView32 are used, which also introduced vertical navigation to places such as Track Tool.

-#### Expanding columns explorer: one routine, multiple app modules

Column retriever routine is not only employed by Studio app module, but is also used in Track Tool, Creator, and Remote VT app modules (part of the add-on). These app modules (specifically, track item classes) uses column retriever for reviewing column data via table navigation commands and announcing column information (Control+NVDA+1  through 0, now termed Columns Explorer for Track Tool/SPL Creator/playlist editor).

#### Playlist editor: column navigation keeps expanding

Creator comes with Playlist Editor, a tool to manage locally generated playlists. Remote VT client also comes with a dedicated playlist editor but is designed to edit playlists stored remotely. Track items shown on the playlist editor window are indeed SPL track items, and as such they support column navigation and Columns Explorer. Prior to Creator and Remote VT 5.50, there is no custom Columns Explorer because these tracks only show up to 8 columns. With 5.50 and later, more columns are shown, allowing expansion of Columns Explorer to cover playlist editor.

### Few remarks

Of all the features in the StationPlaylist add-on, column navigation is one of my favorites (besides Cart Explorer and encoder support and others). I enjoyed working with this routine and learned a few things about Windows API, as well as open possibilities not previously explorered before, such as Track Tool and Column Search. I hope that you'll find column navigation commands to be useful in your broadcasts.

I would like to take this time to answer a question posed by some users and developers: Can NVDA be ported to other operating systems? No. The above column retriever routine is a prime example why this cannot be done easily: different operating systems use different API's, and porting NonVisual Desktop Access to other operating systems will involve significant architectural changes to use the new API's. In case of ReactOS, this isn't possible, as there are no stable foundation from which NVDA screen reader can exercise its full rights: accessibility API's are needed, stable driver development framework is needed, ability to run a program as a service must be ready and so on. Add to the fact that we have several add-ons relying on Windows API (including this add-on) and you'll see the huge work involved in an attempt to port NVDA to other operating systems.

## Microphone alarm and library scan: threads, threads and more threads

Of all the work done on this add-on, one of them stands out the most: background tasks. I spent many hours and months perfecting this concept, read documentation on this feature and learned a lot through this experience. Today, this work is used in various parts of the Studio app module and beyond, and we'll take a look at two most important results of this work: library scan and microphone alarm.

### Brief feature overview

When you are producing a live show, you may forget that your microphone is active. The microphone alarm feature lets NVDA notify you if microphone has been active for a while. This happens even if you are using another program.

Library scan comes in handy when you want to see the progress of a background library scan. Typically, you would initiate library scans from Insert Tracks dialog (press Control+Shift+R). NVDA will then tell you how the scan is going, and if you close Insert Tracks dialog, NVDA will continue to monitor library scans in the background.

But there's more to it than a simple description when it comes to looking at internals of these features. As you'll see, these features use a concept that is gaining traction: running multiple tasks at once, or at least try to emulate it. We'll visit this concept first before returning to our regularly scheduled program of describing the internals of the two features above.

### Recent trends in computing: more and more processors in a single computer

Years ago, people thought a single core CPU was enough to run multiple programs. This involved the processor spending small fraction of a second devoted to each program. Nowadays, it has become common to see desktops, laptops, smartphones and other small devices using at least two cores (termed multi-core; two cores is dubbed "dual core"). As of 2020, many computers use processors with four cores (dubbed "quad core"), while enthusiasts prefer more cores (it is common nowadays to see PC's and servers boasting upwards of ten cores or more).

Despite the fact that many computers come equipped with multi-core processors, not all programs take advantage of this. Python interpreter is one of those programs, and since NVDA is a Python-based screen reader and due to its operational architecture, many of its operations cannot take advantage of multiple processors. Fortunately, Python provides a way to simulate this - run certain tasks in the background, and this is utilized by NVDA and some of its add-ons as you'll see in this section on library scan and microphone alarm.

### A gentle introduction to threads: multiple tasks at once

During normal business hours, a program will run from beginning to end with some interuptions (keyboard input, switching to a different part of the program and so on). However, there are times when the program will need to work with many things simultaneously, such as calculating distance between many points, adding multiple numbers at once, comparing many pairs of strings and so on. Fortunately, a mechanism called threads allow a program to do multiple things simultaneously.

A thread is a procedure independent of other tasks. If one thread is busy with something, other threads can work on other tasks. The best analogy is multiple bank tellers in a bank: customers can talk to different tellers, with one teller working on updating customer records for a customer while another customer discusses fraudulent credit card charges with a different teller.

A thread can be involved with parts of a task, devoted to a single task or multiple tasks. For example, an antivirus program could have multiple threads (workers) working independently of each other. One worker can display the overall progress of a scan, while other threads can scan multiple drives at once, with each thread devoted to scanning files and folders on separate drives. In NVDA world, multiple workers are involved to perform various tasks, including making sure NVDA is responsive, handling browse mode in different web browsers and so on.

### Threads: a more geeky introduction

A thread (sometimes termed "thread of execution) is an independent path of execution. A single process (app) can have as many threads as it desires (minimum is one for the main thread). Each thread can be asked to perform certain operations with other threads in parallel, which can range from a single, repetitive task (part of a function) to being responsible for an entire module or a significant part of the program. In case of antivirus example above, each scanner thread is responsible for scanning an entire drive, with each of them reporting its progress to a manager thread which displays overall progress of a virus scan.

Using threads means each thread can execute on a processor core on a multi-core system. Because of this, many people would want many programs to take advantage of this and finish their jobs faster. However, threads introduce disadvantages, namely many days spent designing careful coordination routines between threads, preventing attempts by multiple threads to change a critical value that a manager thread depends on (called race condition) and so forth.

### Python's way of managing threads and the threading module

Python interpreter (and programs which uses them, including NVDA) is not exactly multithreaded. Because of internal issues, Python uses so-called global interpreter lock to prevent multiple threads from messing with each other. One way to bring true parallelism in Python is use of multiprocessing module (multiple Python interpreters, each one devoted to a single task), which has its own advantages and drawbacks (NVDA does not ship with multiprocessing module in the first place).

To manage threads, Python programs (including NVDA) use Python's threading module. This library includes various ways of managing threads, including defining which function can execute in a separate thread, coordinating sharing of information between threads (locks, semaphores (resource access counter) and so on), and letting a thread run its task after waiting for a while (called timers). Even with multiple threads defined, NVDA is mostly single-threaded (serial execution).

To use threads, a programmer will define the thread type (regular thread, timer and so on), define some properties and tell the thread which routine to execute. Once the thread is defined, the start (thread.start) method is called to let the thread do its work.

### Threads in Studio app module

For the most part, Studio app module uses only one thread (NVDA's main thread) to do its job. However, there are times when multiple threads are used - up to three can be active at a time: NVDA's main thread (announcing status changes, alarms, Cart Explorer and others), microphone alarm (a timer) and library scan (a background thread). Another situation threads are used is when background encoder monitoring is enabled (see the encoder routines section for details and use of threads there).

The main reason for using threads is to prevent background tasks from blocking user input (commands will not work when a long running task is run from the main NVDA thread). This is more noticeable when library scan is active as you'll find out soon. For now, let's take a look at microphone alarm.

#### Microphone alarm: A timer duo waiting to do their work

Simply put, microphone alarm is a timer (akin to a countdown timer). When the microphone becomes active, Studio app module will tell a timer thread to come alive. This timer's only job is to play the alarm sound and display a warning message, and it will wait a while (microphone alarm value in seconds; for example, five seconds).

The master switch which flips the microphone alarm timer is:

alarm = threading.Timer(micAlarm, messageSound, args=[micAlarmWav, micAlarmMessage])

Where "micAlarm" denotes how long this timer will wait and the second argument is the task to be performed (messageSound function). If microphone alarm is off (value is 0), this switch will be left alone forever (turned off until you enable the alarm by specifying a value above 0).

However, microphone alarm is more than a timer: a unique feature of timers is responding to events (a cancel event, that is). When the microphone becomes active, microphone alarm timer will become active. If you happen to turn off your microphone before microphone alarm kicks in, NVDA instructs microphone alarm to quit (timer is canceled). In other words, the "real" master switch is status change, and one of the activities performed by name change event handler (event_nameChange function described earlier) is to manage microphone alarm timer via doExtraAction method (in fact, microphone alarm and Cart Explorer are managed from this function).

In some cases, NVDA can be told to periodically notify you that microphone is active. If this is the case, NVDA will start a new timer (this time, wx.PyTimer) that'll run a function to do just that periodically after the initial microphone alarm is sounded. Just like the master microphone alarm timer, this time will quit if microphone is turned off.

#### Library scan: a unique combination of Studio API and a background thread

When NVDA is told to keep an eye on background library scanning, it calls up another thread to perform this duty. This thread will ask Studio for number of items scanned so far and take appropriate action after scanning is complete (in fact, multiple helper functions are used).

The library scan routine is performed as follows:

1. NVDA will make sure you are not in Insert Tracks dialog (if you are, background library scan routine will not be invoked, as event_nameChange will perform this duty instead).
2. If you do close Insert Tracks while a scan is in progress, or invoke library scan from SPL Assistant (Shift+R), NVDA will instruct a thread to keep an eye on scan progress in the background(see below for signature) to allow you to use Studio commands and to let you hear scan progress from other programs.
3. Library scan thread will ask Studio to return number of items scanned (this is done every second) and will store the result for record keeping.
4. After the scan result is obtained, the thread will check where you are in studio, and if you are back in Insert Tracks dialog, the thread will terminate (see step 1).
5. Every five seconds, library scan thread will call a private function (which wants to see how many items were scanned and current library scan announcement setting) to announce library scan results as follows:
	* If you tell NVDA to announce scan progress, NVDA will say, "scanning" and/or play a beep (if told to do so).
	* If NVDA is told to announce scan count, number of items scanned so far will be announced (again with or without a beep).
	* This reporter function will not be invoked if you tell NVDA to ignore library scan completely or ask it to interupt you only when the overall scan is complete (you can press Alt+NVDA+R to cycle through different library scan announcement settings).
6. Once library scanning is complete (after checking scan result value every second and seeing that the previous scan result and the current one have same values), NVDA will announce scan results (in some cases, number of items scanned will be announced). In Studio 5.10 and later, the library scan counter will not be defined when scan completes, which is more efficient than keeping track of equalities.

You can imagine what would have happened if the above operation was not a background task: cannot perform other NVDA commands until library scan is complete, cannot cancel this operation and what not. And this is the signature of the thread that performs the above operation:

libraryScanner = threading.Thread(target=self.libraryScanReporter, args=(_SPLWin, countA, countB, parem))

There are important arguments in use: the function (task) to be performed and arguments for this function. The most important argument is the last one: Studio 5.0x and 5.10 expects different arguments when told to report number of items scanned so far.

Despite limitations of Python's threading routines, if used properly, it can open new possibilities, and you saw some of them above: microphone alarm and background library scan. Use of threads in the Studio app module also allows NVDA to be responsive while using Studio and allows background tasks to be faithful to the tasks at hand. We'll come back to threads when we talk about encoder connection routines. There is a more "magical" feature we'll visit, and this is our next stop on the Add-on Internals: Cart Explorer.

## The magic behind Cart Explorer

A live radio broadcast would not be complete without jingles. This can range from station promotions (often called "promos"), advertisements, jingles to convey the mood of a show, segment jingles and more. Many station automation programs, including StationPlaylist Studio includes facilities to manage jingles (sometimes called carts), including defining a cart to be played when cart keys are pressed, announcing the name of the playing cart and saving specific carts to a safe location.

For blind broadcasters, one of the things they worry is pressing a wrong jingle key by accident, thus script writers were asked to implement a way for broadcasters to learn which carts are assigned to cart keys. As of time of this post, all three screen readers (JAWS for Windows (script author: Brian Hartgen), Window-Eyes (script author: Jeff Bishop), NVDA (script author: Joseph Lee (I, the author of this article)) includes a feature to learn jingle assignments. As this is an article on internals of an NVDA add-on, I'll give you an overview of what happens when you activate and explore cart assignments (in fact, this section was the most interesting and feedback driven portion of the add-on). Along the way you'll learn where Cart Explorer (NVDA's version of cart learn mode) draws its power and why it is very important.

### Carts in StationPlaylist Studio

Studio comes in three editions: Demo (same as Pro but for limited time trial), Standard and Pro. The first user visible difference between Standard and Pro is number of cart assignments: Standard can store 48 jingles, while Pro can work with 96 of them.

To play jingles, a broadcaster would use Cart Edit Mode Control+T), then assign a hotkey to a file. For Studio Standard, you can assign F1 through F12 by themselves or in combination with Control, Shift or Alt. In Demo and Pro, number row can be assigned (1 through 9, 0, hyphen (-) and equals (=) either by themselves or in combination with Control, Shift or Alt, for a grand total of 96 jingles). Once jingles are assigned, they will appear under cart menus (there are four cart menus, one for standalone keys (called main) and one each for Control, Shift and Alt).

### Where does Studio store carts?

Studio's "carts" are housed in Studio installation folder. There are four cart files (called banks) in use: a .cart file for each of the cart banks (main, Shift, Control, Alt). During normal business hours, Studio will work with these four banks unless told by a broadcaster to load carts from a different cart bank file.

### Cart Explorer: my own Summer of Code

It was a hot day in June 2014 when I sat down to design a way to let broadcasters learn cart assignments. Since I was developing add-on 3.0 back then, I decided that this feature should be a top priority feature to be included in the upcoming release.

When I started writing this feature, the first thing I thought about was its name. I felt "cart learn mode" didn't really convey the picture - after all, I reasoned that broadcasters will use this feature to explore cart assignments. Thus the name "Cart Explorer" was chosen - in effect, when you use this feature, you are browsing jingle assignments in preparation for a show.

Next, I read JAWS script documentation to get a glimpse of how Brian has managed to implement cart learn mode. In JAWS scripts, script settings are stored in the user configuration directory (typically this is %systemdrive%\Users\%username%\AppData\Roaming\Freedom Scientific\JAWS\%JAWSVersion%\Settings\Enu; Brian, please correct me if I'm wrong). A section of this script configuration file is dedicated to carts, and JAWS scripts use a map of key names and cart values to announce cart information while cart learn mode is active.

Based on this information, I started writing an ini file parser, seeing that broadcasters would store cart assignments in a configuration database. This was prone to a number of errors, including wrong cart name format, nonexistent cart key assignment, invalid configuration format and others. I once wrote a blog post (on my personal blog) explaining how this worked (times have changed, as you'll see very soon).

Then I became curious as to how Studio stores its own cart banks, and naturally, I opened the folder where carts were stored and opened each .cart file in Notepad++ (a very handy text editor). From reading the cart bank format (explained below), I thought it might be useful to write a cart bank file parser. Thus I resumed writing Cart Explorer routines, this time incorporating the cart bank format, not forgetting to handle suttle errors, and this is the routine used in add-on releases up to 5.x (6.0 uses a completely different yet related routine, as you'll see).

While writing the first version of Cart Explorer, I realized that this feature needed some real life testing, so I asked a seasoned blind broadcaster to test this feature. We spent a better part of Independence Day writing, debugging and rewriting this routine until we felt satisfied. In the end, our hard work paid off, as you can see in subsequent paragraphs.

### Introducing Cart Explorer version 1

Cart Explorer version 1, shipped as part of add-on 3.0, worked as follows:

1. You press Control+NVDA+3 to activate Cart Explorer. When this happens, NVDA will make sure you are in main playlist viewer, then it will set a flag indicating that Cart Explorer is active.
2. NVDA will then open and parse cart bank files, storing cart assignments in a dictionary of cart keys to cart names. This parser also takes care of some corner cases, including skipping unassigned carts and determining Studio edition in use. Once carts were parsed, NVDA says, "Entering Cart Explorer", and if errors occur, NVDA will inform you that it cannot enter Cart Explorer (this happens if the cart bank file doesn't exist).
3. While using Cart Explorer, if you press a cart key, NVDA will look up the name of the key in the carts dictionary, and announce the cart name associated with it (if found, otherwise, NVDA says, "cart unassigned").
4. It so happens that some people will activate Cart Edit Mode to modify cart assignments while in the middle of exploring carts. If this happens, NVDA will remind you (via doExtraAction function used by name change event) that Cart Explorer is active, and when Cart Edit Mode is turned off, NVDA will ask you to reenter Cart Explorer (this was done to parse newly updated cart bank files).
5. You press Control+NVDA+3, and NVDA will clear carts dictionary, thereby leaving Cart Explorer.

But there was a major concern with this approach: what if a future version of Studio uses a different cart bank format? Thus, I revisited cart bank files again in July 2015, and this time, I noticed a familiar structure: comma-separated values, and thought about a possibility that a spreadsheet application such as Excel would handle this gracefully. To test my hypothesis, I opened .cart files in Excel, and voila, it presented itself just like any CSV file. Thus I worked on modifying cart parsing routine, this time using Python's CSV module to parse "cart" files (cart bank files are really CSV files in disguise). This new routine (described below) made its appearance as part of add-on 6.0.

### The magic behind Cart Explorer version 2: handling CSV files

Since Python comes with a library to handle CSV files and since cart banks are CSV files, I rewrote Cart Explorer routine (a function in splmisc module which returns the carts dictionary) as follows:

1. When entering Cart Explorer, Cart Explorer preparation routine (splmisc.cartExplorerInit) will take a snapshot of your user name and Studio edition (Studio's title bar indicates which version is in use). Then it initializes the carts dictionary and stores the Studio edition in use.
2. Next, the preparation function will write down names and paths to cart banks. In case a user other than default user is using Studio, it'll modify the cart file names to match the name likely to be used by Studio to present user-specific cart banks. These cart names form one part of the cart bank path (the other part is the path to the folder where the carts live, obtained by using an environment variable).
3. For each cart bank, NVDA will ask Python to parse the cart bank as a CSV file (csv.reader; when finished, it returns a list of lists, with each list representing one row of a CSV table).
4. Once the csv version of the selected cart bank is ready, the row containing cart keys and cart names, together with the cart bank modifier and the carts dictionary are sent to a helper function (part of splmisc module) that will do the following:
	1. Depending on Studio edition, this helper will work with only the first half (Standard will only work with function keys, which are the first twelve columns of this row) or the entire row (the rest are number row keys) will be processed.
	2. Depending on column position (items in the row list), it will see if function keys or number row keys should be assigned to the selected cart entry. This routine also checks the type of the cart bank (modifiers or none (main)) and modifies the cart key name accordingly.
	3. Next, the helper routine will try to locate the name of the jingle assigned to the cart key in question, and if there is one, it'll add the cart key and jingle name pair into the carts dictionary.
5. Back at the cartExplorerInit function, if no erorrs were found while parsing a cart bank, it'll move onto the next one, otherwise it will inform the Studio app module by modifying a flag value in the carts dictionary (stored as an integer, representing number of cart bankks with errors).
6. By now cartExplorerInit is desperate to pass the carts dictionary to someone, and this someone turns out to be the Studio app module - once picked up by the app module, carts dictionary is hired by you to look up cart names for cart keys while you use Cart Explorer (to fire the carts dictionary, simply deactivate Cart Explorer by pressing Control+NVDA+3).

In effect, the routine above (the "magic" behind Cart Explorer) replaced a hand-written cart bank parser and simplified the add-on code (I regret not investigating CSV module in 2014). As far as user experience is concerned, this is same as Cart Explorer 1, with the difference being the parsing routine. With the addition of splmisc.cartExplorerInit, the majority of the splmisc module (miscellaneous services, containing the Track Finder/Column Search combo dialog, column retriever and Cart Explorer preparation tool) was completed. But the innovations continued.

### Enter Cart Explorer version 3: file modification timestamps

There were two issues with Cart Explorer version 2: confusing statements when cart insert mode was active, and inability to detect that cart editing is finished. Cart insert mode allows broadcasters to press the cart command to have the file inserted into the playlist as a regular track. Inability to detect cart edit completion meant one had to reenter Cart Explorer to view updated cart assignments.

The first issue was solved by telling users that Cart Explorer was active while cart insert mode was active. The resolution to the second issue required a bit of work, and involved rewriting parts of Cart Explorer (now version 3), which is included as of add-on 17.01 (optimized in 17.04). The biggest difference is recording file modification timestamps for carts when carts dictionary is being built (see above), and if cart edit is turned off, checking the timestamps of newly modified cart banks against previous timestamps (when cart edit is off, when cart assignments have changed, cart files are written back to disk) and skipping unmodified cart banks. In spring 2017, this was further optimized by allowing carts dictionary to be modified on the fly (only changed bits will be modified, including possible new assignments, changes and deletions). This means no more need to reenter cart Explorer when cart assignments have changed, a huge relief for broadcasters who need to change cart assignments for holidays or other special occasions.

### Few remarks

Cart Explorer has come a long way; from a simple suggestion to the CSV parsing routine above to checking timestamps for cart assignment changes, Cart Explorer has changed to meet the needs of broadcasters using Studio and NVDA. I would like to improve this further in future releases (another suggestion I received was ability to specify cart file names for individual banks, and I'm thinking about implementing this in the near future).

One of the things you may have noticed as you read this article so far is how I and other developers continue to research better ways of accomplishing something. You also saw a glimpse of how developers and users shape a feature and how much work is involved to bring a feature suggestion to life. These activities (research and feature development collaboration) are just two of the pillars of this add-on, and highlights how design philosophy and product development approach affects future course of product development.

This ends our detailed tour of internals of major features in Studio app module. When we come back, we'll visit our friend from the past: SPL Assistant layer and inner workings of various layer commands.

## All about StationPlaylist Assistant layer

You may recall visiting two layer command sets in an earlier section: SPL Controller and SPL Assistant, the former used to perform Studio functions from any program and the latter for status announcements. I mentioned throughout this series that we'll tour these layer sets, and we'll start with SPL Assistant layer.

### Talk about layer commands

One of the common features of Studio scripts for JAWS, Window-Eyes and NVDA is extensive use of layer commands. This was popularized by JAWS and its Studio layer (grave key). Some of the benefits of this approach include saving keyboard commands, reminding users as to commands available in Studio and so on.

### Birth of SPL Assistant layer

As mentioned previously, since version 1.0 in January 2014, StationPlaylist add-on comes with two layer commands to represent the global plugin and the studio app module. In case of Studio app module and its layer set (SPL Assistant), I borrowed some commands from both JAWS and Window-Eyes scripts with some notable differences, namely some commands and how things were announced.

When I sat down to design this layer set, I felt it would be helpful for broadcasters if most of the Assistant layer commands borrowed from Studio command assignments. For example, a broadcaster will press M to toggle microphone on and off, and in SPL Assistant layer, pressing M announces microphone status. Another example was Cart Edit Mode - pressing Control+T in Studio will toggle this, and pressing SPL Assistant, T will announce whether this mode is on or off (the reason for assigning T for Cart Edit Mode status will be discussed later).

Originally, one could invoke SPL Assistant layer by pressing Control+NVDA+grave key from within Studio. However, some NVDA translators told me that this key combination is used for NVDA screen reader commands in their languages. Thus, in add-on 2.0 (late spring 2014), I decided to remove this command, which means in order for you (broadcasters) to invoke SPL Assistant layer, you need to go to Input Gestures dialog while focused in Studio, expand StationPlaylist category and look for the Assistant entry (I personally use Control+NVDA+grave, and in recent add-on development builds, I told the add-on to let SPL Controller layer command (discussed later) to invoke Assistant layer).

Another addition to SPL Assistant layer is ability to emulate layer commands provided by other screen readers. This is achieved by using gestures map for each screen reader (NVDA included), with the correct gestures map chosen when entering SPL Assistant layer. Currently, in addition to default NVDA layout, the add-on includes JAWS for Windows layer commands (Window-Eyes layer was removed in 2020).

### Categorizing SPL Assistant commands

Once you invoke SPL Assistant layer (a beep will be heard), you can perform one of the following operations:

* Status announcements (automation, microphone, etc.).
* Tools (library scan, track time analysis, obtaining playlist snapshots and transcripts and so on).
* Configuration (switching broadcast profiles).
* Ask for help (opening SPL Assistant help document or the online user guide).
* Until 18.12, checking for add-on updates (manually).

For the first two categories, they can be divided further into commands which uses studio API (via studioAPI function discussed in a previous section), ones using Windows API (Columns explorer) and those relying on object navigation (multiple components are involved and is sensitive to user interface changes). We'll go through each of these categories in turn.

#### SPL Assistant 1: status announcements

These commands allow you to obtain various status information such as title and duration of the next track, cart edit mode status and so on. These can be divided into those which uses object navigation (old style) and Studio API (new style) commands. In some cases, both methods are available and the appropriate version is chosen based on Studio version in use.

The following commands (sorted alphabetically) utilize Studio API to perform needed functions:

* E: Announces if any metadata streaming URL's are defined.
* H: Duration of tracks in the selected hour.
* Shift+H: Duration of the remaining tracks in the hour slot.
* P: Playback status.
* Shift+1 through Shift+4 and Shift+0: Checks metadata streaming status for each URL (0 is DSP encoder). See below for details.

Note that playlist remainder announcement (SPL Assistant, D) was part of this category until add-on 6.x. In add-on 7.0, due to refactoring work surrounding this command, it has been moved to tools category.

##### A step sideways: Metadata streaming

Studio can be told to stream track metadata to five URL's: the DSP encoder address and four additional URL's (Options/Now Playing). By default, DSP encoder address is used to send metadata information.

One of the activities Studio app module performs when starting is to check if metadata streaming is enabled on any URL's. In addition, NVDA can tell you status of metadata streaming for all uRL's (SPL Assistant, E) or for individual addresses (SPL Assistant, Shift+1 through Shift+4 and Shift+0). This is done through a metadata management and announcement function (metadataAnnouncer) that gathers streaming flags for URL's and presents status messages and connects to predefined servers if you tell Studio to connect to streaming servers.

When the metadata announcer is called, NVDA does the following:

1. NVDA will look at connection flag (reminder = True, but in reality, this is mostly used as the connection flag), and if the flag is set, connects to a predefined set of streaming URL's.
2. Gathers metadata streaming flags, starting with the DSP encoder.
3. The announcer will count number of metadata enabled URL's used to format the status message.
4. announces the status message. This message isn't announced right away if this function is called when the app module starts - after a short pause, the status message will be announced and an alarm sound will be played. This is done to make sure this message is the last message to be announced when Studio starts.

##### Revisiting the past: object navigation

Before the new style routines were written, all commands used object navigation. Typically, the command will use a helper function and an object map to locate the needed object and will announce what you are looking for (typically obj.name or an error message). The process was as follows:

1. The Studio app module contains a map of indecies where the object lives in relation to the foreground window. For example, for a given object, if index was 0, NVDA nows that the object is the first child of the foreground object. Technically, it is a dictionary of lists, with each list item (indecies) corresponding to the version of Studio the add-on supports.
2. To fetch needed objects and to record the command type, a number of constants are defined in the app module (all integers, denoting what you wish to hear). These constants serve as keys to the object index map.
3. After entering SPL Assistant layer and once you press one of the commands below, NVDA will do the following:
	1. Each command will obtain the object in question by calling object fetcher (status function) with the announcement type as the parameter (status(SPLConstant; for example, for cart edit mode, the signature is self.status(self.SPLPlayStatus), with the constant denoting a status bar).
	2. The object fetcher (status function) will first consult an object cache (part of the Studio app module) hoping that the needed object is ready for use (for performance reasons; this is also performed in Playlist Editor for performance reasons as explained later).
	3. If the object was not cached or the location is invalid (no location information), the fetcher will first write down the foreground window, then use the directions specified in the object index map (the constant passed into the status function is the key to this map and different values are returned based on Studio version) to locate, cache and return the object in question (in that order).
	4. Back at the routine for the command, it is up to the routine as to what to do with it (sometimes, the actual object is a child of the just returned object).

The commands which utilizes object navigation steps above include:

* A. Automation.
* C: Title of the currently playing track.
* I: Listener count (I have tried using Studio API to obtain this information, but after experimenting with it, object navigation routine was more stable).
* L: Line in.
* M: Microphone.
* N: Title and duration for the next track.
* Shift+P: Track pitch.
* R: Record to file.
* S: Track scheduled for.
* Shift+S: Duration of selected tracks in the current hour slot.
* T: Cart Edit Mode (I assigned T to this command for efficiency reasons).
* U: Studio up time.
* W: Weather and temperature (if configured).
* Y: Playlist modification.

Note that in Studio 5.20 and later, some of these (such as automation) uses Studio API.

For example, if you press A to obtain automation status from Studio 5.10:

1. Invoke SPL Assistant, then press A.
2. The status function (object fetcher) is called, taking the status bar constant (SPLPlayStatus, which is 0) as the key to the index map.
3. Object fetcher will see if the status bar object (cache dictionary with the key of 0) has been cached. For this example, it isn't.
4. Seeing that the status bar isn't cached, object fetcher will now look at the index map and will decide which column to read (for this example, it is column 2 (index 1)). The column records the child position of the status bar relative to the foreground window (in our case, index is 6 or the seventh child).
5. Once the child object position index is obtained, object fetcher will locate the actual object and cache it (self._cachedStatusObjs[infoIndex] = fg.children[statusObj]), then returns the object to the automation announcement routine.
6. Back at the script routine, NVDA will be reminded that it needs to look at one of the object's children (status bars can contain child objects if exposed by accessibility API's), then will announce one of it's contents (second child object, which records automation status).

In Studio 5.20 and later:

1. Invoke SPL Assistant, then press A.
2. Calls Studio API to retrieve the given status flag (in this case, 1, which records automation status).
3. A lookup table with possible status bar messages is then consulted, and the appropriate message based on status flag and value is retrieved and announced.

Not all status bar messages will use Studio API and status messages table. The lone exception is cart mode status, which requires consulting two flag values returned by Studio to construct the actual announcement (cart edit mode on/off and whether cart insert mode is active).

##### Another side tour: Playlist Editor and object caching

As noted above, part of object navigation commands in SPL Assistant involve object cache. This is necessary for performance reasons, as retrieving and navigating via objects is slow versus retrieving needed object from a cache, which is faster than manual object retrieval. This technique is frequently labeled "memoization" and is used to improve responsiveness if an important data is present somewhere for fast retrieval.

Similar to SPL Assistant commands involving object navigation, Creator's Playlist Editor's status objects require caching because slowness of object navigation. Without caching, retrieving needed information will take seconds instead of fraction of a second. Just like Studio, cached information is cleared when Creator app module is terminated.

#### SPL Assistant 2: tools

These are miscellaneous commands in SPL Assistant, and three of them use Studio API:

* D: Remaining time for the opened playlist.
* K: Moves to a marked track. This was discussed in column routines and place marker sections.
* Control+K: Sets track place marker. Consult the place marker section to learn how it works.
* Shift+R: Library scan. This is a convenience function to start library scan in the background, useful if you have added new tracks from a number of folders via Studio Options dialog. Consult library scan section for details on library scan internals.
* F8: Obtains playlist snapshot information for the currently loaded track, including track count, shortest and longest tracks and top artists. This feature uses a combination of Windows and Studio API's.
* Shift+F8: requests a playlist transcript (data about loaded playlist). Just like playlist snapshots, it uses a combination of object navigation and Windows API.
* F9: Marks the current position of the playlist as start of track time analysis (more on this feature below).
* F10: Performs track time analysis (add-on 6.0).

##### Track time analysis: Duration of "selected" tracks

During a Skype chat with a number of add-on users in early 2015, someone suggested a feature where NVDA will tell you how long it'll take to play selected tracks. Since I was familiar with this concept from JAWS scripts, I decided to work on it as part of add-on 6.0.

The resulting routine (which is available if you are focused on the main playlist viewer with the playlist loaded) is as follows:

1. Move to the position in a playlist to mark as start of track time analysis.
2. Enter SPL assistant, then press F9.
3. Move to another track in the playlist, open SPL Assistant then press F10. NVDA will then:
	1. Determine analysis range. For most cases, it'll be top to bottom analysis, but in some cases, it could be reverse (bottom to top). Also, a variable to hold total duration will be prepared.
	2. For each track in the analysis range, NVDA will obtain file name and track duration (in reality, segue) via Studio API. Once the track duration is received, it is then added to the total duration variable.
	3. Once time analysis (calculating total duration) is done, NVDA will announce number of tracks selected and the total duration using mm:ss format.

If you are a seasoned NVDA user, you may have noticed a familiar pattern: the command to set a marker to copy review cursor text is NVDA+F9, and you would move to a different location and press NVDA+F10 to copy the selected text to the clipboard. Replacing the NVDA modifier key with SPL Assistant produces the commands above: F9 to mark current position for time analysis, and F10 to perform the actual calculation. I intentionally chose these two function keys to provide consistent experience and to reenforce concepts used in NVDA screen reader: review cursor.

##### Playlist remainder announcement

Until add-on 6.x, playlist remainder announcement was based on Studio API. However, it was found that this "remainder" was actually the remaining time within the selected hour slot. To get around this, in add-on 7.0, this routine was rewritten to take advantage of Track Dial introduced in add-on 5.0 (see Track Dial section above).

Technically, a combination of column content fetching and track navigation routines are used to accomplish this. When SPL Assistant, D is pressed, NVDA will write down the focused track and will move down the playlist (starting from the focused track), recording the segue (total track duration minus crossfade). Once playlist navigation is complete, the total duration is then sent to time announcement routine (see above) for processing (converted to hours, minutes and seconds format).

##### Playlist snapshots and transcripts

Although similar in appearance, playlist snapshots and transcripts are two different things. Both uses a combination of object navigation and Windows API, work by retrieving and analyzing column content for tracks, and involve SPL Assistant followed by F8 with or without modifiers. Whereas a snapshot is used to gather statistics about the loaded playlist, a transcript is the entire playlist formatted in different ways. Also, after invoking SPL Assistant layer, just pressing F8 will launch snapshots, whereas you need to press Shift+F8 to obtain a playlist transcript and choose appropriate action such as transcript range, output format and so on via the dialog that appears afterwards.

A playlist snapshot presents statistics about the currently loaded playlist (or parts of it). Information gathered include how many items (including hour markers) are loaded, longest and shortest tracks, and average track duration. Also, if asked to do so, up to top ten artists, categories, and/or track genres are recorded. This information is presented either via speech and braille, or if the command is pressed twice, in a browse mode window.

In contrast, a playlist transcript is the complete overview of the loaded playlist (or parts of it) presented in various formats. This complete overview includes data from all columns (not just the ones examined by playlist snapshots). Once data from all columns are gathered for a track, NVDA will convert this information into various formats, including plain text, HTML table, comma-separated values (CSV) and so on for viewing in a browse mode window, copying to clipboard (for some formats), or saving to a file.

#### SPL Assistant 3: configuration

There is another function key assigned to SPL Assistant: pressing F12 will switch to an instant switch profile (if defined). We'll come back to what is meant by "instant switch profile" and the mechanics of it (and internals of SPL Assistant, F12) in the next section.

#### SPL Assistant 4: getting help

I believe that a product isn't complete without a good quality documentation. For this reason, SPL Assistant provides two commands (one since 2022) to help you use the layer commands or the add-on itself. They are:

* F1: Opens a browse mode document presenting a list of SPL Assistant layer commands.
* Shift+F1: Opens the online user guide (os.startfile, removed in 2022 to improve add-on security).

#### SPL Assistant 5: Checking for add-on updates

If using add-on 18.12 and earlier, pressing Control+Shift+U after entering SPL Assistant layer will cause the add-on to check for add-on updates. Unlike the automatic update check process described earlier, this one is a manual check, thus it'll perform additional actions such as stopping the automatic update check timer before actually checking for updates. Another difference is that this command will display a results dialog if there are no updates or other errors are encountered, whereas in automatic check mode, they are not shown.

### A surprise: some Assistant layer commands can be invoked without entering the layer first

There are times when a broadcaster will need to obtain certain information quickly. So the question becomes, "is there a way to announce something without first invoking Assistant layer?" Yes, you can assign a custom command for the following Assistant commands:

* Name of the next track.
* Name of the current track.
* Weather and temperature.
* Playlist snapshots.
* Track time analysis marker.
* Track time analysis.

For these routines, an extra step is performed to make sure that SPL Assistant flag is turned off automatically after the shortcut for these routines are pressed. Without this step, you might end up with a situation like the following:

1. You invoke Assistant layer.
2. You then press the shortcut key (not the layer counterpart) for the layer command you wish to use.
3. You press another key which may announce something else, or you hear the same thing twice if you do press the layer command counterpart to the command you have pressed. In effect, you have invoked two layer commands in one sitting (the purpose of the layer set is to let you hear one announcement at a time).

## Introducing configuration facilities: add-on settings dialog and broadcast profiles

We have arrived at our last station stop for Studio app module internals: configuration management. This facility allows a broadcaster to configure various options such as alarms, column announcement order and so on, as well as package settings for a show as a broadcast profile to be invoked during the show. Along the way you'll learn how NVDA screen reader stores various settings, what happens if something goes wrong and get into internals of how broadcast profiles work.

### ConfigObj: NVDA's configuration manager assistant

NVDA uses ConfigObj library to manage settings. This Python module, inspired by Python's own Config Parser, allows developers to store settings in a text file, read and interpret settings and validate options against default configuration options.

NVDA comes with a collection of default options. They live in source/config/__init__ and are used for various things, including presenting preferences, validating user configuration and so on. The config management module also includes facilities to handle profiles (a package of user settings to be used in an app, during say all or reserved for manual activation).

### NVDA configuration profiles: multiple configuration files, one online database

A number of users asked NV Access if it would be possible to have profiles where certain settings can take effect while one is using apps or during say all. NV Access listened and introduced configuration profiles in late 2013. As of August 2015, one can create a manual or an automated (triggered) profile, with the latter further divided into say all profile and app-specific one.

Configuration profiles involve a few support routines and a careful coordination between configuration files. In essence, each configuration profile (stored in profiles folder in user configuration folder) is a snapshot of differences between the profile and the main user configuration file (named nvda.ini). When a profile becomes active, NVDA will load the profile file associated with the given profile and modify user settings according to values stored in the newly activated profile, and wwill record the name of the profile file to remind itself as to which profile is active (the default user configuration profile is named "normal configuration" with the file name of nvda.ini).

What if settings had errors? As part of the startup routine (portions of main function (source/core.py) prior to entering the main loop), NVDA will display a configuration error dialog if it detects serious issues with configuration values (in reality, ConfigObj notifies NVDA of this problem). You'll see this is also implemented in the Studio app module to deal with add-on configuration issues.

### All about StationPlaylist add-on Configuration Manager

Until recently, Studio app module handled all add-on configuration routines. With the advent of add-on 5.0 which introduced add-on settings dialog, configuration management routines were split into a dedicated Configuration Manager (splstudio.splconfig). The new module takes care of configuration routines, including validating the user configuration, presenting add-on settings dialog and other dialogs inside it, handling broadcast profiles and more. In add-on 7.0, routines pertaining to configuration dialog were split into splconfui module, with the main add-on settings listed under NVDA preferences menu.

### How settings are loaded, used and saved

As mentioned in the chapter on life of the Studio app module, one of the things the app module does is load the add-on configuration database by calling splconfig.initialize function. The job of this function is to load the add-on configuration map from various places (for add-on 5.x, it will be the main configuration map only, while 6.0 also searches appModules/profiles folder to load broadcast profiles). The format of the configuration file is that of a typical ini file, and as far as NVDA is concerned, it is a dictionary.

When the configuration database is ready, Studio app module will then use values stored in this settings dictionary to perform various tasks, including microphone alarm, announcing listener count and so on. If multiple profiles are defined, NVDA will start with the first configuration map (normal profile), and the active profile is denoted by splconfig.SPLConfig map (more on profiles in a moment).

After you are done using Studio, close Studio so settings can be saved to disk. This involves saving individual profiles, copying global settings to the normal profile and saving the normal profile to disk.

### The StationPlaylist Add-on Settings Dialog

Studio app module allows you to configure various settings in two ways: via a shortcut key (discussed in a section on configuring basic settings) or via the settings dialog. When you use a shortcut key to change settings, NVDA will look up the value for the setting, change it, announce the new setting and store the newly changed value in the settings map.

Alternatively, you can configure settings via the add-on settings dialog (Alt+NVDA+0). As it is a settings dialog (powered by gui.SettingsDialog), it will look just like any NVDA preferences dialog. For some advanced options, this dialog is the only gateway to access them (covered below).

Until 2018, add-on settings were divided into various dialogs. With the release of NVDA 2018.2, it became possible to house all settings under one roof, divided into various settings panels. Visually, it resembles a two-column layout, with the left column showing a list of settings categories, and the right column displaying settings for the chosen category. See below for notes on multi-category settings.

In 2020, broadcast profiles management was split into its own dialog. Prior to this split, most add-on settings panels relied on broadcast profiles panel for synchronization and updating their controls. This created complications, especially when panels other than broadcast profiles were opened directly. To avoid this issue and to make panels independent of each other, broadcast profiles dialog was born.

The add-on settings dialog (splconfui.SPLConfigDialog) contains following options:

* Global settings: these are settings not affected by profiles. These include status announcements, announcing listener count, library scan options and so on.
* Profile-specific settings: Currently alarms, metadata streaming and column announcement settings are profile-specific. These are end of track alarm and the option to use this alarm, song ramp (intro) time and the setting to use this alarm, microphone alarm and microphone alarm interval. It also includes URL's for metadata streaming and column announcement order and inclusion. For numeric settings such as alarm value, it is a spin control (wx.SpinCtrl; use up or down arrow keys to change them).
* Reset settings: NVDA will ask if you wish to reset settings in the currently active profile back to factory defaults. This is done by using a function in splconfig module (splconfig.resetConfig) that will set current profile values to defaults (a default configuration map is included for this purpose; this map uses a configuration specification (confspec, part of defining validation routine via validator module (a close friend of ConfigObj), and this confspec is defined in the splconfspec module).

When you press Alt+NVDA+0 from Studio to open this dialog, the following will happen:

1. Just like alarm dialogs (see above), NVDA will make sure no other dialogs are open.
2. It'll then call a function in splconfui module, which in turn will prepare the dialog to be shown.
3. The preparation routine (SettingsDialog.makeSettings) will populate the dialog with controls and options associated with each control, with current options coming from configuration values stored in the active profile.
4. Once the dialog is ready, it'll pop up and you'll land on "General add-on settings" button (formerly status message checkbox) or list of active profiles depending on the add-on version and add-on command-line switches (former is 5.x or restrictions on loading profiles is in place, latter is 6.0 and no restrictions). You can then use typical dialog navigation commands to navigate through various options.

After configuring some settings, click OK or Apply. NVDA will then locate the selected profile and tell SPLConfig to use this profile, then store options from the settings dialog into the configuration map. If Apply button is pressed and if the selected profile is not the active one, NVDA will present a message reminding users that settings will be saved to the profile selected from settings dialog, not the active one at the moment. After that, changes will be saved and add-on settings will reappear.

In case you discard new settings (clicking Cancel), NVDA will check to see if an instant switch profile is defined, and if so, it'll perform various operations depending on whether the instant profile has been renamed or deleted.

#### Multi-category settings

The description above refers to the old add-on settings interface, which was based on old NVDA settings routines. In the past, there were discussions between add-on users regarding changing the current add-on interface to that of a multi-category settings interface so all add-on settings can be found under one roof.

In the old days, if one wanted to change settings in NVDA, one would open NVDA's preferences menu and hunt for correct dialog. For instance, when changing browse mode related settings, the place to go was NVDA menu/Preferences/Browse Mode. This meant settings were scattered throughout different dialogs.

In 2018, a major paradigm shift occurred in NVDA's own user interface: multi-category settings screen. In NVDA 2018.2, a new settings screen, combining various dialogs into a panel, launched. For many settings, one can now open NVDA Menu/Preferences/Settings, select the desired settings category, then change settings. This also had the benefit of moving many settings under one roof.

As a follow-up to this development, StationPlaylist add-on settings has undergone a major facelift. As noted throughout this article, add-on settings are housed under various dialogs, with the main add-on settings dialog serving as a gateway to these dialogs. In 2018, this has changed into a multi-category settings screen.

### All about broadcast profiles

In Studio app module world, a broadcast profile (usually shortened to profile) is a group of settings to be used in a show. This is achieved by using a configuration profile container (splconfig.SPLConfigPool for add-on 6.x and 7.x, splconfig.SPLConfig.profiles for 8.0 and later) for storing these profiles, and one of them is used at any given time (by default, the first profile).

There are two ways of creating a profile: brand new or as a copy. Both uses the same dialog (splconfui.NewProfileDialog), with the difference being the base profile in use. For a brand new profile, settings from the normal profile will be used (minus profile-specific settings, which are set to default values), and for a copy, the new profile will contain all settings from the base profile. In both cases, a memory resident profile will be created and initialized just like other profiles (splconfig.unlockConfig/splconfig.SPLConfig.createProfile, taking the name of the new profile as a parameter); this was done to reduce unnecessary disk writes. Also, new/copy profile dialog (and other dialogs invoked from the main configuration dialog) will disable the main settings dialog.

In case the selected profile is deleted, the profile will be removed from the profiles list, the configuration file associated with the profile will be deleted (if it exists) and a previously active profile will take over unless if the active profile itself is gone, in which case normal profile will be set as the active profile. In case of a rename operation, it'll look for a profile with the old name and change some properties to reflect name change. There is an important step the app module will perform if an instant switch profile is renamed or deleted (if renamed, the instant profile variable will hold the new name, and if deleted, instant profile value will be None). A similar procedure was invoked in older releases when dealing with time-based profiles.

#### Broadcast profiles dialog

Inspired by NVDA screen reader's configuration profiles dialog, this dialog (splconfui.BroadcastProfilesDialog) shows various profile management controls. When you press Alt+NVDA+P to open this dialog, you'll be greeted with  a list of profiles loaded and buttons to create a brand new profile or a copy of an existing profile, rename and delete profiles. It also contains a "triggers" button to configure profile triggers such as instant profile switching.

There is one more control: activate button. This button is disabled by default if the selected profile is the active profile, becoming active otherwise. Regardless of status of activate button, pressing Enter from profiles list will activate the selected profile.

But there are no OK and Cancel buttons - there is only a "Close" button. How can a broadcast profile become "active" when you press Enter? This is done by setting AffirmativeId to "Activate" button. In effect, "activate" button acts as OK button, which will eventually call the handler associated with "close" button.

#### Introducing Config Hub

In add-on 6.x and 7.x, a combination of SPLConfig map and the config pool was used to allow users to switch between profiles. Because these were using facilities provided by other modules, this meant custom variables such as active profile flag had to live in splconfig module.

To solve this problem and to allow centralized profile management, a concept of Configuration Hub (ConfigHub) was introduced in add-on 8.0. Inspired by NVDA's own configuration management facility and powered by Chain Map (a dictionary that holds multiple lookup maps), this class not only stores list of currently loaded profiles and the dictionary representing current settings, it also houses various records such as name of the active profile, a history of previously activated profiles and so on, as well as support routines for profile management.

The various changes due to introduction of Config Hub are:

* Switching profiles: no longer need to copy settings back and forth between live config dictionary and the designated profile in the config pool. Profile switching is simple as swapping new and old profile maps.
* A history of activated profiles is now kept inside this dictionary.
* It is possible to pass in additional options when creating a new profile, such as whether it should be cached, validated now and so on.

#### How does profile switching work

Note: information on time-based profile is included for completeness.

Besides switching to different profiles via broadcast profiles dialog, a profile can be set to be switched to instantly during a live show. In older releases, time-based profiles were supported in which NVDA will switch to a designated broadcast profile just before the show starts.

An instant switch profile is a profile to be switched to if told by the user. This is used before you connect to a streaming server to load settings appropriate for a show (as of time of this writing, only one can be selected as an instant switch profile; to define this profile, select a profile to be used as a show, then go to profile switching button and select it).

In contrast, a time-based profile is a special type of instant switch profile that will be activated at a specific date and time. A separate map (a pickle map) is employed to store settings related to these profiles, and the user-facing options can be found in triggers dialog found in add-on settings (see the next section for an overview of this dialog and the configuration format for this map).

To activate an instant switch profile, press SPL Assistant, F12. For time-based profile, it'll activate itself when it is time to do so (with help from a countdown timer located in splmisc module). In ither case, the switching procedure is as follows:

1. Performs some checks, including:
	* Checks if a switch profile (instant or time-based) is defined.
	* For instant switch profiles, if a profile is defined, it'll make sure you are not using the instant switch profile yet.
2. For add-on 7.x and earlier, saves the index of the active profile.
3. Locates the name of the switch profile and the profile associated with it and switches to the switch profile (for add-on 7.x, reassigns SPLConfig to use the switch profile; for 8.0 and later, swaps normal profile with the instant profile map). At this point, NVDA may announce metadata streaming status if told to do so when switching profiles, and with 17.12, made simpler through an action extension point notifier that tells appropriate functions to respond to profile switch action.
4. If no duration is specified for a time-based profile, NVDA will set next switch time and date by calling splconfig.setNextTrigger, otherwise this is delayed until the show is complete.
5. If told to return to the previously active profile, it'll tell SPLConfig to use the previously active profile (the index for the previously active profile is located and is used to pull the profile with the given index from the config pool).
6. When deactivating a time-based profile, NVDA will now find out when the next switch date and time will be.

#### Time-based switching fields and triggers dialog

Note: this section is no longer applicable since 2020 but is kept for historical reasons.

For each time-based profile, a list with seven fields is employed to describe trigger (switch) date and time. These are:

* Trigger date (integer between 0 and 127): A 7-bit integer, denoting days on which a given profile should be activated. This field is used in profile triggers dialog to set or clear activation day checkboxes. A value of 0 means the profile should not be activated, and if so, it is removed from the triggers map.
* Switch date and time (five integers): The first five fields used for constructing datetime.datetime object (year, month, day, hour, minute) are stored. This is used to let NVDA know when to switch profiles.
* Duration (integer between 0 and 1439): An integer specifying the duration of this profile (show) in minutes. This is mainly used by a timer that becomes active when the profile in question becomes active, and the only job of this timer is to switch back to another profile when the show is complete.

The triggers dialog, used to configure these fields for the selected profile, consists of two groups of controls:

* Trigger days: seven checkboxes, one for each day of the week. Checking or clearing these boxes sets corresponding bits in the trigger date field.
* Switch time: three number entry fields denoting when to switch to this profile (hour and minute) and the duration of this show (minutes).

Once the data is gathered, NVDA will first check if trigger date checkboxes are checked (if no checkboxes are checked, the profile is removed). Next, NVDA will see if another profile has taken the given time slot, and if not, will proceed to store the next trigger date and time (will not be saved until OK button is clicked from the main add-on settings dialog).

#### Profile caching

Note: profile caching was a core component of broadcast profiles management from add-on 7.0 to 21.10 and is documented for historical reasons.

More recent computers ship with a type of drive called a solid-state drive (sSD). This is the internal disk version of a high-quality flash drive that is larger (physically and in capacity) than a typical USB flash drive. Unlike a spinning hard drives, solid-state drives use flash memory to store information, and therefore data can be read and written faster.

One downside of an SSD is limited data writes. Flash memory can endure a limited number of read and write cycles before data cannot be written to a specific location. To avoid this, system software will do its best to store new content across the entire disk so every location can store content (this is called ware leveling).

To help prolong SSD life, add-on 7.0 introduced broadcast profile caching. Whenever profiles (including normal profile) are loaded from disk the first time, a copy of settings stored in profiles is stored in an online cache, a dictionary with profile names as keys, which in turn refers to the dictionary view of profile settings. When profiles are saved, the contents of the profile to be saved is compared to this online cache and the profile contents will be written to disk if settings are changed. This assumption takes advantage of the fact that users would not change add-on settings every time Studio is used.

At first profile caching was seen as a way to increase SSD life. But it was later discovered that the caching mechanism made profile save procedure complex. Further, the SSD technology is more robust in 2021 compared to the first time profile caching was introduced (2016), therefore profile caching mechanism was removed in add-on 21.10.

This concludes a detailed tour of Studio app module internals. The rest of the article will focus on SPL Studio Utilities global plugin, encoder support and a few thoughts on how the add-on is developed, starting with a tour of SPL Controller layer commands.

## Introduction to SPL Utilities: SPLController and focusing to Studio window

Now that we've covered the "kernel" (innermost parts) of this add-on, it is time to talk about the icing: SPL Utilities global plugins and its contents.

Note: until 2019, encoder support was part of SPL Utilities, but it is now part of SPL Engine app module which is covered next. In 2025, some parts from encoder support were moved back to the global plugin.

### Overview and global plugin contents

As described in the add-on design section, SPL add-on comes with several app modules and a global plugin. This was needed not only to differentiate between module types and expertese, but also allow Studio functions to be invoked from other programs.

Previously, SPL Utilities was also the home of encoder support routines, introduced in fall 2014 with add-on 3.0. In 2020, encoder support module was moved into its own app module named SPL Engine (splengine package).

The SPL Utilities global plugin is housed inside globalPlugins/splUtils/__init__.py. The module consists of global plugin class, SPL Controller driver and commands housed inside the class, and global constants used to communiocate with Studio. It also includes a routine to switch focus to Studio from anywhere.

### SPL Controller layer

The SPL Controller layer (entry command unassigned, same reason as the Assistant layer entry command) is used to invoke Studio functions from anywhere. The entry routine is similar to the app module counterpart (SPL Assistant) except for the following:

* NVDA will make sure Studio is running (if so, it'll cache the window handle value just as in the Studio app module), otherwise it cannot enter SPL Controller layer.
* All commands (except five) use Studio API (Studio API and use of user32.dll's SendMessage was described in a previous section).

For mechanics of layer commands, see section on add-on design where layer commands were discussed.

The following commands utilize Studio API:

* A/Shift+A: Automation on/off.
* L/Shift+L: Line in on/off.
* M/Shift+M/N: Microphone on/off/instant on/off toggle.
* P: Play.
* Q: Obtain various status information. Due to API changes, this command works better in studio 5.20 and later.)
* Shift+R: Library scan progress and number of items scanned.
* S/T: Stop with fade/instant stop.
* U: Play/pause.

For readers familiar with Studio keyboard commands, you'll find yourself at home (they are indeed Studio commands except pressing Shift will turn a feature off and Shift+R will remind you of Control+Shift+R for library scan from Insert Tracks dialog). The letter "Q" stands for "query Studio status".

Here are the five exceptions

* C/N: current and next track (these, together with remaining time script, asks Studio app module to announce information).
* E: NVDA will search for and announce connection status of encoders. This is done by locating top-level windows for various encoder windows and using EnumChildWindows to look for actual encoders list.
* R: Remaining time for the currently playing track (if any; prior to 25.07, remaining time was obtained via Studio API).
* F1: Opens a browse mode document displaying Controller layer commands (does this sound familiar?).

### Focusing to Studio window from anywhere

As you are broadcasting a show with Studio, you may find yourself in a situation where you need to switch to Studio quickly to take care of automation, insert new tracks and so on. An ideal situation is to switch to Studio when you press Alt+TAB (this isn't the case if you have more than two programs opened). For this reason, screen reader scripts for Studio includes a command to switch to Studio upon request (unassigned in NVDA).

Until 2016, this was accomplished with a function in the SPL Utilities module (SPLStudioUtils.fetchSPLForegroundWindow). This was employed not only by the main global plugin module (called from a script to focus to Studio window), but also used in encoders for various functions. The routine was as follows:

1. The focus to Studio script will check if Studio is running, and if so, it'll call the fetch window function, which in turn locates the desktop (shell) window to serve as the starting point for locating Studio window.
2. NVDA will scan top-level windows (children of desktop object) until a Studio window (where the window's app module is the Studio app module) is found, and if found, NVDA will increment a Studio window candidate counter.
3. Once top-level window scanning is complete, NVDA will take action based on what the Studio window candidate counter says before passing the foreground object back to the main script. It can do one of the following:
	1. If counter is 0 (fg is None), NVDA will know that you have minimized Studio, so it'll tell you that Studio is minimized.
	2. If counter is 1, NVDA will locate the Studio window by looking for the main Studio window (user32.dll is involved).
	3. For all other values, NVDA will assume the last window found is the Studio window (held in fg variable) and return it.
4. Back at the focus to Studio script, NVDA will either announce if Studio is minimized or switch to the foreground window returned by the fetch window function (fg.SetFocus).

In 2017, this has been simplified to use SetForegroundWindow Windows API function with the handle to the Studio window being the only required parameter. Not only this simplified this routine significantly, it also improved performance of this command. This became the basis for letting NVDA switch to Studio when an encoder is connected (see the next section).

One side effect was difficulty in determining if Studio window is minimized, hence the clue was seeing if NVDA says "unavailable". In 2020, focus to Studio routine was refined to look for visibility of Studio window, and if not visible, present an error message. One can then go to system tray and restore Studio window.

## Encoder support

We have now arrived at the penultimate chapter in this Add-on Internals article for StationPlaylist add-on: encoder support. We'll talk about how encoder support is implemented, how NVDA can detect encoder labels and a behind the scenes overview of what happens when you connect to a streaming server.

### Encoder support: From suggestion to implementation

Originally, I wasn't planning on including encoder support into the SPL add-on. However, after talking to some Studio users who were using SAM encoders and seeing how other screen readers supported it, I decided to investigate SAM encoder support in summer 2014, resulting in encoders support becoming a part of SPL Utilities global plugin in add-on 3.0.

The first issue I had to solve was making NVDA recognize the encoder entries themselves. Once that was solved, the next task was announcing connection error messages, which led to figuring out how SAM encoders react when connected to a streaming server.

Originally, I manipulated text written to the screen to obtain needed status messages (via text infos). This routine caused some to experience screen flickering issues when connecting to a streaming server. This was resolved by using encoder description (obj.description), which opened up a possibility to monitor changes to this text via a background thread (more on this routine below), which also eliminated a need to stay on the encoders window until connected.

While I was resolving problems with SAM encoders, I also worked on refactoring encoder support code to support StationPlaylist encoders (add-on 4.0). Initially, encoder support code was optimized for SAM encoders, but the current code structure (explained below) was written to extend basic encoder support easily, and as a result, both SAM and SPL encoder entries (and other encoder types) present similar interfaces and commands, including a common encoder configuration dialog (add-on 7.0).

Few years later, encoder support became a hot topic when I was asked by a broadcaster to add support for Edcast in 2019. Edcast, while free, was end of life, and Altacast took its place. Thankfully, adding support for AltaCast encoder (Winamp plugin which must be recognized by Studio and Streamer) was a breeze because its user interface is similar to SPL encoders. Thus, AltaCast encoder support is similar to SPL encoders, thus for purposes of this section, AltaCast is synonymous with SPL encoder.

At the same time, encoder support was reorganized. In 2014, with limited knowledge on encoder engines, I felt it was best to house encoder support module inside SPL Utilities. In the course of time, two encoder engines were found: SPL Engine (splengine) and Streamer (splstreamer). After learning that encoder engines were housed inside these apps, it was decided in 2020 to separate encoder support module into its own app module, transfering encoder support from the global plugin to SPL Engine app module package with Streamer deriving most of its power from the former.

### Encoder support structure

Encoder support is part of two app modules: SPL Engine and StationPlaylist Streamer, the former being an app module package similar to SPL Studio package. The complete picture is thus:

* SPL Engine app module (splengine/__init__.py), providing base app module services for use by both SPL Engine and Streamer such as encoder detection.
* Encoder support (splengine/encoders.py), outlining NVDA's support for various encoders and is the focus of this section.
* Streamer app module (splstreamer.py), which simply imports everything from SPL Engine app module package and adds overlay class management for Streamer user interface.

### Encoder entries: Yet another overlay class family

Just like Studio track items (see the section on track items), encoder entries are overlay classes. Each encoder type (SAM, SPL, AltaCast and future encoders) inherit from a single encoder object (splengine.encoders.Encoder) that provides basic services such as settings commands, announcing encoder labels and so on. Then each encoder type adds encoder-specific routines such as different connection detection routines, ways of obtaining encoder labels and so on. Speaking of encoder labels and settings, the base encoder class is helped by some friends from the encoder module itself, including a configuration map to store encoder labels and basic settings, a routine to obtain encoder ID (encoder string and the IAccessible child ID) and so on.

On top of the base encoder class are three encoder classes, representing entries from SAM, SPL, and AltaCast. SAM encoder entries (splengine.encoders.SAMEncoder) are laid out just like Studio's track items with parts deriving from SysListView32 objects, whereas SPL encoder list (splengine.encoders.SPLEncoder) is a typical SysListView32 control (see the section on column routines for more information). Being similar in appearance to SPL encoder, AltaCast encoder (splengine.encoders.AltaCastEncoder) derives from SPL encoder class with encoder specific differences. All encoder classes provide similar routines, with differences being how connection messages are handled and obtaining encoder specific data such as encoder type identifier used for looking up encoder settings with help from encoder ID's.

### Encoder ID's

An encoder ID is a string which uniquely identifies an encoder. This consists of a string denoting the encoder type (SAM for SAM encoder, for instance), followed by the encoder position (separated by a space). For instance, the first SAM encoder is given the ID "SAM 1". The ID's are used to retrieve and configure encoder settings, as well as identifying encoders when monitoring them in the background.

### Common services: basic settings, encoder labels and related methods

All encoder classes provide the following common services:

* Configuring settings: six settings can be configured:
	* A custom encoder label can be defined for ease of identification.
	* Pressing Control+Shift+F11 will tell NVDA if NVDA should switch to Studio when the encoder is connected.
	*Pressing Shift+F11 will tell NVDA if NVDA should ask Studio to play the next track when connected.
	* Pressing Control+F11 will enable background encoder monitoring (more on this in a second).
	* Enabling or disabling connection progress tones (add-on 7.0, configurable from encoder settings dialog described below).
	* Announcing connection status until the selected encoder is connected (add-on 20.03), also configurable from encoder settings dialog.
	* Once these settings are changed, the new values will be stored in appropriate flag in the encoder entry, which in turn are saved in the configuration map.
* Apart from encoder labels, retrieves settings. This is done by various property methods - once called, these methods will look up various settings for the encoder from the configuration map (key is the setting flag, value is the encoder ID). Encoder labels are organized differently (see below).
* Monitors and responds to connection status changes. The response routine (onConnection method) attempts to set focus to Studio and/or play the first checked track if configured to do so.
* Loads encoder labels when an encoder first gains focus (if this was loaded earlier, it could be a waste of space, especially if encoders are never used).
* Announces encoder labels (if defined) via a dedicated name getter. Labels are stored as dictionary keys corresponding to encoder ID's under a dedicated encoder labels section inside the configuration map.
* Define and remove encoder labels. If a label is defined (no empty string), encoder label is stored in an encoder labels collection, otherwise removed from the collection.
* Updates encoder label and flags position when told to do so (via a dialog, activated by pressing Control+F12). This is needed if encoders were removed, as you may hear label for an encoder that no longer exists. This is implemented as a variation of find predecessor algorithm.
* Announces encoder columns. The base class can announce encoder position (Control+NVDA+1) and label (Control+NVDA+2), while SAM can announce encoder format, status and description and SPL and AltaCast allows one to hear encoder format and transfer rate/connection status.
* In add-on 7.0, a central configuration dialog for configuring encoder settings for the selected encoder has been added. Press Alt+NVDA+0 or F12 to open this dialog.

### More and more threads: connection messages and background encoder monitoring

As we saw in a previous chapter, threads allow developers to let programs perform certain tasks in the background. Even in encoder support, threads are employed for various tasks, including connection message announcement and background encoder monitoring.

Each encoder overlay class (not the base encoder) includes dedicated connection handling routines (reportConnectionStatus). Depending on how you invoke this, it starts up as follows:

* If background encoder monitoring is off and you press F9 to connect, NVDA will run this routine in a separate thread. For SAM, this is checked right after sending F9 to the application, and for SPL, this is done after clicking "connect" from the encoder context menu (manipulates focus in the process).
* If background encoder monitoring is on before pressing F9, the routine will run from another thread when this setting is switched on. Then when you press F9, NVDA knows that the background monitoring thread is active, thus skipping the above step.

The connection handling routine performs the following:

1. Locates status message for the encoder entry. For SAM, status message is spread over two columns (child objects), and for SPL, transfer rate column is consulted. This will be done as long as Studio and/or NVDA is live (that is, if the thread is running).
2. Announces error messages if any and will try again after waiting a little while (fraction of a second). If NVDA is told to not announce connection status until the encoder in question is connected, connection reporter thread will stop when an error message is seen.
3. If connected, NVDA will play a tone, then:
	* Do nothing if not told to focus to studio nor play the next track.
	* Focuses to studio and/or plays the next track if no tracks are playing by calling onConnect method.
4. For other messages, NVDA will periodically play a progress tone and announce connection status so far as reported by the encoder (progress tones will not be played if suppressed from encoder settings dialog).
5. This loop repeats as long as this encoder is being monitored in the background.

#### Monitoring multiple encoders with encoder registry

Sometimes it becomes necessary to monitor multiple encoders at once, particularly if streaming to multiple servers or files. To handle this, encoder connection monitoring threads are housed inside an encoders registry, a dictionary that maps encoder ID's to connection reporter threads. This is useful to direct NVDA to announce connection status for multiple encoders one encoder at a time, and if this happens, NVDA will prefix encoder status with the ID associated with the encoder in question.

### Encoder-specific routines

In addition to basic services, each encoder routine has its own goodies, including:

For SAM encoders:

* To disconnect, press F10.
* You can press Control+F9 or Control+F10 to connect or disconnect all encoders (does not work well in recent SAM releases, according to my tests). A workaround was developed to fix this problem (opens context menu and activates the correct item on its own).

For SPL encoder family (including AltaCast):

* When you press Control+F9 to connect all encoders, NVDA does the following:
	1. Locates "connect" button, and if it says "Connect", clicks it (obj.doAction).
	2. Moves focus back to the entry (self.SetFocus).
* To disconnect, press TAB until you arrive at "Disconnect" button and press SPACE.

## Final notes and add-on development process overview

Now that we've visited internals of StationPlaylist add-on, I'd like to give you a tour of my lab where I develop this add-on. Along the way you'll learn how an add-on is born, coded, tested, released and maintained.

### Lab setup, development equipment and software

For all my software development, I use a touchscreen laptop running Windows 11 and latest NVDA alpha snapshots. The computer also runs Cygwin and/or Windows Subsystem for Linux (WSL, otherwise known as BASH on Ubuntu on Windows)to run various command-line tools (Git, SCons, etc.), and in case I need to compile NVDA from source code, installed Visual Studio 2022 with latest update and other dependencies. For Studio, I use latest version unless I need to test older releases.

### Git: a "smart" source code manager

Like other NVDA developers and many add-on writers, I use Git for source code management (contrary to its slogan, Git is very smart). This is a distributed system, meaning a local repository contains the complete record of how the source code is managed (no need to connect to a server to commit and fetch updates). For example, using just my local copy of the SPL add-on source code, I can view commit history and generate older add-on releases.

Another advantage of Git is extensive support for branches. A branch is a development workflow separate from other branches. For example, NVDA screen reader uses at least three branches for its workflow: alpha (master branch), beta (beta branch) and rc (release candidate, used to build official releases). SPL add-on uses this approach as well: there are at least two branches in use, called master (renamed to main in 2021) and stable used for ongoing development or release and maintenance, respectively (we'll come back to branches in a second). With the advent of Test Drive program (see below), a third branch named "staging" or "next" is used to gather all work done on branches under one roof for testing purposes (in 2018, this has changed significantly). The staging branch is no longer used since 2023 when I stepped down from active maintainer role.

### How an add-on feature is born

Let's go through a typical development process for an add-on feature by looking at how broadcast profiles was developed (for more information on broadcast profiles, refer to configuration management section above).

I started working on broadcast profiles in March 2015 while developing add-on 5.0. This was a natural extension of add-on settings dialog: whereas this dialog (and the configuration database it uses) only dealt with a single profile, I thought it might be a good idea to allow multiple profiles to be defined and to let the settings dialog respond to profile changes.

There was an important reason for writing this feature: Since NVDA supports multiple configuration profiles and since some broadcasters were hosting multiple shows, I thought it would be a good idea to implement a similar feature in the SPL add-on. Thus, I envisioned broadcast profiles to be used primarily by people hosting multiple shows, with each show defined as a profile.

In March and April 2015, I started rewriting certain parts of add-on configuration manager (splstudio.splconfig) in preparation for developing broadcast profiles (now included as part of add-on 6.0). I started by writing todo comments (where appropriate) describing what the future feature should be like. I then modified initConfig and saveConfig (discussed in app module sections), initially telling them to work with the default profile (the one and only configuration map then), then I left it alone until add-on 5.0 was released in June 2015.

In June 2015, I opened a new branch (initially using the codename "starfish") to house code related to broadcast profiles. Before any "real" code was written, I studied NVDA source code dealing with configuration profiles to learn more about how Jamie (James Teh from NV Access, now Mozilla) implemented this feature. Once I understood how it worked, I copied, pasted and changed the code to match the overall add-on code base (giving nV Access the credit they deserve).

One of the first things I had to decide was how to store profiles. I experimented with using ConfigObj sections, one per profile, but this proved to be problematic (a profile could be given the name of an existing configuration map key). I then went back to NVDA source code to find out how NV Access solved this problem (using separate ini files), implemented it, and was met with another problem: transfering values between profiles. This was resolved by specifying whether a setting was "global" (applies to all profiles) or specific to a profile. Next came profile controls in the add-on settings dialog and using choice events to set alarm values using values from the selected profile.

The last thing I did before merging the broadcast profiles branch to master branch in July was revising configuration error dialog and writing documentation for broadcast profiles. Once the documentation was ready and small issues were fixed after going through many rounds of testing (on my own computer and from the profiles branch itself), broadcast profiles branch was merged into master. But the development didn't stop there: thanks to provisions I made, it was quite simple to implement instant switch profiles (again it had issues which are now largely resolved).

### Dealing with threaded code: headaches during development of background encoder monitoring feature

You may recall our discussion of Cart Explorer and how it went through extensive testing to arrive at the current state (this was a difficult code segment). When it comes to difficulty, nothing beats multithreaded code, especially if it involves multiple threads working in parallel (rather, almost parallel), and I tasted this when writing background encoder monitor (add-on 5.0). This involved tracking how many threads were running to make sure no unnecessary threads were running, catching suttle errors and race conditions (a connection attempt could run a thread without checking if the encoder is being monitored) and so on. Thankfully, I went through a similar set of problems a few months earlier when I struggled with library scan (add-on 4.0), and that experience taught me to be careful with threads (and to experience fewer headaches).

### Add-on development process

Follow me as I show you how a typical SPL add-on version is developed, released and maintained:

1. Before starting work on the new add-on version, I write down some goals the add-on should achieve, including feature ideas, user (your) suggestions and so on. With changes to the process in 2017, a feature development may span multiple versions.
2. I then hold a conference call with add-on users to see what they think about some ideas and gather feedback (these are also written down).
3. I then create separate branches for each feature in order to isolate  code and not to break existing code.
4. Next, I write todo comments reminding myself as to what the feature should be like, then I start working on it. As each feature is being developed, I do mental simulations as to how you might use the feature under development, such as possible errors, messages spoken and so on.
5. Once the feature is quite stable, I test the feature to uncover bugs and to fill in the missing pieces. When it comes to testing, I test the new feature branch on both of my computers running different versions of Studio to make sure it works across versions (if not, I go back and modify the code to recognize differences between Studio versions).
6. Starting in fall 2015, I've merged development branches into a staging branch for testing purposes. This branch is also used to generate try (Test Drive program) builds so those who've signed up for early access program can leave feedback (try builds are generated about once a week).
7. After testing the feature for a while and if the feature is stable, I merge the feature branch into master.
8. Every few weeks, I publish master branch snapshots to gather feedback from users willing to test drive snapshots. With the advent of add-on updates in add-on 7.0, one can update between snapshots or stable versions (whichever branch one is using, the update check routine wil use that branch; for example, if one is using master snapshots, updates will be fetched from master branch only).
9. At some point, I set release target window for the next add-on version (for 6.0, it was December 2015). This determines when feature freeze should be and beta release window (for 6.0, beta 1 was released in October 2015). Between feature freeze and the first beta release, I concentrate on code refinements and bug fixes. This has changed significantly in 2017 (see below).
10. After going through several beta cycles (typically two), I ask NVDA community add-on reviewers to review my add-on code and request add-on release during the release window (this is done by merging master branch into stable branch).
11. Once the add-on version is released, subsequent maintenance versions (localization updates, bug fixes, minor tweaks) will be released from the stable branch, with the master branch containing the code for the next major version.
12. Once the next version enters beta cycle, further maintenance releases may or may not happen (an exception is long-term support release, described below).

#### Changes in 2017

In late 2016, I and some users had a conference call regarding the future direction of the add-on. During this call, participants felt that the add-on now includes all the features people need, so it was decided to scale back on features and focus on compatibility with new Studio releases. In the end, it was decided that a version of the add-on to be released in 2017 will be the final major version of this add-on, with future updates being byte-sized chunks.

This decision also aligned with my other add-ons where new versions were released every month or so, along with the fact that features are complete for most add-ons. The new regular update schedule for SPL add-on was implemented as of June 2017.

There were two more implications of this decision:

* No more waits: a new stable feature should not be held up for up to six months if it is ready for the public, thus updates include both new features and bug fixes.
* The Test Drive program (see below) should not be an exclusive thing anymore, but an opt-in process, as I felt early feedback loop is crucial to success of a product such as this add-on.

With this in mind, the following things were changed in 2017:

* No more betas: the development branch (now called slow ring) is considered live beta branch.
* Anyone can switch to try build branch (called fast ring snapshots) provided that they are willing to provide early feedback.
* Long-term support updates are now tied to new major Studio releases. This criteria was extended in late 2017 to include critical changes to NVDA (see below).

#### Further changes in 2018

In July 2018, NV Access announced changes to NVDA's release process in order to make testing and integration easier. Prior to this, an NVDA feature was incubated in the next snapshot for at least two weeks, and this meant having to deal with increasing number of pull requests which sometimes produced conflicts. To avoid this, and to let features come to master branch directly, what used to be live beta (master) branch became "alpha" snapshots. People who wanted more stability were moved to beta releases.

On the SPL add-on side, Test Drive Fast and Slow ring builds have become identical in late July 2018. I also felt that add-on development has slowed down considerably, as well as preparing for the next long-term support release (18.09), thus I felt an overhaul of Test Drive Program was in order.

Then in August 2018, I released Add-on Updater, a proof of concept add-on that allows NVDA to check for add-on updates for all add-ons registered with NVDA Community Add-ons website. In its early days, SPL add-on was excluded because it interfered with Add-on Updater's own update check facility. In reality, I generalized SPL add-on's update check code and transfered it to the new Add-on Updater, hence almost identical internals.

Given that my long-term goal was to let NVDA itself check for SPL add-on updates, coupled with observations from above, I asked the community if it would be better to change the nature of Test Drive Fast ring and to let Add-on Updater check for all add-on updates. The community agreed, hence the following changes were made in August 2018 prior to release of 18.09:

* Test Drive Fast and Slow rings were combined into a single "development" channel. Consequently, there is no more update channel selection capability, with users encouraged to obtain the right releases from add-ons website. This was extended in September 2018 to cover long-term support releases.
* A new concept of "pilot features" replaced Test Drive Fast, configurable via a checkbox and internal flags.
* New (risky) features under development will be enabled if pilot features facility is turned on, otherwise content is identical to regular development build.
* Add-on update checking facility is now taken care of by Add-on Updater, and in the future, to be done by NVDA itself (see below for updates since then). Consequently, add-on update feature and the source code that controlled it has been removed in December 2018.

#### Python 3 work in 2019

When the add-on debuted in 2011, it was written in Python 2. Almost ten years later, Python 2 became unsupported, and the add-on was updated to use Python 3. The Python 2 to 3 transition work throughout 2019 affected this add-on, involving pickle protocol changes (track comments), Unicode strings, FindWindowA versus FindWindowW (see above), attribute names in some Python modules (notably, threading module) and other changes. I spent the better part of summer 2019 to make sure the add-on was ready for Python 3, and the transition work shipped in early 2020.

#### Passing the baton in 2023

2023 was another transitional year in a number of ways. First, In 2023, I was admitted to a doctoral program. Knowing the difficulties that lay ahead, I decided to pass the add-on maintenance to someone. Since May 2023, the add-on is maintained by Chris Duffley, a user of this add-on who has shown interest in add-on authoring.

Second, later in 2023, the NV Access add-on store debuted. Among other things, the add-on store allows add-ons to be updated straight from NVDA. As noted in 2018 section, this was the goal I was after: letting NVDA check for add-on updates, including this add-on. The big ideas from this add-on and Add-on Updater (discontinued in 2025) were influential in the design of the add-on store feature.

#### Restructuring and refactoring the add-on source code and repository in 2025

In 2024, NVDA went through another Python transition, this time from 3.7 to 3.11. With blessing form Chris Duffley, i rewrote parts of the add-on in late 2024 to upgrade the code ot use Python 3.11 facilities, including structural pattern matching and assignment expression. Most notably, tnaks for linting and type hints work in 2021 left the code spinrkled with type hints, and I took the opportunity to update type hints syntax to use Python 3.11 changes as part of this work.

In 2025, I revisited the add-on source code, noticing duplications and outdated comments. With another blessing from Chris Duffley, I have restructured and refactored the add-on source code and the code repository. Most notably, the common services (splcommon) module was introduced to gather duplicated code across the app modules set and the SPL Utilities global plugin, including Studio API definitions, constants such as cart keys definition, and the routine to focus to Studio. This package also includes ocnfiguration management (splconfig) so app modules other than Studio can use it directly without going through the Studio app module. This work is not new - I have worked on a similar idea a while ago after noticing that there were commonalities across app modules, but this was the first time working on code deduplication and refactoring across the entire add-on source code.

Add-on code restructuring and refactoring led to the following changes:

* Introduction of SPL add-on common services. To keep the app module > global plugin relationship, I decided to house the common services as part of the app modules package.
* Both the app modules set and the global plugin will use the new common services module when performing actions such as invoking Studio API.
* Only the common services will be imported when requested. This reduces dependency on Studio app module for things such as Studio API call and constants, especially when the common services module is imported from the global plugin.

With this change, the add-on maintainers must think carefully about where the code belongs:

* If the code is to be used from two or more app modules and/or one or more app modules and the global plugin, it should be housed in the SPL common services package.
* Code specific to an app module or the global plugin will remain in their respective modules.

The code refactoring work also led to introduction of Pyright into add-on code checking routines. Pyright is a static type checker similar to Mypy but faster. Examining code with Pyright led to adding more type annotations and resolving bugs, as well as removing obsolete code paths and restructuring how modules were imported (a notable change was moving SPL config module from the Studio app module to the common services package).

#### Long-term support release

A typical add-on version is supported until the next add-on version is released (currently several weeks to months). However, there are times when an add-on version receives extended support (termed long-term support (LTS) release). This happens if the next major version of Studio is released, a version of Studio with user interface changes is released, or critical changes are expected in future NVDA releases such as ending support for a Windows version.

A LTS version is a major version or a major periodic release of the SPL add-on with some notable differences:

* Support duration: A LTS version is supported for at least six months.
* Features: A LTS version may contain some features from later add-on releases provided that they can be safely backported.
* Studio version supported: A LTS version is the last version to support the oldest supported Studio version. This is designed to give people plenty of time to upgrade to newer Studio releases.
* Last version with old NVDA technology in use: in some cases, LTS releases are made to support users of old NVDA releases. After the LTS release is created, add-on source code will shift to using newer code from NVDA. This criteria was first applied in 18.09 as a result of NVDA's end of support for Windows XP, Vista and 7 without Service Pack 1, as well as transition to Python 3.

As of June 2025, the most recent LTS version is add-on 25.06.x (June 2025 to December 2025). Previous LTS releases have included 20.09.x (September 2020 to April 2021), 18.09.x (September 2018 to December 2019), 15.x (formerly 7.x until October 2016; October 2016 to April 2018) and 3.x (September 2014 to June 2015). For example, add-on 3.x was maintained thus:

1. Add-on 3.0 was released in September 2014.
2. Add-on 3.5 (December 2014) could have been the last maintenance version for add-on 3.x if it was not a LTS version.
3. When add-on 4.0 was released (January 2015), add-on 3.6 was released, backporting some features from 4.0. Users were told that add-on 3.x will be the last version to support Studio versions earlier than 5.00. From that time on, add-on 3.x was taken off the stable branch and was moved to an internal branch.
4. When add-on 5.0 beta was released (May 2015), add-on 3.x (3.9 was available then) entered end of support countdown (no more maintenance releases).
5. A few weeks later, when add-on 5.0 came out (June 2015), add-on 3.x became unsupported.

### Final thoughts

As I end this article on StationPlaylist Add-on Internals, I feel it is time I reveal why my add-ons are free: it is because I love you users and as a service for NVDA user and developer community (and in extension, to all blind broadcasters using SPL Studio). What brings me joy as an add-on writer is the fact that this add-on (and accompanying documentation) has made impact in your lives and lives of listeners to your shows, as well as to other NVDA users and developers around the world. Thank you users for your continued support and feedback, and I promise once again that all my add-on code (including SPL add-on) will be free and anyone is welcome to study and improve upon it.

For add-on writers looking for quality add-on documentation, I hope this series gave you an inspiration as to how to write amazing documentation in your future projects. For people new to add-on writing or for those interested in writing an add-on, I hope this Add-ons Internals series served as a handy resource for your projects, and in extension, gave you an idea as to how certain NVDA functions work. If you'd like to reference this documentation or use it as a blueprint, you are more than welcome to do so. Thank you community add-on reviewers for your continued support and reviews.

### Important notices and credits

I'd like to thank StationPlaylist staff for continued collaboration with screen reader users in regards to accessibility of Studio. A special thanks goes to Jamie Teh from NV Access and Geoff Shang (original add-on author) for giving me and others a foundation for future goodies. A special thanks to Chris Duffley for maintaining the ad-don since 2023. As always, the biggest thanks goes to you, the users of SPL add-on for your continued feedback and teaching me new things about studio.

Source code notice: to protect copyrights, parts of Studio API has not been documented. Also, source code discussed throughout this series may change as future add-on versions are developed.

Copyrights: StationPlaylist Studio, Track Tool and StationPlaylist Encoders are copyright StationPlaylist.com. NonVisual Desktop Access is copyright NV Access Limited (released under GPL). SAM Encoders is copyright Spatial Audio. Microsoft Windows and Windows API are copyright Microsoft Corporation. Python is copyright Python Software Foundation. StationPlaylist add-on for NVDA is copyright 2011, 2013-2025 Geoff Shang, Joseph Lee, Chris Duffley, and others (released under GPL). Other products mentioned are copyrighted by owners of these products (licenses vary).

## References

1. JAWS scripts for StationPlaylist Studio (Hartgen Consultancy): http://www.hartgen.org/studio.html
2. Window-Eyes app for StationPlaylist (Jeff Bishop/AI Squared): https://www.gwmicro.com/App_Central/Apps/App_Details/index.php?scriptid=1268&readMore&media=print
3. Plug-in (Wikipedia): https://en.wikipedia.org/wiki/Plug-in_(computing)
4. Application Programming Interface (Wikipedia): https://en.wikipedia.org/wiki/Application_programming_interface
5. Python 2.7.13 documentation overview (Python Software Foundation): https://docs.python.org/2/
6. Handle (Wikipedia): https://en.wikipedia.org/wiki/Handle_(computing)
7. What is a Windows handle (Stack Overflow): http://stackoverflow.com/questions/902967/what-is-a-windows-handle
8. FindWindow (user32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms633499(v=vs.85).aspx
9. SendMessage (user32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms644950(v=vs.85).aspx
10. NVDA Developer Guide (NV Access): http://www.nvaccess.org/files/nvda/documentation/developerGuide.html
11. OpenProcess (kernel32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms684320(v=vs.85).aspx
12. wxPython online docs: http://www.wxpython.org/onlinedocs.php
13. Higher order functions (How do you make a higher order function): http://effbot.org/pyfaq/how-do-you-make-a-higher-order-function-in-python.htm
14. Time (Python documentation, Python Software Foundation): https://docs.python.org/2/library/time.html
15. GetTimeFormat (kernel32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/dd318130(v=vs.85).aspx
16. Event loop (Wikipedia): https://en.wikipedia.org/wiki/Event_loop
17. Event-driven programming (Wikipedia): https://en.wikipedia.org/wiki/Event-driven_programming
18. Sinclair, Rob. Microsoft Active Accessibility architecture, Microsoft Developer Network, August 2000. https://msdn.microsoft.com/en-us/library/ms971310.aspx
19. UI Automation Overview, Microsoft Developer Network. https://msdn.microsoft.com/en-us/library/ms747327(v=vs.110).aspx
20. Java Access Bridge overview, Java SE Desktop Accessibility, Oracle. http://www.oracle.com/technetwork/articles/javase/index-jsp-136191.html
21. Introduction to OOP (Object-Oriented Programming) with Python, Voidspace. http://www.voidspace.org.uk/python/articles/OOP.shtml
22. Non-Programmer's Tutorial for Python 3/Intro to Object Oriented Programming in Python 3 - Wikibooks. https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Intro_to_Object_Oriented_Programming_in_Python_3
23. Method Resolution Order, The History of Python, june 23, 2010. http://python-history.blogspot.com/2010/06/method-resolution-order.html
24. List View, Microsoft Developer Network: https://msdn.microsoft.com/en-us/library/windows/desktop/bb774737(v=vs.85).aspx
25. List View Messages, Microsoft Developer Network: https://msdn.microsoft.com/en-us/library/windows/desktop/ff485961(v=vs.85).aspx
26. List View Item structure, Microsoft Developer Network: https://msdn.microsoft.com/en-us/library/windows/desktop/bb774760(v=vs.85).aspx
27. VirtualAllocEx (kernel32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/aa366890(v=vs.85).aspx
28. VirtualFreeEx (kernel32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/aa366894(v=vs.85).aspx
29. WriteProcessMemory (kernel32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms681674(v=vs.85).aspx
30. ReadProcessMemory (kernel32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms680553(v=vs.85).aspx
31. Ctypes (Python documentation, Python Software Foundation): https://docs.python.org/2/library/ctypes.html
32. Thread (Wikipedia): https://en.wikipedia.org/wiki/Thread_(computing)
33. Multi-core processor (wikipedia): https://en.wikipedia.org/wiki/Multi-core_processor
34. Multi-core introduction, Intel Developer Zone, March 5, 2012: https://software.intel.com/en-us/articles/multi-core-introduction
35. Intel Core I7-5960X specifications (Intel ARK): http://ark.intel.com/products/82930/Intel-Core-i7-5960X-Processor-Extreme-Edition-20M-Cache-up-to-3_50-GHz
36. Intel Xeon E7-8895V3 specifications (Intel ARK): http://ark.intel.com/products/84689/Intel-Xeon-Processor-E7-8895-v3-45M-Cache-2_60-GHz
37. Global Interpreter Lock (Python Wiki): https://wiki.python.org/moin/GlobalInterpreterLock
38. Threading (Python documentation, Python Software Foundation): https://docs.python.org/2/library/threading.html
39. Multiprocessing (Python documentation, Python Software Foundation): https://docs.python.org/2/library/multiprocessing.html#module-multiprocessing
40. Comma-separated values (Wikipedia): https://en.wikipedia.org/wiki/Comma-separated_values
41. RFC 4180 (Common Format and MIME Type for Comma-Separated Values (CSV) Files), Internet Engineering Task Force: https://tools.ietf.org/html/rfc4180
42. Import or export text (.txt or .csv) files, Microsoft Office Support for Microsoft Excel: https://support.office.com/en-za/article/Import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba
43. CSV (Python documentation, Python Software Foundation): https://docs.python.org/2/library/csv.html
44. Cache (Wikipedia): https://en.wikipedia.org/wiki/Cache_(computing)
45. Os (Python documentation, Python Software Foundation): https://docs.python.org/2/library/os.html
46. Configparser (Python documentation, Python Software Foundation): https://docs.python.org/2/library/configparser.html
47. ConfigObj documentation: http://www.voidspace.org.uk/python/configobj.html
48. Validate module documentation: http://www.voidspace.org.uk/python/validate.html
49. Spin control (wx.SpinCtrl) documentation (WXPython): http://wxpython.org/Phoenix/docs/html/SpinCtrl.html
50. SetForegroundWindow (user32.dll) reference (Windows API): https://msdn.microsoft.com/en-us/library/windows/desktop/ms633539(v=vs.85).aspx
