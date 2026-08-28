from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomerInclusionExclusion(str, Enum):
    """Indicates whether customers should be included in, or excluded from, the result set when they match the filtering
    criteria."""

    INCLUDE = "INCLUDE"
    """Customers should be included in the result set when they match the filtering criteria."""

    EXCLUDE = "EXCLUDE"
    """Customers should be excluded from the result set when they match the filtering criteria."""

    __str__ = str.__str__


CustomerInclusionExclusionOrStr: TypeAlias = Annotated[
    CustomerInclusionExclusion | str, open_enum_validator(CustomerInclusionExclusion)
]
