from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .labor_scheduled_shift_created_event_object import (
    LaborScheduledShiftCreatedEventObject,
    LaborScheduledShiftCreatedEventObjectDict,
)


class LaborScheduledShiftCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``scheduled_shift``."""

    id: Optional[str] = UNSET
    """The ID of the affected ``ScheduledShift``."""

    object_: Optional[LaborScheduledShiftCreatedEventObject] = Field(default=UNSET, alias="object")


class LaborScheduledShiftCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LaborScheduledShiftCreatedEventObjectDict]
