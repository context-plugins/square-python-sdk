from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RefundStatus(str, Enum):
    """Indicates a refund's current status."""

    PENDING = "PENDING"
    """The refund is pending."""

    APPROVED = "APPROVED"
    """The refund has been approved by Square."""

    REJECTED = "REJECTED"
    """The refund has been rejected by Square."""

    FAILED = "FAILED"
    """The refund failed."""

    __str__ = str.__str__


RefundStatusOrStr: TypeAlias = Annotated[RefundStatus | str, open_enum_validator(RefundStatus)]
