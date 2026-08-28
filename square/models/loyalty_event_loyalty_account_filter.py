from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyEventLoyaltyAccountFilter(SdkBaseModel):
    """Filter events by loyalty account."""

    loyalty_account_id: str
    """The ID of the `loyalty account <entity:LoyaltyAccount>`__ associated with loyalty events."""


class LoyaltyEventLoyaltyAccountFilterDict(TypedDict):
    loyalty_account_id: str
