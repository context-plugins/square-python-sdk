from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .gift_card_activity_updated_event_object import (
    GiftCardActivityUpdatedEventObject,
    GiftCardActivityUpdatedEventObjectDict,
)


class GiftCardActivityUpdatedEventData(SdkBaseModel):
    """The data associated with a ``gift_card.activity.updated`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``gift_card_activity``."""

    id: Optional[str] = UNSET
    """The ID of the updated gift card activity."""

    object_: Optional[GiftCardActivityUpdatedEventObject] = Field(default=UNSET, alias="object")
    """An object that contains the gift card activity associated with a ``gift_card.activity.updated`` event."""


class GiftCardActivityUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[GiftCardActivityUpdatedEventObjectDict]
