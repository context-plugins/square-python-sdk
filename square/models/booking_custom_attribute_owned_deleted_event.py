from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_event_data import CustomAttributeEventData, CustomAttributeEventDataDict


class BookingCustomAttributeOwnedDeletedEvent(SdkBaseModel):
    """Published when a booking `custom attribute <entity:CustomAttribute>`__ associated with a `custom attribute
    definition <entity:CustomAttributeDefinition>`__ that is owned by the subscribing application is deleted. Subscribe
    to this event to be notified when your application deletes a booking custom attribute."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the seller associated with the event that triggered the event notification."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"booking.custom_attribute.owned.deleted"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event notification."""

    created_at: Optional[str] = UNSET
    """The timestamp that indicates when the event notification was created, in RFC 3339 format."""

    data: Optional[CustomAttributeEventData] = UNSET


class BookingCustomAttributeOwnedDeletedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomAttributeEventData | CustomAttributeEventDataDict]
