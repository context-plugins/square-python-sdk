from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BulkRetrieveBookingsRequest(SdkBaseModel):
    """Request payload for bulk retrieval of bookings."""

    booking_ids: list[str]
    """A non-empty list of `Booking <entity:Booking>`__ IDs specifying bookings to retrieve."""


class BulkRetrieveBookingsRequestDict(TypedDict):
    booking_ids: list[str]
