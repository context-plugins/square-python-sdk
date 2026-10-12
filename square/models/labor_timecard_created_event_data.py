from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .labor_timecard_created_event_object import LaborTimecardCreatedEventObject, LaborTimecardCreatedEventObjectDict


class LaborTimecardCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``timecard``."""

    id: Optional[str] = UNSET
    """The ID of the affected ``Timecard``."""

    object_: Optional[LaborTimecardCreatedEventObject] = Field(default=UNSET, alias="object")


class LaborTimecardCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LaborTimecardCreatedEventObjectDict]
