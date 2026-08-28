from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.device_component_details_external_power import DeviceComponentDetailsExternalPowerOrStr


class DeviceComponentDetailsBatteryDetails(SdkBaseModel):
    visible_percent: OptionalNullable[int] = UNSET
    """The battery charge percentage as displayed on the device."""

    external_power: Optional[DeviceComponentDetailsExternalPowerOrStr] = UNSET
    """An enum for ExternalPower."""


class DeviceComponentDetailsBatteryDetailsDict(TypedDict):
    visible_percent: NotRequired[int | None]
    external_power: NotRequired[DeviceComponentDetailsExternalPowerOrStr]
