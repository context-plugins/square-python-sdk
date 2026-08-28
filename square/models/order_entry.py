from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class OrderEntry(SdkBaseModel):
    """A lightweight description of an `order <entity:Order>`__ that is returned when ``returned_entries`` is ``true``
    on a `SearchOrdersRequest <api-endpoint:Orders-SearchOrders>`__."""

    order_id: OptionalNullable[str] = UNSET
    """The ID of the order."""

    version: Optional[int] = UNSET
    """The version number, which is incremented each time an update is committed to the order. Orders that were not
    created through the API do not include a version number and therefore cannot be updated.

    `Read more about working with versions.
    <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders>`__"""

    location_id: OptionalNullable[str] = UNSET
    """The location ID the order belongs to."""


class OrderEntryDict(TypedDict):
    order_id: NotRequired[str | None]
    version: NotRequired[int]
    location_id: NotRequired[str | None]
