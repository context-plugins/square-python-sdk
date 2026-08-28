from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .order import Order, OrderDict


class UpdateOrderRequest(SdkBaseModel):
    """Defines the fields that are included in requests to the `UpdateOrder <api-endpoint:Orders-UpdateOrder>`__
    endpoint."""

    order: Optional[Order] = UNSET
    """Contains all information related to a single order to process with Square, including line items that specify the
    products to purchase. ``Order`` objects also include information about any associated tenders, refunds, and returns.

    All Connect V2 Transactions have all been converted to Orders including all associated itemization data."""

    fields_to_clear: Optional[list[str | None]] = UNSET
    """The `dot notation paths
    <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#identifying-fields-to-delete>`__ fields
    to clear. For example, ``line_items[uid].note``. For more information, see `Deleting fields
    <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#deleting-fields>`__."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A value you specify that uniquely identifies this update request.

    If you are unsure whether a particular update was applied to an order successfully, you can reattempt it with the
    same idempotency key without worrying about creating duplicate updates to the order. The latest order version is
    returned.

    For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class UpdateOrderRequestDict(TypedDict):
    order: NotRequired[Order | OrderDict]
    fields_to_clear: NotRequired[list[str | None]]
    idempotency_key: NotRequired[str | None]
