from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class FulfillmentPickupDetailsCurbsidePickupDetails(SdkBaseModel):
    """Specific details for curbside pickup."""

    curbside_details: OptionalNullable[str] = UNSET
    """Specific details for curbside pickup, such as parking number and vehicle model."""

    buyer_arrived_at: OptionalNullable[str] = UNSET
    """The `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ indicating when the buyer
    arrived and is waiting for pickup. The timestamp must be in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z")."""


class FulfillmentPickupDetailsCurbsidePickupDetailsDict(TypedDict):
    curbside_details: NotRequired[str | None]
    buyer_arrived_at: NotRequired[str | None]
