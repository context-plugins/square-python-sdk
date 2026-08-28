from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EmployeeStatus(str, Enum):
    """The status of the Employee being retrieved.

    DEPRECATED at version 2020-08-26. Replaced by `TeamMemberStatus <entity:TeamMemberStatus>`__."""

    ACTIVE = "ACTIVE"
    """Specifies that the employee is in the Active state."""

    INACTIVE = "INACTIVE"
    """Specifies that the employee is in the Inactive state."""

    __str__ = str.__str__


EmployeeStatusOrStr: TypeAlias = Annotated[EmployeeStatus | str, open_enum_validator(EmployeeStatus)]
