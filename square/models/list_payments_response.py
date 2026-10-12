from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment import Payment, PaymentDict


class ListPaymentsResponse(SdkBaseModel):
    """Defines the response returned by `ListPayments <api-endpoint:Payments-ListPayments>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    payments: Optional[list[Payment]] = UNSET
    """The requested list of payments."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListPaymentsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    payments: NotRequired[list[PaymentDict]]
    cursor: NotRequired[str]
