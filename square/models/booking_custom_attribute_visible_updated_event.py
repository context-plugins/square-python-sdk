from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_event_data import CustomAttributeEventData, CustomAttributeEventDataDict


class BookingCustomAttributeVisibleUpdatedEvent(SdkBaseModel):
    """Published when a booking `custom attribute <entity:CustomAttribute>`__ with the ``visibility`` field set to
    ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES`` is updated. An application that subscribes to this
    event is notified when a booking custom attribute is updated by any application for which the subscribing
    application has read access to the booking custom attribute."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the seller associated with the event that triggered the event notification."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"booking.custom_attribute.visible.updated"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event notification."""

    created_at: Optional[str] = UNSET
    """The timestamp that indicates when the event notification was created, in RFC 3339 format."""

    data: Optional[CustomAttributeEventData] = UNSET


class BookingCustomAttributeVisibleUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomAttributeEventDataDict]
