from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteDisputeEvidenceResponse(SdkBaseModel):
    """Defines the fields in a ``DeleteDisputeEvidence`` response."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""


class DeleteDisputeEvidenceResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
