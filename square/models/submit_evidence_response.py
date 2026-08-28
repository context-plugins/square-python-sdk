from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dispute import Dispute, DisputeDict
from .error import Error, ErrorDict


class SubmitEvidenceResponse(SdkBaseModel):
    """Defines the fields in a ``SubmitEvidence`` response."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    dispute: Optional[Dispute] = UNSET
    """Represents a `dispute <https://developer.squareup.com/docs/disputes-api/overview>`__ a cardholder initiated with
    their bank."""


class SubmitEvidenceResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    dispute: NotRequired[Dispute | DisputeDict]
