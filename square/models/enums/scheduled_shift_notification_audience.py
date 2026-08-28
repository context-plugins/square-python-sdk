from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScheduledShiftNotificationAudience(str, Enum):
    """Indicates whether Square sends an email notification to team members when a scheduled shift is published and
    which team members receive the notification."""

    ALL = "ALL"
    """Notify all active team members. Note that republishing an unchanged shift with this setting resends the
    notification."""

    AFFECTED = "AFFECTED"
    """Notify the team member assigned to the shift. If the shift assignment changes, notify both the newly assigned and
    previously assigned team members."""

    NONE = "NONE"
    """Do not send a notification."""

    __str__ = str.__str__


ScheduledShiftNotificationAudienceOrStr: TypeAlias = Annotated[
    ScheduledShiftNotificationAudience | str, open_enum_validator(ScheduledShiftNotificationAudience)
]
