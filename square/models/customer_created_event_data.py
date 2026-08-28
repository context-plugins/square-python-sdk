from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .customer_created_event_object import CustomerCreatedEventObject, CustomerCreatedEventObjectDict


class CustomerCreatedEventData(SdkBaseModel):
    """The data associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``customer``."""

    id: Optional[str] = UNSET
    """The ID of the new customer."""

    object_: Optional[CustomerCreatedEventObject] = Field(default=UNSET, alias="object")
    """An object that contains the customer associated with the event."""


class CustomerCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[CustomerCreatedEventObject | CustomerCreatedEventObjectDict]
