from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .order_fulfillment_updated_event_data import OrderFulfillmentUpdatedEventData, OrderFulfillmentUpdatedEventDataDict


class OrderFulfillmentUpdatedEvent(SdkBaseModel):
    """Published when an `OrderFulfillment <entity:OrderFulfillment>`__ is created or updated. This event is triggered
    only by the `UpdateOrder <api-endpoint:Orders-UpdateOrder>`__ endpoint call."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"order.fulfillment.updated"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[OrderFulfillmentUpdatedEventData] = UNSET


class OrderFulfillmentUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[OrderFulfillmentUpdatedEventDataDict]
