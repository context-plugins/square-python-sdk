from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .employee_wage import EmployeeWage, EmployeeWageDict
from .error import Error, ErrorDict


class GetEmployeeWageResponse(SdkBaseModel):
    """A response to a request to get an ``EmployeeWage``. The response contains the requested ``EmployeeWage`` objects
    and might contain a set of ``Error`` objects if the request resulted in errors."""

    employee_wage: Optional[EmployeeWage] = UNSET
    """The hourly wage rate that an employee earns on a ``Shift`` for doing the job specified by the ``title`` property
    of this object. Deprecated at version 2020-08-26. Use `TeamMemberWage <entity:TeamMemberWage>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class GetEmployeeWageResponseDict(TypedDict):
    employee_wage: NotRequired[EmployeeWage | EmployeeWageDict]
    errors: NotRequired[list[Error | ErrorDict]]
