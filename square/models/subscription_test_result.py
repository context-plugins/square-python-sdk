from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SubscriptionTestResult(SdkBaseModel):
    """Represents the details of a webhook subscription, including notification URL, event types, and signature key."""

    id: Optional[str] = UNSET
    """A Square-generated unique ID for the subscription test result."""

    status_code: OptionalNullable[int] = UNSET
    """The status code returned by the subscription notification URL."""

    payload: OptionalNullable[str] = UNSET
    """An object containing the payload of the test event. For example, a ``payment.created`` event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the subscription was created, in RFC 3339 format. For example,
    "2016-09-04T23:59:33.123Z"."""

    updated_at: Optional[str] = UNSET
    """The timestamp of when the subscription was updated, in RFC 3339 format. For example, "2016-09-04T23:59:33.123Z".
    Because a subscription test result is unique, this field is the same as the ``created_at`` field."""


class SubscriptionTestResultDict(TypedDict):
    id: NotRequired[str]
    status_code: NotRequired[int | None]
    payload: NotRequired[str | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
