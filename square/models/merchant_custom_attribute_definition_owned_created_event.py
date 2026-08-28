from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_definition_event_data import (
    CustomAttributeDefinitionEventData,
    CustomAttributeDefinitionEventDataDict,
)


class MerchantCustomAttributeDefinitionOwnedCreatedEvent(SdkBaseModel):
    """Published when a merchant `custom attribute definition <entity:CustomAttributeDefinition>`__ is created by the
    subscribing application. Subscribe to this event to be notified when your application creates a merchant custom
    attribute definition."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the seller associated with the event that triggered the event notification."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"merchant.custom_attribute_definition.owned.created"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event notification."""

    created_at: Optional[str] = UNSET
    """The timestamp that indicates when the event notification was created, in RFC 3339 format."""

    data: Optional[CustomAttributeDefinitionEventData] = UNSET
    """Represents an object in the CustomAttributeDefinition event notification payload that contains the affected
    custom attribute definition."""


class MerchantCustomAttributeDefinitionOwnedCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomAttributeDefinitionEventData | CustomAttributeDefinitionEventDataDict]
