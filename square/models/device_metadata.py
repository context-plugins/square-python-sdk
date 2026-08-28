from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DeviceMetadata(SdkBaseModel):
    battery_percentage: OptionalNullable[str] = UNSET
    """The Terminal’s remaining battery percentage, between 1-100."""

    charging_state: OptionalNullable[str] = UNSET
    """The current charging state of the Terminal. Options: ``CHARGING``, ``NOT_CHARGING``"""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the Square seller business location associated with the Terminal."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the Square merchant account that is currently signed-in to the Terminal."""

    network_connection_type: OptionalNullable[str] = UNSET
    """The Terminal’s current network connection type. Options: ``WIFI``, ``ETHERNET``"""

    payment_region: OptionalNullable[str] = UNSET
    """The country in which the Terminal is authorized to take payments."""

    serial_number: OptionalNullable[str] = UNSET
    """The unique identifier assigned to the Terminal, which can be found on the lower back of the device."""

    os_version: OptionalNullable[str] = UNSET
    """The current version of the Terminal’s operating system."""

    app_version: OptionalNullable[str] = UNSET
    """The current version of the application running on the Terminal."""

    wifi_network_name: OptionalNullable[str] = UNSET
    """The name of the Wi-Fi network to which the Terminal is connected."""

    wifi_network_strength: OptionalNullable[str] = UNSET
    """The signal strength of the Wi-FI network connection. Options: ``POOR``, ``FAIR``, ``GOOD``, ``EXCELLENT``"""

    ip_address: OptionalNullable[str] = UNSET
    """The IP address of the Terminal."""


class DeviceMetadataDict(TypedDict):
    battery_percentage: NotRequired[str | None]
    charging_state: NotRequired[str | None]
    location_id: NotRequired[str | None]
    merchant_id: NotRequired[str | None]
    network_connection_type: NotRequired[str | None]
    payment_region: NotRequired[str | None]
    serial_number: NotRequired[str | None]
    os_version: NotRequired[str | None]
    app_version: NotRequired[str | None]
    wifi_network_name: NotRequired[str | None]
    wifi_network_strength: NotRequired[str | None]
    ip_address: NotRequired[str | None]
