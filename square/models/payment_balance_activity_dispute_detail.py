from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaymentBalanceActivityDisputeDetail(SdkBaseModel):
    payment_id: OptionalNullable[str] = UNSET
    """The ID of the payment associated with this activity."""

    dispute_id: OptionalNullable[str] = UNSET
    """The ID of the dispute associated with this activity."""


class PaymentBalanceActivityDisputeDetailDict(TypedDict):
    payment_id: NotRequired[str | None]
    dispute_id: NotRequired[str | None]
