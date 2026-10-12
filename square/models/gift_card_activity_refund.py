from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class GiftCardActivityRefund(SdkBaseModel):
    """Represents details about a ``REFUND`` `gift card activity type <entity:GiftCardActivityType>`__."""

    redeem_activity_id: OptionalNullable[str] = UNSET
    """The ID of the refunded ``REDEEM`` gift card activity. Square populates this field if the ``payment_id`` in the
    corresponding `RefundPayment <api-endpoint:Refunds-RefundPayment>`__ request represents a gift card redemption.

    For applications that use a custom payment processing system, this field is required when creating a ``REFUND``
    activity. The provided ``REDEEM`` activity ID must be linked to the same gift card."""

    amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    reference_id: OptionalNullable[str] = UNSET
    """A client-specified ID that associates the gift card activity with an entity in another system."""

    payment_id: Optional[str] = UNSET
    """The ID of the refunded payment. Square populates this field if the refund is for a payment processed by Square.
    This field matches the ``payment_id`` in the corresponding `RefundPayment <api-endpoint:Refunds-RefundPayment>`__
    request."""


class GiftCardActivityRefundDict(TypedDict):
    redeem_activity_id: NotRequired[str | None]
    amount_money: NotRequired[MoneyDict]
    reference_id: NotRequired[str | None]
    payment_id: NotRequired[str]
