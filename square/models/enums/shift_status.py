from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShiftStatus(str, Enum):
    """Enumerates the possible status of a ``Shift``.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    OPEN = "OPEN"
    """Employee started a work shift and the shift is not complete"""

    CLOSED = "CLOSED"
    """Employee started and ended a work shift."""

    __str__ = str.__str__


ShiftStatusOrStr: TypeAlias = Annotated[ShiftStatus | str, open_enum_validator(ShiftStatus)]
