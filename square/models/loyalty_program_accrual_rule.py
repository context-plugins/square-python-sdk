from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.loyalty_program_accrual_rule_type import LoyaltyProgramAccrualRuleTypeOrStr
from .loyalty_program_accrual_rule_category_data import (
    LoyaltyProgramAccrualRuleCategoryData,
    LoyaltyProgramAccrualRuleCategoryDataDict,
)
from .loyalty_program_accrual_rule_item_variation_data import (
    LoyaltyProgramAccrualRuleItemVariationData,
    LoyaltyProgramAccrualRuleItemVariationDataDict,
)
from .loyalty_program_accrual_rule_spend_data import (
    LoyaltyProgramAccrualRuleSpendData,
    LoyaltyProgramAccrualRuleSpendDataDict,
)
from .loyalty_program_accrual_rule_visit_data import (
    LoyaltyProgramAccrualRuleVisitData,
    LoyaltyProgramAccrualRuleVisitDataDict,
)


class LoyaltyProgramAccrualRule(SdkBaseModel):
    """Represents an accrual rule, which defines how buyers can earn points from the base `loyalty program
    <entity:LoyaltyProgram>`__."""

    accrual_type: LoyaltyProgramAccrualRuleTypeOrStr
    """The type of the accrual rule that defines how buyers can earn points."""

    points: OptionalNullable[int] = UNSET
    """The number of points that buyers earn based on the ``accrual_type``."""

    visit_data: Optional[LoyaltyProgramAccrualRuleVisitData] = UNSET
    """Represents additional data for rules with the ``VISIT`` accrual type."""

    spend_data: Optional[LoyaltyProgramAccrualRuleSpendData] = UNSET
    """Represents additional data for rules with the ``SPEND`` accrual type."""

    item_variation_data: Optional[LoyaltyProgramAccrualRuleItemVariationData] = UNSET
    """Represents additional data for rules with the ``ITEM_VARIATION`` accrual type."""

    category_data: Optional[LoyaltyProgramAccrualRuleCategoryData] = UNSET
    """Represents additional data for rules with the ``CATEGORY`` accrual type."""


class LoyaltyProgramAccrualRuleDict(TypedDict):
    accrual_type: LoyaltyProgramAccrualRuleTypeOrStr
    points: NotRequired[int | None]
    visit_data: NotRequired[LoyaltyProgramAccrualRuleVisitData | LoyaltyProgramAccrualRuleVisitDataDict]
    spend_data: NotRequired[LoyaltyProgramAccrualRuleSpendData | LoyaltyProgramAccrualRuleSpendDataDict]
    item_variation_data: NotRequired[
        LoyaltyProgramAccrualRuleItemVariationData | LoyaltyProgramAccrualRuleItemVariationDataDict
    ]
    category_data: NotRequired[LoyaltyProgramAccrualRuleCategoryData | LoyaltyProgramAccrualRuleCategoryDataDict]
