from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_account import LoyaltyAccount, LoyaltyAccountDict


class LoyaltyAccountUpdatedEventObject(SdkBaseModel):
    loyalty_account: Optional[LoyaltyAccount] = UNSET
    """Describes a loyalty account in a `loyalty program <entity:LoyaltyProgram>`__. For more information, see `Create
    and Retrieve Loyalty Accounts <https://developer.squareup.com/docs/loyalty-api/loyalty-accounts>`__."""


class LoyaltyAccountUpdatedEventObjectDict(TypedDict):
    loyalty_account: NotRequired[LoyaltyAccount | LoyaltyAccountDict]
