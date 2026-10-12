from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_checkout_query import TerminalCheckoutQuery, TerminalCheckoutQueryDict


class SearchTerminalCheckoutsRequest(SdkBaseModel):
    query: Optional[TerminalCheckoutQuery] = UNSET
    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of
    results for the original query. See `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more information."""

    limit: Optional[int] = UNSET
    """Limits the number of results returned for a single request."""


class SearchTerminalCheckoutsRequestDict(TypedDict):
    query: NotRequired[TerminalCheckoutQueryDict]
    cursor: NotRequired[str]
    limit: NotRequired[int]
