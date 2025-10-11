"""Shared helpers for StationPlaylist track properties dialogs."""

from __future__ import annotations

from collections import deque

import controlTypes
import ui
from logHandler import log
from NVDAObjects import NVDAObject

import addonHandler

addonHandler.initTranslation()


_LABEL_CACHE: dict[int, str] = {}
_RAW_NAME_CACHE_KEYS: set[int] = set()


def _get_label_cache_key(obj: NVDAObject) -> int | None:
	"""Return a cache key for per-control label reuse."""
	handle = getattr(obj, "windowHandle", None)
	if isinstance(handle, int) and handle:
		return handle
	return None


def _cache_store_label(cacheKey: int | None, label: str) -> None:
	if cacheKey is None:
		return
	if len(_LABEL_CACHE) >= 512:
		_LABEL_CACHE.clear()
		_RAW_NAME_CACHE_KEYS.clear()
	_LABEL_CACHE[cacheKey] = label
	_RAW_NAME_CACHE_KEYS.discard(cacheKey)


def _cache_store_raw_name(cacheKey: int | None) -> None:
	if cacheKey is None:
		return
	if len(_RAW_NAME_CACHE_KEYS) >= 512:
		_LABEL_CACHE.clear()
		_RAW_NAME_CACHE_KEYS.clear()
	_RAW_NAME_CACHE_KEYS.add(cacheKey)
	_LABEL_CACHE.pop(cacheKey, None)


def _truncate_debug_value(value: str | None, limit: int = 120) -> str | None:
	if not value:
		return value
	if len(value) <= limit:
		return value
	return f"{value[: limit - 3]}..."


def is_track_properties_field(obj: NVDAObject) -> bool:
	"""Return True if the NVDAObject is part of the Track Properties dialog."""
	# Use direct window handle approach to avoid recursion
	try:
		import winUser
		hwnd = getattr(obj, "windowHandle", None)
		if not hwnd:
			return False
		
		# Check up to 10 parent windows for the track properties dialog
		for _ in range(10):
			className = winUser.getClassName(hwnd)
			if className == "TTagForm.UnicodeClass":
				return True
			hwnd = winUser.getAncestor(hwnd, winUser.GA_PARENT)
			if not hwnd:
				break
		return False
	except Exception:
		return False

# Control ID to field label mappings for StationPlaylist track properties
_TRACK_PROPERTIES_LABELS: dict[int, str] = {
	# StationPlaylist Studio - Track Info tab
	# Basic track fields
	9634808: "Song Artist",
	4327074: "Song Title", 
	984828: "Album Artist",
	919516: "Album Title",
	
	# Metadata and technical information
	2954694: "Album Track#",
	1121524: "Track Date",
	2229822: "Composer",
	331768: "Conductor",
	462754: "Record Label",
	397286: "ISRC",
	6166324: "CD Code",
	7733566: "URL 1",
	2098340: "URL 2",
	462828: "Other",
	1114448: "Comment",
	528366: "Client",
	
	# File information
	2360108: "Filename",
	
	# StationPlaylist Studio - Categorization tab
	1384388: "Year",
	1378290: "Genre",
	1777526: "Mood",
	2432786: "Region",
	13441666: "Energy",
	4460060: "Tempo",
	1250790: "BPM (0 - 255)",
	3606152: "Rating",
	1448422: "Gender",
	
	# StationPlaylist Studio - Timing tab
	9117666: "Duration",
	1909150: "Intro",
	11149732: "Outro",
	9709228: "Hook Start",
	2040886: "Hook Duration",
	3679206: "Hook Len",
	1648674: "Segue",
	4792566: "Audio Gain",
	3019842: "Segue Time",
	34744030: "Track Date",
	6429736: "Intro Link",
	2628932: "Outro Link",
	
	# StationPlaylist Studio - Schedule Restrictions tab
	# Start section
	11213104: "Start Year",
	1252710: "Start Month", 
	2301266: "Start Day",
	# Finish section
	2694606: "Finish Year",
	1252808: "Finish Month",
	7347406: "Finish Day",
	
	# TrackTool - field mappings from debug logs
	731434: "BPM (0 - 255)",  # BPM field in TrackTool
	2887292: "BPM (0 - 255)",  # BPM field in TrackTool (alternate controlID)
	6362528: "Comment",  # Comment field in TrackTool  
	528824: "Song Artist",  # Song Artist in TrackTool
	463068: "Song Title",   # Song Title in TrackTool
	4334588: "Album Artist", # Album Artist in TrackTool
	993626: "Album Title",   # Album Title in TrackTool
	5253636: "Album Track#", # Album Track# in TrackTool
	725550: "Track Date",    # Track Date in TrackTool
	594378: "Client",        # Client in TrackTool
	6234566: "Other",        # Other in TrackTool
	12920660: "Record Label", # Record Label in TrackTool
	659690: "CD Code",       # CD Code in TrackTool
	7152264: "ISRC",         # ISRC in TrackTool
	1116380: "Conductor",    # Conductor in TrackTool
	725740: "Composer",      # Composer in TrackTool
	529018: "URL 2",         # URL 2 in TrackTool
	1581694: "URL 1",        # URL 1 in TrackTool
	665968: "Year",          # Year in TrackTool Categorization
	665980: "Genre",         # Genre in TrackTool
	665966: "Mood",          # Mood in TrackTool
	665926: "Region",        # Region in TrackTool
	20587818: "Rating",      # Rating in TrackTool
	1249660: "Tempo",        # Tempo in TrackTool
	1381066: "Energy",       # Energy in TrackTool
	4008664: "Gender",       # Gender in TrackTool
	4139736: "Track Date",   # Track Date in TrackTool
}


