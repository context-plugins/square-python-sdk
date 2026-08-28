from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DateRange(SdkBaseModel):
    """A range defined by two dates. Used for filtering a query for Connect v2 objects that have date properties."""

    start_date: OptionalNullable[str] = UNSET
    """A string in ``YYYY-MM-DD`` format, such as ``2017-10-31``, per the ISO 8601 extended format for calendar dates.
    The beginning of a date range (inclusive)."""

    end_date: OptionalNullable[str] = UNSET
    """A string in ``YYYY-MM-DD`` format, such as ``2017-10-31``, per the ISO 8601 extended format for calendar dates.
    The end of a date range (inclusive)."""


class DateRangeDict(TypedDict):
    start_date: NotRequired[str | None]
    end_date: NotRequired[str | None]
