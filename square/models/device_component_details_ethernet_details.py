from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DeviceComponentDetailsEthernetDetails(SdkBaseModel):
    active: OptionalNullable[bool] = UNSET
    """A boolean to represent whether the Ethernet interface is currently active."""

    ip_address_v4: OptionalNullable[str] = UNSET
    """The string representation of the device’s IPv4 address."""

    mac_address: OptionalNullable[str] = UNSET
    """The mac address of the device in this network."""


class DeviceComponentDetailsEthernetDetailsDict(TypedDict):
    active: NotRequired[bool | None]
    ip_address_v4: NotRequired[str | None]
    mac_address: NotRequired[str | None]
