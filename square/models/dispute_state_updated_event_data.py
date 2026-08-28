from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dispute_state_updated_event_object import DisputeStateUpdatedEventObject, DisputeStateUpdatedEventObjectDict


class DisputeStateUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected dispute's type."""

    id: Optional[str] = UNSET
    """ID of the affected dispute."""

    object_: Optional[DisputeStateUpdatedEventObject] = Field(default=UNSET, alias="object")


class DisputeStateUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[DisputeStateUpdatedEventObject | DisputeStateUpdatedEventObjectDict]
