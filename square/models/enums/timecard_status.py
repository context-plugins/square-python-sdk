from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TimecardStatus(str, Enum):
    """**Read only** Enumerates the possible status of a `timecard <entity:Timecard>`__."""

    OPEN = "OPEN"
    """The timecard has a ``start_at`` time but no ``end_at`` time, indicating an ongoing shift."""

    CLOSED = "CLOSED"
    """The timecard has both ``start_at`` and ``end_at`` times, indicating a completed shift."""

    __str__ = str.__str__


TimecardStatusOrStr: TypeAlias = Annotated[TimecardStatus | str, open_enum_validator(TimecardStatus)]
