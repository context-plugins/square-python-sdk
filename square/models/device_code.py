from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.device_code_status import DeviceCodeStatusOrStr
from .enums.product_type import ProductTypeOrStr


class DeviceCode(SdkBaseModel):
    id: Optional[str] = UNSET
    """The unique id for this device code."""

    name: OptionalNullable[str] = UNSET
    """An optional user-defined name for the device code."""

    code: Optional[str] = UNSET
    """The unique code that can be used to login."""

    device_id: Optional[str] = UNSET
    """The unique id of the device that used this code. Populated when the device is paired up."""

    product_type: ProductTypeOrStr
    location_id: OptionalNullable[str] = UNSET
    """The location assigned to this code."""

    status: Optional[DeviceCodeStatusOrStr] = UNSET
    """DeviceCode.Status enum."""

    pair_by: Optional[str] = UNSET
    """When this DeviceCode will expire and no longer login. Timestamp in RFC 3339 format."""

    created_at: Optional[str] = UNSET
    """When this DeviceCode was created. Timestamp in RFC 3339 format."""

    status_changed_at: Optional[str] = UNSET
    """When this DeviceCode's status was last changed. Timestamp in RFC 3339 format."""

    paired_at: Optional[str] = UNSET
    """When this DeviceCode was paired. Timestamp in RFC 3339 format."""


class DeviceCodeDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str | None]
    code: NotRequired[str]
    device_id: NotRequired[str]
    product_type: ProductTypeOrStr
    location_id: NotRequired[str | None]
    status: NotRequired[DeviceCodeStatusOrStr]
    pair_by: NotRequired[str]
    created_at: NotRequired[str]
    status_changed_at: NotRequired[str]
    paired_at: NotRequired[str]
