from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class TeamMemberWage(SdkBaseModel):
    """Job and wage information for a `team member <entity:TeamMember>`__. This convenience object provides details
    needed to specify the ``wage`` field for a `timecard <entity:Timecard>`__."""

    id: Optional[str] = UNSET
    """The UUID for this object."""

    team_member_id: OptionalNullable[str] = UNSET
    """The ``TeamMember`` that this wage is assigned to."""

    title: OptionalNullable[str] = UNSET
    """The job title that this wage relates to."""

    hourly_rate: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    job_id: OptionalNullable[str] = UNSET
    """An identifier for the `job <entity:Job>`__ that this wage relates to."""

    tip_eligible: OptionalNullable[bool] = UNSET
    """Whether team members are eligible for tips when working this job."""


class TeamMemberWageDict(TypedDict):
    id: NotRequired[str]
    team_member_id: NotRequired[str | None]
    title: NotRequired[str | None]
    hourly_rate: NotRequired[Money | MoneyDict]
    job_id: NotRequired[str | None]
    tip_eligible: NotRequired[bool | None]
