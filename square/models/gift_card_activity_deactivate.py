from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.gift_card_activity_deactivate_reason import GiftCardActivityDeactivateReasonOrStr


class GiftCardActivityDeactivate(SdkBaseModel):
    """Represents details about a ``DEACTIVATE`` `gift card activity type <entity:GiftCardActivityType>`__."""

    reason: GiftCardActivityDeactivateReasonOrStr
    """Indicates the reason for deactivating a `gift card <entity:GiftCard>`__."""


class GiftCardActivityDeactivateDict(TypedDict):
    reason: GiftCardActivityDeactivateReasonOrStr
