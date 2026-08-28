from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionProduct(str, Enum):
    """Indicates the Square product used to process a transaction."""

    REGISTER = "REGISTER"
    """Square Point of Sale."""

    EXTERNAL_API = "EXTERNAL_API"
    """The Square Connect API."""

    BILLING = "BILLING"
    """A Square subscription for one of multiple products."""

    APPOINTMENTS = "APPOINTMENTS"
    """Square Appointments."""

    INVOICES = "INVOICES"
    """Square Invoices."""

    ONLINE_STORE = "ONLINE_STORE"
    """Square Online Store."""

    PAYROLL = "PAYROLL"
    """Square Payroll."""

    OTHER = "OTHER"
    """A Square product that does not match any other value."""

    __str__ = str.__str__


TransactionProductOrStr: TypeAlias = Annotated[TransactionProduct | str, open_enum_validator(TransactionProduct)]
