from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessAppointmentSettingsMaxAppointmentsPerDayLimitType(str, Enum):
    """Types of daily appointment limits."""

    PER_TEAM_MEMBER = "PER_TEAM_MEMBER"
    """The maximum number of daily appointments is set on a per team member basis."""

    PER_LOCATION = "PER_LOCATION"
    """The maximum number of daily appointments is set on a per location basis."""

    __str__ = str.__str__


BusinessAppointmentSettingsMaxAppointmentsPerDayLimitTypeOrStr: TypeAlias = Annotated[
    BusinessAppointmentSettingsMaxAppointmentsPerDayLimitType | str,
    open_enum_validator(BusinessAppointmentSettingsMaxAppointmentsPerDayLimitType),
]
