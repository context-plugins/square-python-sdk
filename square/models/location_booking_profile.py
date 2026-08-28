from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class LocationBookingProfile(SdkBaseModel):
    """The booking profile of a seller's location, including the location's ID and whether the location is enabled for
    online booking."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the `location <entity:Location>`__."""

    booking_site_url: OptionalNullable[str] = UNSET
    """Url for the online booking site for this location."""

    online_booking_enabled: OptionalNullable[bool] = UNSET
    """Indicates whether the location is enabled for online booking."""


class LocationBookingProfileDict(TypedDict):
    location_id: NotRequired[str | None]
    booking_site_url: NotRequired[str | None]
    online_booking_enabled: NotRequired[bool | None]
