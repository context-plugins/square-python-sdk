from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class TimecardWage(SdkBaseModel):
    """The hourly wage rate used to compensate a team member for a `timecard <entity:Timecard>`__."""

    title: OptionalNullable[str] = UNSET
    """The name of the job performed during this timecard."""

    hourly_rate: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    job_id: Optional[str] = UNSET
    """The ID of the `job <entity:Job>`__ performed for this timecard. Square labor-reporting UIs might group timecards
    together by ID."""

    tip_eligible: OptionalNullable[bool] = UNSET
    """Whether team members are eligible for tips when working this job."""


class TimecardWageDict(TypedDict):
    title: NotRequired[str | None]
    hourly_rate: NotRequired[MoneyDict]
    job_id: NotRequired[str]
    tip_eligible: NotRequired[bool | None]
