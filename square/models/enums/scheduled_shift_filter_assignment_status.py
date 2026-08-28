from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScheduledShiftFilterAssignmentStatus(str, Enum):
    """Defines valid values for the ``assignment_status`` filter in a `SearchScheduledShifts
    <api-endpoint:Labor-SearchScheduledShifts>`__ request. Assignment status is based on the
    ``draft_shift_details.team_member_id`` and ``published_shift_details.team_member_id`` fields of the scheduled
    shift."""

    ASSIGNED = "ASSIGNED"
    """The shift is assigned to a team member."""

    UNASSIGNED = "UNASSIGNED"
    """The shift isn't assigned to a team member."""

    __str__ = str.__str__


ScheduledShiftFilterAssignmentStatusOrStr: TypeAlias = Annotated[
    ScheduledShiftFilterAssignmentStatus | str, open_enum_validator(ScheduledShiftFilterAssignmentStatus)
]
