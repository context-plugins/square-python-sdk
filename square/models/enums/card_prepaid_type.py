from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardPrepaidType(str, Enum):
    """Indicates a card's prepaid type, such as ``NOT_PREPAID`` or ``PREPAID``."""

    UNKNOWN_PREPAID_TYPE = "UNKNOWN_PREPAID_TYPE"
    NOT_PREPAID = "NOT_PREPAID"
    PREPAID = "PREPAID"

    __str__ = str.__str__


CardPrepaidTypeOrStr: TypeAlias = Annotated[CardPrepaidType | str, open_enum_validator(CardPrepaidType)]
