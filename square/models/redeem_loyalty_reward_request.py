from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RedeemLoyaltyRewardRequest(SdkBaseModel):
    """A request to redeem a loyalty reward."""

    idempotency_key: str
    """A unique string that identifies this ``RedeemLoyaltyReward`` request. Keys can be any valid string, but must be
    unique for every request."""

    location_id: str
    """The ID of the `location <entity:Location>`__ where the reward is redeemed."""


class RedeemLoyaltyRewardRequestDict(TypedDict):
    idempotency_key: str
    location_id: str
