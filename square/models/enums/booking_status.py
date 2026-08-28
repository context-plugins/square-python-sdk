from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BookingStatus(str, Enum):
    """Supported booking statuses."""

    PENDING = "PENDING"
    """An unaccepted booking. It is visible to both sellers and customers."""

    CANCELLED_BY_CUSTOMER = "CANCELLED_BY_CUSTOMER"
    """A customer-cancelled booking. It is visible to both the seller and the customer."""

    CANCELLED_BY_SELLER = "CANCELLED_BY_SELLER"
    """A seller-cancelled booking. It is visible to both the seller and the customer."""

    DECLINED = "DECLINED"
    """A declined booking. It had once been pending, but was then declined by the seller."""

    ACCEPTED = "ACCEPTED"
    """An accepted booking agreed to or accepted by the seller."""

    NO_SHOW = "NO_SHOW"
    """A no-show booking. The booking was accepted at one time, but have now been marked as a no-show by the seller
    because the client either missed the booking or cancelled it without enough notice."""

    __str__ = str.__str__


BookingStatusOrStr: TypeAlias = Annotated[BookingStatus | str, open_enum_validator(BookingStatus)]
