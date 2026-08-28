from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class CancelPaymentByIdempotencyKeyResponse(SdkBaseModel):
    """Defines the response returned by `CancelPaymentByIdempotencyKey
    <api-endpoint:Payments-CancelPaymentByIdempotencyKey>`__. On success, ``errors`` is empty."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class CancelPaymentByIdempotencyKeyResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
