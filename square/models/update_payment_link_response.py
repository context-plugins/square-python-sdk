from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment_link import PaymentLink, PaymentLinkDict


class UpdatePaymentLinkResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred when updating the payment link."""

    payment_link: Optional[PaymentLink] = UNSET


class UpdatePaymentLinkResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    payment_link: NotRequired[PaymentLink | PaymentLinkDict]
