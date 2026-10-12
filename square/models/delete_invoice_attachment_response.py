from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteInvoiceAttachmentResponse(SdkBaseModel):
    """Represents a `DeleteInvoiceAttachment <api-endpoint:Invoices-DeleteInvoiceAttachment>`__ response."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""


class DeleteInvoiceAttachmentResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
