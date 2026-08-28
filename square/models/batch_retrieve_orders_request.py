from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class BatchRetrieveOrdersRequest(SdkBaseModel):
    """Defines the fields that are included in requests to the ``BatchRetrieveOrders`` endpoint."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the location for these orders. This field is optional: omit it to retrieve orders within the scope of
    the current authorization's merchant ID."""

    order_ids: list[str]
    """The IDs of the orders to retrieve. A maximum of 100 orders can be retrieved per request."""


class BatchRetrieveOrdersRequestDict(TypedDict):
    location_id: NotRequired[str | None]
    order_ids: list[str]
