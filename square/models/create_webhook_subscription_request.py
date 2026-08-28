from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .webhook_subscription import WebhookSubscription, WebhookSubscriptionDict


class CreateWebhookSubscriptionRequest(SdkBaseModel):
    """Creates a `Subscription <entity:WebhookSubscription>`__."""

    idempotency_key: Optional[str] = UNSET
    """A unique string that identifies the `CreateWebhookSubscription
    <api-endpoint:WebhookSubscriptions-CreateWebhookSubscription>`__ request."""

    subscription: WebhookSubscription
    """Represents the details of a webhook subscription, including notification URL, event types, and signature key."""


class CreateWebhookSubscriptionRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    subscription: WebhookSubscription | WebhookSubscriptionDict
