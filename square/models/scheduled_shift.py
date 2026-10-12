from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scheduled_shift_details import ScheduledShiftDetails, ScheduledShiftDetailsDict


class ScheduledShift(SdkBaseModel):
    """Represents a specific time slot in a work schedule. This object is used to manage the lifecycle of a scheduled
    shift from the draft to published state. A scheduled shift contains the latest draft shift details and current
    published shift details."""

    id: Optional[str] = UNSET
    """**Read only** The Square-issued ID of the scheduled shift."""

    draft_shift_details: Optional[ScheduledShiftDetails] = UNSET
    """Represents shift details for draft and published versions of a `scheduled shift <entity:ScheduledShift>`__, such
    as job ID, team member assignment, and start and end times."""

    published_shift_details: Optional[ScheduledShiftDetails] = UNSET
    """Represents shift details for draft and published versions of a `scheduled shift <entity:ScheduledShift>`__, such
    as job ID, team member assignment, and start and end times."""

    version: Optional[int] = UNSET
    """**Read only** The current version of the scheduled shift, which is incremented with each update. This field is
    used for `optimistic concurrency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__ control to ensure
    that requests don't overwrite data from another request."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the scheduled shift was created, in RFC 3339 format presented as UTC."""

    updated_at: Optional[str] = UNSET
    """The timestamp of when the scheduled shift was last updated, in RFC 3339 format presented as UTC."""


class ScheduledShiftDict(TypedDict):
    id: NotRequired[str]
    draft_shift_details: NotRequired[ScheduledShiftDetailsDict]
    published_shift_details: NotRequired[ScheduledShiftDetailsDict]
    version: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
