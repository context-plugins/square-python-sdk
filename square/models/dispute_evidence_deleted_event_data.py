from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dispute_evidence_deleted_event_object import (
    DisputeEvidenceDeletedEventObject,
    DisputeEvidenceDeletedEventObjectDict,
)


class DisputeEvidenceDeletedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected dispute's type."""

    id: Optional[str] = UNSET
    """ID of the affected dispute."""

    object_: Optional[DisputeEvidenceDeletedEventObject] = Field(default=UNSET, alias="object")


class DisputeEvidenceDeletedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[DisputeEvidenceDeletedEventObjectDict]
