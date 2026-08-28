from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .subscription_event import SubscriptionEvent, SubscriptionEventDict


class ListSubscriptionEventsResponse(SdkBaseModel):
    """Defines output parameters in a response from the `ListSubscriptionEvents
    <api-endpoint:Subscriptions-ListSubscriptionEvents>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered during the request."""

    subscription_events: Optional[list[SubscriptionEvent]] = UNSET
    """The retrieved subscription events."""

    cursor: Optional[str] = UNSET
    """When the total number of resulting subscription events exceeds the limit of a paged response, the response
    includes a cursor for you to use in a subsequent request to fetch the next set of events. If the cursor is unset,
    the response contains the last page of the results.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListSubscriptionEventsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    subscription_events: NotRequired[list[SubscriptionEvent | SubscriptionEventDict]]
    cursor: NotRequired[str]
