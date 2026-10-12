from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_subscriptions_filter import SearchSubscriptionsFilter, SearchSubscriptionsFilterDict


class SearchSubscriptionsQuery(SdkBaseModel):
    """Represents a query, consisting of specified query expressions, used to search for subscriptions."""

    filter: Optional[SearchSubscriptionsFilter] = UNSET
    """Represents a set of query expressions (filters) to narrow the scope of targeted subscriptions returned by the
    `SearchSubscriptions <api-endpoint:Subscriptions-SearchSubscriptions>`__ endpoint."""


class SearchSubscriptionsQueryDict(TypedDict):
    filter: NotRequired[SearchSubscriptionsFilterDict]
