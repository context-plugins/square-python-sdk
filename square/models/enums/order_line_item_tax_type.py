from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderLineItemTaxType(str, Enum):
    """Indicates how the tax is applied to the associated line item or order."""

    UNKNOWN_TAX = "UNKNOWN_TAX"
    """Used for reporting only. The original transaction tax type is currently not supported by the API."""

    ADDITIVE = "ADDITIVE"
    """The tax is an additive tax. The tax amount is added on top of the price. For example, an item with a cost of 1.00
    USD and a 10% additive tax has a total cost to the buyer of 1.10 USD."""

    INCLUSIVE = "INCLUSIVE"
    """The tax is an inclusive tax. Inclusive taxes are already included in the line item price or order total. For
    example, an item with a cost of 1.00 USD and a 10% inclusive tax has a pretax cost of 0.91 USD (91 cents) and a 0.09
    (9 cents) tax for a total cost of 1.00 USD to the buyer."""

    __str__ = str.__str__


OrderLineItemTaxTypeOrStr: TypeAlias = Annotated[OrderLineItemTaxType | str, open_enum_validator(OrderLineItemTaxType)]
