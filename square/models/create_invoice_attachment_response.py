from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .invoice_attachment import InvoiceAttachment, InvoiceAttachmentDict


class CreateInvoiceAttachmentResponse(SdkBaseModel):
    """Represents a `CreateInvoiceAttachment <api-endpoint:Invoices-CreateInvoiceAttachment>`__ response."""

    attachment: Optional[InvoiceAttachment] = UNSET
    """Represents a file attached to an `invoice <entity:Invoice>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""


class CreateInvoiceAttachmentResponseDict(TypedDict):
    attachment: NotRequired[InvoiceAttachment | InvoiceAttachmentDict]
    errors: NotRequired[list[Error | ErrorDict]]
