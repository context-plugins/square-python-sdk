from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .loyalty_account_deleted_event_object import LoyaltyAccountDeletedEventObject, LoyaltyAccountDeletedEventObjectDict


class LoyaltyAccountDeletedEventData(SdkBaseModel):
    """The data associated with a ``loyalty.account.deleted`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``loyalty_account``."""

    id: Optional[str] = UNSET
    """The ID of the affected loyalty account."""

    object_: Optional[LoyaltyAccountDeletedEventObject] = Field(default=UNSET, alias="object")


class LoyaltyAccountDeletedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LoyaltyAccountDeletedEventObject | LoyaltyAccountDeletedEventObjectDict]
