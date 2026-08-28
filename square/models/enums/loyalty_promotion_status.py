from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LoyaltyPromotionStatus(str, Enum):
    """Indicates the status of a `loyalty promotion <entity:LoyaltyPromotion>`__."""

    ACTIVE = "ACTIVE"
    """The loyalty promotion is currently active. Buyers can earn points for purchases that meet the promotion
    conditions, such as the promotion's ``available_time``."""

    ENDED = "ENDED"
    """The loyalty promotion has ended because the specified ``end_date`` was reached. ``ENDED`` is a terminal
    status."""

    CANCELED = "CANCELED"
    """The loyalty promotion was canceled. ``CANCELED`` is a terminal status."""

    SCHEDULED = "SCHEDULED"
    """The loyalty promotion is scheduled to start in the future. Square changes the promotion status to ``ACTIVE`` when
    the ``start_date`` is reached."""

    __str__ = str.__str__


LoyaltyPromotionStatusOrStr: TypeAlias = Annotated[
    LoyaltyPromotionStatus | str, open_enum_validator(LoyaltyPromotionStatus)
]
