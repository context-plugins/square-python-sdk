from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceDeliveryMethod(str, Enum):
    """Indicates how Square delivers the `invoice <entity:Invoice>`__ to the customer."""

    EMAIL = "EMAIL"
    """Directs Square to send invoices, reminders, and receipts to the customer using email."""

    SHARE_MANUALLY = "SHARE_MANUALLY"
    """Directs Square to take no action on the invoice. In this case, the seller or application developer follows up
    with the customer for payment. For example, a seller might collect a payment in the Seller Dashboard or Point of
    Sale (POS) application. The seller might also share the URL of the Square-hosted invoice page (``public_url``) with
    the customer to request payment."""

    SMS = "SMS"
    """Directs Square to send invoices and receipts to the customer using SMS (text message).

    You cannot set ``SMS`` as a delivery method using the Invoices API, but you can change an ``SMS`` delivery method to
    ``EMAIL`` or ``SHARE_MANUALLY``."""

    __str__ = str.__str__


InvoiceDeliveryMethodOrStr: TypeAlias = Annotated[
    InvoiceDeliveryMethod | str, open_enum_validator(InvoiceDeliveryMethod)
]
