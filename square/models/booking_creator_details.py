from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.booking_creator_details_creator_type import BookingCreatorDetailsCreatorTypeOrStr


class BookingCreatorDetails(SdkBaseModel):
    """Information about a booking creator."""

    creator_type: Optional[BookingCreatorDetailsCreatorTypeOrStr] = UNSET
    """Supported types of a booking creator."""

    team_member_id: Optional[str] = UNSET
    """The ID of the team member who created the booking, when the booking creator is of the ``TEAM_MEMBER`` type.
    Access to this field requires seller-level permissions."""

    customer_id: Optional[str] = UNSET
    """The ID of the customer who created the booking, when the booking creator is of the ``CUSTOMER`` type. Access to
    this field requires seller-level permissions."""


class BookingCreatorDetailsDict(TypedDict):
    creator_type: NotRequired[BookingCreatorDetailsCreatorTypeOrStr]
    team_member_id: NotRequired[str]
    customer_id: NotRequired[str]
