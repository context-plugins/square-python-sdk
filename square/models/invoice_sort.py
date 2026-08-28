from __future__ import annotations

from typing import Literal

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.sort_order import SortOrderOrStr


class InvoiceSort(SdkBaseModel):
    """Identifies the sort field and sort order."""

    field: Literal["INVOICE_SORT_DATE"] = "INVOICE_SORT_DATE"
    """The field to use for sorting."""

    order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""


class InvoiceSortDict(TypedDict):
    field: NotRequired[Literal["INVOICE_SORT_DATE"]]
    order: NotRequired[SortOrderOrStr]
