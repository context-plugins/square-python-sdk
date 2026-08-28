from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription import Subscription, SubscriptionDict


class SearchSubscriptionsResponse(SdkBaseModel):
    """Defines output parameters in a response from the `SearchSubscriptions
    <api-endpoint:Subscriptions-SearchSubscriptions>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    subscriptions: Optional[list[Subscription]] = UNSET
    """The subscriptions matching the specified query expressions."""

    cursor: Optional[str] = UNSET
    """When the total number of resulting subscription exceeds the limit of a paged response, the response includes a
    cursor for you to use in a subsequent request to fetch the next set of results. If the cursor is unset, the response
    contains the last page of the results.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class SearchSubscriptionsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    subscriptions: NotRequired[list[Subscription | SubscriptionDict]]
    cursor: NotRequired[str]
