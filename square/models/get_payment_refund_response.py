from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment_refund import PaymentRefund, PaymentRefundDict


class GetPaymentRefundResponse(SdkBaseModel):
    """Defines the response returned by `GetRefund <api-endpoint:Refunds-GetPaymentRefund>`__.

    Note: If there are errors processing the request, the refund field might not be present or it might be present in a
    FAILED state."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    refund: Optional[PaymentRefund] = UNSET
    """Represents a refund of a payment made using Square. Contains information about the original payment and the
    amount of money refunded."""


class GetPaymentRefundResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    refund: NotRequired[PaymentRefund | PaymentRefundDict]
