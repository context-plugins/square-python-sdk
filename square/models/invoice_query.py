from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .invoice_filter import InvoiceFilter, InvoiceFilterDict
from .invoice_sort import InvoiceSort, InvoiceSortDict


class InvoiceQuery(SdkBaseModel):
    """Describes query criteria for searching invoices."""

    filter: InvoiceFilter
    """Describes query filters to apply."""

    sort: Optional[InvoiceSort] = UNSET
    """Identifies the sort field and sort order."""


class InvoiceQueryDict(TypedDict):
    filter: InvoiceFilter | InvoiceFilterDict
    sort: NotRequired[InvoiceSort | InvoiceSortDict]
