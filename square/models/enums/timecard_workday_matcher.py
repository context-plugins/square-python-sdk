from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TimecardWorkdayMatcher(str, Enum):
    """Defines the logic used to apply a workday filter."""

    START_AT = "START_AT"
    """All timecards that start on or after the specified workday"""

    END_AT = "END_AT"
    """All timecards that end on or before the specified workday"""

    INTERSECTION = "INTERSECTION"
    """All timecards that start between the start and end workdays (inclusive)"""

    __str__ = str.__str__


TimecardWorkdayMatcherOrStr: TypeAlias = Annotated[
    TimecardWorkdayMatcher | str, open_enum_validator(TimecardWorkdayMatcher)
]
