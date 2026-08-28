from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class JobAssignmentPayType(str, Enum):
    """Enumerates the possible pay types that a job can be assigned."""

    NONE = "NONE"
    """The job does not have a defined pay type."""

    HOURLY = "HOURLY"
    """The job pays an hourly rate."""

    SALARY = "SALARY"
    """The job pays an annual salary."""

    __str__ = str.__str__


JobAssignmentPayTypeOrStr: TypeAlias = Annotated[JobAssignmentPayType | str, open_enum_validator(JobAssignmentPayType)]
