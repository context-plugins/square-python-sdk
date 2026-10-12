from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payout_entry import PayoutEntry, PayoutEntryDict


class ListPayoutEntriesResponse(SdkBaseModel):
    """The response to retrieve payout records entries."""

    payout_entries: Optional[list[PayoutEntry]] = UNSET
    """The requested list of payout entries, ordered with the given or default sort order."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response. For more
    information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""


class ListPayoutEntriesResponseDict(TypedDict):
    payout_entries: NotRequired[list[PayoutEntryDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[ErrorDict]]
