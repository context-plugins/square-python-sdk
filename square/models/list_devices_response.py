from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device import Device, DeviceDict
from .error import Error, ErrorDict


class ListDevicesResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Information about errors that occurred during the request."""

    devices: Optional[list[Device]] = UNSET
    """The requested list of ``Device`` objects."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response. See `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more information."""


class ListDevicesResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    devices: NotRequired[list[DeviceDict]]
    cursor: NotRequired[str]
