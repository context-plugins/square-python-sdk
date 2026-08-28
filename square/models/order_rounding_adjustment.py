from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class OrderRoundingAdjustment(SdkBaseModel):
    """A rounding adjustment of the money being returned. Commonly used to apply cash rounding when the minimum unit of
    the account is smaller than the lowest physical denomination of the currency."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID that identifies the rounding adjustment only within this order."""

    name: OptionalNullable[str] = UNSET
    """The name of the rounding adjustment from the original sale order."""

    amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class OrderRoundingAdjustmentDict(TypedDict):
    uid: NotRequired[str | None]
    name: NotRequired[str | None]
    amount_money: NotRequired[Money | MoneyDict]
