from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gift_card import GiftCard, GiftCardDict


class GiftCardUpdatedEventObject(SdkBaseModel):
    """An object that contains the gift card associated with a ``gift_card.updated`` event."""

    gift_card: Optional[GiftCard] = UNSET
    """Represents a Square gift card."""


class GiftCardUpdatedEventObjectDict(TypedDict):
    gift_card: NotRequired[GiftCard | GiftCardDict]
