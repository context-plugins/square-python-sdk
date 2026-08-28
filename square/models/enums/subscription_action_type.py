from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionActionType(str, Enum):
    """Supported types of an action as a pending change to a subscription."""

    CANCEL = "CANCEL"
    """The action to execute a scheduled cancellation of a subscription."""

    PAUSE = "PAUSE"
    """The action to execute a scheduled pause of a subscription."""

    RESUME = "RESUME"
    """The action to execute a scheduled resumption of a subscription."""

    SWAP_PLAN = "SWAP_PLAN"
    """The action to execute a scheduled swap of a subscription plan in a subscription."""

    CHANGE_BILLING_ANCHOR_DATE = "CHANGE_BILLING_ANCHOR_DATE"
    """A billing anchor date change action."""

    COMPLETE = "COMPLETE"
    """The action marking when a subscription completes a fixed number of phases."""

    __str__ = str.__str__


SubscriptionActionTypeOrStr: TypeAlias = Annotated[
    SubscriptionActionType | str, open_enum_validator(SubscriptionActionType)
]
