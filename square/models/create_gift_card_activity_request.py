from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .gift_card_activity import GiftCardActivity, GiftCardActivityDict


class CreateGiftCardActivityRequest(SdkBaseModel):
    """A request to create a gift card activity."""

    idempotency_key: str
    """A unique string that identifies the ``CreateGiftCardActivity`` request."""

    gift_card_activity: GiftCardActivity
    """Represents an action performed on a `gift card <entity:GiftCard>`__ that affects its state or balance. A gift
    card activity contains information about a specific activity type. For example, a ``REDEEM`` activity includes a
    ``redeem_activity_details`` field that contains information about the redemption."""


class CreateGiftCardActivityRequestDict(TypedDict):
    idempotency_key: str
    gift_card_activity: GiftCardActivity | GiftCardActivityDict
