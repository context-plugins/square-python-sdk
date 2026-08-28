from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionPricingType(str, Enum):
    """Determines the pricing of a `Subscription <entity:Subscription>`__"""

    STATIC = "STATIC"
    """Static pricing"""

    RELATIVE = "RELATIVE"
    """Relative pricing"""

    __str__ = str.__str__


SubscriptionPricingTypeOrStr: TypeAlias = Annotated[
    SubscriptionPricingType | str, open_enum_validator(SubscriptionPricingType)
]
