from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaymentBalanceActivityOtherAdjustmentDetail(SdkBaseModel):
    payment_id: OptionalNullable[str] = UNSET
    """The ID of the payment associated with this activity."""


class PaymentBalanceActivityOtherAdjustmentDetailDict(TypedDict):
    payment_id: NotRequired[str | None]
