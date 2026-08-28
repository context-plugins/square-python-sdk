from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardActivityAdjustIncrementReason(str, Enum):
    """Indicates the reason for adding money to a `gift card <entity:GiftCard>`__."""

    COMPLIMENTARY = "COMPLIMENTARY"
    """The seller gifted a complimentary gift card balance increase."""

    SUPPORT_ISSUE = "SUPPORT_ISSUE"
    """The seller increased the gift card balance to accommodate support issues."""

    TRANSACTION_VOIDED = "TRANSACTION_VOIDED"
    """The transaction is voided."""

    __str__ = str.__str__


GiftCardActivityAdjustIncrementReasonOrStr: TypeAlias = Annotated[
    GiftCardActivityAdjustIncrementReason | str, open_enum_validator(GiftCardActivityAdjustIncrementReason)
]
