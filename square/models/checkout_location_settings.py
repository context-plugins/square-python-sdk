from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .checkout_location_settings_branding import CheckoutLocationSettingsBranding, CheckoutLocationSettingsBrandingDict
from .checkout_location_settings_coupons import CheckoutLocationSettingsCoupons, CheckoutLocationSettingsCouponsDict
from .checkout_location_settings_policy import CheckoutLocationSettingsPolicy, CheckoutLocationSettingsPolicyDict
from .checkout_location_settings_tipping import CheckoutLocationSettingsTipping, CheckoutLocationSettingsTippingDict


class CheckoutLocationSettings(SdkBaseModel):
    location_id: OptionalNullable[str] = UNSET
    """The ID of the location that these settings apply to."""

    customer_notes_enabled: OptionalNullable[bool] = UNSET
    """Indicates whether customers are allowed to leave notes at checkout."""

    policies: OptionalNullable[list[CheckoutLocationSettingsPolicy]] = UNSET
    """Policy information is displayed at the bottom of the checkout pages. You can set a maximum of two policies."""

    branding: Optional[CheckoutLocationSettingsBranding] = UNSET
    tipping: Optional[CheckoutLocationSettingsTipping] = UNSET
    coupons: Optional[CheckoutLocationSettingsCoupons] = UNSET
    updated_at: Optional[str] = UNSET
    """The timestamp when the settings were last updated, in RFC 3339 format. Examples for January 25th, 2020 6:25:34pm
    Pacific Standard Time: UTC: 2020-01-26T02:25:34Z Pacific Standard Time with UTC offset: 2020-01-25T18:25:34-08:00"""


class CheckoutLocationSettingsDict(TypedDict):
    location_id: NotRequired[str | None]
    customer_notes_enabled: NotRequired[bool | None]
    policies: NotRequired[list[CheckoutLocationSettingsPolicyDict] | None]
    branding: NotRequired[CheckoutLocationSettingsBrandingDict]
    tipping: NotRequired[CheckoutLocationSettingsTippingDict]
    coupons: NotRequired[CheckoutLocationSettingsCouponsDict]
    updated_at: NotRequired[str]
