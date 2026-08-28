from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class DisputedPayment(SdkBaseModel):
    """The payment the cardholder disputed."""

    payment_id: OptionalNullable[str] = UNSET
    """Square-generated unique ID of the payment being disputed."""


class DisputedPaymentDict(TypedDict):
    payment_id: NotRequired[str | None]
