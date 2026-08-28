from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_segment import CustomerSegment, CustomerSegmentDict
from .error import Error, ErrorDict


class ListCustomerSegmentsResponse(SdkBaseModel):
    """Defines the fields that are included in the response body for requests to the ``ListCustomerSegments`` endpoint.

    Either ``errors`` or ``segments`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    segments: Optional[list[CustomerSegment]] = UNSET
    """The list of customer segments belonging to the associated Square account."""

    cursor: Optional[str] = UNSET
    """A pagination cursor to be used in subsequent calls to ``ListCustomerSegments`` to retrieve the next set of query
    results. The cursor is only present if the request succeeded and additional results are available.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListCustomerSegmentsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    segments: NotRequired[list[CustomerSegment | CustomerSegmentDict]]
    cursor: NotRequired[str]
