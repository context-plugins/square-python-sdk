from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessAppointmentSettingsBookingLocationType(str, Enum):
    """Supported types of location where service is provided."""

    BUSINESS_LOCATION = "BUSINESS_LOCATION"
    """The service is provided at a seller location."""

    CUSTOMER_LOCATION = "CUSTOMER_LOCATION"
    """The service is provided at a customer location."""

    PHONE = "PHONE"
    """The service is provided over the phone."""

    __str__ = str.__str__


BusinessAppointmentSettingsBookingLocationTypeOrStr: TypeAlias = Annotated[
    BusinessAppointmentSettingsBookingLocationType | str,
    open_enum_validator(BusinessAppointmentSettingsBookingLocationType),
]
