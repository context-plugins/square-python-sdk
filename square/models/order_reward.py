from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OrderReward(SdkBaseModel):
    """Represents a reward that can be applied to an order if the necessary reward tier criteria are met. Rewards are
    created through the Loyalty API."""

    id: str
    """The identifier of the reward."""

    reward_tier_id: str
    """The identifier of the reward tier corresponding to this reward."""


class OrderRewardDict(TypedDict):
    id: str
    reward_tier_id: str
