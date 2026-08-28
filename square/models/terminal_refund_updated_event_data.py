from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .terminal_refund_updated_event_object import TerminalRefundUpdatedEventObject, TerminalRefundUpdatedEventObjectDict


class TerminalRefundUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the updated object’s type, ``"refund"``."""

    id: Optional[str] = UNSET
    """ID of the updated terminal refund."""

    object_: Optional[TerminalRefundUpdatedEventObject] = Field(default=UNSET, alias="object")


class TerminalRefundUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TerminalRefundUpdatedEventObject | TerminalRefundUpdatedEventObjectDict]
