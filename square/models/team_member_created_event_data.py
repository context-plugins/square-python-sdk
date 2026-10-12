from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .team_member_created_event_object import TeamMemberCreatedEventObject, TeamMemberCreatedEventObjectDict


class TeamMemberCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"team_member"``."""

    id: Optional[str] = UNSET
    """ID of the created team member."""

    object_: Optional[TeamMemberCreatedEventObject] = Field(default=UNSET, alias="object")


class TeamMemberCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TeamMemberCreatedEventObjectDict]
