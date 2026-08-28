from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .checkout_merchant_settings import CheckoutMerchantSettings, CheckoutMerchantSettingsDict


class UpdateMerchantSettingsRequest(SdkBaseModel):
    merchant_settings: CheckoutMerchantSettings


class UpdateMerchantSettingsRequestDict(TypedDict):
    merchant_settings: CheckoutMerchantSettings | CheckoutMerchantSettingsDict