KNOWN_LABELS = [label.lower() for label in _TRACK_PROPERTIES_LABELS.values()]


_SUFFIX_CANONICAL: dict[str, str] = {
	"value": "value",
	"field": "field",
	"option": "option",
}


_LOGGED_FALLBACKS: set[tuple[int, str | None]] = set()
_FALLBACK_DIAG_DEPTH = 0
_NEAREST_LABEL_LOOKUP_DEPTH = 0


def _dedupe_suffix(label: str | None) -> str | None:
	if not label:
		return label
	tokens = label.strip().split()
	if len(tokens) < 2:
		return label
	last = tokens[-1].strip("\t :-;").lower()
	prev = tokens[-2].strip("\t :-;").lower()
	lastCanon = _SUFFIX_CANONICAL.get(last)
	prevCanon = _SUFFIX_CANONICAL.get(prev)
	if lastCanon and lastCanon == prevCanon:
		tokens.pop()
		return " ".join(tokens)
	return label


class TrackPropertiesLabeledField(NVDAObject):
	"""Provide static/fallback labels for unlabeled Track Properties edit fields."""
	
	@classmethod
	def getKnownControlIDs(cls):
		"""Return set of control IDs that we have labels for."""
		return set(_TRACK_PROPERTIES_LABELS.keys())

	def _get_name(self):
		# Block processing for unwanted Track Tool buttons
		ctrlID = getattr(self, "windowControlID", None)
		if ctrlID == 19799360:  # Track Tool button
			return super()._get_name()  # Use original name without modifications
		
		rawName = super()._get_name()
		setattr(self, "_spl_trackToolRawName", rawName)
		cacheKey = _get_label_cache_key(self)
		if cacheKey is not None:
			if cacheKey in _LABEL_CACHE:
				return _LABEL_CACHE[cacheKey]
			if cacheKey in _RAW_NAME_CACHE_KEYS:
				return rawName
		ctrlID = getattr(self, "windowControlID", None)
		className = self.windowClassName or ""
		if className == "TDateTimePicker" and rawName:
			rawName = None
		app_name = getattr(getattr(self, "appModule", None), "appName", "")
		label = _TRACK_PROPERTIES_LABELS.get(ctrlID)
		if not label and rawName:
			raw_preview = _truncate_debug_value(rawName)
			log.debug("TrackProperties rawName ctrlID=%r class=%r rawName=%r", ctrlID, className, raw_preview)
		if app_name == "tracktool":
			if not label:
				label = self._inferLabelTrackTool()
			if label:
				label = _dedupe_suffix(label) or label
				log.debug("TrackProperties inferred label ctrlID=%r label=%r", ctrlID, label)
				_cache_store_label(cacheKey, label)
				return label
		else:
			if label:
				_cache_store_label(cacheKey, label)
				return label
			label = self._simpleFallbackLabel(className, rawName)
			if label:
				label = _dedupe_suffix(label) or label
				_cache_store_label(cacheKey, label)
				return label
		log.debug(
			"TrackProperties label missing ctrlID=%r class=%r parentCtrlID=%r location=%r",
			ctrlID,
			className,
			getattr(getattr(self, "parent", None), "windowControlID", None),
			getattr(self, "location", None),
		)
		_cache_store_raw_name(cacheKey)
		return rawName


	def _match_known_label(self, rawName: str | None) -> str | None:
		if not rawName:
			return None
		raw_lower = rawName.lower()
		matches: list[tuple[int, str]] = []
		for label, label_lower in ((lbl, lbl.lower()) for lbl in _TRACK_PROPERTIES_LABELS.values()):
			index = raw_lower.find(label_lower)
			if index != -1:
				matches.append((index, label))
		if matches:
			matches.sort(key=lambda item: (item[0], len(item[1])))
			return matches[0][1]
		return None

	def _simpleFallbackLabel(self, className: str, rawName: str | None) -> str | None:
		parent = getattr(self, "parent", None)
		if parent is None:
			return None
		try:
			labels = parent._spl_tpFallbackLabels  # type: ignore[attr-defined]
		except AttributeError:
			labels = {}
			setattr(parent, "_spl_tpFallbackLabels", labels)
		ctrlID = getattr(self, "windowControlID", None)
		if isinstance(ctrlID, int) and ctrlID in labels:
			return labels[ctrlID]
		parent_name = getattr(parent, "name", None) or "Track Properties"
		parent_class = getattr(parent, "windowClassName", "") or ""
		class_lower = className.lower()
		label = self._match_known_label(rawName)
		nearest_labels: list[tuple[int, int | None, str | None, tuple[int, int, int, int]]] | None = None
		if not label:
			nearest_labels = self._collect_nearest_labels(limit=6)
			label = self._label_from_nearest(nearest_labels)
		if not label and class_lower == "tedit" and parent_name.strip().lower() == "track properties":
			label = "Track Info"
		if not label:
			if class_lower == "tdatetimepicker":
				suffix = 'time' if rawName and ":" in rawName else 'date'
				label = f"{parent_name} {suffix}"
			elif class_lower in {"tspinedit", "tspineditms"}:
				label = f"{parent_name} value"
			elif class_lower in {"ttntedit.unicodeclass", "tedit", "ttntmemo.unicodeclass"}:
				label = f"{parent_name} value"
			elif class_lower in {"ttntcombobox.unicodeclass", "tcombobox", "ttntcombobox"}:
				prefix = f"{parent_name} option"
				index = sum(1 for existing in labels.values() if isinstance(existing, str) and existing.startswith(prefix)) + 1
				label = f"{prefix} {index}"
			else:
				prefix = f"{parent_name} field"
				index = sum(1 for existing in labels.values() if isinstance(existing, str) and existing.startswith(prefix)) + 1
				label = f"{prefix} {index}"
		if not label and rawName:
			label = rawName
		label = _dedupe_suffix(label) or label
		if isinstance(ctrlID, int):
			labels[ctrlID] = label
		value_preview = _truncate_debug_value(getattr(self, "windowText", None))
		log.debug(
			"TrackProperties simple fallback ctrlID=%r parent=%r parentClass=%r class=%r fallback=%r value=%r",
			ctrlID,
			parent_name,
			parent_class,
			className,
			label,
			value_preview,
		)
		self._logFallbackDiagnostics(ctrlID, label, nearest_labels)
		return label

	def _get_value(self):
		className = self.windowClassName or ""
		value = super()._get_value()
		if value in (None, ""):
			value = getattr(self, "windowText", None)
		rawName = getattr(self, "_spl_trackToolRawName", None)
		if className == "TDateTimePicker":
			return str(rawName or value or "")
		if className in {
			"TSpinEdit",
			"TSpinEditMS",
			"TTntComboBox.UnicodeClass",
			"TComboBox",
			"TTntComboBox",
		}:
			if value in (None, ""):
				# Special handling for fields with incorrect rawName
				ctrlID = getattr(self, "windowControlID", None)
				if ctrlID == 9709228:  # Hook Start - don't use rawName as value
					value = ""
				else:
					value = rawName
			return str(value or "")
		return value

	def _announceLabelAndValue(self) -> None:
		label = self.name
		valueText = str(self._get_value() or "").strip()
		value_preview = _truncate_debug_value(valueText)
		log.debug(
			"TrackProperties announce ctrlID=%r class=%r label=%r value=%r",
			getattr(self, "windowControlID", None),
			self.windowClassName,
			label,
			value_preview,
		)
		if valueText and len(valueText) > 200:
			spokenValue = f"{valueText[:197]}..."
		else:
			spokenValue = valueText
		if spokenValue and label and spokenValue.lower() != label.lower():
			ui.message(f"{label} {spokenValue}")
		elif spokenValue and not label:
			ui.message(spokenValue)
		elif label:
			ui.message(label)

	def _inferLabelTrackTool(self) -> str | None:
		ctrlID = getattr(self, "windowControlID", None)
		parent = getattr(self, "parent", None)
		visited: set[int] = set()
		while parent is not None:
			if parent is self or getattr(parent, "windowControlID", None) == ctrlID:
				parent = getattr(parent, "parent", None)
				continue
			parentID = id(parent)
			if parentID in visited:
				break
			visited.add(parentID)
			log.debug(
				"TrackProperties infer label: field ctrlID=%r parentClass=%r parentCtrlID=%r",
				ctrlID,
				getattr(parent, "windowClassName", None),
				getattr(parent, "windowControlID", None),
			)
			try:
				labels = parent._spl_trackToolFieldLabels  # type: ignore[attr-defined]
			except AttributeError:
				labels = self._buildLabelCache(parent)
			label = labels.get(ctrlID)
			if label:
				return label
			parent = getattr(parent, "parent", None)
		return None

	def _buildLabelCache(self, parent: NVDAObject) -> dict[int, str]:
		parent_class = getattr(parent, "windowClassName", "") or ""
		labels: dict[int, str] = {}
		try:
			children = list(parent.children)
		except Exception:
			children = []
		if not children:
			return {}
		if len(children) > 120:
			log.debug(
				"TrackProperties label inference skip parent=%r class=%r childCount=%d",
				getattr(parent, "windowControlID", None),
				parent_class,
				len(children),
			)
			return {}
		labelCandidates: list[tuple[str, tuple[int, int, int, int]]] = []
		fieldCandidates: list[tuple[int, tuple[int, int, int, int], NVDAObject]] = []
		for child in children:
			ctrlID = getattr(child, "windowControlID", None)
			role = getattr(child, "role", None)
			rectObj = getattr(child, "location", None)
			rect = self._normalizeRect(rectObj)
			if rect is None:
				continue
			if role == controlTypes.Role.STATICTEXT and child.name:
				labelCandidates.append((child.name, rect))
			elif (
				role in (
					controlTypes.Role.EDITABLETEXT,
					controlTypes.Role.COMBOBOX,
					controlTypes.Role.SPINBUTTON,
				)
				or getattr(child, "windowClassName", None) == "TDateTimePicker"
			) and isinstance(ctrlID, int):
				fieldCandidates.append((ctrlID, rect, child))
		log.debug(
			"TrackProperties label inference: parent=%r %d labels, %d fields",
			getattr(parent, "windowControlID", None),
			len(labelCandidates),
			len(fieldCandidates),
		)
		for name, rect in labelCandidates:
			log.debug("TrackProperties label candidate name=%r rect=%r", name, rect)
		for ctrlID, rect, _obj in fieldCandidates:
			log.debug("TrackProperties field candidate ctrlID=%r rect=%r", ctrlID, rect)
		for ctrlID, editRect, childObj in fieldCandidates:
			labelName = self._matchLabelByGeometry(ctrlID, editRect, labelCandidates)
			if labelName:
				labelName = _dedupe_suffix(labelName) or labelName
				if labelName == "(0 - 255)" and any(name.strip().upper() == "BPM" for name, _ in labelCandidates):
					labelName = _("BPM (0 - 255)")
				labels[ctrlID] = labelName
				log.debug("TrackProperties inferred label ctrlID=%r -> %r", ctrlID, labelName)
			else:
				log.debug("TrackProperties no inferred label for ctrlID=%r rect=%r", ctrlID, editRect)
		remaining = [(ctrlID, rect, childObj) for ctrlID, rect, childObj in fieldCandidates if ctrlID not in labels]
		if remaining:
			remaining.sort(key=lambda item: (item[1][1], item[1][0]))
			for index, (ctrlID, rect, childObj) in enumerate(remaining, start=1):
				fallback = self._fallbackGroupLabel(parent, childObj, index)
				if fallback:
					labels[ctrlID] = fallback
					log.debug("TrackProperties fallback label ctrlID=%r -> %r", ctrlID, fallback)
		setattr(parent, "_spl_trackToolFieldLabels", labels)
		return labels

	def _fallbackGroupLabel(self, parent: NVDAObject, child: NVDAObject, index: int) -> str | None:
		parentName = getattr(parent, "name", None)
		if not parentName:
			return None
		className = getattr(child, "windowClassName", "") or ""
		rawName = getattr(child, "_spl_trackToolRawName", None)
		ctrlID = getattr(child, "windowControlID", None)
		location = getattr(child, "location", None)
		value_preview = _truncate_debug_value(getattr(child, "windowText", None))
		if className == "TDateTimePicker":
			suffix = 'time' if rawName and ":" in rawName else 'date'
			label = _dedupe_suffix(f"{parentName} {suffix}") or f"{parentName} {suffix}"
		elif className in {
			"TTntComboBox.UnicodeClass",
			"TComboBox",
			"TTntComboBox",
		}:
			label = _dedupe_suffix(f"{parentName} option {index}") or f"{parentName} option {index}"
		elif className in {
			"TTntEdit.UnicodeClass",
			"TEdit",
			"TTntMemo.UnicodeClass",
		}:
			label = _dedupe_suffix(f"{parentName} value") or f"{parentName} value"
		else:
			label = _dedupe_suffix(f"{parentName} field {index}") or f"{parentName} field {index}"
		log.debug(
			"TrackProperties fallback ctrlID=%r parent=%r index=%d class=%r label=%r location=%r value=%r",
			ctrlID,
			parentName,
			index,
			className,
			label,
			location,
			value_preview,
		)
		self._logFallbackDiagnostics(ctrlID, label, None)
		return label

	def _collect_nearest_labels(self, limit: int = 5) -> list[tuple[int, int | None, str | None, tuple[int, int, int, int]]]:
		fieldRect = self._normalizeRect(getattr(self, "location", None))
		root = self._findDialogRoot()
		if fieldRect is None or root is None:
			return []
		global _NEAREST_LABEL_LOOKUP_DEPTH
		if _NEAREST_LABEL_LOOKUP_DEPTH > 0:
			return []
		_NEAREST_LABEL_LOOKUP_DEPTH += 1
		nearest: list[tuple[int, int | None, str | None, tuple[int, int, int, int]]] = []
		queue: deque[NVDAObject] = deque([root])
		visited: set[int] = set()
		try:
			while queue:
				obj = queue.popleft()
				obj_id = id(obj)
				if obj_id in visited:
					continue
				visited.add(obj_id)
				try:
					children = list(obj.children)
				except Exception:
					children = []
				for child in children:
					if child is self:
						continue
					queue.append(child)
					if getattr(child, "role", None) != controlTypes.Role.STATICTEXT:
						continue
					rect = self._normalizeRect(getattr(child, "location", None))
					if rect is None:
						continue
					text = _truncate_debug_value(getattr(child, "windowText", None))
					if not text:
						ia = getattr(child, "IAccessibleObject", None)
						childID = getattr(child, "IAccessibleObjectChildID", 0)
						if ia is not None:
							try:
								text = _truncate_debug_value(ia.accName(childID))
							except Exception:
								text = None
					if not text:
						continue
					distance = self._rect_distance(fieldRect, rect)
					nearest.append((distance, getattr(child, "windowControlID", None), text, rect))
		finally:
			_NEAREST_LABEL_LOOKUP_DEPTH -= 1
		nearest.sort(key=lambda item: item[0])
		if limit and len(nearest) > limit:
			return nearest[:limit]
		return nearest

	def _label_from_nearest(
		self,
		nearest_labels: list[tuple[int, int | None, str | None, tuple[int, int, int, int]]] | None,
	) -> str | None:
		if not nearest_labels:
			return None
		for _distance, _neighborID, text, _rect in nearest_labels:
			if not text:
				continue
			candidate = text.strip().strip(":")
			if not candidate:
				continue
			candidate = _dedupe_suffix(candidate) or candidate
			if candidate.lower() in KNOWN_LABELS:
				return candidate
		generic = {"track properties"}
		for _distance, _neighborID, text, _rect in nearest_labels:
			if not text:
				continue
			candidate = text.strip().strip(":")
			if not candidate or candidate.lower() in generic:
				continue
			candidate = _dedupe_suffix(candidate) or candidate
			return candidate
		return None

	def _logFallbackDiagnostics(
		self,
		ctrlID: int | None,
		label: str | None,
		nearest_labels: list[tuple[int, int | None, str | None, tuple[int, int, int, int]]] | None,
	) -> None:
		fieldRect = self._normalizeRect(getattr(self, "location", None))
		if not isinstance(ctrlID, int):
			return
		key = (ctrlID, label)
		if key in _LOGGED_FALLBACKS:
			return
		_LOGGED_FALLBACKS.add(key)
		global _FALLBACK_DIAG_DEPTH
		if _FALLBACK_DIAG_DEPTH > 0:
			return
		log.debug(
			"TrackProperties fallback diag ctrlID=%r label=%r fieldRect=%r",
			ctrlID,
			label,
			fieldRect,
		)
		if nearest_labels is None:
			nearest_labels = self._collect_nearest_labels(limit=5)
		if not nearest_labels:
			return
		for distance, neighborID, text, rect in nearest_labels[:5]:
			log.debug(
				"TrackProperties fallback nearest label ctrlID=%r neighborCtrlID=%r label=%r distance=%r rect=%r",
				ctrlID,
				neighborID,
				text,
				distance,
				rect,
			)

	@staticmethod
	def _rect_distance(rect1: tuple[int, int, int, int], rect2: tuple[int, int, int, int]) -> int:
		x1, y1, w1, h1 = rect1
		x2, y2, w2, h2 = rect2
		cx1 = x1 + w1 // 2
		cy1 = y1 + h1 // 2
		cx2 = x2 + w2 // 2
		cy2 = y2 + h2 // 2
		return abs(cx1 - cx2) + abs(cy1 - cy2)

	def _findDialogRoot(self) -> NVDAObject | None:
		ancestor = getattr(self, "parent", None)
		visited: set[int] = set()
		while ancestor is not None:
			if id(ancestor) in visited:
				break
			visited.add(id(ancestor))
			class_name = getattr(ancestor, "windowClassName", "") or ""
			if class_name == "TTagForm.UnicodeClass":
				return ancestor
			ancestor = getattr(ancestor, "parent", None)
		return getattr(self, "parent", None)

	@staticmethod
	def _matchLabelByGeometry(
		ctrlID: int,
		editRect: tuple[int, int, int, int],
		labelCandidates: list[tuple[str, tuple[int, int, int, int]]],
	) -> str | None:
		editLeft, editTop, editWidth, editHeight = editRect
		editCenterY = editTop + (editHeight // 2)
		bestLabel: str | None = None
		bestDistance: int | None = None
		editRight = editLeft + editWidth
		for name, (labelLeft, labelTop, labelWidth, labelHeight) in labelCandidates:
			labelCenterY = labelTop + (labelHeight // 2)
			verticalDistance = abs(labelCenterY - editCenterY)
			labelRight = labelLeft + labelWidth
			if labelLeft >= editRight:
				horizontalGap = labelLeft - editRight
				horizontalPenalty = horizontalGap + max(editWidth // 2, 40)
			elif labelRight <= editLeft:
				horizontalGap = editLeft - labelRight
				horizontalPenalty = horizontalGap
			else:
				horizontalGap = 0
				horizontalPenalty = 0
			if horizontalGap > max(editWidth, 200):
				log.debug(
					"TrackProperties geometry skip label=%r for ctrlID=%r: horizontalGap=%r editWidth=%r",
					name,
					ctrlID,
					horizontalGap,
					editWidth,
				)
				continue
			labelLower = name.strip().lower()
			unitPenalty = 0
			if labelLower in {"sec", "dsec", "db"} or (
				labelLower.startswith("(") and labelLower.endswith(")")
			):
				unitPenalty = max(editHeight, 40)
			score = verticalDistance + (horizontalPenalty // 2) + unitPenalty
			if bestDistance is None or score < bestDistance:
				bestLabel = name
				bestDistance = score
		if bestDistance is not None and bestDistance <= max(editHeight, 40) + (editWidth // 2):
			log.debug(
				"TrackProperties geometry match ctrlID=%r bestLabel=%r distance=%r threshold=%r",
				ctrlID,
				bestLabel,
				bestDistance,
				max(editHeight, 40) + (editWidth // 2),
			)
			return bestLabel
		log.debug(
			"TrackProperties geometry no match ctrlID=%r bestDistance=%r editRect=%r",
			ctrlID,
			bestDistance,
			editRect,
		)
		return None

	@staticmethod
	def _normalizeRect(rectObj) -> tuple[int, int, int, int] | None:
		if rectObj is None:
			return None
		if isinstance(rectObj, tuple) and len(rectObj) == 4:
			left, top, width, height = rectObj
			return int(left), int(top), int(width), int(height)
		for attr in ("left", "top", "width", "height"):
			if not hasattr(rectObj, attr):
				break
		else:
			left = int(getattr(rectObj, "left"))
			top = int(getattr(rectObj, "top"))
			width = int(getattr(rectObj, "width"))
			height = int(getattr(rectObj, "height"))
			return (left, top, width, height)
		return None

	def event_valueChange(self):
		className = self.windowClassName or ""
		ctrlID = getattr(self, "windowControlID", None)
		label = self.name
		valueText = str(self._get_value() or "").strip()
		log.debug("TrackProperties valueChange class=%r ctrlID=%r label=%r value=%r", className, ctrlID, label, valueText)
		if className in {
			"TDateTimePicker",
			"TSpinEdit",
			"TSpinEditMS",
			"TTntComboBox.UnicodeClass",
			"TComboBox",
			"TTntComboBox",
		}:
			if not valueText:
				super().event_valueChange()
			else:
				self._announceLabelAndValue()
			return
		super().event_valueChange()

	def event_gainFocus(self):
		# Block focus announcement on unwanted buttons, but allow normal navigation
		ctrlID = getattr(self, "windowControlID", None)
		if ctrlID == 19799360:  # Track Tool button - don't announce but allow navigation
			super().event_gainFocus()
			return  # Block announcement but allow focus
		
		super().event_gainFocus()
		if self.windowClassName in {
			"TDateTimePicker",
			"TSpinEdit",
			"TSpinEditMS",
			"TTntComboBox.UnicodeClass",
			"TComboBox",
			"TTntComboBox",
		}:
			self._announceLabelAndValue()