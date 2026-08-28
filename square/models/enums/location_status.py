from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LocationStatus(str, Enum):
    """A location's status."""

    ACTIVE = "ACTIVE"
    """A location that is active for business."""

    INACTIVE = "INACTIVE"
    """A location that is not active for business. Inactive locations provide historical information. Hide inactive
    locations unless the user has requested to see them."""

    __str__ = str.__str__


LocationStatusOrStr: TypeAlias = Annotated[LocationStatus | str, open_enum_validator(LocationStatus)]
