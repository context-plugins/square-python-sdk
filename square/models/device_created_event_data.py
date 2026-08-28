from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .device_created_event_object import DeviceCreatedEventObject, DeviceCreatedEventObjectDict


class DeviceCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the event data object. The value is ``"device"``."""

    id: Optional[str] = UNSET
    """The ID of the device."""

    object_: Optional[DeviceCreatedEventObject] = Field(default=UNSET, alias="object")


class DeviceCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[DeviceCreatedEventObject | DeviceCreatedEventObjectDict]
