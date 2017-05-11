# SPL Studio Miscellaneous User Interfaces and internal services
# An app module and global plugin package for NVDA
# Copyright 2015-2017 Joseph Lee and others, released under GPL.
# Miscellaneous functions and user interfaces
# Split from config module in 2015.

# JL's disclaimer: Apart from CSV module, others in this folder are my modules. CSV is part of Python distribution (Copyright Python Software Foundation).

import ctypes
import weakref
import os
from csv import reader # For cart explorer.
import gui
import wx
import ui
from winUser import user32, sendMessage
from spldebugging import debugOutput

# Locate column content.
# Given an object and the column number, locate text in the given column.
# This is the module level version of column content getter found in the app module.
# This is used by the track item class, Track Tool items and in track finder.
# In track finder, this is used when encountering the track item but NVDA says otherwise.
def _getColumnContent(obj, col):
	import winKernel
	from NVDAObjects.IAccessible import sysListView32
	# Borrowed from SysListView32 implementation.
	buffer=None
	processHandle=obj.processHandle
	sizeofLVITEM = ctypes.sizeof(sysListView32.LVITEM)
	internalItem=winKernel.virtualAllocEx(processHandle,None,sizeofLVITEM,winKernel.MEM_COMMIT,winKernel.PAGE_READWRITE)
	try:
		internalText=winKernel.virtualAllocEx(processHandle,None,520,winKernel.MEM_COMMIT,winKernel.PAGE_READWRITE)
		try:
			item=sysListView32.LVITEM(iItem=obj.IAccessibleChildID-1,mask=sysListView32.LVIF_TEXT|sysListView32.LVIF_COLUMNS,iSubItem=col,pszText=internalText,cchTextMax=260)
			winKernel.writeProcessMemory(processHandle,internalItem,ctypes.byref(item),sizeofLVITEM,None)
			len = sendMessage(obj.windowHandle,sysListView32.LVM_GETITEMTEXTW, (obj.IAccessibleChildID-1), internalItem)
			if len:
				winKernel.readProcessMemory(processHandle,internalItem,ctypes.byref(item),sizeofLVITEM,None)
				buffer=ctypes.create_unicode_buffer(len)
				winKernel.readProcessMemory(processHandle,item.pszText,buffer,ctypes.sizeof(buffer),None)
		finally:
			winKernel.virtualFreeEx(processHandle,internalText,0,winKernel.MEM_RELEASE)
	finally:
		winKernel.virtualFreeEx(processHandle,internalItem,0,winKernel.MEM_RELEASE)
	return buffer.value if buffer else None

# A common dialog for Track Finder
_findDialogOpened = False

# Track Finder error dialog.
# This will be refactored into something else.
def _finderError():
	# Translators: Text of the dialog when another find dialog is open.
	gui.messageBox(_("Another find dialog is open."),_("Error"),style=wx.OK | wx.ICON_ERROR)

