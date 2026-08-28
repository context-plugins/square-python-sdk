from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .labor_scheduled_shift_published_event_data import (
    LaborScheduledShiftPublishedEventData,
    LaborScheduledShiftPublishedEventDataDict,
)


class LaborScheduledShiftPublishedEvent(SdkBaseModel):
    """Published when a `ScheduledShift <entity:ScheduledShift>`__ is published."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the merchant associated with the event."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the location associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event. For this event, the value is ``labor.scheduled_shift.published``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[LaborScheduledShiftPublishedEventData] = UNSET


class LaborScheduledShiftPublishedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[LaborScheduledShiftPublishedEventData | LaborScheduledShiftPublishedEventDataDict]
