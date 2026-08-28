from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceCustomFieldPlacement(str, Enum):
    """Indicates where to render a custom field on the Square-hosted invoice page and in emailed or PDF copies of the
    invoice."""

    ABOVE_LINE_ITEMS = "ABOVE_LINE_ITEMS"
    """Render the custom field above the invoice line items."""

    BELOW_LINE_ITEMS = "BELOW_LINE_ITEMS"
    """Render the custom field below the invoice line items."""

    __str__ = str.__str__


InvoiceCustomFieldPlacementOrStr: TypeAlias = Annotated[
    InvoiceCustomFieldPlacement | str, open_enum_validator(InvoiceCustomFieldPlacement)
]
