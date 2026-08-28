from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .time_range import TimeRange, TimeRangeDict


class LoyaltyEventDateTimeFilter(SdkBaseModel):
    """Filter events by date time range."""

    created_at: TimeRange
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""


class LoyaltyEventDateTimeFilterDict(TypedDict):
    created_at: TimeRange | TimeRangeDict
