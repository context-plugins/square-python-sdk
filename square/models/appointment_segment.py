from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class AppointmentSegment(SdkBaseModel):
    """Defines an appointment segment of a booking."""

    duration_minutes: OptionalNullable[int] = UNSET
    """The time span in minutes of an appointment segment."""

    service_variation_id: OptionalNullable[str] = UNSET
    """The ID of the `CatalogItemVariation <entity:CatalogItemVariation>`__ object representing the service booked in
    this segment."""

    team_member_id: str
    """The ID of the `TeamMember <entity:TeamMember>`__ object representing the team member booked in this segment."""

    service_variation_version: OptionalNullable[int] = UNSET
    """The current version of the item variation representing the service booked in this segment."""

    intermission_minutes: Optional[int] = UNSET
    """Time between the end of this segment and the beginning of the subsequent segment."""

    any_team_member: Optional[bool] = UNSET
    """Whether the customer accepts any team member, instead of a specific one, to serve this segment."""

    resource_ids: Optional[list[str]] = UNSET
    """The IDs of the seller-accessible resources used for this appointment segment."""


class AppointmentSegmentDict(TypedDict):
    duration_minutes: NotRequired[int | None]
    service_variation_id: NotRequired[str | None]
    team_member_id: str
    service_variation_version: NotRequired[int | None]
    intermission_minutes: NotRequired[int]
    any_team_member: NotRequired[bool]
    resource_ids: NotRequired[list[str]]
