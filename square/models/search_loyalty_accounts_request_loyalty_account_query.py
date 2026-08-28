from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_account_mapping import LoyaltyAccountMapping, LoyaltyAccountMappingDict


class SearchLoyaltyAccountsRequestLoyaltyAccountQuery(SdkBaseModel):
    """The search criteria for the loyalty accounts."""

    mappings: Optional[list[LoyaltyAccountMapping | None]] = UNSET
    """The set of mappings to use in the loyalty account search.

    This cannot be combined with ``customer_ids``.

    Max: 30 mappings"""

    customer_ids: Optional[list[str | None]] = UNSET
    """The set of customer IDs to use in the loyalty account search.

    This cannot be combined with ``mappings``.

    Max: 30 customer IDs"""


class SearchLoyaltyAccountsRequestLoyaltyAccountQueryDict(TypedDict):
    mappings: NotRequired[list[LoyaltyAccountMapping | LoyaltyAccountMappingDict | None]]
    customer_ids: NotRequired[list[str | None]]
