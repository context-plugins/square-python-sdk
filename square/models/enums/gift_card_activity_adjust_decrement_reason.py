from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardActivityAdjustDecrementReason(str, Enum):
    """Indicates the reason for deducting money from a `gift card <entity:GiftCard>`__."""

    SUSPICIOUS_ACTIVITY = "SUSPICIOUS_ACTIVITY"
    """The balance was decreased because the seller detected suspicious or fraudulent activity on the gift card."""

    BALANCE_ACCIDENTALLY_INCREASED = "BALANCE_ACCIDENTALLY_INCREASED"
    """The balance was decreased to reverse an unintentional balance increase."""

    SUPPORT_ISSUE = "SUPPORT_ISSUE"
    """The balance was decreased to accommodate support issues."""

    PURCHASE_WAS_REFUNDED = "PURCHASE_WAS_REFUNDED"
    """The balance was decreased because the order used to purchase or reload the gift card was refunded."""

    __str__ = str.__str__


GiftCardActivityAdjustDecrementReasonOrStr: TypeAlias = Annotated[
    GiftCardActivityAdjustDecrementReason | str, open_enum_validator(GiftCardActivityAdjustDecrementReason)
]
