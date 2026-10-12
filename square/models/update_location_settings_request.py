from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .checkout_location_settings import CheckoutLocationSettings, CheckoutLocationSettingsDict


class UpdateLocationSettingsRequest(SdkBaseModel):
    location_settings: CheckoutLocationSettings


class UpdateLocationSettingsRequestDict(TypedDict):
    location_settings: CheckoutLocationSettingsDict
