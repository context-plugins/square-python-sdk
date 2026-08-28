from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .invoice import Invoice, InvoiceDict


class UpdateInvoiceResponse(SdkBaseModel):
    """Describes a ``UpdateInvoice`` response."""

    invoice: Optional[Invoice] = UNSET
    """Stores information about an invoice. You use the Invoices API to create and manage invoices. For more
    information, see `Invoices API Overview <https://developer.squareup.com/docs/invoices-api/overview>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""


class UpdateInvoiceResponseDict(TypedDict):
    invoice: NotRequired[Invoice | InvoiceDict]
    errors: NotRequired[list[Error | ErrorDict]]
