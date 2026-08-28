from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyPromotionTriggerLimitInterval(str, Enum):
    """Indicates the time period that the `trigger limit <entity:LoyaltyPromotionTriggerLimit>`__ applies to, which is
    used to determine the number of times a buyer can earn points for a `loyalty promotion
    <entity:LoyaltyPromotion>`__."""

    ALL_TIME = "ALL_TIME"
    """The limit applies to the entire time that the promotion is active. For example, if ``times`` is set to 1 and
    ``time_period`` is set to ``ALL_TIME``, a buyer can earn promotion points a maximum of one time during the
    promotion."""

    DAY = "DAY"
    """The limit applies per day, according to the ``available_time`` schedule specified for the promotion. For example,
    if the ``times`` field of the trigger limit is set to 1, a buyer can trigger the promotion a maximum of once per
    day."""

    __str__ = str.__str__


LoyaltyPromotionTriggerLimitIntervalOrStr: TypeAlias = Annotated[
    LoyaltyPromotionTriggerLimitInterval | str, open_enum_validator(LoyaltyPromotionTriggerLimitInterval)
]
