from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoicePaymentReminderStatus(str, Enum):
    """The status of a payment request reminder."""

    PENDING = "PENDING"
    """The reminder will be sent on the ``relative_scheduled_date`` (if the invoice is published)."""

    NOT_APPLICABLE = "NOT_APPLICABLE"
    """The reminder is not applicable and is not sent. The following are examples of when reminders are not applicable
    and are not sent:
    - You schedule a reminder to be sent before the invoice is published.
    - The invoice is configured with multiple payment requests and a payment request reminder
    is configured to be sent after the next payment request ``due_date``.
    - Two reminders (for different payment requests) are configured to be sent on the
    same date. Therefore, only one reminder is sent.
    - You configure a reminder to be sent on the date that the invoice is scheduled to be sent.
    - The payment request is already paid.
    - The invoice status is ``CANCELED`` or ``FAILED``."""

    SENT = "SENT"
    """The reminder is sent."""

    __str__ = str.__str__


InvoicePaymentReminderStatusOrStr: TypeAlias = Annotated[
    InvoicePaymentReminderStatus | str, open_enum_validator(InvoicePaymentReminderStatus)
]
