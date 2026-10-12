from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scheduled_shift import ScheduledShift, ScheduledShiftDict


class CreateScheduledShiftRequest(SdkBaseModel):
    """Represents a `CreateScheduledShift <api-endpoint:Labor-CreateScheduledShift>`__ request."""

    idempotency_key: Optional[str] = UNSET
    """A unique identifier for the ``CreateScheduledShift`` request, used to ensure the `idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ of the operation."""

    scheduled_shift: ScheduledShift
    """Represents a specific time slot in a work schedule. This object is used to manage the lifecycle of a scheduled
    shift from the draft to published state. A scheduled shift contains the latest draft shift details and current
    published shift details."""


class CreateScheduledShiftRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    scheduled_shift: ScheduledShiftDict
