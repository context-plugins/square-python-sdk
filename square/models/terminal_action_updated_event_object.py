from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_action import TerminalAction, TerminalActionDict


class TerminalActionUpdatedEventObject(SdkBaseModel):
    action: Optional[TerminalAction] = UNSET
    """Represents an action processed by the Square Terminal."""


class TerminalActionUpdatedEventObjectDict(TypedDict):
    action: NotRequired[TerminalAction | TerminalActionDict]
