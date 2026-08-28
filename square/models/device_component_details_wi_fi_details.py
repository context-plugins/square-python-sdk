from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .device_component_details_measurement import (
    DeviceComponentDetailsMeasurement,
    DeviceComponentDetailsMeasurementDict,
)


class DeviceComponentDetailsWiFiDetails(SdkBaseModel):
    active: OptionalNullable[bool] = UNSET
    """A boolean to represent whether the WiFI interface is currently active."""

    ssid: OptionalNullable[str] = UNSET
    """The name of the connected WIFI network."""

    ip_address_v4: OptionalNullable[str] = UNSET
    """The string representation of the device’s IPv4 address."""

    secure_connection: OptionalNullable[str] = UNSET
    """The security protocol for a secure connection (e.g. WPA2). None provided if the connection is unsecured."""

    signal_strength: Optional[DeviceComponentDetailsMeasurement] = UNSET
    """A value qualified by unit of measure."""

    mac_address: OptionalNullable[str] = UNSET
    """The mac address of the device in this network."""


class DeviceComponentDetailsWiFiDetailsDict(TypedDict):
    active: NotRequired[bool | None]
    ssid: NotRequired[str | None]
    ip_address_v4: NotRequired[str | None]
    secure_connection: NotRequired[str | None]
    signal_strength: NotRequired[DeviceComponentDetailsMeasurement | DeviceComponentDetailsMeasurementDict]
    mac_address: NotRequired[str | None]
