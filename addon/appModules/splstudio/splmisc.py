# SPL Studio Miscellaneous User Interfaces and internal services
# An app module and global plugin package for NVDA
# Copyright 2015 Joseph Lee and others, released under GPL.
# Miscellaneous functions and user interfaces
# Split from config module in 2015.

# JL's disclaimer: Apart from CSV module, others in this folder are my modules. CSV is part of Python distribution (Copyright Python Software Foundation).

import ctypes
import weakref
import os
from csv import reader # For cart explorer.
import gui
import wx
from NVDAObjects.IAccessible import sysListView32
from winUser import user32, sendMessage
import winKernel

# Locate column content.
# Given an object and the column number, locate text in the given column.
# This is the module level version of column content getter found in the app module.
# This is used by the track item class, Track Tool items and in track finder.
# In track finder, this is used when encountering the track item but NVDA says otherwise.
def _getColumnContent(obj, col):
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
			findPrompt = _("Enter the name or the artist of the track you wish to &search")
		else:
			findPrompt = _("Enter text to be &searched in a column")

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		findSizer = wx.BoxSizer(wx.HORIZONTAL)
		findMessage = wx.StaticText(self, wx.ID_ANY, label=findPrompt)
		findSizer.Add(findMessage)
		self.findEntry = wx.TextCtrl(self, wx.ID_ANY)
		self.findEntry.SetValue(text)
		findSizer.Add(self.findEntry)
		mainSizer.Add(findSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		if columnSearch:
			columnSizer = wx.BoxSizer(wx.HORIZONTAL)
			# Translators: The label in track finder to search columns.
			label = wx.StaticText(self, wx.ID_ANY, label=_("C&olumn to search:"))
			left = 1 if obj.appModule.productVersion >= "5.10" else 0
			if obj.appModule._columnHeaders is None:
				obj.appModule._columnHeaders = obj.parent.children[-1]
			headers = [header.name for header in obj.appModule._columnHeaders.children[left:]]
			self.columnHeaders = wx.Choice(self, wx.ID_ANY, choices=headers)
			try:
				self.columnHeaders.SetSelection(0)
			except:
				pass
			columnSizer.Add(label)
			columnSizer.Add(self.columnHeaders)
			mainSizer.Add(columnSizer, border=10, flag=wx.BOTTOM)

		mainSizer.AddSizer(self.CreateButtonSizer(wx.OK|wx.CANCEL))
		self.Bind(wx.EVT_BUTTON,self.onOk,id=wx.ID_OK)
		self.Bind(wx.EVT_BUTTON,self.onCancel,id=wx.ID_CANCEL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Center(wx.BOTH | wx.CENTER_ON_SCREEN)
		self.findEntry.SetFocus()

	def onOk(self, evt):
		global _findDialogOpened
		text = self.findEntry.GetValue()
		# Studio, are you alive?
		if user32.FindWindowA("SPLStudio", None) and text:
			appMod = self.obj.appModule
			column = [self.columnHeaders.Selection] if self.columnSearch else None
			if column is not None and appMod.productVersion >= "5.10": column[0]+=1
			startObj = self.obj
			if text == appMod.findText: startObj = startObj.next
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

		super(SPLTimeRangeDialog, self).__init__(parent, wx.ID_ANY, "Time range finder")
		self.obj = obj
		self.func = func

		mainSizer = wx.BoxSizer(wx.VERTICAL)

		minSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Minimum duration")), wx.HORIZONTAL)
		prompt = wx.StaticText(self, wx.ID_ANY, label="Minute")
		minSizer.Add(prompt)
		self.minMinEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=60)
		self.minMinEntry.SetValue(3)
		self.minMinEntry.SetSelection(-1, -1)
		minSizer.Add(self.minMinEntry)
		prompt = wx.StaticText(self, wx.ID_ANY, label="Second")
		minSizer.Add(prompt)
		self.minSecEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=60)
		self.minSecEntry.SetValue(0)
		self.minSecEntry.SetSelection(-1, -1)
		minSizer.Add(self.minSecEntry)
		mainSizer.Add(minSizer,border=20,flag=wx.LEFT|wx.RIGHT|wx.TOP)

		maxSizer = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Maximum duration")), wx.HORIZONTAL)
		prompt = wx.StaticText(self, wx.ID_ANY, label="Minute")
		maxSizer.Add(prompt)
		self.maxMinEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=60)
		self.maxMinEntry.SetValue(5)
		self.maxMinEntry.SetSelection(-1, -1)
		maxSizer.Add(self.maxMinEntry)
		prompt = wx.StaticText(self, wx.ID_ANY, label="Second")
		maxSizer.Add(prompt)
		self.maxSecEntry = wx.SpinCtrl(self, wx.ID_ANY, min=0, max=60)
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
		self.Destroy()
		global _findDialogOpened
		if user32.FindWindowA("SPLStudio", None):
			minDuration = ((self.minMinEntry.GetValue() * 60) + self.minSecEntry.GetValue()) * 1000
			maxDuration = ((self.maxMinEntry.GetValue() * 60) + self.maxSecEntry.GetValue()) * 1000
			obj = self.obj.next
			# Manually locate tracks here.
			while obj is not None:
				filename = self.func(obj.IAccessibleChildID-1, 211, ret=True)
				if minDuration <= self.func(filename, 30, ret=True) <= maxDuration:
					break
				obj = obj.next
			if obj is not None:
				# This time, set focus once, as doing it twice causes focus problems.
				obj.setFocus()
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

def _populateCarts(carts, cartlst, modifier, standardEdition=False):
	# The real cart string parser, a helper for cart explorer for building cart entries.
	# 5.2: Discard number row if SPL Standard is in use.
	if standardEdition: cartlst = cartlst[:12]
	for entry in cartlst:
		# An unassigned cart is stored with three consecutive commas, so skip it.
		if ",,," in entry: continue
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
		if modifier == "main": cart = identifier
		else: cart = "%s+%s"%(modifier, identifier)
		carts[cart] = cartName

# Initialize Cart Explorer i.e. fetch carts.
# Cart files list is for future use when custom cart names are used.
def cartExplorerInit(StudioTitle, cartFiles=None):
	# Use cart files in SPL's data folder to build carts dictionary.
	# use a combination of SPL user name and static cart location to locate cart bank files.
	# Once the cart banks are located, use the routines in the populate method above to assign carts.
	# Since sstandard edition does not support number row carts, skip them if told to do so.
	carts = {"standardLicense":StudioTitle.startswith("StationPlaylist Studio Standard")}
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
	for f in cartFiles:
		try:
			mod = f.split()[-2] # Checking for modifier string such as ctrl.
			# Todo: Check just in case some SPL flavors doesn't ship with a particular cart file.
		except IndexError:
			faultyCarts = True # In a rare event that the broadcaster has saved the cart bank with the name like "carts.cart".
			continue
		cartFile = os.path.join(cartsDataPath,f)
		if not os.path.isfile(cartFile): # Cart explorer will fail if whitespaces are in the beginning or at the end of a user name.
			faultyCarts = True
			continue
		with open(cartFile) as cartInfo:
			cl = [row for row in reader(cartInfo)]
		_populateCarts(carts, cl[1], mod, standardEdition=carts["standardLicense"]) # See the comment for _populate method above.
	carts["faultyCarts"] = faultyCarts
	return carts

