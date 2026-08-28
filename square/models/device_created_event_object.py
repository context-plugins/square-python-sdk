from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device import Device, DeviceDict


class DeviceCreatedEventObject(SdkBaseModel):
    device: Optional[Device] = UNSET


class DeviceCreatedEventObjectDict(TypedDict):
    device: NotRequired[Device | DeviceDict]
