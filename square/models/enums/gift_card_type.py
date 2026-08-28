from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardType(str, Enum):
    """Indicates the gift card type."""

    PHYSICAL = "PHYSICAL"
    """A plastic gift card."""

    DIGITAL = "DIGITAL"
    """A digital gift card."""

    __str__ = str.__str__


GiftCardTypeOrStr: TypeAlias = Annotated[GiftCardType | str, open_enum_validator(GiftCardType)]
