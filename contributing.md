# Contributing to StationPlaylist NVDA add-on

Thank you for your interest in contributing to StationPlaylist NVDA add-on. The purpose of this document is to outline the overall add-on contribution requirements, development process, and offer tips when contributing.

## About StationPlaylist ad-on

StationPlaylist NVDA add-on provides improved accessibility and usability for StationPlaylist (SPL) suite of applications, including Studio, Creator, Track Tool, and encoders. Inspired by SPL suite scripts for JAWS for Windows, StationPlaylist add-on includes features such as announcing changes to status such as automation, reviewing columns for track/playlist entries, reporting elapsed and remaining time for the playing track, track comments, playlist analysis, encoder connection status reporting, and a set of layer commands to operate Studio from other programs.

## Contribution requirements

1. The latest available stable version of NVDA at the time of your contributions. Using beta or alpha NVDA builds is useful but not recommended unless contribution states otherwise such as supporting an upcoming NVDA feature.
2. Latest available SPL suite releases (6.20 as of April 2026)
3. Windows 11
4. To package your modifications into an add-on build, you must be using Python 3.13 (64-bit) or later.

Note: from time to time the add-on drops support for old SPL suite releases.

## Ways to contribute

You can contribute to StationPlaylist add-on in several ways:

1. Testing: provided that you are using supported SPL suite releases, you can test the add-on and provide feedback.
2. Issues and pull requests: we (add-on developers) welcome issues and pull requests submitted via GitHub (see the section on issues and pull requests for more information).
3. Localization: Crowdin is used to manage existing localizations (no new languages are accepted).

## Contribution process

### Testing the add-on

You can contribute by testing the add-on. To facilitate this, a development snapshot of this add-on is released from time to time so people can test latest changes.

To test the add-on, you must be running the latest stable or development build of NVDA, latest StationPlaylist release,  and latest stable or development build of StationPlaylist add-on. You can obtain latest StationPlaylist add-on via NV Access add-on store (NVDA menu/Tools/add-on store, available or updatable add-ons tab). You can obtain StationPlaylist suite of programs from stationplaylist.com website.

Before testing the add-on:

1. Install the latest availible NVDA release.
2. If you haven't, install the latest StationPlaylist suite of programs. At a minimum, StationPlaylist Studio must be installed.
3. Visit NV Access add-on store (NVDA menu/tools/add-on store).
4. Check StationPlaylist add-on channel from installed add-ons tab. You can test the stable add-on release, but to test latest code, we recommend switching to beta or dev channel.
5. To switch to beta or dev channel, from add-on store, press Control+Tab to go to either updatable or available add-ons tabs.
6. Select "all", "beta", or "dev" from channel list.
7. Press Tab several times until arriving at updatable/available add-ons list, then select StationPlaylist add-on with the appropriate channel defined.
8. Press Enter, then from the context menu, select "update" or "install" depending on if StationPlaylist add-on is installed or not.
9. Close add-on store, and installation will begin, then restart NVDA when prompted.

Testing the add-on simply involves using NVDA with StationPlaylist programs as usual. If you do encounter issues:

1. Restart NVDA with add-ons disabled.
2. Enable one add-on at a time to make sure the issue is not related to add-ons other than StationPlaylist.
3. If the issue occurs after enabling StationPlaylist, note the steps to reproduce the issue.
4. Use GitHub and submit a new issue (https://github.com/chrisduffley/stationplaylist/issues/new). Be sure to include NVDA version, add-on version, StationPlaylist program name and version, Windows version, and steps to reproduce the problem.
5. Sometimes the author will ask for a debug log. If so, restart NvDA with debug logging enabled, try reproducing the issue, then either attach the debug log as part of the GitHub issue or copy and paste the relevant log fragment from the log viewer (NVDA+F1).

### Offering code and pull requests

#### StationPlaylist version requirement

To contribute code and pull requests, you must use latest StationPlaylist suite (6.20)) release.

#### Coding style

StationPlaylist add-on follows NVDA's own coding style (tabs for indentation, camel case, etc.). Although you don't have to, please align closely to NVDA's own coding style.

#### Pull request process

1. If you want, create a new issue on GitHub proposing specific changes. This is so that more people can discuss changes.
2. Create an accompanying pull request via GitHub (be sure to fork the add-on source code before doing so). Unless otherwise noted, pull request base branch should be "main" and each pull request must be done from a different branch.
3. In the pull request comment, describe the pull request, including applicable StationPlaylist release(s).
4. It can take up to a week for the pull request to be reviewed and a decision made. Depending on the severity of the issue, it can be included in the next maintenance version of the add-on or delayed for the next major release.

### Localizing add-on documentation and messages

You must do this through NVDA translations workflow (Crowdin), not through pull requests.

## Additional notes

### Development and release process

StationPlaylist add-on uses continuous, iterative development process. This means a given feature or a change can take up to several weeks to months to be implemented and refined based on user feedback (this can take several development/release cycles), along with being sensitive to changes to NVDA and SPL suite. To facilitate this, development snapshots are released to assist with testing changes and fixes.

The main development branch is named "main". This branch holds code for the upcoming release. Although quality may vary, the aim is to house code that can ship as a stable version at anytime and can be backported to maintenance releases easily.

StationPlaylist add-on uses rolling release model with periodic feature updates. Releases including major feature updates and minor maintenance and localization releases are published regularly, typically at the beginning or end of the month. At least one release is made every year to declare NVDA version compatibility.

### Support duration

A given StationPlaylist add-on release is supported until the next version is released. For development snapshots, only the latest build is supported. A stable version is supported until the next stable version is released. Both major (typically monthly) and minor (backports and localizations) are grouped under stable versions.

For NVDA releases, StationPlaylist add-on supports latest NVDA releases, including development builds. Unless noted otherwise, past stable NVDA releases are also supported.

For StationPlaylist releases, the add-on supports major releases such as 6.0 and 6.10 for at least four years. Minor releases such as 6.01 and 6.11 are grouped under major releases and are identified with the major release e.g. 6.0x, 6.1x. Up to an additional year of support (via a dedicated long-term support branch) is provided to allow users to upgrade to newer StationPlaylist releases. See below for a list of StationPlaylist releases and support duration from the add-on.

#### Supported StationPlaylist releases

* Versions prior to 5.x: add-on 1.0 to 3.9 (January 2014-June 2015)
* 5.0x: Add-on 1.0 to 7.5, 15.0 to 15.14 (January 2014-April 2018)
* 5.1x: Add-on 3.2 to 18.09.13 (November 2014-December 2019)
* 5.20: Add-on 16.11 to 20.09.7 (November 2016-April 2021)
* 5.3x: Add-on 17.11 to 22.12 (November 2017-December 2022)
* 5.40: Add-on 19.11 to 25.05.4 (November 2019-May 2025)
* 5.50: Add-on 20.11 to 25.06.12 (November 2020-December 2025)
* 6.0x: Add-on 21.11 to 26.04.2 (November 2021-April 2026)
* 6.1x: Add-on 24.03 to 26.04.2 (April 2024-April 2026)
* 6.20: Add-on 25.11 to 26.04.2 (November 2025-April 2026)
