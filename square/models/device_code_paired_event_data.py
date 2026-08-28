from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .device_code_paired_event_object import DeviceCodePairedEventObject, DeviceCodePairedEventObjectDict


class DeviceCodePairedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the paired object’s type, ``"device_code"``."""

    id: Optional[str] = UNSET
    """ID of the paired device code."""

    object_: Optional[DeviceCodePairedEventObject] = Field(default=UNSET, alias="object")


class DeviceCodePairedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[DeviceCodePairedEventObject | DeviceCodePairedEventObjectDict]
