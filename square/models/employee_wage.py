from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .money import Money, MoneyDict


class EmployeeWage(SdkBaseModel):
    """The hourly wage rate that an employee earns on a ``Shift`` for doing the job specified by the ``title`` property
    of this object. Deprecated at version 2020-08-26. Use `TeamMemberWage <entity:TeamMemberWage>`__."""

    id: Optional[str] = UNSET
    """The UUID for this object."""

    employee_id: OptionalNullable[str] = UNSET
    """The ``Employee`` that this wage is assigned to."""

    title: OptionalNullable[str] = UNSET
    """The job title that this wage relates to."""

    hourly_rate: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""


class EmployeeWageDict(TypedDict):
    id: NotRequired[str]
    employee_id: NotRequired[str | None]
    title: NotRequired[str | None]
    hourly_rate: NotRequired[MoneyDict]
