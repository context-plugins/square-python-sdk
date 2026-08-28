from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .vendor_created_event_data import VendorCreatedEventData, VendorCreatedEventDataDict


class VendorCreatedEvent(SdkBaseModel):
    """Published when a `Vendor <entity:Vendor>`__ is created."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of a seller associated with this event."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of a location associated with the event, if the event is associated with the location of the seller."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"vendor.created".``"""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for this event."""

    created_at: Optional[str] = UNSET
    """The RFC 3339-formatted time when the underlying event data object is created."""

    data: Optional[VendorCreatedEventData] = UNSET
    """Defines the ``vendor.created`` event data structure."""


class VendorCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[VendorCreatedEventData | VendorCreatedEventDataDict]
