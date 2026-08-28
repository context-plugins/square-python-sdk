from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .gift_card_activity import GiftCardActivity, GiftCardActivityDict


class ListGiftCardActivitiesResponse(SdkBaseModel):
    """A response that contains a list of ``GiftCardActivity`` objects. If the request resulted in errors, the response
    contains a set of ``Error`` objects."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    gift_card_activities: Optional[list[GiftCardActivity]] = UNSET
    """The requested gift card activities or an empty object if none are found."""

    cursor: Optional[str] = UNSET
    """When a response is truncated, it includes a cursor that you can use in a subsequent request to retrieve the next
    set of activities. If a cursor is not present, this is the final response. For more information, see `Pagination
    <https://developer.squareup.com/docs/working-with-apis/pagination>`__."""


class ListGiftCardActivitiesResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    gift_card_activities: NotRequired[list[GiftCardActivity | GiftCardActivityDict]]
    cursor: NotRequired[str]
