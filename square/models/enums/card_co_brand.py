from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardCoBrand(str, Enum):
    """Indicates the brand for a co-branded card."""

    UNKNOWN = "UNKNOWN"
    AFTERPAY = "AFTERPAY"
    CLEARPAY = "CLEARPAY"

    __str__ = str.__str__


CardCoBrandOrStr: TypeAlias = Annotated[CardCoBrand | str, open_enum_validator(CardCoBrand)]
