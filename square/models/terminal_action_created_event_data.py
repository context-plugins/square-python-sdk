from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .terminal_action_created_event_object import TerminalActionCreatedEventObject, TerminalActionCreatedEventObjectDict


class TerminalActionCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the created object’s type, ``"action"``."""

    id: Optional[str] = UNSET
    """ID of the created terminal action."""

    object_: Optional[TerminalActionCreatedEventObject] = Field(default=UNSET, alias="object")


class TerminalActionCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TerminalActionCreatedEventObjectDict]
