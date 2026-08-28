from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DeviceDetails(SdkBaseModel):
    """Details about the device that took the payment."""

    device_id: OptionalNullable[str] = UNSET
    """The Square-issued ID of the device."""

    device_installation_id: OptionalNullable[str] = UNSET
    """The Square-issued installation ID for the device."""

    device_name: OptionalNullable[str] = UNSET
    """The name of the device set by the seller."""


class DeviceDetailsDict(TypedDict):
    device_id: NotRequired[str | None]
    device_installation_id: NotRequired[str | None]
    device_name: NotRequired[str | None]
