from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .segment_filter import SegmentFilter, SegmentFilterDict
from .time_range import TimeRange, TimeRangeDict


class SearchAvailabilityFilter(SdkBaseModel):
    """A query filter to search for buyer-accessible availabilities by."""

    start_at_range: TimeRange
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    location_id: OptionalNullable[str] = UNSET
    """The query expression to search for buyer-accessible availabilities with their location IDs matching the specified
    location ID. This query expression cannot be set if ``booking_id`` is set."""

    segment_filters: OptionalNullable[list[SegmentFilter]] = UNSET
    """The query expression to search for buyer-accessible availabilities matching the specified list of segment
    filters. If the size of the ``segment_filters`` list is ``n``, the search returns availabilities with ``n`` segments
    per availability.

    This query expression cannot be set if ``booking_id`` is set."""

    booking_id: OptionalNullable[str] = UNSET
    """The query expression to search for buyer-accessible availabilities for an existing booking by matching the
    specified ``booking_id`` value. This is commonly used to reschedule an appointment. If this expression is set, the
    ``location_id`` and ``segment_filters`` expressions cannot be set."""


class SearchAvailabilityFilterDict(TypedDict):
    start_at_range: TimeRangeDict
    location_id: NotRequired[str | None]
    segment_filters: NotRequired[list[SegmentFilterDict] | None]
    booking_id: NotRequired[str | None]
