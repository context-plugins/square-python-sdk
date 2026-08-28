from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .component import Component, ComponentDict
from .device_attributes import DeviceAttributes, DeviceAttributesDict
from .device_status import DeviceStatus, DeviceStatusDict


class Device(SdkBaseModel):
    id: Optional[str] = UNSET
    """A synthetic identifier for the device. The identifier includes a standardized prefix and is otherwise an opaque
    id generated from key device fields."""

    attributes: DeviceAttributes
    components: Optional[list[Component | None]] = UNSET
    """A list of components applicable to the device."""

    status: Optional[DeviceStatus] = UNSET


class DeviceDict(TypedDict):
    id: NotRequired[str]
    attributes: DeviceAttributes | DeviceAttributesDict
    components: NotRequired[list[Component | ComponentDict | None]]
    status: NotRequired[DeviceStatus | DeviceStatusDict]
