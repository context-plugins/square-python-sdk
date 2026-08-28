from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .employee import Employee, EmployeeDict
from .error import Error, ErrorDict


class ListEmployeesResponse(SdkBaseModel):
    employees: Optional[list[Employee]] = UNSET
    cursor: Optional[str] = UNSET
    """The token to be used to retrieve the next page of results."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class ListEmployeesResponseDict(TypedDict):
    employees: NotRequired[list[Employee | EmployeeDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
