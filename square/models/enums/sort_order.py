from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SortOrder(str, Enum):
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""

    DESC = "DESC"
    """The results are returned in descending (e.g., newest-first or Z-A) order."""

    ASC = "ASC"
    """The results are returned in ascending (e.g., oldest-first or A-Z) order."""

    __str__ = str.__str__


SortOrderOrStr: TypeAlias = Annotated[SortOrder | str, open_enum_validator(SortOrder)]
