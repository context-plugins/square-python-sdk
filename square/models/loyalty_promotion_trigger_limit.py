from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.loyalty_promotion_trigger_limit_interval import LoyaltyPromotionTriggerLimitIntervalOrStr


class LoyaltyPromotionTriggerLimit(SdkBaseModel):
    """Represents the number of times a buyer can earn points during a `loyalty promotion <entity:LoyaltyPromotion>`__.
    If this field is not set, buyers can trigger the promotion an unlimited number of times to earn points during the
    time that the promotion is available.

    A purchase that is disqualified from earning points because of this limit might qualify for another active
    promotion."""

    times: int
    """The maximum number of times a buyer can trigger the promotion during the specified ``interval``."""

    interval: Optional[LoyaltyPromotionTriggerLimitIntervalOrStr] = UNSET
    """Indicates the time period that the `trigger limit <entity:LoyaltyPromotionTriggerLimit>`__ applies to, which is
    used to determine the number of times a buyer can earn points for a `loyalty promotion
    <entity:LoyaltyPromotion>`__."""


class LoyaltyPromotionTriggerLimitDict(TypedDict):
    times: int
    interval: NotRequired[LoyaltyPromotionTriggerLimitIntervalOrStr]
