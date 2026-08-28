from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderLineItemTaxScope(str, Enum):
    """Indicates whether this is a line-item or order-level tax."""

    OTHER_TAX_SCOPE = "OTHER_TAX_SCOPE"
    """Used for reporting only. The original transaction tax scope is currently not supported by the API."""

    LINE_ITEM = "LINE_ITEM"
    """The tax should be applied only to line items specified by the ``OrderLineItemAppliedTax`` reference records."""

    ORDER = "ORDER"
    """The tax should be applied to the entire order."""

    __str__ = str.__str__


OrderLineItemTaxScopeOrStr: TypeAlias = Annotated[
    OrderLineItemTaxScope | str, open_enum_validator(OrderLineItemTaxScope)
]
