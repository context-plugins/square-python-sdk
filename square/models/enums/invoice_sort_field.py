from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InvoiceSortField(str, Enum):
    """The field to use for sorting."""

    INVOICE_SORT_DATE = "INVOICE_SORT_DATE"
    """The field works as follows:

    - If the invoice is a draft, it uses the invoice ``created_at`` date.
    - If the invoice is scheduled for publication, it uses the ``scheduled_at`` date.
    - If the invoice is published, it uses the invoice publication date."""

    __str__ = str.__str__


InvoiceSortFieldOrStr: TypeAlias = Annotated[InvoiceSortField | str, open_enum_validator(InvoiceSortField)]
