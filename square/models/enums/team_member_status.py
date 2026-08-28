from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TeamMemberStatus(str, Enum):
    """Enumerates the possible statuses the team member can have within a business."""

    ACTIVE = "ACTIVE"
    """The team member can sign in to Point of Sale and the Seller Dashboard."""

    INACTIVE = "INACTIVE"
    """The team member can no longer sign in to Point of Sale or the Seller Dashboard, but the team member's sales
    reports remain available."""

    __str__ = str.__str__


TeamMemberStatusOrStr: TypeAlias = Annotated[TeamMemberStatus | str, open_enum_validator(TeamMemberStatus)]
