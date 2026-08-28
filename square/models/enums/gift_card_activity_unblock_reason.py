from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardActivityUnblockReason(str, Enum):
    """Indicates the reason for unblocking a `gift card <entity:GiftCard>`__."""

    CHARGEBACK_UNBLOCK = "CHARGEBACK_UNBLOCK"
    """The gift card is unblocked because a chargeback was ruled in favor of the seller."""

    __str__ = str.__str__


GiftCardActivityUnblockReasonOrStr: TypeAlias = Annotated[
    GiftCardActivityUnblockReason | str, open_enum_validator(GiftCardActivityUnblockReason)
]
