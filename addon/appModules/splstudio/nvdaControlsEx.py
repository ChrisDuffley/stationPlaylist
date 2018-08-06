# -*- coding: UTF-8 -*-
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2016-2018 NV Access Limited, Derek Riemer
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

# Used in SPL add-on until merged into NVDA directly (Joseph Lee)

from nvdaBuiltin.gui.nvdaControls import *
from . import accPropServer
import oleacc
import winUser
import comtypes
from comtypes import GUID

# Apart from certain controls from check list box and friends, it is identical to NVDA Core version.

# GUIDS for IAccessible properties that can be overridden by means of annotation.
#Use these to look up the GUID needed when implementing a server.
#Number of digits Format: "{8-4-4-4-12}"
PROPID_ACC_NAME = GUID("{608d3df8-8128-4aa7-a428-f55e49267291}")
PROPID_ACC_VALUE = GUID("{123fe443-211a-4615-9527-c45a7e93717a}")
PROPID_ACC_DESCRIPTION = GUID("{4d48dfe4-bd3f-491f-a648-492d6f20c588}")
PROPID_ACC_ROLE = GUID("{CB905FF2-7BD1-4C05-B3C8-E6C241364D70}")
PROPID_ACC_STATE = GUID("{A8D4D5B0-0A21-42D0-A5C0-514E984F457B}")
PROPID_ACC_HELP = GUID("{c831e11f-44db-4a99-9768-cb8f978b7231}")
PROPID_ACC_KEYBOARDSHORTCUT = GUID("{7d9bceee-7d1e-4979-9382-5180f4172c34}")
PROPID_ACC_DEFAULTACTION = GUID("{180c072b-c27f-43c7-9922-f63562a4632b}")
PROPID_ACC_VALUEMAP = GUID("{da1c3d79-fc5c-420e-b399-9d1533549e75}")
PROPID_ACC_ROLEMAP = GUID("{f79acda2-140d-4fe6-8914-208476328269}")
PROPID_ACC_STATEMAP = GUID("{43946c5e-0ac0-4042-b525-07bbdbe17fa7}")
PROPID_ACC_FOCUS = GUID("{6eb335df-1c29-4127-b12c-dee9fd157f2b}")
PROPID_ACC_SELECTION = GUID("{b99d073c-d731-405b-9061-d95e8f842984}")
PROPID_ACC_PARENT = GUID("{474c22b6-ffc2-467a-b1b5-e958b4657330}")
PROPID_ACC_NAV_UP = GUID("{016e1a2b-1a4e-4767-8612-3386f66935ec}")
PROPID_ACC_NAV_LEFT = GUID("{228086cb-82f1-4a39-8705-dcdc0fff92f5}")
PROPID_ACC_NAV_RIGHT = GUID("{cd211d9f-e1cb-4fe5-a77c-920b884d095b}")
PROPID_ACC_NAV_PREV = GUID("{776d3891-c73b-4480-b3f6-076a16a15af6}")
PROPID_ACC_NAV_NEXT = GUID("{1cdc5455-8cd9-4c92-a371-3939a2fe3eee}")
PROPID_ACC_NAV_FIRSTCHILD = GUID("{cfd02558-557b-4c67-84f9-2a09fce40749}")
PROPID_ACC_NAV_LASTCHILD = GUID("{302ecaa5-48d5-4f8d-b671-1a8d20a77832}")

class ListCtrlAccPropServer(accPropServer.IAccPropServer_Impl):
	"""AccPropServer for wx checkable lists which aren't fully accessible."""
	def _getPropValue(self, pIDString, dwIDStringLen, idProp):
		# Import late to prevent circular import.
		from IAccessibleHandler import accPropServices
		handle, objid, childid = accPropServices.DecomposeHwndIdentityString(pIDString, dwIDStringLen)
		if childid != winUser.CHILDID_SELF:
			if idProp == PROPID_ACC_ROLE:
				return oleacc.ROLE_SYSTEM_CHECKBUTTON, 1
			if idProp == PROPID_ACC_STATE:
				states = oleacc.STATE_SYSTEM_SELECTABLE|oleacc.STATE_SYSTEM_FOCUSABLE
				if self.control.IsChecked(childid-1):
					states |= oleacc.STATE_SYSTEM_CHECKED
				if self.control.IsSelected(childid-1):
					# wx doesn't seem to  have a method to check whether a list item is focused.
					# Therefore, assume that a selected item is focused,which is the case in single select list boxes.
					states |= oleacc.STATE_SYSTEM_SELECTED | oleacc.STATE_SYSTEM_FOCUSED
				return states, 1
		return comtypes.automation.VT_EMPTY, 0

#: An array with the GUIDs of the properties that an AccPropServer should override for list controls with checkboxes.
#: The role is supposed to be checkbox, rather than list item.
#: The state should be overridden to include the checkable state as well as the checked state if the item is checked.
CHECK_LIST_PROPS = (comtypes.GUID * 2)(*[PROPID_ACC_ROLE,PROPID_ACC_STATE])

