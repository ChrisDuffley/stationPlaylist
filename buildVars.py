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
	addon_version="26.01",
	# Brief changelog for this version
	# Translators: what's new content for the add-on version to be shown in the add-on store
	addon_changelog=_("""* NVDA 2025.3.2 or later is required.
* Add-on settings screen is now available while using Creator, Remote VT, and Track Tool with different settings for each app.
* NVDA will announce labels for SPL app screens, including track properties, insert tracks dialog's search criteria controls (Studio, Creator, Remote VT), and Studio options dialog.
* In Studio (local and remote), Creator, and Remote VT, NVDA will play a beep when search is completed in insert tracks dialog when NVDA is configured to play beeps for status announcements from SPL add-on settings/general category.
* In Studio (local and remote) and Track Tool, NVDA will no longer announce dialog property content (description) in places such as track properties and Studio options screen.
* In local Studio, NVDA will be less verbose when performing library rescan from insert tracks dialog (Control+Shift+R).
* In local Studio, NVDA will report library scan count regardless of "beep for status announcements" setting from add-on settings.
* In Remote Studio, when closing options screen (Control+O) while cart explorer is active, it is no longer necessary to reenter Cart Explorer to view updated cart assignments.
* Resolved several issues while using insert tracks dialog in Remote Studio, including NVDA saying "scan start" when pressing Control+Shift+R and verbose output for search results status.
* In track list in Creator and Track Tool, pressing Alt+number row keys to change column sort order will cause NVDA to announce the new sort order based on the column selected. There will be a delay when performing these commands in Creator.
* In Creator, Remote VT, and Track Tool, status bar content will be reported when performing read status bar command (NVDA+End/desktop layout, NVDA+Shift+End/laptop layout). In particular, improved status bar content announcement performance in Creator.
* In Creator and Remote VT, NVDA will announce search results count when searching for tracks in insert tracks dialog.
* In Creator and Remote VT, NVDA will no longer appear to do nothing or play error tones when reporting playlist information from playlist editor such as playlist hour and day, scheduled, and rotation."""),
	# Author(s)
	addon_author="Christopher Duffley <nvda@chrisduffley.com> (formerly Joseph Lee <joseph.lee22590@gmail.com>, originally by Geoff Shang and other contributors)",
	# URL for the add-on documentation support
	addon_url="https://github.com/ChrisDuffley/stationPlaylist",
	# URL for the add-on repository where the source code can be found
	addon_sourceURL="https://github.com/ChrisDuffley/stationPlaylist",
	# Documentation file name
	addon_docFileName="readme.html",
	# Minimum NVDA version supported (e.g. "2019.3.0", minor version is optional)
	addon_minimumNVDAVersion="2025.3.2",
	# Last NVDA version supported/tested (e.g. "2024.4.0", ideally more recent than minimum version)
	addon_lastTestedNVDAVersion="2025.3.3",
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
