from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .webhook_subscription import WebhookSubscription, WebhookSubscriptionDict


class CreateWebhookSubscriptionResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `CreateWebhookSubscription
    <api-endpoint:WebhookSubscriptions-CreateWebhookSubscription>`__ endpoint.

    Note: if there are errors processing the request, the `Subscription <entity:WebhookSubscription>`__ will not be
    present."""

    errors: Optional[list[Error]] = UNSET
    """Information on errors encountered during the request."""

    subscription: Optional[WebhookSubscription] = UNSET
    """Represents the details of a webhook subscription, including notification URL, event types, and signature key."""


class CreateWebhookSubscriptionResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    subscription: NotRequired[WebhookSubscriptionDict]