class CustomCheckListBox(wx.CheckListBox):
	"""Custom checkable list to fix a11y bugs in the standard wx checkable list box."""

	def __init__(self, *args, **kwargs):
		super(CustomCheckListBox, self).__init__(*args, **kwargs)
		# Import late to prevent circular import.
		from IAccessibleHandler import accPropServices
		# Register object with COM to fix accessibility bugs in wx.
		server = ListCtrlAccPropServer(self)
		accPropServices.SetHwndPropServer(
			hwnd=self.Handle,
			idObject=winUser.OBJID_CLIENT,
			idChild=0,
			paProps=CHECK_LIST_PROPS,
			cProps=len(CHECK_LIST_PROPS),
			pServer=server,
			AnnoScope=1
		)
		# Register ourself with ourself's selected event, so that we can notify winEvent of the state change.
		self.Bind(wx.EVT_CHECKLISTBOX, self.notifyIAccessible)

	def notifyIAccessible(self, evt):
		# Notify winEvent that something changed.
		# We must do this, so that NVDA receives a stateChange.
		evt.Skip()
		winUser.user32.NotifyWinEvent(winUser.EVENT_OBJECT_STATECHANGE, self.Handle, winUser.OBJID_CLIENT, evt.Selection+1)

class AutoWidthColumnCheckListCtrl(AutoWidthColumnListCtrl, listmix.CheckListCtrlMixin):
	"""
	An L{AutoWidthColumnListCtrl} with accessible checkboxes per item.
	In contrast with L{CustomCheckableListBox}, this class supports multiple columns.
	Also note that this class ignores the L{CheckListCtrlMixin.OnCheckItem} callback.
	If you want to be notified of checked/unchecked events,
	create an event handler for wx.EVT_CHECKLISTBOX.
	This event is only fired when an item is toggled with the mouse or keyboard.
	"""

	def __init__(self, parent, id=wx.ID_ANY, autoSizeColumnIndex="LAST", pos=wx.DefaultPosition, size=wx.DefaultSize, style=0,
		check_image=None, uncheck_image=None, imgsz=(16, 16)
	):
		AutoWidthColumnListCtrl.__init__(self, parent, id=id, pos=pos, size=size, style=style)
		listmix.CheckListCtrlMixin.__init__(self, check_image, uncheck_image, imgsz)
		# Import late to prevent circular import.
		from IAccessibleHandler import accPropServices
		# Register object with COM to fix accessibility bugs in wx.
		server = ListCtrlAccPropServer(self)
		accPropServices.SetHwndPropServer(
			hwnd=self.Handle,
			idObject=winUser.OBJID_CLIENT,
			idChild=0,
			paProps=CHECK_LIST_PROPS,
			cProps=len(CHECK_LIST_PROPS),
			pServer=server,
			AnnoScope=1
		)
		# Register our hook to check/uncheck items with space.
		# Use wx.EVT_CHAR_HOOK, because EVT_LIST_KEY_DOWN isn't triggered for space.
		self.Bind(wx.EVT_CHAR_HOOK, self.onCharHook)
		# Register an additional event handler to call sendCheckListBoxEvent for mouse clicks if appropriate.
		self.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)

	def GetCheckedItems(self):
		return tuple(i for i in xrange(self.ItemCount) if self.IsChecked(i))

	def SetCheckedItems(self, indexes):
		for i in indexes:
			assert 0 <= i < self.ItemCount, "Index (%s) out of range" % i
		for i in xrange(self.ItemCount):
			self.CheckItem(i, i in indexes)

	CheckedItems = property(fget=GetCheckedItems, fset=SetCheckedItems)

	def onCharHook(self,evt):
		key = evt.GetKeyCode()
		if key!=wx.WXK_SPACE:
			evt.Skip()
			return
		index = self.FocusedItem
		if index == -1:
			evt.Skip()
			return
		self.ToggleItem(index)
		self.sendCheckListBoxEvent(index)

	def onLeftDown(self,evt):
		"""Additional event handler for mouse clicks to call L{sendCheckListBoxEvent}."""
		(index, flags) = self.HitTest(evt.GetPosition())
		evt.Skip()
		if flags == wx.LIST_HITTEST_ONITEMICON:
			self.sendCheckListBoxEvent(index)

	def CheckItem(self, index, check=True):
		"""
		Adapted from L{CheckListCtrlMixin} to ignore the OnCheckItem callback and to call L{notifyIAccessible}.
		"""
		img_idx = self.GetItem(index).GetImage()
		if img_idx == 0 and check:
			self.SetItemImage(index, 1)
		elif img_idx == 1 and not check:
			self.SetItemImage(index, 0)
		self.notifyIAccessible(index)

	def notifyIAccessible(self, index):
		# Notify winEvent that something changed.
		# We must do this, so that NVDA receives a stateChange.
		winUser.user32.NotifyWinEvent(winUser.EVENT_OBJECT_STATECHANGE, self.Handle, winUser.OBJID_CLIENT, index+1)

	def sendCheckListBoxEvent(self, index):
		evt = wx.CommandEvent(wx.wxEVT_CHECKLISTBOX,self.Id)
		evt.EventObject = self
		evt.Int = index
		self.ProcessEvent(evt)
