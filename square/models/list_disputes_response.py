from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .dispute import Dispute, DisputeDict
from .error import Error, ErrorDict


class ListDisputesResponse(SdkBaseModel):
    """Defines fields in a ``ListDisputes`` response."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    disputes: Optional[list[Dispute]] = UNSET
    """The list of disputes."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If unset, this is the final response. For more
    information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListDisputesResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    disputes: NotRequired[list[Dispute | DisputeDict]]
    cursor: NotRequired[str]
