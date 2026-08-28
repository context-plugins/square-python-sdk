from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InvoiceAttachment(SdkBaseModel):
    """Represents a file attached to an `invoice <entity:Invoice>`__."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the attachment."""

    filename: Optional[str] = UNSET
    """The file name of the attachment, which is displayed on the invoice."""

    description: Optional[str] = UNSET
    """The description of the attachment, which is displayed on the invoice. This field maps to the seller-defined
    **Message** field."""

    filesize: Optional[int] = UNSET
    """The file size of the attachment in bytes."""

    hash: Optional[str] = UNSET
    """The MD5 hash that was generated from the file contents."""

    mime_type: Optional[str] = UNSET
    """The mime type of the attachment. The following mime types are supported: image/gif, image/jpeg, image/png,
    image/tiff, image/bmp, application/pdf."""

    uploaded_at: Optional[str] = UNSET
    """The timestamp when the attachment was uploaded, in RFC 3339 format."""


class InvoiceAttachmentDict(TypedDict):
    id: NotRequired[str]
    filename: NotRequired[str]
    description: NotRequired[str]
    filesize: NotRequired[int]
    hash: NotRequired[str]
    mime_type: NotRequired[str]
    uploaded_at: NotRequired[str]
