from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .job_created_event_object import JobCreatedEventObject, JobCreatedEventObjectDict


class JobCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"job"``."""

    id: Optional[str] = UNSET
    """ID of the created job."""

    object_: Optional[JobCreatedEventObject] = Field(default=UNSET, alias="object")


class JobCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[JobCreatedEventObjectDict]
