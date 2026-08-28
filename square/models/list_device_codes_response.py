from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .device_code import DeviceCode, DeviceCodeDict
from .error import Error, ErrorDict


class ListDeviceCodesResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    device_codes: Optional[list[DeviceCode]] = UNSET
    """The queried DeviceCode."""

    cursor: Optional[str] = UNSET
    """A pagination cursor to retrieve the next set of results for your original query to the endpoint. This value is
    present only if the request succeeded and additional results are available.

    See `Paginating results <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more
    information."""


class ListDeviceCodesResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    device_codes: NotRequired[list[DeviceCode | DeviceCodeDict]]
    cursor: NotRequired[str]
