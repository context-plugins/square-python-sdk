from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .loyalty_program_updated_event_object import LoyaltyProgramUpdatedEventObject, LoyaltyProgramUpdatedEventObjectDict


class LoyaltyProgramUpdatedEventData(SdkBaseModel):
    """The data associated with a ``loyalty.program.updated`` event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``loyalty_program``."""

    id: Optional[str] = UNSET
    """The ID of the affected loyalty program."""

    object_: Optional[LoyaltyProgramUpdatedEventObject] = Field(default=UNSET, alias="object")
    """An object that contains the loyalty program associated with a ``loyalty.program.updated`` event."""


class LoyaltyProgramUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[LoyaltyProgramUpdatedEventObjectDict]
