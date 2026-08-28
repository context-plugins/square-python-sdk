from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_location_settings import CheckoutLocationSettings, CheckoutLocationSettingsDict
from .error import Error, ErrorDict


class UpdateLocationSettingsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred when updating the location settings."""

    location_settings: Optional[CheckoutLocationSettings] = UNSET


class UpdateLocationSettingsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    location_settings: NotRequired[CheckoutLocationSettings | CheckoutLocationSettingsDict]
