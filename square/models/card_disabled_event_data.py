from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .card_disabled_event_object import CardDisabledEventObject, CardDisabledEventObjectDict


class CardDisabledEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the event data object. The value is ``"card"``."""

    id: Optional[str] = UNSET
    """The ID of the event data object."""

    object_: Optional[CardDisabledEventObject] = Field(default=UNSET, alias="object")


class CardDisabledEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[CardDisabledEventObjectDict]
