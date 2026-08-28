from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1TenderEntryMethod(str, Enum):
    MANUAL = "MANUAL"
    SCANNED = "SCANNED"
    SQUARE_CASH = "SQUARE_CASH"
    SQUARE_WALLET = "SQUARE_WALLET"
    SWIPED = "SWIPED"
    WEB_FORM = "WEB_FORM"
    OTHER = "OTHER"

    __str__ = str.__str__


V1TenderEntryMethodOrStr: TypeAlias = Annotated[V1TenderEntryMethod | str, open_enum_validator(V1TenderEntryMethod)]
