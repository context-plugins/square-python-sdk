from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .terminal_refund import TerminalRefund, TerminalRefundDict


class SearchTerminalRefundsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    refunds: Optional[list[TerminalRefund]] = UNSET
    """The requested search result of ``TerminalRefund`` objects."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response.

    See `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more
    information."""


class SearchTerminalRefundsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    refunds: NotRequired[list[TerminalRefundDict]]
    cursor: NotRequired[str]
