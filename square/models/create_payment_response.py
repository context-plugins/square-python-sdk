from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment import Payment, PaymentDict


class CreatePaymentResponse(SdkBaseModel):
    """Defines the response returned by `CreatePayment <api-endpoint:Payments-CreatePayment>`__.

    If there are errors processing the request, the ``payment`` field might not be present, or it might be present with
    a status of ``FAILED``."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the request."""

    payment: Optional[Payment] = UNSET
    """Represents a payment processed by the Square API."""


class CreatePaymentResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    payment: NotRequired[Payment | PaymentDict]
