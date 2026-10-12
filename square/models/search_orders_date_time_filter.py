from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .time_range import TimeRange, TimeRangeDict


class SearchOrdersDateTimeFilter(SdkBaseModel):
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

    created_at: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    updated_at: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    closed_at: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""


class SearchOrdersDateTimeFilterDict(TypedDict):
    created_at: NotRequired[TimeRangeDict]
    updated_at: NotRequired[TimeRangeDict]
    closed_at: NotRequired[TimeRangeDict]
