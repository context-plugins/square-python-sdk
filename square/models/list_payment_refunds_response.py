from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment_refund import PaymentRefund, PaymentRefundDict


class ListPaymentRefundsResponse(SdkBaseModel):
    """Defines the response returned by `ListPaymentRefunds <api-endpoint:Refunds-ListPaymentRefunds>`__.

    Either ``errors`` or ``refunds`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    refunds: Optional[list[PaymentRefund]] = UNSET
    """The list of requested refunds."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If empty, this is the final response.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListPaymentRefundsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    refunds: NotRequired[list[PaymentRefund | PaymentRefundDict]]
    cursor: NotRequired[str]
