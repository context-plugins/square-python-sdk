from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .order import Order, OrderDict


class BatchRetrieveOrdersResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the ``BatchRetrieveOrders``
    endpoint."""

    orders: Optional[list[Order]] = UNSET
    """The requested orders. This will omit any requested orders that do not exist."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class BatchRetrieveOrdersResponseDict(TypedDict):
    orders: NotRequired[list[OrderDict]]
    errors: NotRequired[list[ErrorDict]]
