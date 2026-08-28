from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionCadence(str, Enum):
    """Determines the billing cadence of a `Subscription <entity:Subscription>`__"""

    DAILY = "DAILY"
    """Once per day"""

    WEEKLY = "WEEKLY"
    """Once per week"""

    EVERY_TWO_WEEKS = "EVERY_TWO_WEEKS"
    """Every two weeks"""

    THIRTY_DAYS = "THIRTY_DAYS"
    """Once every 30 days"""

    SIXTY_DAYS = "SIXTY_DAYS"
    """Once every 60 days"""

    NINETY_DAYS = "NINETY_DAYS"
    """Once every 90 days"""

    MONTHLY = "MONTHLY"
    """Once per month"""

    EVERY_TWO_MONTHS = "EVERY_TWO_MONTHS"
    """Once every two months"""

    QUARTERLY = "QUARTERLY"
    """Once every three months"""

    EVERY_FOUR_MONTHS = "EVERY_FOUR_MONTHS"
    """Once every four months"""

    EVERY_SIX_MONTHS = "EVERY_SIX_MONTHS"
    """Once every six months"""

    ANNUAL = "ANNUAL"
    """Once per year"""

    EVERY_TWO_YEARS = "EVERY_TWO_YEARS"
    """Once every two years"""

    __str__ = str.__str__


SubscriptionCadenceOrStr: TypeAlias = Annotated[SubscriptionCadence | str, open_enum_validator(SubscriptionCadence)]
