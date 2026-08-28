from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderServiceChargeCalculationPhase(str, Enum):
    """Represents a phase in the process of calculating order totals. Service charges are applied after the indicated
    phase.

    `Read more about how order totals are calculated.
    <https://developer.squareup.com/docs/orders-api/how-it-works#how-totals-are-calculated>`__"""

    SUBTOTAL_PHASE = "SUBTOTAL_PHASE"
    """The service charge is applied after discounts, but before taxes."""

    TOTAL_PHASE = "TOTAL_PHASE"
    """The service charge is applied after all discounts and taxes are applied."""

    APPORTIONED_PERCENTAGE_PHASE = "APPORTIONED_PERCENTAGE_PHASE"
    """The service charge is calculated as a compounding adjustment after any discounts, but before amount based
    apportioned service charges and any tax considerations."""

    APPORTIONED_AMOUNT_PHASE = "APPORTIONED_AMOUNT_PHASE"
    """The service charge is calculated as a compounding adjustment after any discounts and percentage based apportioned
    service charges, but before any tax considerations."""

    __str__ = str.__str__


OrderServiceChargeCalculationPhaseOrStr: TypeAlias = Annotated[
    OrderServiceChargeCalculationPhase | str, open_enum_validator(OrderServiceChargeCalculationPhase)
]
