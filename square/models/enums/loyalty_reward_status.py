from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyRewardStatus(str, Enum):
    """The status of the loyalty reward."""

    ISSUED = "ISSUED"
    """The reward is issued."""

    REDEEMED = "REDEEMED"
    """The reward is redeemed."""

    DELETED = "DELETED"
    """The reward is deleted."""

    __str__ = str.__str__


LoyaltyRewardStatusOrStr: TypeAlias = Annotated[LoyaltyRewardStatus | str, open_enum_validator(LoyaltyRewardStatus)]
