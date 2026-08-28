from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment import Payment, PaymentDict


class CompletePaymentResponse(SdkBaseModel):
    """Defines the response returned by`CompletePayment <api-endpoint:Payments-CompletePayment>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    payment: Optional[Payment] = UNSET
    """Represents a payment processed by the Square API."""


class CompletePaymentResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    payment: NotRequired[Payment | PaymentDict]
