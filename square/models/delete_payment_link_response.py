from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class DeletePaymentLinkResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    id: Optional[str] = UNSET
    """The ID of the link that is deleted."""

    cancelled_order_id: Optional[str] = UNSET
    """The ID of the order that is canceled. When a payment link is deleted, Square updates the the ``state`` (of the
    order that the checkout link created) to CANCELED."""


class DeletePaymentLinkResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    id: NotRequired[str]
    cancelled_order_id: NotRequired[str]
