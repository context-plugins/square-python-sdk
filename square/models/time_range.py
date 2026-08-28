from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class TimeRange(SdkBaseModel):
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    start_at: OptionalNullable[str] = UNSET
    """A datetime value in RFC 3339 format indicating when the time range starts."""

    end_at: OptionalNullable[str] = UNSET
    """A datetime value in RFC 3339 format indicating when the time range ends."""


class TimeRangeDict(TypedDict):
    start_at: NotRequired[str | None]
    end_at: NotRequired[str | None]
