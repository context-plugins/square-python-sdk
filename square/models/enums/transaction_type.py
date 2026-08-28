from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TransactionType(str, Enum):
    """The transaction type used in the disputed payment."""

    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

    __str__ = str.__str__


TransactionTypeOrStr: TypeAlias = Annotated[TransactionType | str, open_enum_validator(TransactionType)]
