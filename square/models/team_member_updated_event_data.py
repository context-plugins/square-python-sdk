from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .team_member_updated_event_object import TeamMemberUpdatedEventObject, TeamMemberUpdatedEventObjectDict


class TeamMemberUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"team_member"``."""

    id: Optional[str] = UNSET
    """ID of the affected team member."""

    object_: Optional[TeamMemberUpdatedEventObject] = Field(default=UNSET, alias="object")


class TeamMemberUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TeamMemberUpdatedEventObject | TeamMemberUpdatedEventObjectDict]
