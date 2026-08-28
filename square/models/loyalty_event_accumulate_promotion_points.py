from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class LoyaltyEventAccumulatePromotionPoints(SdkBaseModel):
    """Provides metadata when the event ``type`` is ``ACCUMULATE_PROMOTION_POINTS``."""

    loyalty_program_id: Optional[str] = UNSET
    """The Square-assigned ID of the `loyalty program <entity:LoyaltyProgram>`__."""

    loyalty_promotion_id: Optional[str] = UNSET
    """The Square-assigned ID of the `loyalty promotion <entity:LoyaltyPromotion>`__."""

    points: int
    """The number of points earned by the event."""

    order_id: str
    """The ID of the `order <entity:Order>`__ for which the buyer earned the promotion points. Only applications that
    use the Orders API to process orders can trigger this event."""


class LoyaltyEventAccumulatePromotionPointsDict(TypedDict):
    loyalty_program_id: NotRequired[str]
    loyalty_promotion_id: NotRequired[str]
    points: int
    order_id: str
