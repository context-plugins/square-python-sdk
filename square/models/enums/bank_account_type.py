from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BankAccountType(str, Enum):
    """Indicates the financial purpose of the bank account."""

    CHECKING = "CHECKING"
    """An account at a financial institution against which checks can be drawn by the account depositor."""

    SAVINGS = "SAVINGS"
    """An account at a financial institution that pays interest but cannot be used directly as money in the narrow sense
    of a medium of exchange."""

    INVESTMENT = "INVESTMENT"
    """An account at a financial institution that contains a deposit of funds and/or securities."""

    OTHER = "OTHER"
    """An account at a financial institution which cannot be described by the other types."""

    BUSINESS_CHECKING = "BUSINESS_CHECKING"
    """An account at a financial institution against which checks can be drawn specifically for business purposes
    (non-personal use)."""

    __str__ = str.__str__


BankAccountTypeOrStr: TypeAlias = Annotated[BankAccountType | str, open_enum_validator(BankAccountType)]
