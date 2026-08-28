from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceStatus(str, Enum):
    """Indicates the status of an `invoice <entity:Invoice>`__."""

    DRAFT = "DRAFT"
    """The invoice is a draft. You must publish a draft invoice before Square can process it. A draft invoice has no
    ``public_url``, so it is not available to customers."""

    UNPAID = "UNPAID"
    """The invoice is published but not yet paid."""

    SCHEDULED = "SCHEDULED"
    """The invoice is scheduled to be processed. On the scheduled date, Square sends the invoice, initiates an automatic
    payment, or takes no action, depending on the delivery method and payment request settings. Square also sets the
    invoice status to the appropriate state: ``UNPAID``, ``PAID``, ``PARTIALLY_PAID``, or ``PAYMENT_PENDING``."""

    PARTIALLY_PAID = "PARTIALLY_PAID"
    """A partial payment is received for the invoice."""

    PAID = "PAID"
    """The customer paid the invoice in full."""

    PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"
    """The invoice is paid (or partially paid) and some but not all the amount paid is refunded."""

    REFUNDED = "REFUNDED"
    """The full amount that the customer paid for the invoice is refunded."""

    CANCELED = "CANCELED"
    """The invoice is canceled. Square no longer requests payments from the customer. The Square-hosted payment page is
    still accessible using the temporary ``public_url`` link, but the invoice is shown as canceled and does not accept
    payment."""

    FAILED = "FAILED"
    """Square canceled the invoice due to suspicious activity."""

    PAYMENT_PENDING = "PAYMENT_PENDING"
    """A payment on the invoice was initiated but has not yet been processed.

    When in this state, invoices cannot be updated and other payments cannot be initiated."""

    __str__ = str.__str__


InvoiceStatusOrStr: TypeAlias = Annotated[InvoiceStatus | str, open_enum_validator(InvoiceStatus)]
