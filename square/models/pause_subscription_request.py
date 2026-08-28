from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.change_timing import ChangeTimingOrStr


class PauseSubscriptionRequest(SdkBaseModel):
    """Defines input parameters in a request to the `PauseSubscription <api-endpoint:Subscriptions-PauseSubscription>`__
    endpoint."""

    pause_effective_date: OptionalNullable[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date when the scheduled ``PAUSE`` action takes place on the subscription.

    When this date is unspecified or falls within the current billing cycle, the subscription is paused on the starting
    date of the next billing cycle."""

    pause_cycle_duration: OptionalNullable[int] = UNSET
    """The number of billing cycles the subscription will be paused before it is reactivated.

    When this is set, a ``RESUME`` action is also scheduled to take place on the subscription at the end of the
    specified pause cycle duration. In this case, neither ``resume_effective_date`` nor ``resume_change_timing`` may be
    specified."""

    resume_effective_date: OptionalNullable[str] = UNSET
    """The date when the subscription is reactivated by a scheduled ``RESUME`` action. This date must be at least one
    billing cycle ahead of ``pause_effective_date``."""

    resume_change_timing: Optional[ChangeTimingOrStr] = UNSET
    """Supported timings when a pending change, as an action, takes place to a subscription."""

    pause_reason: OptionalNullable[str] = UNSET
    """The user-provided reason to pause the subscription."""


class PauseSubscriptionRequestDict(TypedDict):
    pause_effective_date: NotRequired[str | None]
    pause_cycle_duration: NotRequired[int | None]
    resume_effective_date: NotRequired[str | None]
    resume_change_timing: NotRequired[ChangeTimingOrStr]
    pause_reason: NotRequired[str | None]
