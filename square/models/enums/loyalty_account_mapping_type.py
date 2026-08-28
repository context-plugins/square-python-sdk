from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyAccountMappingType(str, Enum):
    """The type of mapping."""

    PHONE = "PHONE"
    """The loyalty account is mapped by phone."""

    __str__ = str.__str__


LoyaltyAccountMappingTypeOrStr: TypeAlias = Annotated[
    LoyaltyAccountMappingType | str, open_enum_validator(LoyaltyAccountMappingType)
]
