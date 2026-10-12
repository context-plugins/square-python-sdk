from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.subscription_event_subscription_event_type import SubscriptionEventSubscriptionEventTypeOrStr
from .phase import Phase, PhaseDict
from .subscription_event_info import SubscriptionEventInfo, SubscriptionEventInfoDict


class SubscriptionEvent(SdkBaseModel):
    """Describes changes to a subscription and the subscription status."""

    id: str
    """The ID of the subscription event."""

    subscription_event_type: SubscriptionEventSubscriptionEventTypeOrStr
    """Supported types of an event occurred to a subscription."""

    effective_date: str
    """The ``YYYY-MM-DD``-formatted date (for example, 2013-01-15) when the subscription event occurred."""

    monthly_billing_anchor_date: Optional[int] = UNSET
    """The day-of-the-month the billing anchor date was changed to, if applicable."""

    info: Optional[SubscriptionEventInfo] = UNSET
    """Provides information about the subscription event."""

    phases: OptionalNullable[list[Phase]] = UNSET
    """A list of Phases, to pass phase-specific information used in the swap."""

    plan_variation_id: str
    """The ID of the subscription plan variation associated with the subscription."""


class SubscriptionEventDict(TypedDict):
    id: str
    subscription_event_type: SubscriptionEventSubscriptionEventTypeOrStr
    effective_date: str
    monthly_billing_anchor_date: NotRequired[int]
    info: NotRequired[SubscriptionEventInfoDict]
    phases: NotRequired[list[PhaseDict] | None]
    plan_variation_id: str
