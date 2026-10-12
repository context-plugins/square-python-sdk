from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_account import LoyaltyAccount, LoyaltyAccountDict


class SearchLoyaltyAccountsResponse(SdkBaseModel):
    """A response that includes loyalty accounts that satisfy the search criteria."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    loyalty_accounts: Optional[list[LoyaltyAccount]] = UNSET
    """The loyalty accounts that met the search criteria, in order of creation date."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to use in a subsequent request. If empty, this is the final response. For more information,
    see `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class SearchLoyaltyAccountsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    loyalty_accounts: NotRequired[list[LoyaltyAccountDict]]
    cursor: NotRequired[str]
