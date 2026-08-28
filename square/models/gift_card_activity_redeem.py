from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.gift_card_activity_redeem_status import GiftCardActivityRedeemStatusOrStr
from .money import Money, MoneyDict


class GiftCardActivityRedeem(SdkBaseModel):
    """Represents details about a ``REDEEM`` `gift card activity type <entity:GiftCardActivityType>`__."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    payment_id: Optional[str] = UNSET
    """The ID of the payment that represents the gift card redemption. Square populates this field if the payment was
    processed by Square."""

    reference_id: OptionalNullable[str] = UNSET
    """A client-specified ID that associates the gift card activity with an entity in another system.

    Applications that use a custom payment processing system can use this field to track information related to an order
    or payment."""

    status: Optional[GiftCardActivityRedeemStatusOrStr] = UNSET
    """Indicates the status of a `gift card <entity:GiftCard>`__ redemption. This status is relevant only for
    redemptions made from Square products (such as Square Point of Sale) because Square products use a two-state
    process. Gift cards redeemed using the Gift Card Activities API always have a ``COMPLETED`` status."""


class GiftCardActivityRedeemDict(TypedDict):
    amount_money: Money | MoneyDict
    payment_id: NotRequired[str]
    reference_id: NotRequired[str | None]
    status: NotRequired[GiftCardActivityRedeemStatusOrStr]
