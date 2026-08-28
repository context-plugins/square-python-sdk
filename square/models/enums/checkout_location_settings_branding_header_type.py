from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CheckoutLocationSettingsBrandingHeaderType(str, Enum):
    BUSINESS_NAME = "BUSINESS_NAME"
    FRAMED_LOGO = "FRAMED_LOGO"
    FULL_WIDTH_LOGO = "FULL_WIDTH_LOGO"

    __str__ = str.__str__


CheckoutLocationSettingsBrandingHeaderTypeOrStr: TypeAlias = Annotated[
    CheckoutLocationSettingsBrandingHeaderType | str, open_enum_validator(CheckoutLocationSettingsBrandingHeaderType)
]
