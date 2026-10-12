from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .loyalty_account_created_event_object import LoyaltyAccountCreatedEventObject, LoyaltyAccountCreatedEventObjectDict


class LoyaltyAccountCreatedEventData(SdkBaseModel):
    """The data associated with a ``loyalty.account.created`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``loyalty_account``."""

    id: Optional[str] = UNSET
    """The ID of the affected loyalty account."""

    object_: Optional[LoyaltyAccountCreatedEventObject] = Field(default=UNSET, alias="object")


class LoyaltyAccountCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LoyaltyAccountCreatedEventObjectDict]
