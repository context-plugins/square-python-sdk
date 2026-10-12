from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .location_created_event_data import LocationCreatedEventData, LocationCreatedEventDataDict


class LocationCreatedEvent(SdkBaseModel):
    """Published when a `Location <entity:Location>`__ is created."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the `Location <entity:Location>`__ associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"location.created"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[LocationCreatedEventData] = UNSET


class LocationCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[LocationCreatedEventDataDict]
