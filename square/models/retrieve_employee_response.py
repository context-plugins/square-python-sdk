from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .employee import Employee, EmployeeDict
from .error import Error, ErrorDict


class RetrieveEmployeeResponse(SdkBaseModel):
    employee: Optional[Employee] = UNSET
    """An employee object that is used by the external API.

    DEPRECATED at version 2020-08-26. Replaced by `TeamMember <entity:TeamMember>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class RetrieveEmployeeResponseDict(TypedDict):
    employee: NotRequired[EmployeeDict]
    errors: NotRequired[list[ErrorDict]]
