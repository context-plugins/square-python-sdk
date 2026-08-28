from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.loyalty_program_status import LoyaltyProgramStatusOrStr
from .loyalty_program_accrual_rule import LoyaltyProgramAccrualRule, LoyaltyProgramAccrualRuleDict
from .loyalty_program_expiration_policy import LoyaltyProgramExpirationPolicy, LoyaltyProgramExpirationPolicyDict
from .loyalty_program_reward_tier import LoyaltyProgramRewardTier, LoyaltyProgramRewardTierDict
from .loyalty_program_terminology import LoyaltyProgramTerminology, LoyaltyProgramTerminologyDict


class LoyaltyProgram(SdkBaseModel):
    """Represents a Square loyalty program. Loyalty programs define how buyers can earn points and redeem points for
    rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard.
    For more information, see `Loyalty Program Overview <https://developer.squareup.com/docs/loyalty/overview>`__."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the loyalty program. Updates to the loyalty program do not modify the identifier."""

    status: Optional[LoyaltyProgramStatusOrStr] = UNSET
    """Indicates whether the program is currently active."""

    reward_tiers: Optional[list[LoyaltyProgramRewardTier | None]] = UNSET
    """The list of rewards for buyers, sorted by ascending points."""

    expiration_policy: Optional[LoyaltyProgramExpirationPolicy] = UNSET
    """Describes when the loyalty program expires."""

    terminology: Optional[LoyaltyProgramTerminology] = UNSET
    """Represents the naming used for loyalty points."""

    location_ids: Optional[list[str | None]] = UNSET
    """The `locations <entity:Location>`__ at which the program is active."""

    created_at: Optional[str] = UNSET
    """The timestamp when the program was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the reward was last updated, in RFC 3339 format."""

    accrual_rules: Optional[list[LoyaltyProgramAccrualRule | None]] = UNSET
    """Defines how buyers can earn loyalty points from the base loyalty program. To check for associated `loyalty
    promotions <entity:LoyaltyPromotion>`__ that enable buyers to earn extra points, call `ListLoyaltyPromotions
    <api-endpoint:Loyalty-ListLoyaltyPromotions>`__."""


class LoyaltyProgramDict(TypedDict):
    id: NotRequired[str]
    status: NotRequired[LoyaltyProgramStatusOrStr]
    reward_tiers: NotRequired[list[LoyaltyProgramRewardTier | LoyaltyProgramRewardTierDict | None]]
    expiration_policy: NotRequired[LoyaltyProgramExpirationPolicy | LoyaltyProgramExpirationPolicyDict]
    terminology: NotRequired[LoyaltyProgramTerminology | LoyaltyProgramTerminologyDict]
    location_ids: NotRequired[list[str | None]]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    accrual_rules: NotRequired[list[LoyaltyProgramAccrualRule | LoyaltyProgramAccrualRuleDict | None]]
