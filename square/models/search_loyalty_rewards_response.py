from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_reward import LoyaltyReward, LoyaltyRewardDict


class SearchLoyaltyRewardsResponse(SdkBaseModel):
    """A response that includes the loyalty rewards satisfying the search criteria."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    rewards: Optional[list[LoyaltyReward]] = UNSET
    """The loyalty rewards that satisfy the search criteria. These are returned in descending order by
    ``updated_at``."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response."""


class SearchLoyaltyRewardsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    rewards: NotRequired[list[LoyaltyReward | LoyaltyRewardDict]]
    cursor: NotRequired[str]
