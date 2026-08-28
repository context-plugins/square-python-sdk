from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TenderCardDetailsEntryMethod(str, Enum):
    """Indicates the method used to enter the card's details."""

    SWIPED = "SWIPED"
    """The card was swiped through a Square reader or Square stand."""

    KEYED = "KEYED"
    """The card information was keyed manually into Square Point of Sale or a Square-hosted web form."""

    EMV = "EMV"
    """The card was processed via EMV with a Square reader."""

    ON_FILE = "ON_FILE"
    """The buyer's card details were already on file with Square."""

    CONTACTLESS = "CONTACTLESS"
    """The card was processed via a contactless (i.e., NFC) transaction with a Square reader."""

    __str__ = str.__str__


TenderCardDetailsEntryMethodOrStr: TypeAlias = Annotated[
    TenderCardDetailsEntryMethod | str, open_enum_validator(TenderCardDetailsEntryMethod)
]
