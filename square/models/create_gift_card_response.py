from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .gift_card import GiftCard, GiftCardDict


class CreateGiftCardResponse(SdkBaseModel):
    """A response that contains a ``GiftCard``. The response might contain a set of ``Error`` objects if the request
    resulted in errors."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    gift_card: Optional[GiftCard] = UNSET
    """Represents a Square gift card."""


class CreateGiftCardResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    gift_card: NotRequired[GiftCard | GiftCardDict]
