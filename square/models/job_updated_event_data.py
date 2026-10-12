from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .job_updated_event_object import JobUpdatedEventObject, JobUpdatedEventObjectDict


class JobUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"job"``."""

    id: Optional[str] = UNSET
    """ID of the updated job."""

    object_: Optional[JobUpdatedEventObject] = Field(default=UNSET, alias="object")


class JobUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[JobUpdatedEventObjectDict]
