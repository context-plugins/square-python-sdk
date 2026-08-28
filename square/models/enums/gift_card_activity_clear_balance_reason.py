from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardActivityClearBalanceReason(str, Enum):
    """Indicates the reason for clearing the balance of a `gift card <entity:GiftCard>`__."""

    SUSPICIOUS_ACTIVITY = "SUSPICIOUS_ACTIVITY"
    """The seller suspects suspicious activity."""

    REUSE_GIFTCARD = "REUSE_GIFTCARD"
    """The seller cleared the balance to reuse the gift card."""

    UNKNOWN_REASON = "UNKNOWN_REASON"
    """The gift card balance was cleared for an unknown reason.

    This reason is read-only and cannot be used to create a ``CLEAR_BALANCE`` activity using the Gift Card Activities
    API."""

    __str__ = str.__str__


GiftCardActivityClearBalanceReasonOrStr: TypeAlias = Annotated[
    GiftCardActivityClearBalanceReason | str, open_enum_validator(GiftCardActivityClearBalanceReason)
]
