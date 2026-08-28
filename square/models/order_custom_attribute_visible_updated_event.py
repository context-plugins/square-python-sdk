from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_event_data import CustomAttributeEventData, CustomAttributeEventDataDict


class OrderCustomAttributeVisibleUpdatedEvent(SdkBaseModel):
    """Published when an order `custom attribute <entity:CustomAttribute>`__ that is visible to the subscribing app is
    updated."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target seller associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"order.custom_attribute.visible.updated"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[CustomAttributeEventData] = UNSET


class OrderCustomAttributeVisibleUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomAttributeEventData | CustomAttributeEventDataDict]
