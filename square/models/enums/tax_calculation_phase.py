from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TaxCalculationPhase(str, Enum):
    """When to calculate the taxes due on a cart."""

    TAX_SUBTOTAL_PHASE = "TAX_SUBTOTAL_PHASE"
    """The fee is calculated based on the payment's subtotal."""

    TAX_TOTAL_PHASE = "TAX_TOTAL_PHASE"
    """The fee is calculated based on the payment's total."""

    __str__ = str.__str__


TaxCalculationPhaseOrStr: TypeAlias = Annotated[TaxCalculationPhase | str, open_enum_validator(TaxCalculationPhase)]
