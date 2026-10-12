from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .invoice import Invoice, InvoiceDict


class CreateInvoiceRequest(SdkBaseModel):
    """Describes a ``CreateInvoice`` request."""

    invoice: Invoice
    """Stores information about an invoice. You use the Invoices API to create and manage invoices. For more
    information, see `Invoices API Overview <https://developer.squareup.com/docs/invoices-api/overview>`__."""

    idempotency_key: Optional[str] = UNSET
    """A unique string that identifies the ``CreateInvoice`` request. If you do not provide ``idempotency_key`` (or
    provide an empty string as the value), the endpoint treats each request as independent.

    For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class CreateInvoiceRequestDict(TypedDict):
    invoice: InvoiceDict
    idempotency_key: NotRequired[str]
