from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.gift_card_activity_clear_balance_reason import GiftCardActivityClearBalanceReasonOrStr


class GiftCardActivityClearBalance(SdkBaseModel):
    """Represents details about a ``CLEAR_BALANCE`` `gift card activity type <entity:GiftCardActivityType>`__."""

    reason: GiftCardActivityClearBalanceReasonOrStr
    """Indicates the reason for clearing the balance of a `gift card <entity:GiftCard>`__."""


class GiftCardActivityClearBalanceDict(TypedDict):
    reason: GiftCardActivityClearBalanceReasonOrStr
