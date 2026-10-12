from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .labor_shift_updated_event_object import LaborShiftUpdatedEventObject, LaborShiftUpdatedEventObjectDict


class LaborShiftUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``shift``."""

    id: Optional[str] = UNSET
    """ID of the affected ``Shift``."""

    object_: Optional[LaborShiftUpdatedEventObject] = Field(default=UNSET, alias="object")


class LaborShiftUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LaborShiftUpdatedEventObjectDict]
