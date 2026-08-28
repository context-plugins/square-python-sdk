from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.loyalty_reward_status import LoyaltyRewardStatusOrStr


class SearchLoyaltyRewardsRequestLoyaltyRewardQuery(SdkBaseModel):
    """The set of search requirements."""

    loyalty_account_id: str
    """The ID of the `loyalty account <entity:LoyaltyAccount>`__ to which the loyalty reward belongs."""

    status: Optional[LoyaltyRewardStatusOrStr] = UNSET
    """The status of the loyalty reward."""


class SearchLoyaltyRewardsRequestLoyaltyRewardQueryDict(TypedDict):
    loyalty_account_id: str
    status: NotRequired[LoyaltyRewardStatusOrStr]
