from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_action_query import TerminalActionQuery, TerminalActionQueryDict


class SearchTerminalActionsRequest(SdkBaseModel):
    query: Optional[TerminalActionQuery] = UNSET
    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of
    results for the original query. See `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more information."""

    limit: Optional[int] = UNSET
    """Limit the number of results returned for a single request."""


class SearchTerminalActionsRequestDict(TypedDict):
    query: NotRequired[TerminalActionQueryDict]
    cursor: NotRequired[str]
    limit: NotRequired[int]
