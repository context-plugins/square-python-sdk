from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .loyalty_account_mapping import LoyaltyAccountMapping, LoyaltyAccountMappingDict


class SearchLoyaltyAccountsRequestLoyaltyAccountQuery(SdkBaseModel):
    """The search criteria for the loyalty accounts."""

    mappings: OptionalNullable[list[LoyaltyAccountMapping]] = UNSET
    """The set of mappings to use in the loyalty account search.

    This cannot be combined with ``customer_ids``.

    Max: 30 mappings"""

    customer_ids: OptionalNullable[list[str]] = UNSET
    """The set of customer IDs to use in the loyalty account search.

    This cannot be combined with ``mappings``.

    Max: 30 customer IDs"""


class SearchLoyaltyAccountsRequestLoyaltyAccountQueryDict(TypedDict):
    mappings: NotRequired[list[LoyaltyAccountMappingDict] | None]
    customer_ids: NotRequired[list[str] | None]
