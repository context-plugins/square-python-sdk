from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .additional_recipient import AdditionalRecipient, AdditionalRecipientDict
from .enums.tender_type import TenderTypeOrStr
from .money import Money, MoneyDict
from .tender_bank_account_details import TenderBankAccountDetails, TenderBankAccountDetailsDict
from .tender_buy_now_pay_later_details import TenderBuyNowPayLaterDetails, TenderBuyNowPayLaterDetailsDict
from .tender_card_details import TenderCardDetails, TenderCardDetailsDict
from .tender_cash_details import TenderCashDetails, TenderCashDetailsDict
from .tender_square_account_details import TenderSquareAccountDetails, TenderSquareAccountDetailsDict


class Tender(SdkBaseModel):
    """Represents a tender (i.e., a method of payment) used in a Square transaction."""

    id: Optional[str] = UNSET
    """The tender's unique ID. It is the associated payment ID."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the transaction's associated location."""

    transaction_id: OptionalNullable[str] = UNSET
    """The ID of the tender's associated transaction."""

    created_at: Optional[str] = UNSET
    """The timestamp for when the tender was created, in RFC 3339 format."""

    note: OptionalNullable[str] = UNSET
    """An optional note associated with the tender at the time of payment."""

    amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    tip_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    processing_fee_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    customer_id: OptionalNullable[str] = UNSET
    """If the tender is associated with a customer or represents a customer's card on file, this is the ID of the
    associated customer."""

    type_: TenderTypeOrStr = Field(alias="type")
    """Indicates a tender's type."""

    card_details: Optional[TenderCardDetails] = UNSET
    """Represents additional details of a tender with ``type`` ``CARD`` or ``SQUARE_GIFT_CARD``"""

    cash_details: Optional[TenderCashDetails] = UNSET
    """Represents the details of a tender with ``type`` ``CASH``."""

    bank_account_details: Optional[TenderBankAccountDetails] = UNSET
    """Represents the details of a tender with ``type`` ``BANK_ACCOUNT``.

    See `BankAccountPaymentDetails <entity:BankAccountPaymentDetails>`__ for more exposed details of a bank account
    payment."""

    buy_now_pay_later_details: Optional[TenderBuyNowPayLaterDetails] = UNSET
    """Represents the details of a tender with ``type`` ``BUY_NOW_PAY_LATER``."""

    square_account_details: Optional[TenderSquareAccountDetails] = UNSET
    """Represents the details of a tender with ``type`` ``SQUARE_ACCOUNT``."""

    additional_recipients: Optional[list[AdditionalRecipient | None]] = UNSET
    """Additional recipients (other than the merchant) receiving a portion of this tender. For example, fees assessed on
    the purchase by a third party integration."""

    payment_id: OptionalNullable[str] = UNSET
    """The ID of the `Payment <entity:Payment>`__ that corresponds to this tender. This value is only present for
    payments created with the v2 Payments API."""


class TenderDict(TypedDict):
    id: NotRequired[str]
    location_id: NotRequired[str | None]
    transaction_id: NotRequired[str | None]
    created_at: NotRequired[str]
    note: NotRequired[str | None]
    amount_money: NotRequired[Money | MoneyDict]
    tip_money: NotRequired[Money | MoneyDict]
    processing_fee_money: NotRequired[Money | MoneyDict]
    customer_id: NotRequired[str | None]
    type_: TenderTypeOrStr
    card_details: NotRequired[TenderCardDetails | TenderCardDetailsDict]
    cash_details: NotRequired[TenderCashDetails | TenderCashDetailsDict]
    bank_account_details: NotRequired[TenderBankAccountDetails | TenderBankAccountDetailsDict]
    buy_now_pay_later_details: NotRequired[TenderBuyNowPayLaterDetails | TenderBuyNowPayLaterDetailsDict]
    square_account_details: NotRequired[TenderSquareAccountDetails | TenderSquareAccountDetailsDict]
    additional_recipients: NotRequired[list[AdditionalRecipient | AdditionalRecipientDict | None]]
    payment_id: NotRequired[str | None]
