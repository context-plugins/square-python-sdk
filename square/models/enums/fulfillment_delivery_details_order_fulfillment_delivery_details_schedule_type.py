from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentDeliveryDetailsOrderFulfillmentDeliveryDetailsScheduleType(str, Enum):
    """The schedule type of the delivery fulfillment."""

    SCHEDULED = "SCHEDULED"
    """Indicates the fulfillment to deliver at a scheduled deliver time."""

    ASAP = "ASAP"
    """Indicates that the fulfillment to deliver as soon as possible and should be prepared immediately."""

    __str__ = str.__str__


FulfillmentDeliveryDetailsOrderFulfillmentDeliveryDetailsScheduleTypeOrStr: TypeAlias = Annotated[
    FulfillmentDeliveryDetailsOrderFulfillmentDeliveryDetailsScheduleType | str,
    open_enum_validator(FulfillmentDeliveryDetailsOrderFulfillmentDeliveryDetailsScheduleType),
]
