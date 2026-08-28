from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderServiceChargeScope(str, Enum):
    """Indicates whether this is a line-item or order-level apportioned service charge."""

    OTHER_SERVICE_CHARGE_SCOPE = "OTHER_SERVICE_CHARGE_SCOPE"
    """Used for reporting only. The original transaction service charge scope is currently not supported by the API."""

    LINE_ITEM = "LINE_ITEM"
    """The service charge should be applied to only line items specified by ``OrderLineItemAppliedServiceCharge``
    reference records."""

    ORDER = "ORDER"
    """The service charge should be applied to the entire order."""

    __str__ = str.__str__


OrderServiceChargeScopeOrStr: TypeAlias = Annotated[
    OrderServiceChargeScope | str, open_enum_validator(OrderServiceChargeScope)
]
