from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .money import Money, MoneyDict


class GiftCardActivityTransferBalanceTo(SdkBaseModel):
    """Represents details about a ``TRANSFER_BALANCE_TO`` `gift card activity type <entity:GiftCardActivityType>`__."""

    transfer_from_gift_card_id: str
    """The ID of the gift card from which the specified amount was transferred."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class GiftCardActivityTransferBalanceToDict(TypedDict):
    transfer_from_gift_card_id: str
    amount_money: MoneyDict
