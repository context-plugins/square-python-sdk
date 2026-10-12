from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .loyalty_event_created_event_object import LoyaltyEventCreatedEventObject, LoyaltyEventCreatedEventObjectDict


class LoyaltyEventCreatedEventData(SdkBaseModel):
    """The data associated with a ``loyalty.event.created`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``loyalty_event``."""

    id: Optional[str] = UNSET
    """ID of the affected loyalty event."""

    object_: Optional[LoyaltyEventCreatedEventObject] = Field(default=UNSET, alias="object")


class LoyaltyEventCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LoyaltyEventCreatedEventObjectDict]
