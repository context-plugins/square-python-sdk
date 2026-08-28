from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .terminal_checkout_created_event_object import (
    TerminalCheckoutCreatedEventObject,
    TerminalCheckoutCreatedEventObjectDict,
)


class TerminalCheckoutCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the created object’s type, ``"checkout"``."""

    id: Optional[str] = UNSET
    """ID of the created terminal checkout."""

    object_: Optional[TerminalCheckoutCreatedEventObject] = Field(default=UNSET, alias="object")


class TerminalCheckoutCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TerminalCheckoutCreatedEventObject | TerminalCheckoutCreatedEventObjectDict]
