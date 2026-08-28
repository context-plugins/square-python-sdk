from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .gift_card import GiftCard, GiftCardDict


class UnlinkCustomerFromGiftCardResponse(SdkBaseModel):
    """A response that contains the unlinked ``GiftCard`` object. If the request resulted in errors, the response
    contains a set of ``Error`` objects."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    gift_card: Optional[GiftCard] = UNSET
    """Represents a Square gift card."""


class UnlinkCustomerFromGiftCardResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    gift_card: NotRequired[GiftCard | GiftCardDict]
