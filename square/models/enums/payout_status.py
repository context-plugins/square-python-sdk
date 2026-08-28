from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PayoutStatus(str, Enum):
    """Payout status types"""

    SENT = "SENT"
    """Indicates that the payout was successfully sent to the banking destination."""

    FAILED = "FAILED"
    """Indicates that the payout was rejected by the banking destination."""

    PAID = "PAID"
    """Indicates that the payout has successfully completed."""

    __str__ = str.__str__


PayoutStatusOrStr: TypeAlias = Annotated[PayoutStatus | str, open_enum_validator(PayoutStatus)]
