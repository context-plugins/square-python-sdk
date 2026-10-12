from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .payment_link import PaymentLink, PaymentLinkDict


class UpdatePaymentLinkRequest(SdkBaseModel):
    payment_link: PaymentLink


class UpdatePaymentLinkRequestDict(TypedDict):
    payment_link: PaymentLinkDict
