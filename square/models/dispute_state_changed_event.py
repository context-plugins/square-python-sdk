from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dispute_state_changed_event_data import DisputeStateChangedEventData, DisputeStateChangedEventDataDict


class DisputeStateChangedEvent(SdkBaseModel):
    """Published when the state of a `Dispute <entity:Dispute>`__ changes. This includes the dispute resolution (WON,
    LOST) reported by the bank. The event data includes details of what changed."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the target location associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[DisputeStateChangedEventData] = UNSET


class DisputeStateChangedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[DisputeStateChangedEventDataDict]
