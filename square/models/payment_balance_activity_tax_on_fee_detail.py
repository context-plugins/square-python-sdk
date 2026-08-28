from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PaymentBalanceActivityTaxOnFeeDetail(SdkBaseModel):
    payment_id: OptionalNullable[str] = UNSET
    """The ID of the payment associated with this activity."""

    tax_rate_description: OptionalNullable[str] = UNSET
    """The description of the tax rate being applied. For example: "GST", "HST"."""


class PaymentBalanceActivityTaxOnFeeDetailDict(TypedDict):
    payment_id: NotRequired[str | None]
    tax_rate_description: NotRequired[str | None]
