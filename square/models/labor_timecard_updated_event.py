from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .labor_timecard_updated_event_data import LaborTimecardUpdatedEventData, LaborTimecardUpdatedEventDataDict


class LaborTimecardUpdatedEvent(SdkBaseModel):
    """Published when a `Timecard <entity:Timecard>`__ is updated."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event. For this event, the value is ``labor.timecard.updated``."""

    event_id: OptionalNullable[str] = UNSET
    """The unique ID for the event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[LaborTimecardUpdatedEventData] = UNSET


class LaborTimecardUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[LaborTimecardUpdatedEventData | LaborTimecardUpdatedEventDataDict]
