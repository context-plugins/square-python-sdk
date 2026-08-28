from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.scheduled_shift_notification_audience import ScheduledShiftNotificationAudienceOrStr


class PublishScheduledShiftRequest(SdkBaseModel):
    """Represents a `PublishScheduledShift <api-endpoint:Labor-PublishScheduledShift>`__ request."""

    idempotency_key: str
    """A unique identifier for the ``PublishScheduledShift`` request, used to ensure the `idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ of the operation."""

    version: Optional[int] = UNSET
    """The current version of the scheduled shift, used to enable `optimistic concurrency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__ control. If the
    provided version doesn't match the server version, the request fails. If omitted, Square executes a blind write,
    potentially overwriting data from another publish request."""

    scheduled_shift_notification_audience: Optional[ScheduledShiftNotificationAudienceOrStr] = UNSET
    """Indicates whether Square sends an email notification to team members when a scheduled shift is published and
    which team members receive the notification."""


class PublishScheduledShiftRequestDict(TypedDict):
    idempotency_key: str
    version: NotRequired[int]
    scheduled_shift_notification_audience: NotRequired[ScheduledShiftNotificationAudienceOrStr]
