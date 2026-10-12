from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .dispute_evidence_created_event_data import DisputeEvidenceCreatedEventData, DisputeEvidenceCreatedEventDataDict


class DisputeEvidenceCreatedEvent(SdkBaseModel):
    """Published when evidence is added to a `Dispute <entity:Dispute>`__ from the Disputes Dashboard in the Seller
    Dashboard, the Square Point of Sale app, or by calling either `CreateDisputeEvidenceFile
    <api-endpoint:Disputes-CreateDisputeEvidenceFile>`__ or `CreateDisputeEvidenceText
    <api-endpoint:Disputes-CreateDisputeEvidenceText>`__."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the target location associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[DisputeEvidenceCreatedEventData] = UNSET


class DisputeEvidenceCreatedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[DisputeEvidenceCreatedEventDataDict]
