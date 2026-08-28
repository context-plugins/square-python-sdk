from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class UpdateWebhookSubscriptionSignatureKeyRequest(SdkBaseModel):
    """Updates a `Subscription <entity:WebhookSubscription>`__ by replacing the existing signature key with a new
    one."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A unique string that identifies the `UpdateWebhookSubscriptionSignatureKey
    <api-endpoint:WebhookSubscriptions-UpdateWebhookSubscriptionSignatureKey>`__ request."""


class UpdateWebhookSubscriptionSignatureKeyRequestDict(TypedDict):
    idempotency_key: NotRequired[str | None]
