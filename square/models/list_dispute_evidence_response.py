from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dispute_evidence import DisputeEvidence, DisputeEvidenceDict
from .error import Error, ErrorDict


class ListDisputeEvidenceResponse(SdkBaseModel):
    """Defines the fields in a ``ListDisputeEvidence`` response."""

    evidence: Optional[list[DisputeEvidence]] = UNSET
    """The list of evidence previously uploaded to the specified dispute."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If unset, this is the final response. For more
    information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListDisputeEvidenceResponseDict(TypedDict):
    evidence: NotRequired[list[DisputeEvidence | DisputeEvidenceDict]]
    errors: NotRequired[list[Error | ErrorDict]]
    cursor: NotRequired[str]
