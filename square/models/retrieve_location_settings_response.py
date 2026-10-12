from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout_location_settings import CheckoutLocationSettings, CheckoutLocationSettingsDict
from .error import Error, ErrorDict


class RetrieveLocationSettingsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    location_settings: Optional[CheckoutLocationSettings] = UNSET


class RetrieveLocationSettingsResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    location_settings: NotRequired[CheckoutLocationSettingsDict]
