from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .vendor_updated_event_data import VendorUpdatedEventData, VendorUpdatedEventDataDict


class VendorUpdatedEvent(SdkBaseModel):
    """Published when a `Vendor <entity:Vendor>`__ is updated."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of a seller associated with this event."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of a seller location associated with this event, if the event is associated with the location."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"vendor.updated".``"""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for this webhoook event."""

    created_at: Optional[str] = UNSET
    """The RFC 3339-formatted time when the underlying event data object is created."""

    data: Optional[VendorUpdatedEventData] = UNSET
    """Defines the ``vendor.updated`` event data structure."""


class VendorUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[VendorUpdatedEventData | VendorUpdatedEventDataDict]
