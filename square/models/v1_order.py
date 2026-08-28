from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict
from .enums.v1_order_state import V1OrderStateOrStr
from .error import Error, ErrorDict
from .v1_money import V1Money, V1MoneyDict
from .v1_order_history_entry import V1OrderHistoryEntry, V1OrderHistoryEntryDict
from .v1_tender import V1Tender, V1TenderDict


class V1Order(SdkBaseModel):
    """V1Order"""

    errors: Optional[list[Error | None]] = UNSET
    """Any errors that occurred during the request."""

    id: Optional[str] = UNSET
    """The order's unique identifier."""

    buyer_email: OptionalNullable[str] = UNSET
    """The email address of the order's buyer."""

    recipient_name: OptionalNullable[str] = UNSET
    """The name of the order's buyer."""

    recipient_phone_number: OptionalNullable[str] = UNSET
    """The phone number to use for the order's delivery."""

    state: Optional[V1OrderStateOrStr] = UNSET
    shipping_address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    subtotal_money: Optional[V1Money] = UNSET
    total_shipping_money: Optional[V1Money] = UNSET
    total_tax_money: Optional[V1Money] = UNSET
    total_price_money: Optional[V1Money] = UNSET
    total_discount_money: Optional[V1Money] = UNSET
    created_at: Optional[str] = UNSET
    """The time when the order was created, in ISO 8601 format."""

    updated_at: Optional[str] = UNSET
    """The time when the order was last modified, in ISO 8601 format."""

    expires_at: OptionalNullable[str] = UNSET
    """The time when the order expires if no action is taken, in ISO 8601 format."""

    payment_id: OptionalNullable[str] = UNSET
    """The unique identifier of the payment associated with the order."""

    buyer_note: OptionalNullable[str] = UNSET
    """A note provided by the buyer when the order was created, if any."""

    completed_note: OptionalNullable[str] = UNSET
    """A note provided by the merchant when the order's state was set to COMPLETED, if any"""

    refunded_note: OptionalNullable[str] = UNSET
    """A note provided by the merchant when the order's state was set to REFUNDED, if any."""

    canceled_note: OptionalNullable[str] = UNSET
    """A note provided by the merchant when the order's state was set to CANCELED, if any."""

    tender: Optional[V1Tender] = UNSET
    """A tender represents a discrete monetary exchange. Square represents this exchange as a money object with a
    specific currency and amount, where the amount is given in the smallest denomination of the given currency.

    Square POS can accept more than one form of tender for a single payment (such as by splitting a bill between a
    credit card and a gift card). The ``tender`` field of the Payment object lists all forms of tender used for the
    payment.

    Split tender payments behave slightly differently from single tender payments:

    The receipt_url for a split tender corresponds only to the first tender listed in the tender field. To get the
    receipt URLs for the remaining tenders, use the receipt_url fields of the corresponding Tender objects.

    *A note on gift cards**: when a customer purchases a Square gift card from a merchant, the merchant receives the
    full amount of the gift card in the associated payment.

    When that gift card is used as a tender, the balance of the gift card is reduced and the merchant receives no funds.
    A ``Tender`` object with a type of ``SQUARE_GIFT_CARD`` indicates a gift card was used for some or all of the
    associated payment."""

    order_history: Optional[list[V1OrderHistoryEntry | None]] = UNSET
    """The history of actions associated with the order."""

    promo_code: OptionalNullable[str] = UNSET
    """The promo code provided by the buyer, if any."""

    btc_receive_address: OptionalNullable[str] = UNSET
    """For Bitcoin transactions, the address that the buyer sent Bitcoin to."""

    btc_price_satoshi: OptionalNullable[float] = UNSET
    """For Bitcoin transactions, the price of the buyer's order in satoshi (100 million satoshi equals 1 BTC)."""


class V1OrderDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict | None]]
    id: NotRequired[str]
    buyer_email: NotRequired[str | None]
    recipient_name: NotRequired[str | None]
    recipient_phone_number: NotRequired[str | None]
    state: NotRequired[V1OrderStateOrStr]
    shipping_address: NotRequired[Address | AddressDict]
    subtotal_money: NotRequired[V1Money | V1MoneyDict]
    total_shipping_money: NotRequired[V1Money | V1MoneyDict]
    total_tax_money: NotRequired[V1Money | V1MoneyDict]
    total_price_money: NotRequired[V1Money | V1MoneyDict]
    total_discount_money: NotRequired[V1Money | V1MoneyDict]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    expires_at: NotRequired[str | None]
    payment_id: NotRequired[str | None]
    buyer_note: NotRequired[str | None]
    completed_note: NotRequired[str | None]
    refunded_note: NotRequired[str | None]
    canceled_note: NotRequired[str | None]
    tender: NotRequired[V1Tender | V1TenderDict]
    order_history: NotRequired[list[V1OrderHistoryEntry | V1OrderHistoryEntryDict | None]]
    promo_code: NotRequired[str | None]
    btc_receive_address: NotRequired[str | None]
    btc_price_satoshi: NotRequired[float | None]
