from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LocationCapability(str, Enum):
    """The capabilities a location might have."""

    CREDIT_CARD_PROCESSING = "CREDIT_CARD_PROCESSING"
    """The capability to process credit card transactions with Square."""

    AUTOMATIC_TRANSFERS = "AUTOMATIC_TRANSFERS"
    """The capability to receive automatic transfers from Square."""

    UNLINKED_REFUNDS = "UNLINKED_REFUNDS"
    """The capability to process unlinked refunds with Square."""

    __str__ = str.__str__


LocationCapabilityOrStr: TypeAlias = Annotated[LocationCapability | str, open_enum_validator(LocationCapability)]
