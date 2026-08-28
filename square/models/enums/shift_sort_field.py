from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShiftSortField(str, Enum):
    """Enumerates the ``Shift`` fields to sort on.

    Deprecated at Square API version 2025-05-21. See the `migration notes
    <https://developer.squareup.com/docs/labor-api/what-it-does#migration-notes>`__."""

    START_AT = "START_AT"
    """The start date/time of a ``Shift``"""

    END_AT = "END_AT"
    """The end date/time of a ``Shift``"""

    CREATED_AT = "CREATED_AT"
    """The date/time that a ``Shift`` is created"""

    UPDATED_AT = "UPDATED_AT"
    """The most recent date/time that a ``Shift`` is updated"""

    __str__ = str.__str__


ShiftSortFieldOrStr: TypeAlias = Annotated[ShiftSortField | str, open_enum_validator(ShiftSortField)]
