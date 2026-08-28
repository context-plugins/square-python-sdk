from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DisputeEvidenceFile(SdkBaseModel):
    """A file to be uploaded as dispute evidence."""

    filename: OptionalNullable[str] = UNSET
    """The file name including the file extension. For example: "receipt.tiff"."""

    filetype: OptionalNullable[str] = UNSET
    """Dispute evidence files must be application/pdf, image/heic, image/heif, image/jpeg, image/png, or image/tiff
    formats."""


class DisputeEvidenceFileDict(TypedDict):
    filename: NotRequired[str | None]
    filetype: NotRequired[str | None]
