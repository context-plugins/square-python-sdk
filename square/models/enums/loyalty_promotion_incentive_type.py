from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyPromotionIncentiveType(str, Enum):
    """Indicates the type of points incentive for a `loyalty promotion <entity:LoyaltyPromotion>`__, which is used to
    determine how buyers can earn points from the promotion."""

    POINTS_MULTIPLIER = "POINTS_MULTIPLIER"
    """Multiply the number of points earned from the base loyalty program. For example, "Earn double points."
    """

    POINTS_ADDITION = "POINTS_ADDITION"
    """Add a specified number of points to those earned from the base loyalty program. For example, "Earn 10 additional
    points."
    """

    __str__ = str.__str__


LoyaltyPromotionIncentiveTypeOrStr: TypeAlias = Annotated[
    LoyaltyPromotionIncentiveType | str, open_enum_validator(LoyaltyPromotionIncentiveType)
]
