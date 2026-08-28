from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dispute_evidence_type import DisputeEvidenceTypeOrStr


class CreateDisputeEvidenceFileRequest(SdkBaseModel):
    """Defines the parameters for a ``CreateDisputeEvidenceFile`` request."""

    idempotency_key: str
    """A unique key identifying the request. For more information, see `Idempotency
    <https://developer.squareup.com/docs/working-with-apis/idempotency>`__."""

    evidence_type: Optional[DisputeEvidenceTypeOrStr] = UNSET
    """The type of the dispute evidence."""

    content_type: Optional[str] = UNSET
    """The MIME type of the uploaded file. The type can be image/heic, image/heif, image/jpeg, application/pdf,
    image/png, or image/tiff."""


class CreateDisputeEvidenceFileRequestDict(TypedDict):
    idempotency_key: str
    evidence_type: NotRequired[DisputeEvidenceTypeOrStr]
    content_type: NotRequired[str]
