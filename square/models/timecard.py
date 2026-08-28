from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .break_model import BreakModel, BreakModelDict
from .enums.timecard_status import TimecardStatusOrStr
from .money import Money, MoneyDict
from .timecard_wage import TimecardWage, TimecardWageDict


class Timecard(SdkBaseModel):
    """A record of the hourly rate, start time, and end time of a single timecard (shift) for a team member. This might
    include a record of the start and end times of breaks taken during the shift."""

    id: Optional[str] = UNSET
    """**Read only** The Square-issued UUID for this object."""

    location_id: str
    """The ID of the `location <entity:Location>`__ for this timecard. The location should be based on where the team
    member clocked in."""

    timezone: OptionalNullable[str] = UNSET
    """**Read only** The time zone calculated from the location based on the ``location_id``, provided as a convenience
    value. Format: the IANA time zone database identifier for the location time zone."""

    start_at: str
    """The start time of the timecard, in RFC 3339 format and shifted to the location timezone + offset. Precision up to
    the minute is respected; seconds are truncated."""

    end_at: OptionalNullable[str] = UNSET
    """The end time of the timecard, in RFC 3339 format and shifted to the location timezone + offset. Precision up to
    the minute is respected; seconds are truncated."""

    wage: Optional[TimecardWage] = UNSET
    """The hourly wage rate used to compensate a team member for a `timecard <entity:Timecard>`__."""

    breaks: Optional[list[BreakModel | None]] = UNSET
    """A list of all the paid or unpaid breaks that were taken during this timecard."""

    status: Optional[TimecardStatusOrStr] = UNSET
    """**Read only** Enumerates the possible status of a `timecard <entity:Timecard>`__."""

    version: Optional[int] = UNSET
    """**Read only** The current version of the timecard, which is incremented with each update. This field is used for
    `optimistic concurrency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__ control to ensure
    that requests don't overwrite data from another request."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the timecard was created, in RFC 3339 format presented as UTC."""

    updated_at: Optional[str] = UNSET
    """The timestamp of when the timecard was last updated, in RFC 3339 format presented as UTC."""

    team_member_id: str
    """The ID of the `team member <entity:TeamMember>`__ this timecard belongs to."""

    declared_cash_tip_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class TimecardDict(TypedDict):
    id: NotRequired[str]
    location_id: str
    timezone: NotRequired[str | None]
    start_at: str
    end_at: NotRequired[str | None]
    wage: NotRequired[TimecardWage | TimecardWageDict]
    breaks: NotRequired[list[BreakModel | BreakModelDict | None]]
    status: NotRequired[TimecardStatusOrStr]
    version: NotRequired[int]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    team_member_id: str
    declared_cash_tip_money: NotRequired[Money | MoneyDict]
