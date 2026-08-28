from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaymentBalanceActivityAppFeeRefundDetail(SdkBaseModel):
    payment_id: OptionalNullable[str] = UNSET
    """The ID of the payment associated with this activity."""

    refund_id: OptionalNullable[str] = UNSET
    """The ID of the refund associated with this activity."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the location of the merchant associated with the payment refund activity"""


class PaymentBalanceActivityAppFeeRefundDetailDict(TypedDict):
    payment_id: NotRequired[str | None]
    refund_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
