from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .additional_recipient import AdditionalRecipient, AdditionalRecipientDict
from .enums.refund_status import RefundStatusOrStr
from .money import Money, MoneyDict


class Refund(SdkBaseModel):
    """Represents a refund processed for a Square transaction."""

    id: str
    """The refund's unique ID."""

    location_id: str
    """The ID of the refund's associated location."""

    transaction_id: OptionalNullable[str] = UNSET
    """The ID of the transaction that the refunded tender is part of."""

    tender_id: OptionalNullable[str] = UNSET
    """The ID of the refunded tender."""

    created_at: Optional[str] = UNSET
    """The timestamp for when the refund was created, in RFC 3339 format."""

    reason: str
    """The reason for the refund being issued."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    status: RefundStatusOrStr
    """Indicates a refund's current status."""

    processing_fee_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    additional_recipients: Optional[list[AdditionalRecipient | None]] = UNSET
    """Additional recipients (other than the merchant) receiving a portion of this refund. For example, fees assessed on
    a refund of a purchase by a third party integration."""


class RefundDict(TypedDict):
    id: str
    location_id: str
    transaction_id: NotRequired[str | None]
    tender_id: NotRequired[str | None]
    created_at: NotRequired[str]
    reason: str
    amount_money: Money | MoneyDict
    status: RefundStatusOrStr
    processing_fee_money: NotRequired[Money | MoneyDict]
    additional_recipients: NotRequired[list[AdditionalRecipient | AdditionalRecipientDict | None]]
