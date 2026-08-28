from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .shift import Shift, ShiftDict


class UpdateShiftRequest(SdkBaseModel):
    """A request to update a ``Shift`` object."""

    shift: Shift
    """A record of the hourly rate, start, and end times for a single work shift for an employee. This might include a
    record of the start and end times for breaks taken during the shift.

    Deprecated at Square API version 2025-05-21. Replaced by `Timecard <entity:Timecard>`__. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""


class UpdateShiftRequestDict(TypedDict):
    shift: Shift | ShiftDict
