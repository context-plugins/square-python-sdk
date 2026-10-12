from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_definition_event_data import (
    CustomAttributeDefinitionEventData,
    CustomAttributeDefinitionEventDataDict,
)


class CustomerCustomAttributeDefinitionCreatedPublicEvent(SdkBaseModel):
    """Published when a customer `custom attribute definition <entity:CustomAttributeDefinition>`__ that is visible to
    all applications is created. A notification is sent when any application creates a custom attribute definition whose
    ``visibility`` is ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``.

    This event is replaced by `customer.custom_attribute_definition.visible.created
    <webhook:customer.custom_attribute_definition.visible.created>`__, which applies to custom attribute definitions
    that are visible to the subscribing application."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the seller associated with the event that triggered the event notification."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"customer.custom_attribute_definition.public.created"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event notification."""

    created_at: Optional[str] = UNSET
    """The timestamp that indicates when the event notification was created, in RFC 3339 format."""

    data: Optional[CustomAttributeDefinitionEventData] = UNSET
    """Represents an object in the CustomAttributeDefinition event notification payload that contains the affected
    custom attribute definition."""


class CustomerCustomAttributeDefinitionCreatedPublicEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomAttributeDefinitionEventDataDict]
