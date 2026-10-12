from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.v1_tender_card_brand import V1TenderCardBrandOrStr
from .enums.v1_tender_entry_method import V1TenderEntryMethodOrStr
from .enums.v1_tender_type import V1TenderTypeOrStr
from .v1_money import V1Money, V1MoneyDict


class V1Tender(SdkBaseModel):
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

    id: Optional[str] = UNSET
    """The tender's unique ID."""

    type_: Optional[V1TenderTypeOrStr] = Field(default=UNSET, alias="type")
    name: OptionalNullable[str] = UNSET
    """A human-readable description of the tender."""

    employee_id: OptionalNullable[str] = UNSET
    """The ID of the employee that processed the tender."""

    receipt_url: OptionalNullable[str] = UNSET
    """The URL of the receipt for the tender."""

    card_brand: Optional[V1TenderCardBrandOrStr] = UNSET
    """The brand of a credit card."""

    pan_suffix: OptionalNullable[str] = UNSET
    """The last four digits of the provided credit card's account number."""

    entry_method: Optional[V1TenderEntryMethodOrStr] = UNSET
    payment_note: OptionalNullable[str] = UNSET
    """Notes entered by the merchant about the tender at the time of payment, if any. Typically only present for tender
    with the type: OTHER."""

    total_money: Optional[V1Money] = UNSET
    tendered_money: Optional[V1Money] = UNSET
    tendered_at: OptionalNullable[str] = UNSET
    """The time when the tender was created, in ISO 8601 format."""

    settled_at: OptionalNullable[str] = UNSET
    """The time when the tender was settled, in ISO 8601 format."""

    change_back_money: Optional[V1Money] = UNSET
    refunded_money: Optional[V1Money] = UNSET
    is_exchange: OptionalNullable[bool] = UNSET
    """Indicates whether or not the tender is associated with an exchange. If is_exchange is true, the tender represents
    the value of goods returned in an exchange not the actual money paid. The exchange value reduces the tender amounts
    needed to pay for items purchased in the exchange."""


class V1TenderDict(TypedDict):
    id: NotRequired[str]
    type_: NotRequired[V1TenderTypeOrStr]
    name: NotRequired[str | None]
    employee_id: NotRequired[str | None]
    receipt_url: NotRequired[str | None]
    card_brand: NotRequired[V1TenderCardBrandOrStr]
    pan_suffix: NotRequired[str | None]
    entry_method: NotRequired[V1TenderEntryMethodOrStr]
    payment_note: NotRequired[str | None]
    total_money: NotRequired[V1MoneyDict]
    tendered_money: NotRequired[V1MoneyDict]
    tendered_at: NotRequired[str | None]
    settled_at: NotRequired[str | None]
    change_back_money: NotRequired[V1MoneyDict]
    refunded_money: NotRequired[V1MoneyDict]
    is_exchange: NotRequired[bool | None]
