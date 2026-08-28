from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TenderCardDetailsStatus(str, Enum):
    """Indicates the card transaction's current status."""

    AUTHORIZED = "AUTHORIZED"
    """The card transaction has been authorized but not yet captured."""

    CAPTURED = "CAPTURED"
    """The card transaction was authorized and subsequently captured (i.e., completed)."""

    VOIDED = "VOIDED"
    """The card transaction was authorized and subsequently voided (i.e., canceled)."""

    FAILED = "FAILED"
    """The card transaction failed."""

    __str__ = str.__str__


TenderCardDetailsStatusOrStr: TypeAlias = Annotated[
    TenderCardDetailsStatus | str, open_enum_validator(TenderCardDetailsStatus)
]
