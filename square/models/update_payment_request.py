from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment import Payment, PaymentDict


class UpdatePaymentRequest(SdkBaseModel):
    """Describes a request to update a payment using `UpdatePayment <api-endpoint:Payments-UpdatePayment>`__."""

    payment: Optional[Payment] = UNSET
    """Represents a payment processed by the Square API."""

    idempotency_key: str
    """A unique string that identifies this ``UpdatePayment`` request. Keys can be any valid string but must be unique
    for every ``UpdatePayment`` request.

    For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class UpdatePaymentRequestDict(TypedDict):
    payment: NotRequired[PaymentDict]
    idempotency_key: str
