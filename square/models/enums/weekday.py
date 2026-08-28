from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Weekday(str, Enum):
    """The days of the week."""

    MON = "MON"
    """Monday"""

    TUE = "TUE"
    """Tuesday"""

    WED = "WED"
    """Wednesday"""

    THU = "THU"
    """Thursday"""

    FRI = "FRI"
    """Friday"""

    SAT = "SAT"
    """Saturday"""

    SUN = "SUN"
    """Sunday"""

    __str__ = str.__str__


WeekdayOrStr: TypeAlias = Annotated[Weekday | str, open_enum_validator(Weekday)]
