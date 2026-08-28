from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.change_timing import ChangeTimingOrStr


class ResumeSubscriptionRequest(SdkBaseModel):
    """Defines input parameters in a request to the `ResumeSubscription
    <api-endpoint:Subscriptions-ResumeSubscription>`__ endpoint."""

    resume_effective_date: OptionalNullable[str] = UNSET
    """The ``YYYY-MM-DD``-formatted date when the subscription reactivated."""

    resume_change_timing: Optional[ChangeTimingOrStr] = UNSET
    """Supported timings when a pending change, as an action, takes place to a subscription."""


class ResumeSubscriptionRequestDict(TypedDict):
    resume_effective_date: NotRequired[str | None]
    resume_change_timing: NotRequired[ChangeTimingOrStr]
