from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .loyalty_promotion import LoyaltyPromotion, LoyaltyPromotionDict


class CreateLoyaltyPromotionRequest(SdkBaseModel):
    """Represents a `CreateLoyaltyPromotion <api-endpoint:Loyalty-CreateLoyaltyPromotion>`__ request."""

    loyalty_promotion: LoyaltyPromotion
    """Represents a promotion for a `loyalty program <entity:LoyaltyProgram>`__. Loyalty promotions enable buyers to
    earn extra points on top of those earned from the base program.

    A loyalty program can have a maximum of 10 loyalty promotions with an ``ACTIVE`` or ``SCHEDULED`` status."""

    idempotency_key: str
    """A unique identifier for this request, which is used to ensure idempotency. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class CreateLoyaltyPromotionRequestDict(TypedDict):
    loyalty_promotion: LoyaltyPromotionDict
    idempotency_key: str
