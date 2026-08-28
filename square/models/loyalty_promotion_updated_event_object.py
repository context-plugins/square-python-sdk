from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_promotion import LoyaltyPromotion, LoyaltyPromotionDict


class LoyaltyPromotionUpdatedEventObject(SdkBaseModel):
    """An object that contains the loyalty promotion associated with a ``loyalty.promotion.updated`` event."""

    loyalty_promotion: Optional[LoyaltyPromotion] = UNSET
    """Represents a promotion for a `loyalty program <entity:LoyaltyProgram>`__. Loyalty promotions enable buyers to
    earn extra points on top of those earned from the base program.

    A loyalty program can have a maximum of 10 loyalty promotions with an ``ACTIVE`` or ``SCHEDULED`` status."""


class LoyaltyPromotionUpdatedEventObjectDict(TypedDict):
    loyalty_promotion: NotRequired[LoyaltyPromotion | LoyaltyPromotionDict]
