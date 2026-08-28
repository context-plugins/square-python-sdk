from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ChangeTiming(str, Enum):
    """Supported timings when a pending change, as an action, takes place to a subscription."""

    IMMEDIATE = "IMMEDIATE"
    """The action occurs immediately."""

    END_OF_BILLING_CYCLE = "END_OF_BILLING_CYCLE"
    """The action occurs at the end of the billing cycle."""

    __str__ = str.__str__


ChangeTimingOrStr: TypeAlias = Annotated[ChangeTiming | str, open_enum_validator(ChangeTiming)]
