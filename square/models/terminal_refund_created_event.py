from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .terminal_refund_created_event_data import TerminalRefundCreatedEventData, TerminalRefundCreatedEventDataDict


class TerminalRefundCreatedEvent(SdkBaseModel):
    """Published when a Terminal API refund is created."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"terminal.refund.created"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """RFC 3339 timestamp of when the event was created."""

    data: Optional[TerminalRefundCreatedEventData] = UNSET


class TerminalRefundCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[TerminalRefundCreatedEventDataDict]
