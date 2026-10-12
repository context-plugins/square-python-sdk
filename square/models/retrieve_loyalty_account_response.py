from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_account import LoyaltyAccount, LoyaltyAccountDict


class RetrieveLoyaltyAccountResponse(SdkBaseModel):
    """A response that includes the loyalty account."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    loyalty_account: Optional[LoyaltyAccount] = UNSET
    """Describes a loyalty account in a `loyalty program <entity:LoyaltyProgram>`__. For more information, see `Create
    and Retrieve Loyalty Accounts <https://developer.squareup.com/docs/loyalty-api/loyalty-accounts>`__."""


class RetrieveLoyaltyAccountResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    loyalty_account: NotRequired[LoyaltyAccountDict]
