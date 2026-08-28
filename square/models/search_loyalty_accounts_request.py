from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .search_loyalty_accounts_request_loyalty_account_query import (
    SearchLoyaltyAccountsRequestLoyaltyAccountQuery,
    SearchLoyaltyAccountsRequestLoyaltyAccountQueryDict,
)


class SearchLoyaltyAccountsRequest(SdkBaseModel):
    """A request to search for loyalty accounts."""

    query: Optional[SearchLoyaltyAccountsRequestLoyaltyAccountQuery] = UNSET
    """The search criteria for the loyalty accounts."""

    limit: Optional[int] = UNSET
    """The maximum number of results to include in the response. The default value is 30."""

    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of
    results for the original query.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class SearchLoyaltyAccountsRequestDict(TypedDict):
    query: NotRequired[
        SearchLoyaltyAccountsRequestLoyaltyAccountQuery | SearchLoyaltyAccountsRequestLoyaltyAccountQueryDict
    ]
    limit: NotRequired[int]
    cursor: NotRequired[str]
