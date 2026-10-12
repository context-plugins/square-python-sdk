from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .device_created_event_data import DeviceCreatedEventData, DeviceCreatedEventDataDict


class DeviceCreatedEvent(SdkBaseModel):
    """Published when a Device is created."""

    merchant_id: OptionalNullable[str] = UNSET
    """The merchant the newly created device belongs to."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents. The value is ``"device.created"``."""

    event_id: OptionalNullable[str] = UNSET
    """A UUID that uniquely identifies this device creation event."""

    created_at: Optional[str] = UNSET
    """The time when the device creation event was first created, in RFC 3339 format."""

    data: Optional[DeviceCreatedEventData] = UNSET


class DeviceCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[DeviceCreatedEventDataDict]
