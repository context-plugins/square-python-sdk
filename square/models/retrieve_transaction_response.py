from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .transaction import Transaction, TransactionDict


class RetrieveTransactionResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `RetrieveTransaction
    <api-endpoint:Transactions-RetrieveTransaction>`__ endpoint.

    One of ``errors`` or ``transaction`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    transaction: Optional[Transaction] = UNSET
    """Represents a transaction processed with Square, either with the Connect API or with Square Point of Sale.

    The ``tenders`` field of this object lists all methods of payment used to pay in the transaction."""


class RetrieveTransactionResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    transaction: NotRequired[Transaction | TransactionDict]
