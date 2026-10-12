from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .appointment_segment import AppointmentSegment, AppointmentSegmentDict


class Availability(SdkBaseModel):
    """Defines an appointment slot that encapsulates the appointment segments, location and starting time available for
    booking."""

    start_at: OptionalNullable[str] = UNSET
    """The RFC 3339 timestamp specifying the beginning time of the slot available for booking."""

    location_id: Optional[str] = UNSET
    """The ID of the location available for booking."""

    appointment_segments: OptionalNullable[list[AppointmentSegment]] = UNSET
    """The list of appointment segments available for booking"""


class AvailabilityDict(TypedDict):
    start_at: NotRequired[str | None]
    location_id: NotRequired[str]
    appointment_segments: NotRequired[list[AppointmentSegmentDict] | None]
