from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .booking_updated_event_object import BookingUpdatedEventObject, BookingUpdatedEventObjectDict


class BookingUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the event data object. The value is ``"booking"``."""

    id: Optional[str] = UNSET
    """The ID of the event data object."""

    object_: Optional[BookingUpdatedEventObject] = Field(default=UNSET, alias="object")


class BookingUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[BookingUpdatedEventObjectDict]
