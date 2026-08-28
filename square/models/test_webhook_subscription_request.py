from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TestWebhookSubscriptionRequest(SdkBaseModel):
    """Tests a `Subscription <entity:WebhookSubscription>`__ by sending a test event to its notification URL."""

    event_type: OptionalNullable[str] = UNSET
    """The event type that will be used to test the `Subscription <entity:WebhookSubscription>`__. The event type must
    be contained in the list of event types in the `Subscription <entity:WebhookSubscription>`__."""


class TestWebhookSubscriptionRequestDict(TypedDict):
    event_type: NotRequired[str | None]
