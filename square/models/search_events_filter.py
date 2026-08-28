from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .time_range import TimeRange, TimeRangeDict


class SearchEventsFilter(SdkBaseModel):
    """Criteria to filter events by."""

    event_types: Optional[list[str | None]] = UNSET
    """Filter events by event types."""

    merchant_ids: Optional[list[str | None]] = UNSET
    """Filter events by merchant."""

    location_ids: Optional[list[str | None]] = UNSET
    """Filter events by location."""

    created_at: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""


class SearchEventsFilterDict(TypedDict):
    event_types: NotRequired[list[str | None]]
    merchant_ids: NotRequired[list[str | None]]
    location_ids: NotRequired[list[str | None]]
    created_at: NotRequired[TimeRange | TimeRangeDict]
