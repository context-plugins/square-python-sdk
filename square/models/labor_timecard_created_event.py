from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .labor_timecard_created_event_data import LaborTimecardCreatedEventData, LaborTimecardCreatedEventDataDict


class LaborTimecardCreatedEvent(SdkBaseModel):
    """Published when a worker starts a `Timecard <entity:Timecard>`__."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event. For this event, the value is ``labor.timecard.created``."""

    event_id: OptionalNullable[str] = UNSET
    """The unique ID for the event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[LaborTimecardCreatedEventData] = UNSET


class LaborTimecardCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[LaborTimecardCreatedEventDataDict]
