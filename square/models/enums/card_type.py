from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CardType(str, Enum):
    """Indicates a card's type, such as ``CREDIT`` or ``DEBIT``."""

    UNKNOWN_CARD_TYPE = "UNKNOWN_CARD_TYPE"
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

    __str__ = str.__str__


CardTypeOrStr: TypeAlias = Annotated[CardType | str, open_enum_validator(CardType)]
