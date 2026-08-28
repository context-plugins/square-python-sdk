from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyPromotionIncentivePointsAdditionData(SdkBaseModel):
    """Represents the metadata for a ``POINTS_ADDITION`` type of `loyalty promotion incentive
    <entity:LoyaltyPromotionIncentive>`__."""

    points_addition: int
    """The number of additional points to earn each time the promotion is triggered. For example, suppose a purchase
    qualifies for 5 points from the base loyalty program. If the purchase also qualifies for a ``POINTS_ADDITION``
    promotion incentive with a ``points_addition`` of 3, the buyer earns a total of 8 points (5 program points + 3
    promotion points = 8 points)."""


class LoyaltyPromotionIncentivePointsAdditionDataDict(TypedDict):
    points_addition: int
