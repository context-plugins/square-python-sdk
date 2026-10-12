from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .workweek_config import WorkweekConfig, WorkweekConfigDict


class UpdateWorkweekConfigResponse(SdkBaseModel):
    """The response to a request to update a ``WorkweekConfig`` object. The response contains the updated
    ``WorkweekConfig`` object and might contain a set of ``Error`` objects if the request resulted in errors."""

    workweek_config: Optional[WorkweekConfig] = UNSET
    """Sets the day of the week and hour of the day that a business starts a workweek. This is used to calculate
    overtime pay."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class UpdateWorkweekConfigResponseDict(TypedDict):
    workweek_config: NotRequired[WorkweekConfigDict]
    errors: NotRequired[list[ErrorDict]]
