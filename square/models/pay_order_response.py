from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .order import Order, OrderDict


class PayOrderResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `PayOrder
    <api-endpoint:Orders-PayOrder>`__ endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    order: Optional[Order] = UNSET
    """Contains all information related to a single order to process with Square, including line items that specify the
    products to purchase. ``Order`` objects also include information about any associated tenders, refunds, and returns.

    All Connect V2 Transactions have all been converted to Orders including all associated itemization data."""


class PayOrderResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    order: NotRequired[OrderDict]
