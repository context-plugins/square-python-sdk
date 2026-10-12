from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .webhook_subscription import WebhookSubscription, WebhookSubscriptionDict


class ListWebhookSubscriptionsResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `ListWebhookSubscriptions
    <api-endpoint:WebhookSubscriptions-ListWebhookSubscriptions>`__ endpoint.

    Note: if there are errors processing the request, the subscriptions field will not be present."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    subscriptions: Optional[list[WebhookSubscription]] = UNSET
    """The requested list of `Subscription <entity:WebhookSubscription>`__s."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListWebhookSubscriptionsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    subscriptions: NotRequired[list[WebhookSubscriptionDict]]
    cursor: NotRequired[str]
