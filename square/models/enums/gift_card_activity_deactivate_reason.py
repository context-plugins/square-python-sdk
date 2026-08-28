from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardActivityDeactivateReason(str, Enum):
    """Indicates the reason for deactivating a `gift card <entity:GiftCard>`__."""

    SUSPICIOUS_ACTIVITY = "SUSPICIOUS_ACTIVITY"
    """The seller suspects suspicious activity."""

    UNKNOWN_REASON = "UNKNOWN_REASON"
    """The gift card was deactivated for an unknown reason.

    This reason is read-only and cannot be used to create a ``DEACTIVATE`` activity using the Gift Card Activities
    API."""

    CHARGEBACK_DEACTIVATE = "CHARGEBACK_DEACTIVATE"
    """A chargeback on the gift card purchase (or the gift card load) was ruled in favor of the buyer.

    This reason is read-only and cannot be used to create a ``DEACTIVATE`` activity using the Gift Card Activities
    API."""

    __str__ = str.__str__


GiftCardActivityDeactivateReasonOrStr: TypeAlias = Annotated[
    GiftCardActivityDeactivateReason | str, open_enum_validator(GiftCardActivityDeactivateReason)
]
