from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_event import LoyaltyEvent, LoyaltyEventDict


class SearchLoyaltyEventsResponse(SdkBaseModel):
    """A response that contains loyalty events that satisfy the search criteria, in order by the ``created_at`` date."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    events: Optional[list[LoyaltyEvent]] = UNSET
    """The loyalty events that satisfy the search criteria."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response. For more
    information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class SearchLoyaltyEventsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    events: NotRequired[list[LoyaltyEventDict]]
    cursor: NotRequired[str]
