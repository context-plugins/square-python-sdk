from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .booking_created_event_object import BookingCreatedEventObject, BookingCreatedEventObjectDict


class BookingCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the event data object. The value is ``"booking"``."""

    id: Optional[str] = UNSET
    """The ID of the event data object."""

    object_: Optional[BookingCreatedEventObject] = Field(default=UNSET, alias="object")


class BookingCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[BookingCreatedEventObjectDict]
