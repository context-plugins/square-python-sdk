from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .gift_card import GiftCard, GiftCardDict


class RetrieveGiftCardFromGanresponse(SdkBaseModel):
    """A response that contains a ``GiftCard``. This response might contain a set of ``Error`` objects if the request
    resulted in errors."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    gift_card: Optional[GiftCard] = UNSET
    """Represents a Square gift card."""


class RetrieveGiftCardFromGanresponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    gift_card: NotRequired[GiftCardDict]
