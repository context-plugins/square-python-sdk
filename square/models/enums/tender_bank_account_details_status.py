from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TenderBankAccountDetailsStatus(str, Enum):
    """Indicates the bank account payment's current status."""

    PENDING = "PENDING"
    """The bank account payment is in progress."""

    COMPLETED = "COMPLETED"
    """The bank account payment has been completed."""

    FAILED = "FAILED"
    """The bank account payment failed."""

    __str__ = str.__str__


TenderBankAccountDetailsStatusOrStr: TypeAlias = Annotated[
    TenderBankAccountDetailsStatus | str, open_enum_validator(TenderBankAccountDetailsStatus)
]
