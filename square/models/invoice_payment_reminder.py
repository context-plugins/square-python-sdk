from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.invoice_payment_reminder_status import InvoicePaymentReminderStatusOrStr


class InvoicePaymentReminder(SdkBaseModel):
    """Describes a payment request reminder (automatic notification) that Square sends to the customer. You configure a
    reminder relative to the payment request ``due_date``."""

    uid: Optional[str] = UNSET
    """A Square-assigned ID that uniquely identifies the reminder within the ``InvoicePaymentRequest``."""

    relative_scheduled_days: OptionalNullable[int] = UNSET
    """The number of days before (a negative number) or after (a positive number) the payment request ``due_date`` when
    the reminder is sent. For example, -3 indicates that the reminder should be sent 3 days before the payment request
    ``due_date``."""

    message: OptionalNullable[str] = UNSET
    """The reminder message."""

    status: Optional[InvoicePaymentReminderStatusOrStr] = UNSET
    """The status of a payment request reminder."""

    sent_at: Optional[str] = UNSET
    """If sent, the timestamp when the reminder was sent, in RFC 3339 format."""


class InvoicePaymentReminderDict(TypedDict):
    uid: NotRequired[str]
    relative_scheduled_days: NotRequired[int | None]
    message: NotRequired[str | None]
    status: NotRequired[InvoicePaymentReminderStatusOrStr]
    sent_at: NotRequired[str]
