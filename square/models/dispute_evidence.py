from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dispute_evidence_file import DisputeEvidenceFile, DisputeEvidenceFileDict
from .enums.dispute_evidence_type import DisputeEvidenceTypeOrStr


class DisputeEvidence(SdkBaseModel):
    evidence_id: OptionalNullable[str] = UNSET
    """The Square-generated ID of the evidence."""

    id: Optional[str] = UNSET
    """The Square-generated ID of the evidence."""

    dispute_id: OptionalNullable[str] = UNSET
    """The ID of the dispute the evidence is associated with."""

    evidence_file: Optional[DisputeEvidenceFile] = UNSET
    """A file to be uploaded as dispute evidence."""

    evidence_text: OptionalNullable[str] = UNSET
    """Raw text"""

    uploaded_at: OptionalNullable[str] = UNSET
    """The time when the evidence was uploaded, in RFC 3339 format."""

    evidence_type: Optional[DisputeEvidenceTypeOrStr] = UNSET
    """The type of the dispute evidence."""


class DisputeEvidenceDict(TypedDict):
    evidence_id: NotRequired[str | None]
    id: NotRequired[str]
    dispute_id: NotRequired[str | None]
    evidence_file: NotRequired[DisputeEvidenceFile | DisputeEvidenceFileDict]
    evidence_text: NotRequired[str | None]
    uploaded_at: NotRequired[str | None]
    evidence_type: NotRequired[DisputeEvidenceTypeOrStr]
