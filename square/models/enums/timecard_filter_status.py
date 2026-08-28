from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TimecardFilterStatus(str, Enum):
    """Specifies the ``status`` of ``Timecard`` records to be returned."""

    OPEN = "OPEN"
    """Timecards that have been started and not ended."""

    CLOSED = "CLOSED"
    """Timecards that have been started and ended."""

    __str__ = str.__str__


TimecardFilterStatusOrStr: TypeAlias = Annotated[TimecardFilterStatus | str, open_enum_validator(TimecardFilterStatus)]
