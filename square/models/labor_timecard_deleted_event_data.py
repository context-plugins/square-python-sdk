from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class LaborTimecardDeletedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of object affected by the event. For this event, the value is ``timecard``."""

    id: Optional[str] = UNSET
    """The ID of the affected ``Timecard``."""

    deleted: OptionalNullable[bool] = UNSET
    """Is true if the affected object was deleted. Otherwise absent."""


class LaborTimecardDeletedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    deleted: NotRequired[bool | None]
