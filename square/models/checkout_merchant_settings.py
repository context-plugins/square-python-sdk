from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_merchant_settings_payment_methods import (
    CheckoutMerchantSettingsPaymentMethods,
    CheckoutMerchantSettingsPaymentMethodsDict,
)


class CheckoutMerchantSettings(SdkBaseModel):
    payment_methods: Optional[CheckoutMerchantSettingsPaymentMethods] = UNSET
    updated_at: Optional[str] = UNSET
    """The timestamp when the settings were last updated, in RFC 3339 format. Examples for January 25th, 2020 6:25:34pm
    Pacific Standard Time: UTC: 2020-01-26T02:25:34Z Pacific Standard Time with UTC offset: 2020-01-25T18:25:34-08:00"""


class CheckoutMerchantSettingsDict(TypedDict):
    payment_methods: NotRequired[CheckoutMerchantSettingsPaymentMethods | CheckoutMerchantSettingsPaymentMethodsDict]
    updated_at: NotRequired[str]
