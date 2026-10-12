from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .labor_shift_created_event_object import LaborShiftCreatedEventObject, LaborShiftCreatedEventObjectDict


class LaborShiftCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``shift``."""

    id: Optional[str] = UNSET
    """The ID of the affected ``Shift``."""

    object_: Optional[LaborShiftCreatedEventObject] = Field(default=UNSET, alias="object")


class LaborShiftCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LaborShiftCreatedEventObjectDict]
