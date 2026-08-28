from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_merchant_settings import CheckoutMerchantSettings, CheckoutMerchantSettingsDict


class MerchantSettingsUpdatedEventObject(SdkBaseModel):
    merchant_settings: Optional[CheckoutMerchantSettings] = UNSET


class MerchantSettingsUpdatedEventObjectDict(TypedDict):
    merchant_settings: NotRequired[CheckoutMerchantSettings | CheckoutMerchantSettingsDict]
