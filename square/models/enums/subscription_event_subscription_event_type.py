from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SubscriptionEventSubscriptionEventType(str, Enum):
    """Supported types of an event occurred to a subscription."""

    START_SUBSCRIPTION = "START_SUBSCRIPTION"
    """The subscription was started."""

    PLAN_CHANGE = "PLAN_CHANGE"
    """The subscription plan was changed."""

    STOP_SUBSCRIPTION = "STOP_SUBSCRIPTION"
    """The subscription was stopped."""

    DEACTIVATE_SUBSCRIPTION = "DEACTIVATE_SUBSCRIPTION"
    """The subscription was deactivated"""

    RESUME_SUBSCRIPTION = "RESUME_SUBSCRIPTION"
    """The subscription was resumed."""

    PAUSE_SUBSCRIPTION = "PAUSE_SUBSCRIPTION"
    """The subscription was paused."""

    BILLING_ANCHOR_DATE_CHANGED = "BILLING_ANCHOR_DATE_CHANGED"
    """The billing anchor date was changed."""

    __str__ = str.__str__


SubscriptionEventSubscriptionEventTypeOrStr: TypeAlias = Annotated[
    SubscriptionEventSubscriptionEventType | str, open_enum_validator(SubscriptionEventSubscriptionEventType)
]
