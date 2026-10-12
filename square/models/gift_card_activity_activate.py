from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class GiftCardActivityActivate(SdkBaseModel):
    """Represents details about an ``ACTIVATE`` `gift card activity type <entity:GiftCardActivityType>`__."""

    amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    order_id: OptionalNullable[str] = UNSET
    """The ID of the `order <entity:Order>`__ that contains the ``GIFT_CARD`` line item.

    Applications that use the Square Orders API to process orders must specify the order ID `CreateGiftCardActivity
    <api-endpoint:GiftCardActivities-CreateGiftCardActivity>`__ request."""

    line_item_uid: OptionalNullable[str] = UNSET
    """The UID of the ``GIFT_CARD`` line item in the order that represents the gift card purchase.

    Applications that use the Square Orders API to process orders must specify the line item UID in the
    `CreateGiftCardActivity <api-endpoint:GiftCardActivities-CreateGiftCardActivity>`__ request."""

    reference_id: OptionalNullable[str] = UNSET
    """A client-specified ID that associates the gift card activity with an entity in another system.

    Applications that use a custom order processing system can use this field to track information related to an order
    or payment."""

    buyer_payment_instrument_ids: OptionalNullable[list[str]] = UNSET
    """The payment instrument IDs used to process the gift card purchase, such as a credit card ID or bank account ID.

    Applications that use a custom order processing system must specify payment instrument IDs in the
    `CreateGiftCardActivity <api-endpoint:GiftCardActivities-CreateGiftCardActivity>`__ request. Square uses this
    information to perform compliance checks.

    For applications that use the Square Orders API to process payments, Square has the necessary instrument IDs to
    perform compliance checks.

    Each buyer payment instrument ID can contain a maximum of 255 characters."""


class GiftCardActivityActivateDict(TypedDict):
    amount_money: NotRequired[MoneyDict]
    order_id: NotRequired[str | None]
    line_item_uid: NotRequired[str | None]
    reference_id: NotRequired[str | None]
    buyer_payment_instrument_ids: NotRequired[list[str] | None]
