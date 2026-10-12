from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_publish_scheduled_shifts_data import BulkPublishScheduledShiftsData, BulkPublishScheduledShiftsDataDict
from .enums.scheduled_shift_notification_audience import ScheduledShiftNotificationAudienceOrStr


class BulkPublishScheduledShiftsRequest(SdkBaseModel):
    """Represents a `BulkPublishScheduledShifts <api-endpoint:Labor-BulkPublishScheduledShifts>`__ request."""

    scheduled_shifts: dict[str, BulkPublishScheduledShiftsData]
    """A map of 1 to 100 key-value pairs that represent individual publish requests.

    - Each key is the ID of a scheduled shift you want to publish.
    - Each value is a ``BulkPublishScheduledShiftsData`` object that contains the
    ``version`` field or is an empty object."""

    scheduled_shift_notification_audience: Optional[ScheduledShiftNotificationAudienceOrStr] = UNSET
    """Indicates whether Square sends an email notification to team members when a scheduled shift is published and
    which team members receive the notification."""


class BulkPublishScheduledShiftsRequestDict(TypedDict):
    scheduled_shifts: dict[str, BulkPublishScheduledShiftsDataDict]
    scheduled_shift_notification_audience: NotRequired[ScheduledShiftNotificationAudienceOrStr]
