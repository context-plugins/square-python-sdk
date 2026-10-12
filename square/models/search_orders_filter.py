from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_orders_customer_filter import SearchOrdersCustomerFilter, SearchOrdersCustomerFilterDict
from .search_orders_date_time_filter import SearchOrdersDateTimeFilter, SearchOrdersDateTimeFilterDict
from .search_orders_fulfillment_filter import SearchOrdersFulfillmentFilter, SearchOrdersFulfillmentFilterDict
from .search_orders_source_filter import SearchOrdersSourceFilter, SearchOrdersSourceFilterDict
from .search_orders_state_filter import SearchOrdersStateFilter, SearchOrdersStateFilterDict


class SearchOrdersFilter(SdkBaseModel):
    """Filtering criteria to use for a ``SearchOrders`` request. Multiple filters are ANDed together."""

    state_filter: Optional[SearchOrdersStateFilter] = UNSET
    """Filter by the current order ``state``."""

    date_time_filter: Optional[SearchOrdersDateTimeFilter] = UNSET
    """Filter for ``Order`` objects based on whether their ``CREATED_AT``, ``CLOSED_AT``, or ``UPDATED_AT`` timestamps
    fall within a specified time range. You can specify the time range and which timestamp to filter for. You can filter
    for only one time range at a time.

    For each time range, the start time and end time are inclusive. If the end time is absent, it defaults to the time
    of the first request for the cursor.

    __Important:__ If you use the ``DateTimeFilter`` in a ``SearchOrders`` query, you must set the ``sort_field`` in
    `OrdersSort <entity:SearchOrdersSort>`__ to the same field you filter for. For example, if you set the ``CLOSED_AT``
    field in ``DateTimeFilter``, you must set the ``sort_field`` in ``SearchOrdersSort`` to ``CLOSED_AT``. Otherwise,
    ``SearchOrders`` throws an error. `Learn more about filtering orders by time range.
    <https://developer.squareup.com/docs/orders-api/manage-orders/search-orders#important-note-about-filtering-orders-by-time-range>`__"""

    fulfillment_filter: Optional[SearchOrdersFulfillmentFilter] = UNSET
    """Filter based on `order fulfillment <entity:Fulfillment>`__ information."""

    source_filter: Optional[SearchOrdersSourceFilter] = UNSET
    """A filter based on order ``source`` information."""

    customer_filter: Optional[SearchOrdersCustomerFilter] = UNSET
    """A filter based on the order ``customer_id`` and any tender ``customer_id`` associated with the order. It does not
    filter based on the `FulfillmentRecipient <entity:FulfillmentRecipient>`__ ``customer_id``."""


class SearchOrdersFilterDict(TypedDict):
    state_filter: NotRequired[SearchOrdersStateFilterDict]
    date_time_filter: NotRequired[SearchOrdersDateTimeFilterDict]
    fulfillment_filter: NotRequired[SearchOrdersFulfillmentFilterDict]
    source_filter: NotRequired[SearchOrdersSourceFilterDict]
    customer_filter: NotRequired[SearchOrdersCustomerFilterDict]
