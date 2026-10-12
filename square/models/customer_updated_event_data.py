from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .customer_updated_event_object import CustomerUpdatedEventObject, CustomerUpdatedEventObjectDict


class CustomerUpdatedEventData(SdkBaseModel):
    """The data associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``customer``."""

    id: Optional[str] = UNSET
    """The ID of the updated customer."""

    object_: Optional[CustomerUpdatedEventObject] = Field(default=UNSET, alias="object")
    """An object that contains the customer associated with the event."""


class CustomerUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[CustomerUpdatedEventObjectDict]
