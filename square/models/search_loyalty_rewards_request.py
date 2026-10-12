from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_loyalty_rewards_request_loyalty_reward_query import (
    SearchLoyaltyRewardsRequestLoyaltyRewardQuery,
    SearchLoyaltyRewardsRequestLoyaltyRewardQueryDict,
)


class SearchLoyaltyRewardsRequest(SdkBaseModel):
    """A request to search for loyalty rewards."""

    query: Optional[SearchLoyaltyRewardsRequestLoyaltyRewardQuery] = UNSET
    """The set of search requirements."""

    limit: Optional[int] = UNSET
    """The maximum number of results to return in the response. The default value is 30."""

    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of
    results for the original query. For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class SearchLoyaltyRewardsRequestDict(TypedDict):
    query: NotRequired[SearchLoyaltyRewardsRequestLoyaltyRewardQueryDict]
    limit: NotRequired[int]
    cursor: NotRequired[str]
