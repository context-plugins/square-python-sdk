from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .break_type import BreakType, BreakTypeDict
from .error import Error, ErrorDict


class ListBreakTypesResponse(SdkBaseModel):
    """The response to a request for a set of ``BreakType`` objects. The response contains the requested ``BreakType``
    objects and might contain a set of ``Error`` objects if the request resulted in errors."""

    break_types: Optional[list[BreakType]] = UNSET
    """A page of ``BreakType`` results."""

    cursor: Optional[str] = UNSET
    """The value supplied in the subsequent request to fetch the next page of ``BreakType`` results."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class ListBreakTypesResponseDict(TypedDict):
    break_types: NotRequired[list[BreakType | BreakTypeDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
