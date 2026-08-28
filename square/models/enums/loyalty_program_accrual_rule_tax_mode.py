from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyProgramAccrualRuleTaxMode(str, Enum):
    """Indicates how taxes should be treated when calculating the purchase amount used for loyalty points accrual. This
    setting applies only to ``SPEND`` accrual rules or ``VISIT`` accrual rules that have a minimum spend requirement."""

    BEFORE_TAX = "BEFORE_TAX"
    """Exclude taxes from the purchase amount used for loyalty points accrual."""

    AFTER_TAX = "AFTER_TAX"
    """Include taxes in the purchase amount used for loyalty points accrual."""

    __str__ = str.__str__


LoyaltyProgramAccrualRuleTaxModeOrStr: TypeAlias = Annotated[
    LoyaltyProgramAccrualRuleTaxMode | str, open_enum_validator(LoyaltyProgramAccrualRuleTaxMode)
]
