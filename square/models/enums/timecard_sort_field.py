from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TimecardSortField(str, Enum):
    """Enumerates the ``Timecard`` fields to sort on."""

    START_AT = "START_AT"
    """The start date/time of a ``Timecard``"""

    END_AT = "END_AT"
    """The end date/time of a ``Timecard``"""

    CREATED_AT = "CREATED_AT"
    """The date/time that a ``Timecard`` is created"""

    UPDATED_AT = "UPDATED_AT"
    """The most recent date/time that a ``Timecard`` is updated"""

    __str__ = str.__str__


TimecardSortFieldOrStr: TypeAlias = Annotated[TimecardSortField | str, open_enum_validator(TimecardSortField)]
