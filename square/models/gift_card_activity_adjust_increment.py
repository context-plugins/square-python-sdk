from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.gift_card_activity_adjust_increment_reason import GiftCardActivityAdjustIncrementReasonOrStr
from .money import Money, MoneyDict


class GiftCardActivityAdjustIncrement(SdkBaseModel):
    """Represents details about an ``ADJUST_INCREMENT`` `gift card activity type <entity:GiftCardActivityType>`__."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    reason: GiftCardActivityAdjustIncrementReasonOrStr
    """Indicates the reason for adding money to a `gift card <entity:GiftCard>`__."""


class GiftCardActivityAdjustIncrementDict(TypedDict):
    amount_money: Money | MoneyDict
    reason: GiftCardActivityAdjustIncrementReasonOrStr
