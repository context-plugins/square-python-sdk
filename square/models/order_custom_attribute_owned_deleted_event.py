from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_event_data import CustomAttributeEventData, CustomAttributeEventDataDict


class OrderCustomAttributeOwnedDeletedEvent(SdkBaseModel):
    """Published when an order `custom attribute <entity:CustomAttribute>`__ associated with a `custom attribute
    definition <entity:CustomAttributeDefinition>`__ that is owned by the subscribing app is deleted."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target seller associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"order.custom_attribute.owned.deleted"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[CustomAttributeEventData] = UNSET


class OrderCustomAttributeOwnedDeletedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomAttributeEventDataDict]
