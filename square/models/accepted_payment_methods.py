from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AcceptedPaymentMethods(SdkBaseModel):
    apple_pay: OptionalNullable[bool] = UNSET
    """Whether Apple Pay is accepted at checkout."""

    google_pay: OptionalNullable[bool] = UNSET
    """Whether Google Pay is accepted at checkout."""

    cash_app_pay: OptionalNullable[bool] = UNSET
    """Whether Cash App Pay is accepted at checkout."""

    afterpay_clearpay: OptionalNullable[bool] = UNSET
    """Whether Afterpay/Clearpay is accepted at checkout."""


class AcceptedPaymentMethodsDict(TypedDict):
    apple_pay: NotRequired[bool | None]
    google_pay: NotRequired[bool | None]
    cash_app_pay: NotRequired[bool | None]
    afterpay_clearpay: NotRequired[bool | None]
