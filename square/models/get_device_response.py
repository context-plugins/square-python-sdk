from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device import Device, DeviceDict
from .error import Error, ErrorDict


class GetDeviceResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    device: Optional[Device] = UNSET


class GetDeviceResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    device: NotRequired[Device | DeviceDict]
