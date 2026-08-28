from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_merchant_settings_payment_methods_afterpay_clearpay import (
    CheckoutMerchantSettingsPaymentMethodsAfterpayClearpay,
    CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayDict,
)
from .checkout_merchant_settings_payment_methods_payment_method import (
    CheckoutMerchantSettingsPaymentMethodsPaymentMethod,
    CheckoutMerchantSettingsPaymentMethodsPaymentMethodDict,
)


class CheckoutMerchantSettingsPaymentMethods(SdkBaseModel):
    apple_pay: Optional[CheckoutMerchantSettingsPaymentMethodsPaymentMethod] = UNSET
    """The settings allowed for a payment method."""

    google_pay: Optional[CheckoutMerchantSettingsPaymentMethodsPaymentMethod] = UNSET
    """The settings allowed for a payment method."""

    cash_app: Optional[CheckoutMerchantSettingsPaymentMethodsPaymentMethod] = UNSET
    """The settings allowed for a payment method."""

    afterpay_clearpay: Optional[CheckoutMerchantSettingsPaymentMethodsAfterpayClearpay] = UNSET
    """The settings allowed for AfterpayClearpay."""


class CheckoutMerchantSettingsPaymentMethodsDict(TypedDict):
    apple_pay: NotRequired[
        CheckoutMerchantSettingsPaymentMethodsPaymentMethod | CheckoutMerchantSettingsPaymentMethodsPaymentMethodDict
    ]
    google_pay: NotRequired[
        CheckoutMerchantSettingsPaymentMethodsPaymentMethod | CheckoutMerchantSettingsPaymentMethodsPaymentMethodDict
    ]
    cash_app: NotRequired[
        CheckoutMerchantSettingsPaymentMethodsPaymentMethod | CheckoutMerchantSettingsPaymentMethodsPaymentMethodDict
    ]
    afterpay_clearpay: NotRequired[
        (
            CheckoutMerchantSettingsPaymentMethodsAfterpayClearpay
            | CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayDict
        )
    ]
