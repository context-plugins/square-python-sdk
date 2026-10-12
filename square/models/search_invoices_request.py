from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .invoice_query import InvoiceQuery, InvoiceQueryDict


class SearchInvoicesRequest(SdkBaseModel):
    """Describes a ``SearchInvoices`` request."""

    query: InvoiceQuery
    """Describes query criteria for searching invoices."""

    limit: Optional[int] = UNSET
    """The maximum number of invoices to return (200 is the maximum ``limit``). If not provided, the server uses a
    default limit of 100 invoices."""

    cursor: Optional[str] = UNSET
    """A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of
    results for your original query.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class SearchInvoicesRequestDict(TypedDict):
    query: InvoiceQueryDict
    limit: NotRequired[int]
    cursor: NotRequired[str]
