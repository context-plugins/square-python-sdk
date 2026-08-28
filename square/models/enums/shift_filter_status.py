from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShiftFilterStatus(str, Enum):
    """Specifies the ``status`` of ``Shift`` records to be returned.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    OPEN = "OPEN"
    """Shifts that have been started and not ended."""

    CLOSED = "CLOSED"
    """Shifts that have been started and ended."""

    __str__ = str.__str__


ShiftFilterStatusOrStr: TypeAlias = Annotated[ShiftFilterStatus | str, open_enum_validator(ShiftFilterStatus)]
