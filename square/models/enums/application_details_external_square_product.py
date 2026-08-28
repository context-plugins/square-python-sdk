from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ApplicationDetailsExternalSquareProduct(str, Enum):
    """A list of products to return to external callers."""

    APPOINTMENTS = "APPOINTMENTS"
    ECOMMERCE_API = "ECOMMERCE_API"
    INVOICES = "INVOICES"
    ONLINE_STORE = "ONLINE_STORE"
    OTHER = "OTHER"
    RESTAURANTS = "RESTAURANTS"
    RETAIL = "RETAIL"
    SQUARE_POS = "SQUARE_POS"
    TERMINAL_API = "TERMINAL_API"
    VIRTUAL_TERMINAL = "VIRTUAL_TERMINAL"

    __str__ = str.__str__


ApplicationDetailsExternalSquareProductOrStr: TypeAlias = Annotated[
    ApplicationDetailsExternalSquareProduct | str, open_enum_validator(ApplicationDetailsExternalSquareProduct)
]
