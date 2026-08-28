from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .invoice import Invoice, InvoiceDict


class SearchInvoicesResponse(SdkBaseModel):
    """Describes a ``SearchInvoices`` response."""

    invoices: Optional[list[Invoice]] = UNSET
    """The list of invoices returned by the search."""

    cursor: Optional[str] = UNSET
    """When a response is truncated, it includes a cursor that you can use in a subsequent request to fetch the next set
    of invoices. If empty, this is the final response. For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""


class SearchInvoicesResponseDict(TypedDict):
    invoices: NotRequired[list[Invoice | InvoiceDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
