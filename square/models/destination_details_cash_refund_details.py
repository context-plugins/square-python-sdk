from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class DestinationDetailsCashRefundDetails(SdkBaseModel):
    """Stores details about a cash refund. Contains only non-confidential information."""

    seller_supplied_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    change_back_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class DestinationDetailsCashRefundDetailsDict(TypedDict):
    seller_supplied_money: MoneyDict
    change_back_money: NotRequired[MoneyDict]
