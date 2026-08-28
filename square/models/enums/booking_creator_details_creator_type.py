from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BookingCreatorDetailsCreatorType(str, Enum):
    """Supported types of a booking creator."""

    TEAM_MEMBER = "TEAM_MEMBER"
    """The creator is of the seller type."""

    CUSTOMER = "CUSTOMER"
    """The creator is of the buyer type."""

    __str__ = str.__str__


BookingCreatorDetailsCreatorTypeOrStr: TypeAlias = Annotated[
    BookingCreatorDetailsCreatorType | str, open_enum_validator(BookingCreatorDetailsCreatorType)
]
