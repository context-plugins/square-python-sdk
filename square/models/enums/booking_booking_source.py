from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BookingBookingSource(str, Enum):
    """Supported sources a booking was created from."""

    FIRST_PARTY_MERCHANT = "FIRST_PARTY_MERCHANT"
    """The booking was created by a seller from a Square Appointments application, such as the Square Appointments
    Dashboard or a Square Appointments mobile app."""

    FIRST_PARTY_BUYER = "FIRST_PARTY_BUYER"
    """The booking was created by a buyer from a Square Appointments application, such as Square Online Booking Site."""

    THIRD_PARTY_BUYER = "THIRD_PARTY_BUYER"
    """The booking was created by a buyer created from a third-party application."""

    API = "API"
    """The booking was created by a seller or a buyer from the Square Bookings API."""

    __str__ = str.__str__


BookingBookingSourceOrStr: TypeAlias = Annotated[BookingBookingSource | str, open_enum_validator(BookingBookingSource)]
