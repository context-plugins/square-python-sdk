from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .gift_card_updated_event_object import GiftCardUpdatedEventObject, GiftCardUpdatedEventObjectDict


class GiftCardUpdatedEventData(SdkBaseModel):
    """The data associated with a ``gift_card.updated`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``gift_card``."""

    id: Optional[str] = UNSET
    """The ID of the updated gift card."""

    object_: Optional[GiftCardUpdatedEventObject] = Field(default=UNSET, alias="object")
    """An object that contains the gift card associated with a ``gift_card.updated`` event."""


class GiftCardUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[GiftCardUpdatedEventObject | GiftCardUpdatedEventObjectDict]
