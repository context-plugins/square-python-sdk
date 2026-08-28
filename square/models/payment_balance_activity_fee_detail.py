from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaymentBalanceActivityFeeDetail(SdkBaseModel):
    payment_id: OptionalNullable[str] = UNSET
    """The ID of the payment associated with this activity This will only be populated when a principal LedgerEntryToken
    is also populated. If the fee is independent (there is no principal LedgerEntryToken) then this will likely not be
    populated."""


class PaymentBalanceActivityFeeDetailDict(TypedDict):
    payment_id: NotRequired[str | None]
