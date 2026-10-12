from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .device_code_paired_event_data import DeviceCodePairedEventData, DeviceCodePairedEventDataDict


class DeviceCodePairedEvent(SdkBaseModel):
    """Published when a Square Terminal has been paired with a Terminal API client and the device_id of the paired
    Square Terminal is available."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the target location associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"device.code.paired"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """RFC 3339 timestamp of when the event was created."""

    data: Optional[DeviceCodePairedEventData] = UNSET


class DeviceCodePairedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[DeviceCodePairedEventDataDict]
