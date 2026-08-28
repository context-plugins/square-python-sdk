from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DestinationType(str, Enum):
    """List of possible destinations against which a payout can be made."""

    BANK_ACCOUNT = "BANK_ACCOUNT"
    """An external bank account outside of Square."""

    CARD = "CARD"
    """An external card outside of Square used for the transfer."""

    SQUARE_BALANCE = "SQUARE_BALANCE"
    SQUARE_STORED_BALANCE = "SQUARE_STORED_BALANCE"
    """Square Checking or Savings account (US), Square Card (CA)"""

    __str__ = str.__str__


DestinationTypeOrStr: TypeAlias = Annotated[DestinationType | str, open_enum_validator(DestinationType)]
