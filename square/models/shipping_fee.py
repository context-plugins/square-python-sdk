from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class ShippingFee(SdkBaseModel):
    name: OptionalNullable[str] = UNSET
    """The name for the shipping fee."""

    charge: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class ShippingFeeDict(TypedDict):
    name: NotRequired[str | None]
    charge: Money | MoneyDict
