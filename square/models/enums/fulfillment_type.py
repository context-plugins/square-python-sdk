from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FulfillmentType(str, Enum):
    """The type of fulfillment."""

    PICKUP = "PICKUP"
    """A recipient to pick up the fulfillment from a physical `location <entity:Location>`__."""

    SHIPMENT = "SHIPMENT"
    """A shipping carrier to ship the fulfillment."""

    DELIVERY = "DELIVERY"
    """A courier to deliver the fulfillment."""

    IN_STORE = "IN_STORE"
    """A customer to receive the fulfillment within the seller's physical `location <entity:Location>`__."""

    __str__ = str.__str__


FulfillmentTypeOrStr: TypeAlias = Annotated[FulfillmentType | str, open_enum_validator(FulfillmentType)]
