from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .terminal_action_updated_event_data import TerminalActionUpdatedEventData, TerminalActionUpdatedEventDataDict


class TerminalActionUpdatedEvent(SdkBaseModel):
    """Published when a TerminalAction is updated."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"terminal.action.updated"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """RFC 3339 timestamp of when the event was created."""

    data: Optional[TerminalActionUpdatedEventData] = UNSET


class TerminalActionUpdatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[TerminalActionUpdatedEventData | TerminalActionUpdatedEventDataDict]
