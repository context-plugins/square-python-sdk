from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessAppointmentSettingsAlignmentTime(str, Enum):
    """Time units of a service duration for bookings."""

    SERVICE_DURATION = "SERVICE_DURATION"
    """The service duration unit is one visit of a fixed time interval specified by the seller."""

    QUARTER_HOURLY = "QUARTER_HOURLY"
    """The service duration unit is a 15-minute interval. Bookings can be scheduled every quarter hour."""

    HALF_HOURLY = "HALF_HOURLY"
    """The service duration unit is a 30-minute interval. Bookings can be scheduled every half hour."""

    HOURLY = "HOURLY"
    """The service duration unit is a 60-minute interval. Bookings can be scheduled every hour."""

    __str__ = str.__str__


BusinessAppointmentSettingsAlignmentTimeOrStr: TypeAlias = Annotated[
    BusinessAppointmentSettingsAlignmentTime | str, open_enum_validator(BusinessAppointmentSettingsAlignmentTime)
]
