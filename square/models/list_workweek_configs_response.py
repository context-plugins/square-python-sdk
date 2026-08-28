from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .workweek_config import WorkweekConfig, WorkweekConfigDict


class ListWorkweekConfigsResponse(SdkBaseModel):
    """The response to a request for a set of ``WorkweekConfig`` objects. The response contains the requested
    ``WorkweekConfig`` objects and might contain a set of ``Error`` objects if the request resulted in errors."""

    workweek_configs: Optional[list[WorkweekConfig]] = UNSET
    """A page of ``WorkweekConfig`` results."""

    cursor: Optional[str] = UNSET
    """The value supplied in the subsequent request to fetch the next page of ``WorkweekConfig`` results."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class ListWorkweekConfigsResponseDict(TypedDict):
    workweek_configs: NotRequired[list[WorkweekConfig | WorkweekConfigDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
