from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaymentBalanceActivityAutomaticSavingsDetail(SdkBaseModel):
    payment_id: OptionalNullable[str] = UNSET
    """The ID of the payment associated with this activity."""

    payout_id: OptionalNullable[str] = UNSET
    """The ID of the payout associated with this activity."""


class PaymentBalanceActivityAutomaticSavingsDetailDict(TypedDict):
    payment_id: NotRequired[str | None]
    payout_id: NotRequired[str | None]
