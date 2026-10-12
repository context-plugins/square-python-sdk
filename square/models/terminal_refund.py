from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.action_cancel_reason import ActionCancelReasonOrStr
from .money import Money, MoneyDict


class TerminalRefund(SdkBaseModel):
    """Represents a payment refund processed by the Square Terminal. Only supports Interac (Canadian debit network)
    payment refunds."""

    id: Optional[str] = UNSET
    """A unique ID for this ``TerminalRefund``."""

    refund_id: Optional[str] = UNSET
    """The reference to the payment refund created by completing this ``TerminalRefund``."""

    payment_id: str
    """The unique ID of the payment being refunded."""

    order_id: Optional[str] = UNSET
    """The reference to the Square order ID for the payment identified by the ``payment_id``."""

    amount_money: Money
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    reason: str
    """A description of the reason for the refund."""

    device_id: str
    """The unique ID of the device intended for this ``TerminalRefund``. The Id can be retrieved from /v2/devices
    api."""

    deadline_duration: OptionalNullable[str] = UNSET
    """The RFC 3339 duration, after which the refund is automatically canceled. A ``TerminalRefund`` that is ``PENDING``
    is automatically ``CANCELED`` and has a cancellation reason of ``TIMED_OUT``.

    Default: 5 minutes from creation.

    Maximum: 5 minutes"""

    status: Optional[str] = UNSET
    """The status of the ``TerminalRefund``. Options: ``PENDING``, ``IN_PROGRESS``, ``CANCEL_REQUESTED``, ``CANCELED``,
    or ``COMPLETED``."""

    cancel_reason: Optional[ActionCancelReasonOrStr] = UNSET
    created_at: Optional[str] = UNSET
    """The time when the ``TerminalRefund`` was created, as an RFC 3339 timestamp."""

    updated_at: Optional[str] = UNSET
    """The time when the ``TerminalRefund`` was last updated, as an RFC 3339 timestamp."""

    app_id: Optional[str] = UNSET
    """The ID of the application that created the refund."""

    location_id: Optional[str] = UNSET
    """The location of the device where the ``TerminalRefund`` was directed."""


class TerminalRefundDict(TypedDict):
    id: NotRequired[str]
    refund_id: NotRequired[str]
    payment_id: str
    order_id: NotRequired[str]
    amount_money: MoneyDict
    reason: str
    device_id: str
    deadline_duration: NotRequired[str | None]
    status: NotRequired[str]
    cancel_reason: NotRequired[ActionCancelReasonOrStr]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    app_id: NotRequired[str]
    location_id: NotRequired[str]
