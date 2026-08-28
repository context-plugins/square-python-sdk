from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderState(str, Enum):
    """The state of the order."""

    OPEN = "OPEN"
    """Indicates that the order is open. Open orders can be updated."""

    COMPLETED = "COMPLETED"
    """Indicates that the order is completed. Completed orders are fully paid. This is a terminal state."""

    CANCELED = "CANCELED"
    """Indicates that the order is canceled. Canceled orders are not paid. This is a terminal state."""

    DRAFT = "DRAFT"
    """Indicates that the order is in a draft state. Draft orders can be updated, but cannot be paid or fulfilled. For
    more information, see `Create Orders <https://developer.squareup.com/docs/orders-api/create-orders>`__."""

    __str__ = str.__str__


OrderStateOrStr: TypeAlias = Annotated[OrderState | str, open_enum_validator(OrderState)]
