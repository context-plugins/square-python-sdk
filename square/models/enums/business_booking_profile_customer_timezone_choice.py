from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessBookingProfileCustomerTimezoneChoice(str, Enum):
    """Choices of customer-facing time zone used for bookings."""

    BUSINESS_LOCATION_TIMEZONE = "BUSINESS_LOCATION_TIMEZONE"
    """Use the time zone of the business location for bookings."""

    CUSTOMER_CHOICE = "CUSTOMER_CHOICE"
    """Use the customer-chosen time zone for bookings."""

    __str__ = str.__str__


BusinessBookingProfileCustomerTimezoneChoiceOrStr: TypeAlias = Annotated[
    BusinessBookingProfileCustomerTimezoneChoice | str,
    open_enum_validator(BusinessBookingProfileCustomerTimezoneChoice),
]
