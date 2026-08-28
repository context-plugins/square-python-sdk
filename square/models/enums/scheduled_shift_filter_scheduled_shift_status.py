from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ScheduledShiftFilterScheduledShiftStatus(str, Enum):
    """Defines valid values for the ``scheduled_shift_statuses`` filter in a `SearchScheduledShifts
    <api-endpoint:Labor-SearchScheduledShifts>`__ request."""

    DRAFT = "DRAFT"
    """The scheduled shift has never been published or its draft details were updated after it was published. This means
    that the shift has no ``published_shift_details`` field or that ``draft_shift_details`` has different settings than
    ``published_shift_details``."""

    PUBLISHED = "PUBLISHED"
    """The scheduled shift was published. This means that the shift has a ``published_shift_details`` field."""

    __str__ = str.__str__


ScheduledShiftFilterScheduledShiftStatusOrStr: TypeAlias = Annotated[
    ScheduledShiftFilterScheduledShiftStatus | str, open_enum_validator(ScheduledShiftFilterScheduledShiftStatus)
]
