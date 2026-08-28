from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RiskEvaluationRiskLevel(str, Enum):
    PENDING = "PENDING"
    """Indicates Square is still evaluating the payment."""

    NORMAL = "NORMAL"
    """Indicates payment risk is within the normal range."""

    MODERATE = "MODERATE"
    """Indicates elevated risk level associated with the payment."""

    HIGH = "HIGH"
    """Indicates significantly elevated risk level with the payment."""

    __str__ = str.__str__


RiskEvaluationRiskLevelOrStr: TypeAlias = Annotated[
    RiskEvaluationRiskLevel | str, open_enum_validator(RiskEvaluationRiskLevel)
]
