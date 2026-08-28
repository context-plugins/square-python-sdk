from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payment import Payment, PaymentDict


class PaymentUpdatedEventObject(SdkBaseModel):
    payment: Optional[Payment] = UNSET
    """Represents a payment processed by the Square API."""


class PaymentUpdatedEventObjectDict(TypedDict):
    payment: NotRequired[Payment | PaymentDict]
