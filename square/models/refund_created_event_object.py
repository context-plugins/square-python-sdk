from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment_refund import PaymentRefund, PaymentRefundDict


class RefundCreatedEventObject(SdkBaseModel):
    refund: Optional[PaymentRefund] = UNSET
    """Represents a refund of a payment made using Square. Contains information about the original payment and the
    amount of money refunded."""


class RefundCreatedEventObjectDict(TypedDict):
    refund: NotRequired[PaymentRefundDict]
