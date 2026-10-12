from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .loyalty_promotion import LoyaltyPromotion, LoyaltyPromotionDict


class CreateLoyaltyPromotionResponse(SdkBaseModel):
    """Represents a `CreateLoyaltyPromotion <api-endpoint:Loyalty-CreateLoyaltyPromotion>`__ response. Either
    ``loyalty_promotion`` or ``errors`` is present in the response."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    loyalty_promotion: Optional[LoyaltyPromotion] = UNSET
    """Represents a promotion for a `loyalty program <entity:LoyaltyProgram>`__. Loyalty promotions enable buyers to
    earn extra points on top of those earned from the base program.

    A loyalty program can have a maximum of 10 loyalty promotions with an ``ACTIVE`` or ``SCHEDULED`` status."""


class CreateLoyaltyPromotionResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    loyalty_promotion: NotRequired[LoyaltyPromotionDict]
