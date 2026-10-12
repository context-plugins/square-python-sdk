from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .invoice import Invoice, InvoiceDict


class GetInvoiceResponse(SdkBaseModel):
    """Describes a ``GetInvoice`` response."""

    invoice: Optional[Invoice] = UNSET
    """Stores information about an invoice. You use the Invoices API to create and manage invoices. For more
    information, see `Invoices API Overview <https://developer.squareup.com/docs/invoices-api/overview>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""


class GetInvoiceResponseDict(TypedDict):
    invoice: NotRequired[InvoiceDict]
    errors: NotRequired[list[ErrorDict]]
