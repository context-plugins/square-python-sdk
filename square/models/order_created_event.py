from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .order_created_event_data import OrderCreatedEventData, OrderCreatedEventDataDict


class OrderCreatedEvent(SdkBaseModel):
    """Published when an `Order <entity:Order>`__ is created. This event is triggered only by the `CreateOrder
    <api-endpoint:Orders-CreateOrder>`__ endpoint call.

    Creating an order in the Point of Sale app will **not** publish this event."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"order.created"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[OrderCreatedEventData] = UNSET


class OrderCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[OrderCreatedEventDataDict]
