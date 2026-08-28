from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1TenderType(str, Enum):
    CREDIT_CARD = "CREDIT_CARD"
    CASH = "CASH"
    THIRD_PARTY_CARD = "THIRD_PARTY_CARD"
    NO_SALE = "NO_SALE"
    SQUARE_WALLET = "SQUARE_WALLET"
    SQUARE_GIFT_CARD = "SQUARE_GIFT_CARD"
    UNKNOWN = "UNKNOWN"
    OTHER = "OTHER"

    __str__ = str.__str__


V1TenderTypeOrStr: TypeAlias = Annotated[V1TenderType | str, open_enum_validator(V1TenderType)]
