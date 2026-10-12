from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .gift_card import GiftCard, GiftCardDict


class ListGiftCardsResponse(SdkBaseModel):
    """A response that contains a list of ``GiftCard`` objects. If the request resulted in errors, the response contains
    a set of ``Error`` objects."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    gift_cards: Optional[list[GiftCard]] = UNSET
    """The requested gift cards or an empty object if none are found."""

    cursor: Optional[str] = UNSET
    """When a response is truncated, it includes a cursor that you can use in a subsequent request to retrieve the next
    set of gift cards. If a cursor is not present, this is the final response. For more information, see `Pagination
    <https://developer.squareup.com/docs/working-with-apis/pagination>`__."""


class ListGiftCardsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    gift_cards: NotRequired[list[GiftCardDict]]
    cursor: NotRequired[str]
