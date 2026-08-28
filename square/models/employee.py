from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.employee_status import EmployeeStatusOrStr


class Employee(SdkBaseModel):
    """An employee object that is used by the external API.

    DEPRECATED at version 2020-08-26. Replaced by `TeamMember <entity:TeamMember>`__."""

    id: Optional[str] = UNSET
    """UUID for this object."""

    first_name: OptionalNullable[str] = UNSET
    """The employee's first name."""

    last_name: OptionalNullable[str] = UNSET
    """The employee's last name."""

    email: OptionalNullable[str] = UNSET
    """The employee's email address"""

    phone_number: OptionalNullable[str] = UNSET
    """The employee's phone number in E.164 format, i.e. "+12125554250"
    """

    location_ids: Optional[list[str | None]] = UNSET
    """A list of location IDs where this employee has access to."""

    status: Optional[EmployeeStatusOrStr] = UNSET
    """The status of the Employee being retrieved.

    DEPRECATED at version 2020-08-26. Replaced by `TeamMemberStatus <entity:TeamMemberStatus>`__."""

    is_owner: OptionalNullable[bool] = UNSET
    """Whether this employee is the owner of the merchant. Each merchant has one owner employee, and that employee has
    full authority over the account."""

    created_at: Optional[str] = UNSET
    """A read-only timestamp in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """A read-only timestamp in RFC 3339 format."""


class EmployeeDict(TypedDict):
    id: NotRequired[str]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    email: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    location_ids: NotRequired[list[str | None]]
    status: NotRequired[EmployeeStatusOrStr]
    is_owner: NotRequired[bool | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
