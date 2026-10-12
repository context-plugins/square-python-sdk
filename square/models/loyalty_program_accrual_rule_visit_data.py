from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.loyalty_program_accrual_rule_tax_mode import LoyaltyProgramAccrualRuleTaxModeOrStr
from .money import Money, MoneyDict


class LoyaltyProgramAccrualRuleVisitData(SdkBaseModel):
    """Represents additional data for rules with the ``VISIT`` accrual type."""

    minimum_amount_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    tax_mode: LoyaltyProgramAccrualRuleTaxModeOrStr
    """Indicates how taxes should be treated when calculating the purchase amount used for loyalty points accrual. This
    setting applies only to ``SPEND`` accrual rules or ``VISIT`` accrual rules that have a minimum spend requirement."""


class LoyaltyProgramAccrualRuleVisitDataDict(TypedDict):
    minimum_amount_money: NotRequired[MoneyDict]
    tax_mode: LoyaltyProgramAccrualRuleTaxModeOrStr
