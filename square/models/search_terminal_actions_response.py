from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .terminal_action import TerminalAction, TerminalActionDict


class SearchTerminalActionsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    action: Optional[list[TerminalAction]] = UNSET
    """The requested search result of ``TerminalAction``s."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response.

    See `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
    information."""


class SearchTerminalActionsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    action: NotRequired[list[TerminalActionDict]]
    cursor: NotRequired[str]
