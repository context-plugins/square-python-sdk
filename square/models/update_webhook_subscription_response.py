from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .webhook_subscription import WebhookSubscription, WebhookSubscriptionDict


class UpdateWebhookSubscriptionResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `UpdateWebhookSubscription
    <api-endpoint:WebhookSubscriptions-UpdateWebhookSubscription>`__ endpoint.

    Note: If there are errors processing the request, the `Subscription <entity:WebhookSubscription>`__ is not
    present."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    subscription: Optional[WebhookSubscription] = UNSET
    """Represents the details of a webhook subscription, including notification URL, event types, and signature key."""


class UpdateWebhookSubscriptionResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    subscription: NotRequired[WebhookSubscription | WebhookSubscriptionDict]
