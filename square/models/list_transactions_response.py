from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .transaction import Transaction, TransactionDict


class ListTransactionsResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `ListTransactions
    <api-endpoint:Transactions-ListTransactions>`__ endpoint.

    One of ``errors`` or ``transactions`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    transactions: Optional[list[Transaction]] = UNSET
    """An array of transactions that match your query."""

    cursor: Optional[str] = UNSET
    """A pagination cursor for retrieving the next set of results, if any remain. Provide this value as the ``cursor``
    parameter in a subsequent request to this endpoint.

    See `Paginating results <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more
    information."""


class ListTransactionsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    transactions: NotRequired[list[TransactionDict]]
    cursor: NotRequired[str]
