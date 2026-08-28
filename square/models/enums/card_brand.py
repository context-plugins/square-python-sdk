from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardBrand(str, Enum):
    """Indicates a card's brand, such as ``VISA`` or ``MASTERCARD``."""

    OTHER_BRAND = "OTHER_BRAND"
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    AMERICAN_EXPRESS = "AMERICAN_EXPRESS"
    DISCOVER = "DISCOVER"
    DISCOVER_DINERS = "DISCOVER_DINERS"
    JCB = "JCB"
    CHINA_UNIONPAY = "CHINA_UNIONPAY"
    SQUARE_GIFT_CARD = "SQUARE_GIFT_CARD"
    SQUARE_CAPITAL_CARD = "SQUARE_CAPITAL_CARD"
    INTERAC = "INTERAC"
    EFTPOS = "EFTPOS"
    FELICA = "FELICA"
    EBT = "EBT"

    __str__ = str.__str__


CardBrandOrStr: TypeAlias = Annotated[CardBrand | str, open_enum_validator(CardBrand)]
