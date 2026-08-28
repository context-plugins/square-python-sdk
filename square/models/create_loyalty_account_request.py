from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loyalty_account import LoyaltyAccount, LoyaltyAccountDict


class CreateLoyaltyAccountRequest(SdkBaseModel):
    """A request to create a new loyalty account."""

    loyalty_account: LoyaltyAccount
    """Describes a loyalty account in a `loyalty program <entity:LoyaltyProgram>`__. For more information, see `Create
    and Retrieve Loyalty Accounts <https://developer.squareup.com/docs/loyalty-api/loyalty-accounts>`__."""

    idempotency_key: str
    """A unique string that identifies this ``CreateLoyaltyAccount`` request. Keys can be any valid string, but must be
    unique for every request."""


class CreateLoyaltyAccountRequestDict(TypedDict):
    loyalty_account: LoyaltyAccount | LoyaltyAccountDict
    idempotency_key: str
