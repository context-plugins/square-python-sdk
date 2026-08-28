from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.scheduled_shift_filter_assignment_status import ScheduledShiftFilterAssignmentStatusOrStr
from .enums.scheduled_shift_filter_scheduled_shift_status import ScheduledShiftFilterScheduledShiftStatusOrStr
from .scheduled_shift_workday import ScheduledShiftWorkday, ScheduledShiftWorkdayDict
from .time_range import TimeRange, TimeRangeDict


class ScheduledShiftFilter(SdkBaseModel):
    """Defines filter criteria for a `SearchScheduledShifts <api-endpoint:Labor-SearchScheduledShifts>`__ request.
    Multiple filters in a query are combined as an ``AND`` operation."""

    location_ids: Optional[list[str | None]] = UNSET
    """Return shifts for the specified locations. When omitted, shifts for all locations are returned. If needed, call
    `ListLocations <api-endpoint:Locations-ListLocations>`__ to get location IDs."""

    start: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    end: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    workday: Optional[ScheduledShiftWorkday] = UNSET
    """A ``ScheduledShift`` search query filter parameter that sets a range of days that a ``Shift`` must start or end
    in before passing the filter condition."""

    team_member_ids: Optional[list[str | None]] = UNSET
    """Return shifts assigned to specified team members. If needed, call `SearchTeamMembers
    <api-endpoint:Team-SearchTeamMembers>`__ to get team member IDs.

    To return only the shifts assigned to the specified team members, include the ``assignment_status`` filter in the
    query. Otherwise, all unassigned shifts are returned along with shifts assigned to the specified team members."""

    assignment_status: Optional[ScheduledShiftFilterAssignmentStatusOrStr] = UNSET
    """Defines valid values for the ``assignment_status`` filter in a `SearchScheduledShifts
    <api-endpoint:Labor-SearchScheduledShifts>`__ request. Assignment status is based on the
    ``draft_shift_details.team_member_id`` and ``published_shift_details.team_member_id`` fields of the scheduled
    shift."""

    scheduled_shift_statuses: Optional[list[ScheduledShiftFilterScheduledShiftStatusOrStr | None]] = UNSET
    """Return shifts based on the draft or published status of the shift. A shift is published if the
    ``published_shift_details`` field is present.

    Note that shifts with ``draft_shift_details.is_deleted`` set to ``true`` are ignored with the ``DRAFT`` filter. See
    `ScheduledShiftFilterScheduledShiftStatus <#type-scheduledshiftfilterscheduledshiftstatus>`__ for possible values"""


class ScheduledShiftFilterDict(TypedDict):
    location_ids: NotRequired[list[str | None]]
    start: NotRequired[TimeRange | TimeRangeDict]
    end: NotRequired[TimeRange | TimeRangeDict]
    workday: NotRequired[ScheduledShiftWorkday | ScheduledShiftWorkdayDict]
    team_member_ids: NotRequired[list[str | None]]
    assignment_status: NotRequired[ScheduledShiftFilterAssignmentStatusOrStr]
    scheduled_shift_statuses: NotRequired[list[ScheduledShiftFilterScheduledShiftStatusOrStr | None]]
