from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaymentBalanceActivityDepositFeeDetail(SdkBaseModel):
    payout_id: OptionalNullable[str] = UNSET
    """The ID of the payout that triggered this deposit fee activity."""


class PaymentBalanceActivityDepositFeeDetailDict(TypedDict):
    payout_id: NotRequired[str | None]
