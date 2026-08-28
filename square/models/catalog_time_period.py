from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogTimePeriod(SdkBaseModel):
    """Represents a time period - either a single period or a repeating period."""

    event: OptionalNullable[str] = UNSET
    """An iCalendar (RFC 5545) `event <https://tools.ietf.org/html/rfc5545#section-3.6.1>`__, which specifies the name,
    timing, duration and recurrence of this time period.

    Example:

    ```
    DTSTART:20190707T180000 DURATION:P2H RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR
    ```

    Only ``SUMMARY``, ``DTSTART``, ``DURATION`` and ``RRULE`` fields are supported. ``DTSTART`` must be in local
    (unzoned) time format. Note that while ``BEGIN:VEVENT`` and ``END:VEVENT`` is not required in the request. The
    response will always include them."""


class CatalogTimePeriodDict(TypedDict):
    event: NotRequired[str | None]
