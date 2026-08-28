from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class PayOrderRequest(SdkBaseModel):
    """Defines the fields that are included in requests to the `PayOrder <api-endpoint:Orders-PayOrder>`__ endpoint."""

    idempotency_key: str
    """A value you specify that uniquely identifies this request among requests you have sent. If you are unsure whether
    a particular payment request was completed successfully, you can reattempt it with the same idempotency key without
    worrying about duplicate payments.

    For more information, see `Idempotency <https://developer.squareup.com/docs/working-with-apis/idempotency>`__."""

    order_version: OptionalNullable[int] = UNSET
    """The version of the order being paid. If not supplied, the latest version will be paid."""

    payment_ids: Optional[list[str | None]] = UNSET
    """The IDs of the `payments <entity:Payment>`__ to collect. The payment total must match the order total."""


class PayOrderRequestDict(TypedDict):
    idempotency_key: str
    order_version: NotRequired[int | None]
    payment_ids: NotRequired[list[str | None]]
