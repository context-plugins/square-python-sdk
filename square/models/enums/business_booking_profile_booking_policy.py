from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessBookingProfileBookingPolicy(str, Enum):
    """Policies for accepting bookings."""

    ACCEPT_ALL = "ACCEPT_ALL"
    """The seller accepts all booking requests automatically."""

    REQUIRES_ACCEPTANCE = "REQUIRES_ACCEPTANCE"
    """The seller must accept requests to complete bookings."""

    __str__ = str.__str__


BusinessBookingProfileBookingPolicyOrStr: TypeAlias = Annotated[
    BusinessBookingProfileBookingPolicy | str, open_enum_validator(BusinessBookingProfileBookingPolicy)
]
