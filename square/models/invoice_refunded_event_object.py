from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .invoice import Invoice, InvoiceDict


class InvoiceRefundedEventObject(SdkBaseModel):
    invoice: Optional[Invoice] = UNSET
    """Stores information about an invoice. You use the Invoices API to create and manage invoices. For more
    information, see `Invoices API Overview <https://developer.squareup.com/docs/invoices-api/overview>`__."""


class InvoiceRefundedEventObjectDict(TypedDict):
    invoice: NotRequired[InvoiceDict]
