from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardActivityBlockReason(str, Enum):
    """Indicates the reason for blocking a `gift card <entity:GiftCard>`__."""

    CHARGEBACK_BLOCK = "CHARGEBACK_BLOCK"
    """The gift card is blocked because the buyer initiated a chargeback on the gift card purchase."""

    __str__ = str.__str__


GiftCardActivityBlockReasonOrStr: TypeAlias = Annotated[
    GiftCardActivityBlockReason | str, open_enum_validator(GiftCardActivityBlockReason)
]
