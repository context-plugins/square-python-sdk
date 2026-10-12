from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .team_member_wage_setting_updated_event_object import (
    TeamMemberWageSettingUpdatedEventObject,
    TeamMemberWageSettingUpdatedEventObjectDict,
)


class TeamMemberWageSettingUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"wage_setting"``."""

    id: Optional[str] = UNSET
    """ID of the updated team member wage setting."""

    object_: Optional[TeamMemberWageSettingUpdatedEventObject] = Field(default=UNSET, alias="object")


class TeamMemberWageSettingUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TeamMemberWageSettingUpdatedEventObjectDict]
