from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment_link import PaymentLink, PaymentLinkDict
from .payment_link_related_resources import PaymentLinkRelatedResources, PaymentLinkRelatedResourcesDict


class CreatePaymentLinkResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    payment_link: Optional[PaymentLink] = UNSET
    related_resources: Optional[PaymentLinkRelatedResources] = UNSET


class CreatePaymentLinkResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    payment_link: NotRequired[PaymentLink | PaymentLinkDict]
    related_resources: NotRequired[PaymentLinkRelatedResources | PaymentLinkRelatedResourcesDict]
