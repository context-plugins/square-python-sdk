from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CashDrawerShiftState(str, Enum):
    """The current state of a cash drawer shift."""

    OPEN = "OPEN"
    """An open cash drawer shift."""

    ENDED = "ENDED"
    """A cash drawer shift that is ended but has not yet had an employee content audit."""

    CLOSED = "CLOSED"
    """An ended cash drawer shift that is closed with a completed employee content audit and recorded result."""

    __str__ = str.__str__


CashDrawerShiftStateOrStr: TypeAlias = Annotated[CashDrawerShiftState | str, open_enum_validator(CashDrawerShiftState)]
