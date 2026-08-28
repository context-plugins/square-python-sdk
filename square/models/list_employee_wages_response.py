from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .employee_wage import EmployeeWage, EmployeeWageDict
from .error import Error, ErrorDict


class ListEmployeeWagesResponse(SdkBaseModel):
    """The response to a request for a set of ``EmployeeWage`` objects. The response contains a set of ``EmployeeWage``
    objects."""

    employee_wages: Optional[list[EmployeeWage]] = UNSET
    """A page of ``EmployeeWage`` results."""

    cursor: Optional[str] = UNSET
    """The value supplied in the subsequent request to fetch the next page of ``EmployeeWage`` results."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class ListEmployeeWagesResponseDict(TypedDict):
    employee_wages: NotRequired[list[EmployeeWage | EmployeeWageDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
