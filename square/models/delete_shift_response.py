from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeleteShiftResponse(SdkBaseModel):
    """The response to a request to delete a ``Shift``. The response might contain a set of ``Error`` objects if the
    request resulted in errors."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class DeleteShiftResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
