from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateInvoiceAttachmentRequest(SdkBaseModel):
    """Represents a `CreateInvoiceAttachment <api-endpoint:Invoices-CreateInvoiceAttachment>`__ request."""

    idempotency_key: Optional[str] = UNSET
    """A unique string that identifies the ``CreateInvoiceAttachment`` request. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""

    description: Optional[str] = UNSET
    """The description of the attachment to display on the invoice."""


class CreateInvoiceAttachmentRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    description: NotRequired[str]
