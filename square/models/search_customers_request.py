from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_query import CustomerQuery, CustomerQueryDict


class SearchCustomersRequest(SdkBaseModel):
    """Defines the fields that are included in the request body of a request to the ``SearchCustomers`` endpoint."""

    cursor: Optional[str] = UNSET
    """Include the pagination cursor in subsequent calls to this endpoint to retrieve the next set of results associated
    with the original query.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    limit: Optional[int] = UNSET
    """The maximum number of results to return in a single page. This limit is advisory. The response might contain more
    or fewer results. If the specified limit is invalid, Square returns a ``400 VALUE_TOO_LOW`` or ``400
    VALUE_TOO_HIGH`` error. The default value is 100.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    query: Optional[CustomerQuery] = UNSET
    """Represents filtering and sorting criteria for a `SearchCustomers <api-endpoint:Customers-SearchCustomers>`__
    request."""

    count: Optional[bool] = UNSET
    """Indicates whether to return the total count of matching customers in the ``count`` field of the response.

    The default value is ``false``."""


class SearchCustomersRequestDict(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]
    query: NotRequired[CustomerQueryDict]
    count: NotRequired[bool]
