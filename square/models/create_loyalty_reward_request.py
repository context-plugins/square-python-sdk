from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loyalty_reward import LoyaltyReward, LoyaltyRewardDict


class CreateLoyaltyRewardRequest(SdkBaseModel):
    """A request to create a loyalty reward."""

    reward: LoyaltyReward
    """Represents a contract to redeem loyalty points for a `reward tier <entity:LoyaltyProgramRewardTier>`__ discount.
    Loyalty rewards can be in an ISSUED, REDEEMED, or DELETED state. For more information, see `Manage loyalty rewards
    <https://developer.squareup.com/docs/loyalty-api/loyalty-rewards>`__."""

    idempotency_key: str
    """A unique string that identifies this ``CreateLoyaltyReward`` request. Keys can be any valid string, but must be
    unique for every request."""


class CreateLoyaltyRewardRequestDict(TypedDict):
    reward: LoyaltyReward | LoyaltyRewardDict
    idempotency_key: str
