from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .terminal_action import TerminalAction, TerminalActionDict


class DismissTerminalActionResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    action: Optional[TerminalAction] = UNSET
    """Represents an action processed by the Square Terminal."""


class DismissTerminalActionResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    action: NotRequired[TerminalAction | TerminalActionDict]
