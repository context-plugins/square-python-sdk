from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .card_forgotten_event_object import CardForgottenEventObject, CardForgottenEventObjectDict


class CardForgottenEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the event data object. The value is ``"card"``."""

    id: Optional[str] = UNSET
    """The ID of the event data object."""

    object_: Optional[CardForgottenEventObject] = Field(default=UNSET, alias="object")


class CardForgottenEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[CardForgottenEventObject | CardForgottenEventObjectDict]
