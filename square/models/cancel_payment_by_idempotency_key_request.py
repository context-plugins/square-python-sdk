from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CancelPaymentByIdempotencyKeyRequest(SdkBaseModel):
    """Describes a request to cancel a payment using `CancelPaymentByIdempotencyKey
    <api-endpoint:Payments-CancelPaymentByIdempotencyKey>`__."""

    idempotency_key: str
    """The ``idempotency_key`` identifying the payment to be canceled."""


class CancelPaymentByIdempotencyKeyRequestDict(TypedDict):
    idempotency_key: str
