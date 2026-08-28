from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderFulfillmentState(str, Enum):
    """The current state of this fulfillment."""

    PROPOSED = "PROPOSED"
    """Indicates that the fulfillment has been proposed."""

    RESERVED = "RESERVED"
    """Indicates that the fulfillment has been reserved."""

    PREPARED = "PREPARED"
    """Indicates that the fulfillment has been prepared."""

    COMPLETED = "COMPLETED"
    """Indicates that the fulfillment was successfully completed."""

    CANCELED = "CANCELED"
    """Indicates that the fulfillment was canceled."""

    FAILED = "FAILED"
    """Indicates that the fulfillment failed to be completed, but was not explicitly canceled."""

    __str__ = str.__str__


OrderFulfillmentStateOrStr: TypeAlias = Annotated[
    OrderFulfillmentState | str, open_enum_validator(OrderFulfillmentState)
]
