from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Product(str, Enum):
    """Indicates the Square product used to generate a change."""

    SQUARE_POS = "SQUARE_POS"
    """Square Point of Sale application."""

    EXTERNAL_API = "EXTERNAL_API"
    """Square Connect APIs (for example, Orders API or Checkout API)."""

    BILLING = "BILLING"
    """A Square subscription (various products)."""

    APPOINTMENTS = "APPOINTMENTS"
    """Square Appointments."""

    INVOICES = "INVOICES"
    """Square Invoices."""

    ONLINE_STORE = "ONLINE_STORE"
    """Square Online Store."""

    PAYROLL = "PAYROLL"
    """Square Payroll."""

    DASHBOARD = "DASHBOARD"
    """Square Dashboard."""

    ITEM_LIBRARY_IMPORT = "ITEM_LIBRARY_IMPORT"
    """Item Library Import."""

    OTHER = "OTHER"
    """A Square product that does not match any other value."""

    __str__ = str.__str__


ProductOrStr: TypeAlias = Annotated[Product | str, open_enum_validator(Product)]
