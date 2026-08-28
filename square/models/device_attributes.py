from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.device_attributes_device_type import DeviceAttributesDeviceTypeOrStr


class DeviceAttributes(SdkBaseModel):
    type_: DeviceAttributesDeviceTypeOrStr = Field(alias="type")
    """An enum identifier of the device type."""

    manufacturer: str
    """The maker of the device."""

    model: OptionalNullable[str] = UNSET
    """The specific model of the device."""

    name: OptionalNullable[str] = UNSET
    """A seller-specified name for the device."""

    manufacturers_id: OptionalNullable[str] = UNSET
    """The manufacturer-supplied identifier for the device (where available). In many cases, this identifier will be a
    serial number."""

    updated_at: Optional[str] = UNSET
    """The RFC 3339-formatted value of the most recent update to the device information. (Could represent any field
    update on the device.)"""

    version: Optional[str] = UNSET
    """The current version of software installed on the device."""

    merchant_token: OptionalNullable[str] = UNSET
    """The merchant_token identifying the merchant controlling the device."""


class DeviceAttributesDict(TypedDict):
    type_: DeviceAttributesDeviceTypeOrStr
    manufacturer: str
    model: NotRequired[str | None]
    name: NotRequired[str | None]
    manufacturers_id: NotRequired[str | None]
    updated_at: NotRequired[str]
    version: NotRequired[str]
    merchant_token: NotRequired[str | None]
