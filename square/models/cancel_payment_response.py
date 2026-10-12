from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment import Payment, PaymentDict


class CancelPaymentResponse(SdkBaseModel):
    """Defines the response returned by `CancelPayment <api-endpoint:Payments-CancelPayment>`__."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    payment: Optional[Payment] = UNSET
    """Represents a payment processed by the Square API."""


class CancelPaymentResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    payment: NotRequired[PaymentDict]
