from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.device_status_category import DeviceStatusCategoryOrStr


class DeviceStatus(SdkBaseModel):
    category: Optional[DeviceStatusCategoryOrStr] = UNSET


class DeviceStatusDict(TypedDict):
    category: NotRequired[DeviceStatusCategoryOrStr]
