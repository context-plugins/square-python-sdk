from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_subscriptions_query import SearchSubscriptionsQuery, SearchSubscriptionsQueryDict


class SearchSubscriptionsRequest(SdkBaseModel):
    """Defines input parameters in a request to the `SearchSubscriptions
    <api-endpoint:Subscriptions-SearchSubscriptions>`__ endpoint."""

    cursor: Optional[str] = UNSET
    """When the total number of resulting subscriptions exceeds the limit of a paged response, specify the cursor
    returned from a preceding response here to fetch the next set of results. If the cursor is unset, the response
    contains the last page of the results.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    limit: Optional[int] = UNSET
    """The upper limit on the number of subscriptions to return in a paged response."""

    query: Optional[SearchSubscriptionsQuery] = UNSET
    """Represents a query, consisting of specified query expressions, used to search for subscriptions."""

    include: Optional[list[str]] = UNSET
    """An option to include related information in the response.

    The supported values are:

    - ``actions``: to include scheduled actions on the targeted subscriptions."""


class SearchSubscriptionsRequestDict(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]
    query: NotRequired[SearchSubscriptionsQueryDict]
    include: NotRequired[list[str]]
