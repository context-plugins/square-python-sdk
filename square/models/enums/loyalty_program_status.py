from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyProgramStatus(str, Enum):
    """Indicates whether the program is currently active."""

    INACTIVE = "INACTIVE"
    """The loyalty program does not have an active subscription. Loyalty API requests fail."""

    ACTIVE = "ACTIVE"
    """The program is fully functional. The program has an active subscription."""

    __str__ = str.__str__


LoyaltyProgramStatusOrStr: TypeAlias = Annotated[LoyaltyProgramStatus | str, open_enum_validator(LoyaltyProgramStatus)]
