from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .break_type import BreakType, BreakTypeDict
from .error import Error, ErrorDict


class UpdateBreakTypeResponse(SdkBaseModel):
    """A response to a request to update a ``BreakType``. The response contains the requested ``BreakType`` objects and
    might contain a set of ``Error`` objects if the request resulted in errors."""

    break_type: Optional[BreakType] = UNSET
    """A template for a type of `break <entity:Break>`__ that can be added to a `timecard <entity:Timecard>`__,
    including the expected duration and paid status."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class UpdateBreakTypeResponseDict(TypedDict):
    break_type: NotRequired[BreakTypeDict]
    errors: NotRequired[list[ErrorDict]]
