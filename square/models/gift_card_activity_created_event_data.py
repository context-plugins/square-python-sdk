from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .gift_card_activity_created_event_object import (
    GiftCardActivityCreatedEventObject,
    GiftCardActivityCreatedEventObjectDict,
)


class GiftCardActivityCreatedEventData(SdkBaseModel):
    """Represents the data associated with a ``gift_card.activity.created`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``gift_card_activity``."""

    id: Optional[str] = UNSET
    """The ID of the new gift card activity."""

    object_: Optional[GiftCardActivityCreatedEventObject] = Field(default=UNSET, alias="object")
    """An object that contains the gift card activity associated with a ``gift_card.activity.created`` event."""


class GiftCardActivityCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[GiftCardActivityCreatedEventObject | GiftCardActivityCreatedEventObjectDict]
