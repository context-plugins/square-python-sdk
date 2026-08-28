from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScheduledShiftSortField(str, Enum):
    """Defines valid values for the ``field`` sort setting in a `SearchScheduledShifts
    <api-endpoint:Labor-SearchScheduledShifts>`__ request."""

    START_AT = "START_AT"
    """Sort by the start time of the shift."""

    END_AT = "END_AT"
    """Sort by the end time of the shift."""

    CREATED_AT = "CREATED_AT"
    """Sort by the creation date of the shift."""

    UPDATED_AT = "UPDATED_AT"
    """Sort by the last updated date of the shift."""

    __str__ = str.__str__


ScheduledShiftSortFieldOrStr: TypeAlias = Annotated[
    ScheduledShiftSortField | str, open_enum_validator(ScheduledShiftSortField)
]
