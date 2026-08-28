from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LoyaltyEventRedeemReward(SdkBaseModel):
    """Provides metadata when the event ``type`` is ``REDEEM_REWARD``."""

    loyalty_program_id: str
    """The ID of the `loyalty program <entity:LoyaltyProgram>`__."""

    reward_id: Optional[str] = UNSET
    """The ID of the redeemed `loyalty reward <entity:LoyaltyReward>`__. This field is returned only if the event source
    is ``LOYALTY_API``."""

    order_id: Optional[str] = UNSET
    """The ID of the `order <entity:Order>`__ that redeemed the reward. This field is returned only if the Orders API is
    used to process orders."""


class LoyaltyEventRedeemRewardDict(TypedDict):
    loyalty_program_id: str
    reward_id: NotRequired[str]
    order_id: NotRequired[str]
