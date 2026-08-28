from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .wage_setting import WageSetting, WageSettingDict


class UpdateWageSettingRequest(SdkBaseModel):
    """Represents an update request for the ``WageSetting`` object describing a ``TeamMember``."""

    wage_setting: WageSetting
    """Represents information about the overtime exemption status, job assignments, and compensation for a `team member
    <entity:TeamMember>`__."""


class UpdateWageSettingRequestDict(TypedDict):
    wage_setting: WageSetting | WageSettingDict
