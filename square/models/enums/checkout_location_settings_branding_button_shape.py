from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CheckoutLocationSettingsBrandingButtonShape(str, Enum):
    SQUARED = "SQUARED"
    ROUNDED = "ROUNDED"
    PILL = "PILL"

    __str__ = str.__str__


CheckoutLocationSettingsBrandingButtonShapeOrStr: TypeAlias = Annotated[
    CheckoutLocationSettingsBrandingButtonShape | str, open_enum_validator(CheckoutLocationSettingsBrandingButtonShape)
]
