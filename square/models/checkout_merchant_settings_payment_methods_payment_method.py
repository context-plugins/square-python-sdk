from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CheckoutMerchantSettingsPaymentMethodsPaymentMethod(SdkBaseModel):
    """The settings allowed for a payment method."""

    enabled: OptionalNullable[bool] = UNSET
    """Indicates whether the payment method is enabled for the account."""


class CheckoutMerchantSettingsPaymentMethodsPaymentMethodDict(TypedDict):
    enabled: NotRequired[bool | None]
