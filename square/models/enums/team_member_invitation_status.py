from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TeamMemberInvitationStatus(str, Enum):
    """Enumerates the possible invitation statuses the team member can have within a business."""

    UNINVITED = "UNINVITED"
    """The team member has not received an invitation."""

    PENDING = "PENDING"
    """The team member has received an invitation, but had not accepted it."""

    ACCEPTED = "ACCEPTED"
    """The team member has both received and accepted an invitation."""

    __str__ = str.__str__


TeamMemberInvitationStatusOrStr: TypeAlias = Annotated[
    TeamMemberInvitationStatus | str, open_enum_validator(TeamMemberInvitationStatus)
]
