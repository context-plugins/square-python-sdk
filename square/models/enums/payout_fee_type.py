from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayoutFeeType(str, Enum):
    """Represents the type of payout fee that can incur as part of a payout."""

    TRANSFER_FEE = "TRANSFER_FEE"
    """Fee type associated with transfers."""

    TAX_ON_TRANSFER_FEE = "TAX_ON_TRANSFER_FEE"
    """Taxes associated with the transfer fee."""

    __str__ = str.__str__


PayoutFeeTypeOrStr: TypeAlias = Annotated[PayoutFeeType | str, open_enum_validator(PayoutFeeType)]
