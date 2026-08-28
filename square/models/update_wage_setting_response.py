from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .wage_setting import WageSetting, WageSettingDict


class UpdateWageSettingResponse(SdkBaseModel):
    """Represents a response from an update request containing the updated ``WageSetting`` object or error messages."""

    wage_setting: Optional[WageSetting] = UNSET
    """Represents information about the overtime exemption status, job assignments, and compensation for a `team member
    <entity:TeamMember>`__."""

    errors: Optional[list[Error]] = UNSET
    """The errors that occurred during the request."""


class UpdateWageSettingResponseDict(TypedDict):
    wage_setting: NotRequired[WageSetting | WageSettingDict]
    errors: NotRequired[list[Error | ErrorDict]]
