from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_merchant_settings import CheckoutMerchantSettings, CheckoutMerchantSettingsDict
from .error import Error, ErrorDict


class UpdateMerchantSettingsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred when updating the merchant settings."""

    merchant_settings: Optional[CheckoutMerchantSettings] = UNSET


class UpdateMerchantSettingsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    merchant_settings: NotRequired[CheckoutMerchantSettingsDict]
