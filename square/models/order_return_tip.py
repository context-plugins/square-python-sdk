from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class OrderReturnTip(SdkBaseModel):
    """A tip being returned."""

    uid: OptionalNullable[str] = UNSET
    """A unique ID that identifies the tip only within this order."""

    applied_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    source_tender_uid: OptionalNullable[str] = UNSET
    """The tender ``uid`` from the order that contains the original application of this tip."""

    source_tender_id: OptionalNullable[str] = UNSET
    """The tender ``id`` from the order that contains the original application of this tip."""


class OrderReturnTipDict(TypedDict):
    uid: NotRequired[str | None]
    applied_money: NotRequired[Money | MoneyDict]
    source_tender_uid: NotRequired[str | None]
    source_tender_id: NotRequired[str | None]
