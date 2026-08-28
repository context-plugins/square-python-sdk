from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .terminal_action_updated_event_object import TerminalActionUpdatedEventObject, TerminalActionUpdatedEventObjectDict


class TerminalActionUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the updated object’s type, ``"action"``."""

    id: Optional[str] = UNSET
    """ID of the updated terminal action."""

    object_: Optional[TerminalActionUpdatedEventObject] = Field(default=UNSET, alias="object")


class TerminalActionUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TerminalActionUpdatedEventObject | TerminalActionUpdatedEventObjectDict]
