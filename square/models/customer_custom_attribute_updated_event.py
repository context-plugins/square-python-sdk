from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_event_data import CustomAttributeEventData, CustomAttributeEventDataDict


class CustomerCustomAttributeUpdatedEvent(SdkBaseModel):
    """Published when a customer `custom attribute <entity:CustomAttribute>`__ owned by the subscribing application is
    created or updated. Custom attributes are owned by the application that created the corresponding `custom attribute
    definition <entity:CustomAttributeDefinition>`__. Custom attributes whose ``visibility`` is
    ``VISIBILITY_READ_WRITE_VALUES`` can be created or updated by any application.

    This event is replaced by `customer.custom_attribute.owned.updated
    <webhook:customer.custom_attribute.owned.updated>`__."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the seller associated with the event that triggered the event notification."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of this event. The value is ``"customer.custom_attribute.updated"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event notification."""

    created_at: Optional[str] = UNSET
    """The timestamp that indicates when the event notification was created, in RFC 3339 format."""

    data: Optional[CustomAttributeEventData] = UNSET


class CustomerCustomAttributeUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[CustomAttributeEventData | CustomAttributeEventDataDict]