class SPLFindDialog(wx.Dialog):

	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _findDialogOpened:
			raise RuntimeError("An instance of find dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, obj, text, title, columnSearch=False):
		inst = SPLFindDialog._instance() if SPLFindDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		SPLFindDialog._instance = weakref.ref(self)

		super(SPLFindDialog, self).__init__(parent, wx.ID_ANY, title)
		self.obj = obj
		self.columnSearch = columnSearch
		if not columnSearch:
			findPrompt = _("Enter or select the name or the artist of the track you wish to &search")
		else:
			findPrompt = _("Enter or select text to be &searched in a column")

		mainSizer = wx.BoxSizer(wx.VERTICAL)
		findSizerHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

		findHistory = obj.appModule.findText if obj.appModule.findText is not None else []
		self.findEntry = findSizerHelper.addLabeledControl(findPrompt, wx.ComboBox, choices=findHistory)
		self.findEntry.Value = text

		if columnSearch:
			import splconfig
			# Translators: The label in track finder to search columns.
			self.columnHeaders = findSizerHelper.addLabeledControl(_("C&olumn to search:"), wx.Choice, choices=splconfig._SPLDefaults["ColumnAnnouncement"]["ColumnOrder"])
			self.columnHeaders.SetSelection(0)

		findSizerHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.OK | wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Add(findSizerHelper.sizer, border = gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.Sizer = mainSizer
		self.findEntry.SetFocus()
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)

	def onOk(self, evt):
		global _findDialogOpened
		text = self.findEntry.Value
		# Studio, are you alive?
		if user32.FindWindowA("SPLStudio", None) and text:
			appMod = self.obj.appModule
			column = [self.columnHeaders.Selection+1] if self.columnSearch else None
			startObj = self.obj
			if appMod.findText is None or (len(appMod.findText) and text == appMod.findText[0]):
				startObj = startObj.next
				if appMod.findText is None: appMod.findText = [text]
			# If this is called right away, we land on an invisible window.
			wx.CallLater(100, appMod.trackFinder, text, obj=startObj, column=column)
		self.Destroy()
		_findDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _findDialogOpened
		_findDialogOpened = False


# Time range finder: a variation on track finder.
# Similar to track finder, locate tracks with duration that falls between min and max.
class SPLTimeRangeDialog(wx.Dialog):

	_instance = None

	def __new__(cls, parent, *args, **kwargs):
		# Make this a singleton and prompt an error dialog if it isn't.
		if _findDialogOpened:
			raise RuntimeError("An instance of find dialog is opened")
		inst = cls._instance() if cls._instance else None
		if not inst:
			return super(cls, cls).__new__(cls, parent, *args, **kwargs)
		return inst

	def __init__(self, parent, obj, func):
		inst = SPLTimeRangeDialog._instance() if SPLTimeRangeDialog._instance else None
		if inst:
			return
		# Use a weakref so the instance can die.
		SPLTimeRangeDialog._instance = weakref.ref(self)

		# Translators: The title of a dialog to find tracks with duration within a specified range.
		super(SPLTimeRangeDialog, self).__init__(parent, wx.ID_ANY, _("Time range finder"))
		self.obj = obj
		self.func = func

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		minSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Minimum duration")), wx.HORIZONTAL)
		prompt = wx.StaticText(self, wx.ID_ANY, label=_("Minute"))
		minSizer.Add(prompt)
		self.minMinEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.minMinEntry.SetValue(3)
		self.minMinEntry.SetSelection(-1, -1)
		minSizer.Add(self.minMinEntry)
		prompt = wx.StaticText(self, wx.ID_ANY, label=_("Second"))
		minSizer.Add(prompt)
		self.minSecEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.minSecEntry.SetValue(0)
		self.minSecEntry.SetSelection(-1, -1)
		minSizer.Add(self.minSecEntry)
		mainSizer.Add(minSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		maxSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Maximum duration")), wx.HORIZONTAL)
		prompt = wx.StaticText(self, wx.ID_ANY, label=_("Minute"))
		maxSizer.Add(prompt)
		self.maxMinEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.maxMinEntry.SetValue(5)
		self.maxMinEntry.SetSelection(-1, -1)
		maxSizer.Add(self.maxMinEntry)
		prompt = wx.StaticText(self, wx.ID_ANY, label=_("Second"))
		maxSizer.Add(prompt)
		self.maxSecEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=59)
		self.maxSecEntry.SetValue(0)
		self.maxSecEntry.SetSelection(-1, -1)
		maxSizer.Add(self.maxSecEntry)
		mainSizer.Add(maxSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		mainSizer.AddSizer(self.CreateButtonSizer(wx.OK|wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.minMinEntry.SetFocus()

	def onOk(self, evt):
		minDuration = ((self.minMinEntry.GetValue() * 60) + self.minSecEntry.GetValue()) * 1000
		maxDuration = ((self.maxMinEntry.GetValue() * 60) + self.maxSecEntry.GetValue()) * 1000
		# What if minimum is greater than maximum (subtle oversight)?
		if minDuration >= maxDuration:
			gui.messageBox(
				# Translators: Message to report wrong value for duration fields.
				_("Minimum duration is greater than the maximum duration."),
				# Translators: The title of the message box
				_("Error"), wx.OK|wx.ICON_ERROR,self)
			self.minMinEntry.SetFocus()
			return
		self.Destroy()
		global _findDialogOpened
		if user32.FindWindowA("SPLStudio", None):
			obj = self.obj.next
			# Manually locate tracks here.
			while obj is not None:
				filename = self.func(obj.IAccessibleChildID-1, 211, ret=True)
				if minDuration <= self.func(filename, 30, ret=True) <= maxDuration:
					break
				obj = obj.next
			if obj is not None:
				# This time, set focus once, as doing it twice causes focus problems only if using Studio 5.10 or later.
				obj.setFocus()
				# 16.11: Select the desired track manually.
				self.func(-1, 121)
				self.func(obj.IAccessibleChildID-1, 121)
			else:
				wx.CallAfter(gui.messageBox,
				# Translators: Standard dialog message when an item one wishes to search is not found (copy this from main nvda.po).
				_("No track with duration between minimum and maximum duration."),
				# Translators: Standard error title for find error (copy this from main nvda.po).
				_("Time range find error"),wx.OK|wx.ICON_ERROR)
		_findDialogOpened = False

	def onCancel(self, evt):
		self.Destroy()
		global _findDialogOpened
		_findDialogOpened = False


# Cart Explorer helper.

def _populateCarts(carts, cartlst, modifier, standardEdition=False, refresh=False):
	# The real cart string parser, a helper for cart explorer for building cart entries.
	# 5.2: Discard number row if SPL Standard is in use.
	if standardEdition: cartlst = cartlst[:12]
	for entry in cartlst:
		# An unassigned cart is stored with three consecutive commas, so skip it.
		# 17.04: If refresh is on, the cart we're dealing with is the actual carts dictionary that was built previously.
		noEntry = ",,," in entry
		if noEntry and not refresh: continue
		# Pos between 1 and 12 = function carts, 13 through 24 = number row carts, modifiers are checked.
		pos = cartlst.index(entry)+1
		# If a cart name has commas or other characters, SPL surrounds the cart name with quotes (""), so parse it as well.
		if not entry.startswith('"'): cartName = entry.split(",")[0]
		else: cartName = entry.split('"')[1]
		if pos <= 12: identifier = "f%s"%(pos)
		elif 12 < pos < 22: identifier = str(pos-12)
		elif pos == 22: identifier = "0"
		elif pos == 23: identifier = "-"
		else: identifier = "="
		cart = identifier if not modifier else "+".join([modifier, identifier])
		if noEntry and refresh:
			if cart in carts: del carts[cart]
		else:
			carts[cart] = cartName

# Cart file timestamps.
_cartEditTimestamps = None
		# Initialize Cart Explorer i.e. fetch carts.
# Cart files list is for future use when custom cart names are used.
# if told to refresh, timestamps will be checked and updated banks will be reassigned.
# Carts dictionary is used if and only if refresh is on, as it'll modify live cats.
def cartExplorerInit(StudioTitle, cartFiles=None, refresh=False, carts=None):
	global _cartEditTimestamps
	debugOutput("SPL: refreshing Cart Explorer" if refresh else "SPL: preparing cart Explorer")
	# Use cart files in SPL's data folder to build carts dictionary.
	# use a combination of SPL user name and static cart location to locate cart bank files.
	# Once the cart banks are located, use the routines in the populate method above to assign carts.
	# Since sstandard edition does not support number row carts, skip them if told to do so.
	if carts is None: carts = {"standardLicense":StudioTitle.startswith("StationPlaylist Studio Standard")}
	if refresh: carts["modifiedBanks"] = []
	# Obtain the "real" path for SPL via environment variables and open the cart data folder.
	cartsDataPath = os.path.join(os.environ["PROGRAMFILES"],"StationPlaylist","Data") # Provided that Studio was installed using default path.
	if cartFiles is None:
		# See if multiple users are using SPl Studio.
		userNameIndex = StudioTitle.find("-")
		# Read *.cart files and process the cart entries within (be careful when these cart file names change between SPL releases).
		# Until NVDA core moves to Python 3, assume that file names aren't unicode.
		cartFiles = [u"main carts.cart", u"shift carts.cart", u"ctrl carts.cart", u"alt carts.cart"]
		if userNameIndex >= 0:
			cartFiles = [StudioTitle[userNameIndex+2:]+" "+cartFile for cartFile in cartFiles]
	faultyCarts = False
	if not refresh:
		_cartEditTimestamps = []
	for f in cartFiles:
		# Only do this if told to build cart banks from scratch, as refresh flag is set if cart explorer is active in the first place.
		try:
			mod = f.split()[-2] # Checking for modifier string such as ctrl.
			# Todo: Check just in case some SPL flavors doesn't ship with a particular cart file.
		except IndexError:
			faultyCarts = True # In a rare event that the broadcaster has saved the cart bank with the name like "carts.cart".
			continue
		cartFile = os.path.join(cartsDataPath,f)
		# Cart explorer can safely assume that the cart bank exists if refresh flag is set.
		if not refresh and not os.path.isfile(cartFile): # Cart explorer will fail if whitespaces are in the beginning or at the end of a user name.
			faultyCarts = True
			continue
		debugOutput("SPL: examining carts from file %s"%cartFile)
		cartTimestamp = os.path.getmtime(cartFile)
		if refresh and _cartEditTimestamps[cartFiles.index(f)] == cartTimestamp:
			debugOutput("SPL: no changes to cart bank, skipping")
			continue
		_cartEditTimestamps.append(cartTimestamp)
		with open(cartFile) as cartInfo:
			cl = [row for row in reader(cartInfo)]
		# 17.04 (optimization): let empty string represent main cart bank to avoid this being partially consulted up to 24 times.
		# The below method will just check for string length, which is faster than looking for specific substring.
		_populateCarts(carts, cl[1], mod if mod != "main" else "", standardEdition=carts["standardLicense"], refresh=refresh) # See the comment for _populate method above.
		if not refresh:
			debugOutput("SPL: carts processed so far: %s"%(len(carts)-1))
	carts["faultyCarts"] = faultyCarts
	debugOutput("SPL: total carts processed: %s"%(len(carts)-2))
	return carts

# Refresh carts upon request.
# calls cart explorer init with special (internal) flags.
def cartExplorerRefresh(studioTitle, currentCarts):
	return cartExplorerInit(studioTitle, refresh=True, carts=currentCarts)

# Countdown timer.
# This is utilized by many services, chiefly profile triggers routine.

class SPLCountdownTimer(object):

	def __init__(self, duration, func, threshold):
		# Threshold is used to instruct this timer when to start countdown announcement.
		self.duration = duration
		self.total = duration
		self.func = func
		self.threshold = threshold

	def Start(self):
		self.timer = wx.PyTimer(self.countdown)
		ui.message(_("Countdown started"))
		self.timer.Start(1000)

	def Stop(self):
		self.timer.Stop()

	def IsRunning(self):
		return self.timer.IsRunning()

	def countdown(self):
		self.duration -= 1
		if self.duration == 0:
			ui.message(_("Timer complete"))
			if self.func is not None:
				self.func()
			self.Stop()
		elif 0 < self.duration <= self.threshold:
			ui.message(str(self.duration))


# Module-level version of metadata announcer.
# Moved to this module in 2016 to allow this function to work while Studio window isn't focused.
def _metadataAnnouncer(reminder=False, handle=None):
	import time, nvwave, queueHandler, speech, splconfig
	if handle is None: handle = user32.FindWindowA("SPLStudio", None)
	# If told to remind and connect, metadata streaming will be enabled at this time.
	# 6.0: Call Studio API twice - once to set, once more to obtain the needed information.
	# 6.2/7.0: When Studio API is called, add the value into the stream count list also.
	if reminder:
		for url in xrange(5):
			dataLo = 0x00010000 if splconfig.SPLConfig["MetadataStreaming"]["MetadataEnabled"][url] else 0xffff0000
			sendMessage(handle, 1024, dataLo | url, 36)
	# Gather stream flags.
	# DSP is treated specially.
	dsp = sendMessage(handle, 1024, 0, 36)
	# For others, a simple list.append will do.
	# 17.04: Use a conditional list comprehension.
	streamCount = [str(pos) for pos in xrange(1, 5) if sendMessage(handle, 1024, pos, 36)]
	# Announce streaming status when told to do so.
	status = None
	if not len(streamCount):
		# Translators: Status message for metadata streaming.
		if not dsp: status = _("No metadata streaming URL's defined")
		# Translators: Status message for metadata streaming.
		else: status = _("Metadata streaming configured for DSP encoder")
	elif len(streamCount) == 1:
		# Translators: Status message for metadata streaming.
		if dsp: status = _("Metadata streaming configured for DSP encoder and URL {URL}").format(URL = streamCount[0])
		# Translators: Status message for metadata streaming.
		else: status = _("Metadata streaming configured for URL {URL}").format(URL = streamCount[0])
	else:
		# Translators: Status message for metadata streaming.
		if dsp: status = _("Metadata streaming configured for DSP encoder and URL's {URL}").format(URL = ", ".join(streamCount))
		# Translators: Status message for metadata streaming.
		else: status = _("Metadata streaming configured for URL's {URL}").format(URL = ", ".join(streamCount))
	if reminder:
		time.sleep(2)
		speech.cancelSpeech()
		queueHandler.queueFunction(queueHandler.eventQueue, ui.message, status)
		nvwave.playWaveFile(os.path.join(os.path.dirname(__file__), "SPL_Metadata.wav"))
	else: ui.message(status)

