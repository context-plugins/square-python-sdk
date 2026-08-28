from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderFulfillmentType(str, Enum):
    """The type of fulfillment."""

    PICKUP = "PICKUP"
    """A recipient to pick up the fulfillment from a physical `location <entity:Location>`__."""

    SHIPMENT = "SHIPMENT"
    """A shipping carrier to ship the fulfillment."""

    DELIVERY = "DELIVERY"
    """A courier to deliver the fulfillment."""

    __str__ = str.__str__


OrderFulfillmentTypeOrStr: TypeAlias = Annotated[OrderFulfillmentType | str, open_enum_validator(OrderFulfillmentType)]
