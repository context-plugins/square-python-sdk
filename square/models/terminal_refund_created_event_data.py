from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .terminal_refund_created_event_object import TerminalRefundCreatedEventObject, TerminalRefundCreatedEventObjectDict


class TerminalRefundCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the created object’s type, ``"refund"``."""

    id: Optional[str] = UNSET
    """ID of the created terminal refund."""

    object_: Optional[TerminalRefundCreatedEventObject] = Field(default=UNSET, alias="object")


class TerminalRefundCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TerminalRefundCreatedEventObject | TerminalRefundCreatedEventObjectDict]
