from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.job_assignment_pay_type import JobAssignmentPayTypeOrStr
from .money import Money, MoneyDict


class JobAssignment(SdkBaseModel):
    """Represents a job assigned to a `team member <entity:TeamMember>`__, including the compensation the team member
    earns for the job. Job assignments are listed in the team member's `wage setting <entity:WageSetting>`__."""

    job_title: OptionalNullable[str] = UNSET
    """The title of the job."""

    pay_type: JobAssignmentPayTypeOrStr
    """Enumerates the possible pay types that a job can be assigned."""

    hourly_rate: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    annual_rate: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    weekly_hours: OptionalNullable[int] = UNSET
    """The planned hours per week for the job. Set if the job ``PayType`` is ``SALARY``."""

    job_id: OptionalNullable[str] = UNSET
    """The ID of the `job <entity:Job>`__."""


class JobAssignmentDict(TypedDict):
    job_title: NotRequired[str | None]
    pay_type: JobAssignmentPayTypeOrStr
    hourly_rate: NotRequired[MoneyDict]
    annual_rate: NotRequired[MoneyDict]
    weekly_hours: NotRequired[int | None]
    job_id: NotRequired[str | None]
