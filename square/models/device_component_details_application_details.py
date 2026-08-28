from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.application_type import ApplicationTypeOrStr


class DeviceComponentDetailsApplicationDetails(SdkBaseModel):
    application_type: Optional[ApplicationTypeOrStr] = UNSET
    version: Optional[str] = UNSET
    """The version of the application."""

    session_location: OptionalNullable[str] = UNSET
    """The location_id of the session for the application."""

    device_code_id: OptionalNullable[str] = UNSET
    """The id of the device code that was used to log in to the device."""


class DeviceComponentDetailsApplicationDetailsDict(TypedDict):
    application_type: NotRequired[ApplicationTypeOrStr]
    version: NotRequired[str]
    session_location: NotRequired[str | None]
    device_code_id: NotRequired[str | None]
