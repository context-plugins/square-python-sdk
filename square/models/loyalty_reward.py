from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.loyalty_reward_status import LoyaltyRewardStatusOrStr


class LoyaltyReward(SdkBaseModel):
    """Represents a contract to redeem loyalty points for a `reward tier <entity:LoyaltyProgramRewardTier>`__ discount.
    Loyalty rewards can be in an ISSUED, REDEEMED, or DELETED state. For more information, see `Manage loyalty rewards
    <https://developer.squareup.com/docs/loyalty-api/loyalty-rewards>`__."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the loyalty reward."""

    status: Optional[LoyaltyRewardStatusOrStr] = UNSET
    """The status of the loyalty reward."""

    loyalty_account_id: str
    """The Square-assigned ID of the `loyalty account <entity:LoyaltyAccount>`__ to which the reward belongs."""

    reward_tier_id: str
    """The Square-assigned ID of the `reward tier <entity:LoyaltyProgramRewardTier>`__ used to create the reward."""

    points: Optional[int] = UNSET
    """The number of loyalty points used for the reward."""

    order_id: OptionalNullable[str] = UNSET
    """The Square-assigned ID of the `order <entity:Order>`__ to which the reward is attached."""

    created_at: Optional[str] = UNSET
    """The timestamp when the reward was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the reward was last updated, in RFC 3339 format."""

    redeemed_at: Optional[str] = UNSET
    """The timestamp when the reward was redeemed, in RFC 3339 format."""


class LoyaltyRewardDict(TypedDict):
    id: NotRequired[str]
    status: NotRequired[LoyaltyRewardStatusOrStr]
    loyalty_account_id: str
    reward_tier_id: str
    points: NotRequired[int]
    order_id: NotRequired[str | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    redeemed_at: NotRequired[str]
