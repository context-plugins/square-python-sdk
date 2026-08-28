from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .labor_shift_created_event_data import LaborShiftCreatedEventData, LaborShiftCreatedEventDataDict


class LaborShiftCreatedEvent(SdkBaseModel):
    """Published when a worker starts a `Shift <entity:Shift>`__.

    Deprecated at Square API version 2025-05-21. Replaced by ``labor.timecard.created``."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event. For this event, the value is ``labor.shift.created``."""

    event_id: OptionalNullable[str] = UNSET
    """The unique ID for the event."""

    created_at: Optional[str] = UNSET
    """The timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[LaborShiftCreatedEventData] = UNSET


class LaborShiftCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[LaborShiftCreatedEventData | LaborShiftCreatedEventDataDict]
