from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaymentBalanceActivityRefundDetail(SdkBaseModel):
    payment_id: OptionalNullable[str] = UNSET
    """The ID of the payment associated with this activity."""

    refund_id: OptionalNullable[str] = UNSET
    """The ID of the refund associated with this activity."""


class PaymentBalanceActivityRefundDetailDict(TypedDict):
    payment_id: NotRequired[str | None]
    refund_id: NotRequired[str | None]
