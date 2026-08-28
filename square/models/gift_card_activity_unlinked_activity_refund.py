from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class GiftCardActivityUnlinkedActivityRefund(SdkBaseModel):
    """Represents details about an ``UNLINKED_ACTIVITY_REFUND`` `gift card activity type
    <entity:GiftCardActivityType>`__."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    reference_id: OptionalNullable[str] = UNSET
    """A client-specified ID that associates the gift card activity with an entity in another system."""

    payment_id: Optional[str] = UNSET
    """The ID of the refunded payment. This field is not used starting in Square version 2022-06-16."""


class GiftCardActivityUnlinkedActivityRefundDict(TypedDict):
    amount_money: Money | MoneyDict
    reference_id: NotRequired[str | None]
    payment_id: NotRequired[str]
