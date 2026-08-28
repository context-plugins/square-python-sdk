from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .workweek_config import WorkweekConfig, WorkweekConfigDict


class UpdateWorkweekConfigRequest(SdkBaseModel):
    """A request to update a ``WorkweekConfig`` object."""

    workweek_config: WorkweekConfig
    """Sets the day of the week and hour of the day that a business starts a workweek. This is used to calculate
    overtime pay."""


class UpdateWorkweekConfigRequestDict(TypedDict):
    workweek_config: WorkweekConfig | WorkweekConfigDict
