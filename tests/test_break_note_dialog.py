import types

BREAK_NOTE_DIALOG_HINT = "Enter your break note"


class FakeObj:
    def __init__(
        self,
        name="",
        windowClassName="",
        role=None,
        states=None,
        parent=None,
        simpleParent=None,
        simpleNext=None,
        simplePrevious=None,
    ):
        self.name = name
        self.windowClassName = windowClassName
        self.role = role
        self.states = states or []
        self.parent = parent
        self.simpleParent = simpleParent
        self.simpleNext = simpleNext
        self.simplePrevious = simplePrevious


def build_break_note_dialog_allowed():
    def breakNoteDialogAllowed(obj, windowClassName):
        if obj is None:
            return False
        if obj.windowClassName != windowClassName:
            return False
        if obj.role != "EDITABLETEXT":
            return False

        fg = FakeObj(name="Insert Tracks")
        if fg is None or fg.name != "Insert Tracks":
            return False

        parent = obj.simpleParent or obj.parent
        group = None
        while parent is not None:
            if (
                parent.name == "Additional Parameters"
                and parent.windowClassName == "TGroupBox"
            ):
                group = parent
                break
            nextParent = parent.simpleParent or parent.parent
            if nextParent is parent:
                break
            parent = nextParent

        if group is None:
            return False

        candidate = group.simpleNext
        if candidate is None:
            parentCandidate = group.parent
            if parentCandidate is not None:
                candidate = parentCandidate.simpleNext
            if candidate is None:
                return False

        if (
            candidate.name == "Track Type"
            and candidate.windowClassName == "TRadioGroup"
        ):
            candidate = candidate.simpleFirstChild

        if candidate is None:
            return False

        if candidate.windowClassName not in ("TGroupButton", "TRadioButton"):
            current = candidate
            while current is not None:
                if current.windowClassName in ("TGroupButton", "TRadioButton"):
                    candidate = current
                    break
                current = current.simpleNext
            if candidate is None or candidate.windowClassName not in ("TGroupButton", "TRadioButton"):
                return False

        first = candidate
        while first.simplePrevious is not None:
            first = first.simplePrevious

        current = first
        while current is not None:
            if (
                current.name in ("Break Note", "Timed Break Note")
                and "CHECKED" in current.states
            ):
                obj.name = BREAK_NOTE_DIALOG_HINT
                return True
            current = current.simpleNext

        return False

    return breakNoteDialogAllowed


def test_normal_layout():
    breakNoteDialogAllowed = build_break_note_dialog_allowed()

    radio = FakeObj(
        name="Break Note",
        windowClassName="TGroupButton",
        role="BUTTON",
        states=["CHECKED"],
    )
    radio.simplePrevious = None
    radio.simpleNext = None

    group = FakeObj(name="Additional Parameters", windowClassName="TGroupBox")
    group.simpleNext = radio

    edit = FakeObj(
        name="EditField",
        windowClassName="TTntMemo.UnicodeClass",
        role="EDITABLETEXT",
        simpleParent=group,
    )

    assert breakNoteDialogAllowed(edit, "TTntMemo.UnicodeClass") is True
    assert edit.name == BREAK_NOTE_DIALOG_HINT


def test_nested_group_layout():
    breakNoteDialogAllowed = build_break_note_dialog_allowed()

    radio = FakeObj(
        name="Timed Break Note",
        windowClassName="TRadioButton",
        role="BUTTON",
        states=["CHECKED"],
    )
    radio.simplePrevious = None
    radio.simpleNext = None

    wrapper = FakeObj(name="Wrapper", windowClassName="TPanel")
    wrapper.simpleNext = radio

    group = FakeObj(name="Additional Parameters", windowClassName="TGroupBox")
    group.simpleNext = wrapper

    edit = FakeObj(
        name="EditField2",
        windowClassName="TTntMemo.UnicodeClass",
        role="EDITABLETEXT",
        simpleParent=group,
    )

    assert breakNoteDialogAllowed(edit, "TTntMemo.UnicodeClass") is True


def test_wrong_window_class():
    breakNoteDialogAllowed = build_break_note_dialog_allowed()

    group = FakeObj(name="Additional Parameters", windowClassName="TGroupBox")
    radio = FakeObj(name="Break Note", windowClassName="TGroupButton", states=["CHECKED"])
    group.simpleNext = radio

    edit = FakeObj(
        name="EditField3",
        windowClassName="OtherClass",
        role="EDITABLETEXT",
        simpleParent=group,
    )

    assert breakNoteDialogAllowed(edit, "TTntMemo.UnicodeClass") is False
