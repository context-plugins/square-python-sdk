from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dispute_evidence import DisputeEvidence, DisputeEvidenceDict
from .error import Error, ErrorDict


class CreateDisputeEvidenceFileResponse(SdkBaseModel):
    """Defines the fields in a ``CreateDisputeEvidenceFile`` response."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    evidence: Optional[DisputeEvidence] = UNSET


class CreateDisputeEvidenceFileResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    evidence: NotRequired[DisputeEvidence | DisputeEvidenceDict]
