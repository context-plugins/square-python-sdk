from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DayOfWeek(str, Enum):
    """Indicates the specific day of the week."""

    SUN = "SUN"
    """Sunday"""

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

    __str__ = str.__str__


DayOfWeekOrStr: TypeAlias = Annotated[DayOfWeek | str, open_enum_validator(DayOfWeek)]
