from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_location_settings import CheckoutLocationSettings, CheckoutLocationSettingsDict


class LocationSettingsUpdatedEventObject(SdkBaseModel):
    location_settings: Optional[CheckoutLocationSettings] = UNSET


class LocationSettingsUpdatedEventObjectDict(TypedDict):
    location_settings: NotRequired[CheckoutLocationSettingsDict]
