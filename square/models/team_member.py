from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.team_member_status import TeamMemberStatusOrStr
from .team_member_assigned_locations import TeamMemberAssignedLocations, TeamMemberAssignedLocationsDict
from .wage_setting import WageSetting, WageSettingDict


class TeamMember(SdkBaseModel):
    """A record representing an individual team member for a business."""

    id: Optional[str] = UNSET
    """The unique ID for the team member."""

    reference_id: OptionalNullable[str] = UNSET
    """A second ID used to associate the team member with an entity in another system."""

    is_owner: Optional[bool] = UNSET
    """Whether the team member is the owner of the Square account."""

    status: Optional[TeamMemberStatusOrStr] = UNSET
    """Enumerates the possible statuses the team member can have within a business."""

    given_name: OptionalNullable[str] = UNSET
    """The given name (that is, the first name) associated with the team member."""

    family_name: OptionalNullable[str] = UNSET
    """The family name (that is, the last name) associated with the team member."""

    email_address: OptionalNullable[str] = UNSET
    """The email address associated with the team member. After accepting the invitation from Square, only the team
    member can change this value."""

    phone_number: OptionalNullable[str] = UNSET
    """The team member's phone number, in E.164 format. For example: +14155552671 - the country code is 1 for US
    +551155256325 - the country code is 55 for BR"""

    created_at: Optional[str] = UNSET
    """The timestamp when the team member was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the team member was last updated, in RFC 3339 format."""

    assigned_locations: Optional[TeamMemberAssignedLocations] = UNSET
    """An object that represents a team member's assignment to locations."""

    wage_setting: Optional[WageSetting] = UNSET
    """Represents information about the overtime exemption status, job assignments, and compensation for a `team member
    <entity:TeamMember>`__."""


class TeamMemberDict(TypedDict):
    id: NotRequired[str]
    reference_id: NotRequired[str | None]
    is_owner: NotRequired[bool]
    status: NotRequired[TeamMemberStatusOrStr]
    given_name: NotRequired[str | None]
    family_name: NotRequired[str | None]
    email_address: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    assigned_locations: NotRequired[TeamMemberAssignedLocations | TeamMemberAssignedLocationsDict]
    wage_setting: NotRequired[WageSetting | WageSettingDict]
