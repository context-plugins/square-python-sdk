from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.order_state import OrderStateOrStr
from .order_fulfillment_updated_update import OrderFulfillmentUpdatedUpdate, OrderFulfillmentUpdatedUpdateDict


class OrderFulfillmentUpdated(SdkBaseModel):
    order_id: OptionalNullable[str] = UNSET
    """The order's unique ID."""

    version: Optional[int] = UNSET
    """The version number, which is incremented each time an update is committed to the order. Orders that were not
    created through the API do not include a version number and therefore cannot be updated.

    `Read more about working with versions.
    <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders>`__"""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the seller location that this order is associated with."""

    state: Optional[OrderStateOrStr] = UNSET
    """The state of the order."""

    created_at: Optional[str] = UNSET
    """The timestamp for when the order was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp for when the order was last updated, in RFC 3339 format."""

    fulfillment_update: OptionalNullable[list[OrderFulfillmentUpdatedUpdate]] = UNSET
    """The fulfillments that were updated with this version change."""


class OrderFulfillmentUpdatedDict(TypedDict):
    order_id: NotRequired[str | None]
    version: NotRequired[int]
    location_id: NotRequired[str | None]
    state: NotRequired[OrderStateOrStr]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    fulfillment_update: NotRequired[list[OrderFulfillmentUpdatedUpdateDict] | None]
