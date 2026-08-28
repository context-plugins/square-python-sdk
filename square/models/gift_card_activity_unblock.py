from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.gift_card_activity_unblock_reason import GiftCardActivityUnblockReasonOrStr


class GiftCardActivityUnblock(SdkBaseModel):
    """Represents details about an ``UNBLOCK`` `gift card activity type <entity:GiftCardActivityType>`__."""

    reason: GiftCardActivityUnblockReasonOrStr
    """Indicates the reason for unblocking a `gift card <entity:GiftCard>`__."""


class GiftCardActivityUnblockDict(TypedDict):
    reason: GiftCardActivityUnblockReasonOrStr
