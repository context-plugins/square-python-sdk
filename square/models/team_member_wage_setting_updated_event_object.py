from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .wage_setting import WageSetting, WageSettingDict


class TeamMemberWageSettingUpdatedEventObject(SdkBaseModel):
    wage_setting: Optional[WageSetting] = UNSET
    """Represents information about the overtime exemption status, job assignments, and compensation for a `team member
    <entity:TeamMember>`__."""


class TeamMemberWageSettingUpdatedEventObjectDict(TypedDict):
    wage_setting: NotRequired[WageSetting | WageSettingDict]
