from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_reward import LoyaltyReward, LoyaltyRewardDict


class CreateLoyaltyRewardResponse(SdkBaseModel):
    """A response that includes the loyalty reward created."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    reward: Optional[LoyaltyReward] = UNSET
    """Represents a contract to redeem loyalty points for a `reward tier <entity:LoyaltyProgramRewardTier>`__ discount.
    Loyalty rewards can be in an ISSUED, REDEEMED, or DELETED state. For more information, see `Manage loyalty rewards
    <https://developer.squareup.com/docs/loyalty-api/loyalty-rewards>`__."""


class CreateLoyaltyRewardResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    reward: NotRequired[LoyaltyReward | LoyaltyRewardDict]
