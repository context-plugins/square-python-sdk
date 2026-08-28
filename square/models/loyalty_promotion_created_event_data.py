from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .loyalty_promotion_created_event_object import (
    LoyaltyPromotionCreatedEventObject,
    LoyaltyPromotionCreatedEventObjectDict,
)


class LoyaltyPromotionCreatedEventData(SdkBaseModel):
    """The data associated with a ``loyalty.promotion.created`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``loyalty_promotion``."""

    id: Optional[str] = UNSET
    """The ID of the affected loyalty promotion."""

    object_: Optional[LoyaltyPromotionCreatedEventObject] = Field(default=UNSET, alias="object")
    """An object that contains the loyalty promotion associated with a ``loyalty.promotion.created`` event."""


class LoyaltyPromotionCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LoyaltyPromotionCreatedEventObject | LoyaltyPromotionCreatedEventObjectDict]
