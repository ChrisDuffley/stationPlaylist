# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries

# Since some strings in `addon_info` are translatable,
# we need to include them in the .po files.
# Gettext recognizes only strings given as parameters to the `_` function.
# To avoid initializing translations in this module we simply import a "fake" `_` function
# which returns whatever is given to it as an argument.
from site_scons.site_tools.NVDATool.utils import _


# Add-on information variables
addon_info = AddonInfo(
	# add-on Name/identifier, internal for NVDA
	addon_name="stationPlaylist",
	# Add-on summary/title, usually the user visible name of the add-on
	# Translators: Summary/title for this add-on
	# to be shown on installation and add-on information found in add-on store
	addon_summary=_("StationPlaylist"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-on store
	addon_description=_("Enhances support for StationPlaylist apps. In addition, adds global commands for the Studio application from everywhere."),
	# version
	addon_version="25.11",
	# Brief changelog for this version
	# Translators: what's new content for the add-on version to be shown in the add-on store
	addon_changelog=_("""* Added a setting in add-on settings under status announcements to announce when a cart finishes playing (NVDA will say 'cart stopped').
* In add-on settings/status announcements, cart name checkbox is now cart announcement check list box with the former setting becoming a checkable option.
* In Studio 6.20 and later, SPL Controller can be used to control local Studio and/or Remote Studio. A new setting in add-on settings dialog under Advanced settings panel allows configuring SPL Controller coverage/scope between both local Studio and Remote Studio or one or the other. In earlier Studio releases, SPL Controller layer will control local Studio.
* In local Studio, performing track elapsed (Alt+Shift+T) and remaining time (Control+Alt+T) commands will also announce elapsed and remaining time for the currently playing voice track and/or cart. In addition, pressing SPL Controller, R will announce remaining duration of the playing track, voice track, or cart for local Studio.
* Metadata streaming and status announcements settings panels will not be shown when opening add-on settings screen from Remote Studio.
* Settings to report library scans and listener requests will not be shown in add-on settings when opened from Remote Studio.
* In local Studio, NVDA will announce track starts value correctly (SPL Assistant, S).
* In local Studio, NVDA will no longer announce wrong information when locating various screen information such as weather data if error log button is shown on screen.
* Library scan announcement toggle command (NVDA+Shift+R) is now limited to local Studio.
* Changed the following SPL Assistant JAWS layout commands: hour duration (H to T), hour remaining duration (Shift+H to H), library scan (Shift+R to Alt+T), cart edit/insert (T to number row 0).
* Resolved "Time Scheduled/Time" column announcement and usage in local Studio 6.20, including reporting of wrong column content when vertical column navigation is set to "Time Scheduled", NVDA reporting "Time Scheduled not found" when this column is configured as a columns explorer slot, and wrong column title shown in playlist transcripts.
* Resolved issues working with results from insert tracks dialog in local Studio 6.20, including NVDA saying "Artist not found" when performing columns explorer commands (Control+NVDA+number row) to obtain artist information, wrong column information announced in columns explorer, and top and bottom beeps being heard.
* NVDA will no longer include empty column content when generating playlist transcripts in plain text and HTML list formats.
* In local Studio, NVDA will no longer announce "no track playing" when announcing next track title when no tracks are playing but next track title is showing on screen.
* In Remote Studio, taking playlist snapshots (SPL Assistant, F8) shows more accurate results.
* In Remote Studio, NVDA will no longer do nothing or play error tones when announcing current and next track titles and is configured to announce track player information."""),
	# Author(s)
	addon_author="Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee <joseph.lee22590@gmail.com>, originally by Geoff Shang and other contributors)",
	# URL for the add-on documentation support
	addon_url="https://github.com/ChrisDuffley/stationPlaylist",
	# URL for the add-on repository where the source code can be found
	addon_sourceURL="https://github.com/ChrisDuffley/stationPlaylist",
	# Documentation file name
	addon_docFileName="readme.html",
	# Minimum NVDA version supported (e.g. "2019.3.0", minor version is optional)
	addon_minimumNVDAVersion="2025.1.2",
	# Last NVDA version supported/tested (e.g. "2024.4.0", ideally more recent than minimum version)
	addon_lastTestedNVDAVersion="2025.3.2",
	# Add-on update channel (default is None, denoting stable releases,
	# and for development releases, use "dev".)
	# Do not change unless you know what you are doing!
	addon_updateChannel=None,
	# Add-on license such as GPL 2
	addon_license="GPL v2",
	# URL for the license document the ad-on is licensed under
	addon_licenseURL="https://www.gnu.org/licenses/gpl-2.0.html",
)

# Define the python files that are the sources of your add-on.
# You can either list every file (using ""/") as a path separator,
# or use glob expressions.
# For example to include all files with a ".py" extension from the "globalPlugins" dir of your add-on
# the list can be written as follows:
# pythonSources = ["addon/globalPlugins/*.py"]
# For more information on SCons Glob expressions please take a look at:
# https://scons.org/doc/production/HTML/scons-user/apd.html
pythonSources: list[str] = [
	"addon/*.py",
	"addon/appModules/*.py",
	"addon/appModules/splcommon/*.py",
	"addon/appModules/splstudio/*.py",
	"addon/appModules/splengine/*.py",
	"addon/globalPlugins/splUtils.py"
]

# Files that contain strings for translation. Usually your python sources
i18nSources: list[str] = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
# You can either list every file (using ""/") as a path separator,
# or use glob expressions.
excludedFiles: list[str] = []

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
# You must also edit .gitignore file to specify base language files to be ignored.
baseLanguage: str = "en"

# Markdown extensions for add-on documentation
# Most add-ons do not require additional Markdown extensions.
# If you need to add support for markup such as tables, fill out the below list.
# Extensions string must be of the form "markdown.extensions.extensionName"
# e.g. "markdown.extensions.tables" to add tables.
markdownExtensions: list[str] = []

# Custom braille translation tables
# If your add-on includes custom braille tables (most will not), fill out this dictionary.
# Each key is a dictionary named according to braille table file name,
# with keys inside recording the following attributes:
# displayName (name of the table shown to users and translatable),
# contracted (contracted (True) or uncontracted (False) braille code),
# output (shown in output table list),
# input (shown in input table list).
brailleTables: BrailleTables = {}

# Custom speech symbol dictionaries
# Symbol dictionary files reside in the locale folder, e.g. `locale\en`, and are named `symbols-<name>.dic`.
# If your add-on includes custom speech symbol dictionaries (most will not), fill out this dictionary.
# Each key is the name of the dictionary,
# with keys inside recording the following attributes:
# displayName (name of the speech dictionary shown to users and translatable),
# mandatory (True when always enabled, False when not.
symbolDictionaries: SymbolDictionaries = {}
