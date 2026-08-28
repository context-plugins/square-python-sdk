from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TenderSquareAccountDetailsStatus(str, Enum):
    AUTHORIZED = "AUTHORIZED"
    """The Square Account payment has been authorized but not yet captured."""

    CAPTURED = "CAPTURED"
    """The Square Account payment was authorized and subsequently captured (i.e., completed)."""

    VOIDED = "VOIDED"
    """The Square Account payment was authorized and subsequently voided (i.e., canceled)."""

    FAILED = "FAILED"
    """The Square Account payment failed."""

    __str__ = str.__str__


TenderSquareAccountDetailsStatusOrStr: TypeAlias = Annotated[
    TenderSquareAccountDetailsStatus | str, open_enum_validator(TenderSquareAccountDetailsStatus)
]
