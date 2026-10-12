from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .subscription_created_event_object import SubscriptionCreatedEventObject, SubscriptionCreatedEventObjectDict


class SubscriptionCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"subscription"``."""

    id: Optional[str] = UNSET
    """ID of the affected subscription."""

    object_: Optional[SubscriptionCreatedEventObject] = Field(default=UNSET, alias="object")


class SubscriptionCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[SubscriptionCreatedEventObjectDict]
