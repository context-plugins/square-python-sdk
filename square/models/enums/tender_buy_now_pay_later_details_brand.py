from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TenderBuyNowPayLaterDetailsBrand(str, Enum):
    OTHER_BRAND = "OTHER_BRAND"
    AFTERPAY = "AFTERPAY"

    __str__ = str.__str__


TenderBuyNowPayLaterDetailsBrandOrStr: TypeAlias = Annotated[
    TenderBuyNowPayLaterDetailsBrand | str, open_enum_validator(TenderBuyNowPayLaterDetailsBrand)
]
