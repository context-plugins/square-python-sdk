from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_event_data import CustomAttributeEventData, CustomAttributeEventDataDict


class MerchantCustomAttributeOwnedUpdatedEvent(SdkBaseModel):
    """Published when a merchant `custom attribute <entity:CustomAttribute>`__ associated with a `custom attribute
    definition <entity:CustomAttributeDefinition>`__ that is owned by the subscribing application is updated. Subscribe
    to this event to be notified when your application updates a merchant custom attribute."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the seller associated with the event that triggered the event notification."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"merchant.custom_attribute.owned.updated"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event notification."""

    created_at: Optional[str] = UNSET
    """The timestamp that indicates when the event notification was created, in RFC 3339 format."""

    data: Optional[CustomAttributeEventData] = UNSET


class MerchantCustomAttributeOwnedUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomAttributeEventDataDict]
