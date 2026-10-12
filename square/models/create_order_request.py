from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .order import Order, OrderDict


class CreateOrderRequest(SdkBaseModel):
    order: Optional[Order] = UNSET
    """Contains all information related to a single order to process with Square, including line items that specify the
    products to purchase. ``Order`` objects also include information about any associated tenders, refunds, and returns.

    All Connect V2 Transactions have all been converted to Orders including all associated itemization data."""

    idempotency_key: Optional[str] = UNSET
    """A value you specify that uniquely identifies this order among orders you have created.

    If you are unsure whether a particular order was created successfully, you can try it again with the same
    idempotency key without worrying about creating duplicate orders.

    For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class CreateOrderRequestDict(TypedDict):
    order: NotRequired[OrderDict]
    idempotency_key: NotRequired[str]
