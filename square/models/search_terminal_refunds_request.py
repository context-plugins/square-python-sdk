from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_refund_query import TerminalRefundQuery, TerminalRefundQueryDict


class SearchTerminalRefundsRequest(SdkBaseModel):
    query: Optional[TerminalRefundQuery] = UNSET
    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of
    results for the original query."""

    limit: Optional[int] = UNSET
    """Limits the number of results returned for a single request."""


class SearchTerminalRefundsRequestDict(TypedDict):
    query: NotRequired[TerminalRefundQuery | TerminalRefundQueryDict]
    cursor: NotRequired[str]
    limit: NotRequired[int]
