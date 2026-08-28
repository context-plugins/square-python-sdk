from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment_link import PaymentLink, PaymentLinkDict


class RetrievePaymentLinkResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    payment_link: Optional[PaymentLink] = UNSET


class RetrievePaymentLinkResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    payment_link: NotRequired[PaymentLink | PaymentLinkDict]
