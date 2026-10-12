from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.loyalty_promotion_incentive_type import LoyaltyPromotionIncentiveTypeOrStr
from .loyalty_promotion_incentive_points_addition_data import (
    LoyaltyPromotionIncentivePointsAdditionData,
    LoyaltyPromotionIncentivePointsAdditionDataDict,
)
from .loyalty_promotion_incentive_points_multiplier_data import (
    LoyaltyPromotionIncentivePointsMultiplierData,
    LoyaltyPromotionIncentivePointsMultiplierDataDict,
)


class LoyaltyPromotionIncentive(SdkBaseModel):
    """Represents how points for a `loyalty promotion <entity:LoyaltyPromotion>`__ are calculated, either by multiplying
    the points earned from the base program or by adding a specified number of points to the points earned from the base
    program."""

    type_: LoyaltyPromotionIncentiveTypeOrStr = Field(alias="type")
    """Indicates the type of points incentive for a `loyalty promotion <entity:LoyaltyPromotion>`__, which is used to
    determine how buyers can earn points from the promotion."""

    points_multiplier_data: Optional[LoyaltyPromotionIncentivePointsMultiplierData] = UNSET
    """Represents the metadata for a ``POINTS_MULTIPLIER`` type of `loyalty promotion incentive
    <entity:LoyaltyPromotionIncentive>`__."""

    points_addition_data: Optional[LoyaltyPromotionIncentivePointsAdditionData] = UNSET
    """Represents the metadata for a ``POINTS_ADDITION`` type of `loyalty promotion incentive
    <entity:LoyaltyPromotionIncentive>`__."""


class LoyaltyPromotionIncentiveDict(TypedDict):
    type_: LoyaltyPromotionIncentiveTypeOrStr
    points_multiplier_data: NotRequired[LoyaltyPromotionIncentivePointsMultiplierDataDict]
    points_addition_data: NotRequired[LoyaltyPromotionIncentivePointsAdditionDataDict]
