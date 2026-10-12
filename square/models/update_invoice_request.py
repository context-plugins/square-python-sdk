from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .invoice import Invoice, InvoiceDict


class UpdateInvoiceRequest(SdkBaseModel):
    """Describes a ``UpdateInvoice`` request."""

    invoice: Invoice
    """Stores information about an invoice. You use the Invoices API to create and manage invoices. For more
    information, see `Invoices API Overview <https://developer.squareup.com/docs/invoices-api/overview>`__."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A unique string that identifies the ``UpdateInvoice`` request. If you do not provide ``idempotency_key`` (or
    provide an empty string as the value), the endpoint treats each request as independent.

    For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""

    fields_to_clear: OptionalNullable[list[str]] = UNSET
    """The list of fields to clear. Although this field is currently supported, we recommend using null values or the
    ``remove`` field when possible. For examples, see `Update an Invoice
    <https://developer.squareup.com/docs/invoices-api/update-invoices>`__."""


class UpdateInvoiceRequestDict(TypedDict):
    invoice: InvoiceDict
    idempotency_key: NotRequired[str | None]
    fields_to_clear: NotRequired[list[str] | None]
