from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyEventType(str, Enum):
    """The type of the loyalty event."""

    ACCUMULATE_POINTS = "ACCUMULATE_POINTS"
    """Points are added to a loyalty account for a purchase that qualified for points based on an `accrual rule
    <entity:LoyaltyProgramAccrualRule>`__."""

    CREATE_REWARD = "CREATE_REWARD"
    """A `loyalty reward <entity:LoyaltyReward>`__ is created."""

    REDEEM_REWARD = "REDEEM_REWARD"
    """A loyalty reward is redeemed."""

    DELETE_REWARD = "DELETE_REWARD"
    """A loyalty reward is deleted."""

    ADJUST_POINTS = "ADJUST_POINTS"
    """Loyalty points are manually adjusted."""

    EXPIRE_POINTS = "EXPIRE_POINTS"
    """Loyalty points are expired according to the expiration policy of the loyalty program."""

    OTHER = "OTHER"
    """Some other loyalty event occurred."""

    ACCUMULATE_PROMOTION_POINTS = "ACCUMULATE_PROMOTION_POINTS"
    """Points are added to a loyalty account for a purchase that qualified for a `loyalty promotion
    <entity:LoyaltyPromotion>`__."""

    __str__ = str.__str__


LoyaltyEventTypeOrStr: TypeAlias = Annotated[LoyaltyEventType | str, open_enum_validator(LoyaltyEventType)]
