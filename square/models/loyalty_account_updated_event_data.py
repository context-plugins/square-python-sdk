from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .loyalty_account_updated_event_object import LoyaltyAccountUpdatedEventObject, LoyaltyAccountUpdatedEventObjectDict


class LoyaltyAccountUpdatedEventData(SdkBaseModel):
    """The data associated with a ``loyalty.account.updated`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``loyalty_account``."""

    id: Optional[str] = UNSET
    """The ID of the affected loyalty account."""

    object_: Optional[LoyaltyAccountUpdatedEventObject] = Field(default=UNSET, alias="object")


class LoyaltyAccountUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LoyaltyAccountUpdatedEventObject | LoyaltyAccountUpdatedEventObjectDict]
