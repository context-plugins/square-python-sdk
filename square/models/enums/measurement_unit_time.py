from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MeasurementUnitTime(str, Enum):
    """Unit of time used to measure a quantity (a duration)."""

    GENERIC_MILLISECOND = "GENERIC_MILLISECOND"
    """The time is measured in milliseconds."""

    GENERIC_SECOND = "GENERIC_SECOND"
    """The time is measured in seconds."""

    GENERIC_MINUTE = "GENERIC_MINUTE"
    """The time is measured in minutes."""

    GENERIC_HOUR = "GENERIC_HOUR"
    """The time is measured in hours."""

    GENERIC_DAY = "GENERIC_DAY"
    """The time is measured in days."""

    __str__ = str.__str__


MeasurementUnitTimeOrStr: TypeAlias = Annotated[MeasurementUnitTime | str, open_enum_validator(MeasurementUnitTime)]
