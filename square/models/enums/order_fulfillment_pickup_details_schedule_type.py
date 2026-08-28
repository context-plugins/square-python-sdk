from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderFulfillmentPickupDetailsScheduleType(str, Enum):
    """The schedule type of the pickup fulfillment."""

    SCHEDULED = "SCHEDULED"
    """Indicates that the fulfillment will be picked up at a scheduled pickup time."""

    ASAP = "ASAP"
    """Indicates that the fulfillment will be picked up as soon as possible and should be prepared immediately."""

    __str__ = str.__str__


OrderFulfillmentPickupDetailsScheduleTypeOrStr: TypeAlias = Annotated[
    OrderFulfillmentPickupDetailsScheduleType | str, open_enum_validator(OrderFulfillmentPickupDetailsScheduleType)
]
