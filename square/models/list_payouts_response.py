from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payout import Payout, PayoutDict


class ListPayoutsResponse(SdkBaseModel):
    """The response to retrieve payout records entries."""

    payouts: Optional[list[Payout]] = UNSET
    """The requested list of payouts."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response. For more
    information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""


class ListPayoutsResponseDict(TypedDict):
    payouts: NotRequired[list[PayoutDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[ErrorDict]]
