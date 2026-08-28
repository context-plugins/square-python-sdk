from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .gift_card_activity import GiftCardActivity, GiftCardActivityDict


class GiftCardActivityUpdatedEventObject(SdkBaseModel):
    """An object that contains the gift card activity associated with a ``gift_card.activity.updated`` event."""

    gift_card_activity: Optional[GiftCardActivity] = UNSET
    """Represents an action performed on a `gift card <entity:GiftCard>`__ that affects its state or balance. A gift
    card activity contains information about a specific activity type. For example, a ``REDEEM`` activity includes a
    ``redeem_activity_details`` field that contains information about the redemption."""


class GiftCardActivityUpdatedEventObjectDict(TypedDict):
    gift_card_activity: NotRequired[GiftCardActivity | GiftCardActivityDict]
