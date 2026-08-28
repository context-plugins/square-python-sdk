from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.checkout_location_settings_branding_button_shape import CheckoutLocationSettingsBrandingButtonShapeOrStr
from .enums.checkout_location_settings_branding_header_type import CheckoutLocationSettingsBrandingHeaderTypeOrStr


class CheckoutLocationSettingsBranding(SdkBaseModel):
    header_type: Optional[CheckoutLocationSettingsBrandingHeaderTypeOrStr] = UNSET
    button_color: OptionalNullable[str] = UNSET
    """The HTML-supported hex color for the button on the checkout page (for example, "#FFFFFF")."""

    button_shape: Optional[CheckoutLocationSettingsBrandingButtonShapeOrStr] = UNSET


class CheckoutLocationSettingsBrandingDict(TypedDict):
    header_type: NotRequired[CheckoutLocationSettingsBrandingHeaderTypeOrStr]
    button_color: NotRequired[str | None]
    button_shape: NotRequired[CheckoutLocationSettingsBrandingButtonShapeOrStr]
