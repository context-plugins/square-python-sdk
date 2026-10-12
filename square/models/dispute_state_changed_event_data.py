from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dispute_state_changed_event_object import DisputeStateChangedEventObject, DisputeStateChangedEventObjectDict


class DisputeStateChangedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected dispute's type."""

    id: Optional[str] = UNSET
    """ID of the affected dispute."""

    object_: Optional[DisputeStateChangedEventObject] = Field(default=UNSET, alias="object")


class DisputeStateChangedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[DisputeStateChangedEventObjectDict]
