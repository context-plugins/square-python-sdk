from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1TenderCardBrand(str, Enum):
    """The brand of a credit card."""

    OTHER_BRAND = "OTHER_BRAND"
    VISA = "VISA"
    MASTER_CARD = "MASTER_CARD"
    AMERICAN_EXPRESS = "AMERICAN_EXPRESS"
    DISCOVER = "DISCOVER"
    DISCOVER_DINERS = "DISCOVER_DINERS"
    JCB = "JCB"
    CHINA_UNIONPAY = "CHINA_UNIONPAY"
    SQUARE_GIFT_CARD = "SQUARE_GIFT_CARD"

    __str__ = str.__str__


V1TenderCardBrandOrStr: TypeAlias = Annotated[V1TenderCardBrand | str, open_enum_validator(V1TenderCardBrand)]
