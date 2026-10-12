from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_code import DeviceCode, DeviceCodeDict
from .error import Error, ErrorDict


class CreateDeviceCodeResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    device_code: Optional[DeviceCode] = UNSET


class CreateDeviceCodeResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    device_code: NotRequired[DeviceCodeDict]
