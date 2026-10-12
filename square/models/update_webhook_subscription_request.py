from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .webhook_subscription import WebhookSubscription, WebhookSubscriptionDict


class UpdateWebhookSubscriptionRequest(SdkBaseModel):
    """Updates a `Subscription <entity:WebhookSubscription>`__."""

    subscription: Optional[WebhookSubscription] = UNSET
    """Represents the details of a webhook subscription, including notification URL, event types, and signature key."""


class UpdateWebhookSubscriptionRequestDict(TypedDict):
    subscription: NotRequired[WebhookSubscriptionDict]
