from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyProgramAccrualRuleType(str, Enum):
    """The type of the accrual rule that defines how buyers can earn points."""

    VISIT = "VISIT"
    """A visit-based accrual rule. A buyer earns points for each visit. You can specify the minimum purchase
    required."""

    SPEND = "SPEND"
    """A spend-based accrual rule. A buyer earns points based on the amount spent."""

    ITEM_VARIATION = "ITEM_VARIATION"
    """An accrual rule based on an item variation. For example, accrue points for purchasing a coffee."""

    CATEGORY = "CATEGORY"
    """An accrual rule based on an item category. For example, accrue points for purchasing any item in the "hot drink"
    category: coffee, tea, or hot cocoa."""

    __str__ = str.__str__


LoyaltyProgramAccrualRuleTypeOrStr: TypeAlias = Annotated[
    LoyaltyProgramAccrualRuleType | str, open_enum_validator(LoyaltyProgramAccrualRuleType)
]
