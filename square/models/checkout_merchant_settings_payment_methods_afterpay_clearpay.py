from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_merchant_settings_payment_methods_afterpay_clearpay_eligibility_range import (
    CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayEligibilityRange,
    CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayEligibilityRangeDict,
)


class CheckoutMerchantSettingsPaymentMethodsAfterpayClearpay(SdkBaseModel):
    """The settings allowed for AfterpayClearpay."""

    order_eligibility_range: Optional[CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayEligibilityRange] = UNSET
    """A range of purchase price that qualifies."""

    item_eligibility_range: Optional[CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayEligibilityRange] = UNSET
    """A range of purchase price that qualifies."""

    enabled: Optional[bool] = UNSET
    """Indicates whether the payment method is enabled for the account."""


class CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayDict(TypedDict):
    order_eligibility_range: NotRequired[
        (
            CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayEligibilityRange
            | CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayEligibilityRangeDict
        )
    ]
    item_eligibility_range: NotRequired[
        (
            CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayEligibilityRange
            | CheckoutMerchantSettingsPaymentMethodsAfterpayClearpayEligibilityRangeDict
        )
    ]
    enabled: NotRequired[bool]
