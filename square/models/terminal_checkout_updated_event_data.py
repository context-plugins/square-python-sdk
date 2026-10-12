from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .terminal_checkout_updated_event_object import (
    TerminalCheckoutUpdatedEventObject,
    TerminalCheckoutUpdatedEventObjectDict,
)


class TerminalCheckoutUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the updated object’s type, ``"checkout"``."""

    id: Optional[str] = UNSET
    """ID of the updated terminal checkout."""

    object_: Optional[TerminalCheckoutUpdatedEventObject] = Field(default=UNSET, alias="object")


class TerminalCheckoutUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[TerminalCheckoutUpdatedEventObjectDict]
