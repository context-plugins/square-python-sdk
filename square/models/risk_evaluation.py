from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.risk_evaluation_risk_level import RiskEvaluationRiskLevelOrStr


class RiskEvaluation(SdkBaseModel):
    """Represents fraud risk information for the associated payment.

    When you take a payment through Square's Payments API (using the ``CreatePayment`` endpoint), Square evaluates it
    and assigns a risk level to the payment. Sellers can use this information to determine the course of action (for
    example, provide the goods/services or refund the payment)."""

    created_at: Optional[str] = UNSET
    """The timestamp when payment risk was evaluated, in RFC 3339 format."""

    risk_level: Optional[RiskEvaluationRiskLevelOrStr] = UNSET


class RiskEvaluationDict(TypedDict):
    created_at: NotRequired[str]
    risk_level: NotRequired[RiskEvaluationRiskLevelOrStr]
