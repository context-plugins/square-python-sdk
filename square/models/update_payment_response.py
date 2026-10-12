from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment import Payment, PaymentDict


class UpdatePaymentResponse(SdkBaseModel):
    """Defines the response returned by `UpdatePayment <api-endpoint:Payments-UpdatePayment>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    payment: Optional[Payment] = UNSET
    """Represents a payment processed by the Square API."""


class UpdatePaymentResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    payment: NotRequired[PaymentDict]
