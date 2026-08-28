from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dispute_evidence_type import DisputeEvidenceTypeOrStr


class CreateDisputeEvidenceTextRequest(SdkBaseModel):
    """Defines the parameters for a ``CreateDisputeEvidenceText`` request."""

    idempotency_key: str
    """A unique key identifying the request. For more information, see `Idempotency
    <https://developer.squareup.com/docs/working-with-apis/idempotency>`__."""

    evidence_type: Optional[DisputeEvidenceTypeOrStr] = UNSET
    """The type of the dispute evidence."""

    evidence_text: str
    """The evidence string."""


class CreateDisputeEvidenceTextRequestDict(TypedDict):
    idempotency_key: str
    evidence_type: NotRequired[DisputeEvidenceTypeOrStr]
    evidence_text: str
