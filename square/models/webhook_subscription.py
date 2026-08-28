from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class WebhookSubscription(SdkBaseModel):
    """Represents the details of a webhook subscription, including notification URL, event types, and signature key."""

    id: Optional[str] = UNSET
    """A Square-generated unique ID for the subscription."""

    name: OptionalNullable[str] = UNSET
    """The name of this subscription."""

    enabled: OptionalNullable[bool] = UNSET
    """Indicates whether the subscription is enabled (``true``) or not (``false``)."""

    event_types: Optional[list[str | None]] = UNSET
    """The event types associated with this subscription."""

    notification_url: OptionalNullable[str] = UNSET
    """The URL to which webhooks are sent."""

    api_version: OptionalNullable[str] = UNSET
    """The API version of the subscription. This field is optional for ``CreateWebhookSubscription``. The value defaults
    to the API version used by the application."""

    signature_key: Optional[str] = UNSET
    """The Square-generated signature key used to validate the origin of the webhook event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the subscription was created, in RFC 3339 format. For example,
    "2016-09-04T23:59:33.123Z"."""

    updated_at: Optional[str] = UNSET
    """The timestamp of when the subscription was last updated, in RFC 3339 format. For example,
    "2016-09-04T23:59:33.123Z"."""


class WebhookSubscriptionDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str | None]
    enabled: NotRequired[bool | None]
    event_types: NotRequired[list[str | None]]
    notification_url: NotRequired[str | None]
    api_version: NotRequired[str | None]
    signature_key: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
