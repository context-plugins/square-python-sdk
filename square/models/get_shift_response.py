from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .shift import Shift, ShiftDict


class GetShiftResponse(SdkBaseModel):
    """A response to a request to get a ``Shift``. The response contains the requested ``Shift`` object and might
    contain a set of ``Error`` objects if the request resulted in errors."""

    shift: Optional[Shift] = UNSET
    """A record of the hourly rate, start, and end times for a single work shift for an employee. This might include a
    record of the start and end times for breaks taken during the shift.

    Deprecated at Square API version 2025-05-21. Replaced by `Timecard <entity:Timecard>`__. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class GetShiftResponseDict(TypedDict):
    shift: NotRequired[Shift | ShiftDict]
    errors: NotRequired[list[Error | ErrorDict]]
