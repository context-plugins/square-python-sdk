from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_code import DeviceCode, DeviceCodeDict


class DeviceCodePairedEventObject(SdkBaseModel):
    device_code: Optional[DeviceCode] = UNSET


class DeviceCodePairedEventObjectDict(TypedDict):
    device_code: NotRequired[DeviceCodeDict]
