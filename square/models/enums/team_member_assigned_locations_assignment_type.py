from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TeamMemberAssignedLocationsAssignmentType(str, Enum):
    """Enumerates the possible assignment types that the team member can have."""

    ALL_CURRENT_AND_FUTURE_LOCATIONS = "ALL_CURRENT_AND_FUTURE_LOCATIONS"
    """The team member is assigned to all current and future locations. The ``location_ids`` field is empty if the team
    member has this assignment type."""

    EXPLICIT_LOCATIONS = "EXPLICIT_LOCATIONS"
    """The team member is assigned to an explicit subset of locations. The ``location_ids`` field is the list of
    locations that the team member is assigned to."""

    __str__ = str.__str__


TeamMemberAssignedLocationsAssignmentTypeOrStr: TypeAlias = Annotated[
    TeamMemberAssignedLocationsAssignmentType | str, open_enum_validator(TeamMemberAssignedLocationsAssignmentType)
]
