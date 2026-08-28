from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_merchant_settings import CheckoutMerchantSettings, CheckoutMerchantSettingsDict
from .error import Error, ErrorDict


class RetrieveMerchantSettingsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    merchant_settings: Optional[CheckoutMerchantSettings] = UNSET


class RetrieveMerchantSettingsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    merchant_settings: NotRequired[CheckoutMerchantSettings | CheckoutMerchantSettingsDict]
