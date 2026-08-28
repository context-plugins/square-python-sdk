from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TeamMemberBookingProfile(SdkBaseModel):
    """The booking profile of a seller's team member, including the team member's ID, display name, description and
    whether the team member can be booked as a service provider."""

    team_member_id: Optional[str] = UNSET
    """The ID of the `TeamMember <entity:TeamMember>`__ object for the team member associated with the booking
    profile."""

    description: Optional[str] = UNSET
    """The description of the team member."""

    display_name: Optional[str] = UNSET
    """The display name of the team member."""

    is_bookable: OptionalNullable[bool] = UNSET
    """Indicates whether the team member can be booked through the Bookings API or the seller's online booking channel
    or site (``true``) or not (``false``)."""

    profile_image_url: Optional[str] = UNSET
    """The URL of the team member's image for the bookings profile."""


class TeamMemberBookingProfileDict(TypedDict):
    team_member_id: NotRequired[str]
    description: NotRequired[str]
    display_name: NotRequired[str]
    is_bookable: NotRequired[bool | None]
    profile_image_url: NotRequired[str]
