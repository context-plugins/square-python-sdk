from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ScheduledShiftDetails(SdkBaseModel):
    """Represents shift details for draft and published versions of a `scheduled shift <entity:ScheduledShift>`__, such
    as job ID, team member assignment, and start and end times."""

    team_member_id: OptionalNullable[str] = UNSET
    """The ID of the `team member <entity:TeamMember>`__ scheduled for the shift."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the `location <entity:Location>`__ the shift is scheduled for."""

    job_id: OptionalNullable[str] = UNSET
    """The ID of the `job <entity:Job>`__ the shift is scheduled for."""

    start_at: OptionalNullable[str] = UNSET
    """The start time of the shift, in RFC 3339 format in the time zone &plus; offset of the shift location specified in
    ``location_id``. Precision up to the minute is respected; seconds are truncated."""

    end_at: OptionalNullable[str] = UNSET
    """The end time for the shift, in RFC 3339 format in the time zone &plus; offset of the shift location specified in
    ``location_id``. Precision up to the minute is respected; seconds are truncated."""

    notes: OptionalNullable[str] = UNSET
    """Optional notes for the shift."""

    is_deleted: OptionalNullable[bool] = UNSET
    """Indicates whether the draft shift version is deleted. If set to ``true`` when the shift is published, the entire
    scheduled shift (including the published shift) is deleted and cannot be accessed using any endpoint."""

    timezone: Optional[str] = UNSET
    """The time zone of the shift location, calculated based on the ``location_id``. This field is provided for
    convenience."""


class ScheduledShiftDetailsDict(TypedDict):
    team_member_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    job_id: NotRequired[str | None]
    start_at: NotRequired[str | None]
    end_at: NotRequired[str | None]
    notes: NotRequired[str | None]
    is_deleted: NotRequired[bool | None]
    timezone: NotRequired[str]
