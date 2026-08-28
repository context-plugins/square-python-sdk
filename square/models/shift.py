from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .break_model import BreakModel, BreakModelDict
from .enums.shift_status import ShiftStatusOrStr
from .money import Money, MoneyDict
from .shift_wage import ShiftWage, ShiftWageDict


class Shift(SdkBaseModel):
    """A record of the hourly rate, start, and end times for a single work shift for an employee. This might include a
    record of the start and end times for breaks taken during the shift.

    Deprecated at Square API version 2025-05-21. Replaced by `Timecard <entity:Timecard>`__. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    id: Optional[str] = UNSET
    """The UUID for this object."""

    employee_id: OptionalNullable[str] = UNSET
    """The ID of the employee this shift belongs to. DEPRECATED at version 2020-08-26. Use ``team_member_id``
    instead."""

    location_id: str
    """The ID of the location this shift occurred at. The location should be based on where the employee clocked in."""

    timezone: OptionalNullable[str] = UNSET
    """The read-only convenience value that is calculated from the location based on the ``location_id``. Format: the
    IANA timezone database identifier for the location timezone."""

    start_at: str
    """RFC 3339; shifted to the location timezone + offset. Precision up to the minute is respected; seconds are
    truncated."""

    end_at: OptionalNullable[str] = UNSET
    """RFC 3339; shifted to the timezone + offset. Precision up to the minute is respected; seconds are truncated."""

    wage: Optional[ShiftWage] = UNSET
    """The hourly wage rate used to compensate an employee for this shift.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    breaks: Optional[list[BreakModel | None]] = UNSET
    """A list of all the paid or unpaid breaks that were taken during this shift."""

    status: Optional[ShiftStatusOrStr] = UNSET
    """Enumerates the possible status of a ``Shift``.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    version: Optional[int] = UNSET
    """Used for resolving concurrency issues. The request fails if the version provided does not match the server
    version at the time of the request. If not provided, Square executes a blind write; potentially overwriting data
    from another write."""

    created_at: Optional[str] = UNSET
    """A read-only timestamp in RFC 3339 format; presented in UTC."""

    updated_at: Optional[str] = UNSET
    """A read-only timestamp in RFC 3339 format; presented in UTC."""

    team_member_id: OptionalNullable[str] = UNSET
    """The ID of the team member this shift belongs to. Replaced ``employee_id`` at version "2020-08-26"."""

    declared_cash_tip_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class ShiftDict(TypedDict):
    id: NotRequired[str]
    employee_id: NotRequired[str | None]
    location_id: str
    timezone: NotRequired[str | None]
    start_at: str
    end_at: NotRequired[str | None]
    wage: NotRequired[ShiftWage | ShiftWageDict]
    breaks: NotRequired[list[BreakModel | BreakModelDict | None]]
    status: NotRequired[ShiftStatusOrStr]
    version: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    team_member_id: NotRequired[str | None]
    declared_cash_tip_money: NotRequired[Money | MoneyDict]
