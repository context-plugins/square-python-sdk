from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionStatus(str, Enum):
    """Supported subscription statuses."""

    PENDING = "PENDING"
    """The subscription is pending to start in the future."""

    ACTIVE = "ACTIVE"
    """The subscription is active."""

    CANCELED = "CANCELED"
    """The subscription is canceled."""

    DEACTIVATED = "DEACTIVATED"
    """The subscription is deactivated."""

    PAUSED = "PAUSED"
    """The subscription is paused."""

    COMPLETED = "COMPLETED"
    """The subscription has completed all of its phases."""

    __str__ = str.__str__


SubscriptionStatusOrStr: TypeAlias = Annotated[SubscriptionStatus | str, open_enum_validator(SubscriptionStatus)]
