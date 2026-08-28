from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LocationType(str, Enum):
    """A location's type."""

    PHYSICAL = "PHYSICAL"
    """A place of business with a physical location."""

    MOBILE = "MOBILE"
    """A place of business that is mobile, such as a food truck or online store."""

    __str__ = str.__str__


LocationTypeOrStr: TypeAlias = Annotated[LocationType | str, open_enum_validator(LocationType)]
