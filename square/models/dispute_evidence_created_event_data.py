from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dispute_evidence_created_event_object import (
    DisputeEvidenceCreatedEventObject,
    DisputeEvidenceCreatedEventObjectDict,
)


class DisputeEvidenceCreatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected dispute's type."""

    id: Optional[str] = UNSET
    """ID of the affected dispute."""

    object_: Optional[DisputeEvidenceCreatedEventObject] = Field(default=UNSET, alias="object")


class DisputeEvidenceCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[DisputeEvidenceCreatedEventObject | DisputeEvidenceCreatedEventObjectDict]
