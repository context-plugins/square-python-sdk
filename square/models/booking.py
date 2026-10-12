from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict
from .appointment_segment import AppointmentSegment, AppointmentSegmentDict
from .booking_creator_details import BookingCreatorDetails, BookingCreatorDetailsDict
from .enums.booking_booking_source import BookingBookingSourceOrStr
from .enums.booking_status import BookingStatusOrStr
from .enums.business_appointment_settings_booking_location_type import (
    BusinessAppointmentSettingsBookingLocationTypeOrStr,
)


class Booking(SdkBaseModel):
    """Represents a booking as a time-bound service contract for a seller's staff member to provide a specified service
    at a given location to a requesting customer in one or more appointment segments."""

    id: Optional[str] = UNSET
    """A unique ID of this object representing a booking."""

    version: Optional[int] = UNSET
    """The revision number for the booking used for optimistic concurrency."""

    status: Optional[BookingStatusOrStr] = UNSET
    """Supported booking statuses."""

    created_at: Optional[str] = UNSET
    """The RFC 3339 timestamp specifying the creation time of this booking."""

    updated_at: Optional[str] = UNSET
    """The RFC 3339 timestamp specifying the most recent update time of this booking."""

    start_at: OptionalNullable[str] = UNSET
    """The RFC 3339 timestamp specifying the starting time of this booking."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the `Location <entity:Location>`__ object representing the location where the booked service is
    provided. Once set when the booking is created, its value cannot be changed."""

    customer_id: OptionalNullable[str] = UNSET
    """The ID of the `Customer <entity:Customer>`__ object representing the customer receiving the booked service."""

    customer_note: OptionalNullable[str] = UNSET
    """The free-text field for the customer to supply notes about the booking. For example, the note can be preferences
    that cannot be expressed by supported attributes of a relevant `CatalogObject <entity:CatalogObject>`__ instance."""

    seller_note: OptionalNullable[str] = UNSET
    """The free-text field for the seller to supply notes about the booking. For example, the note can be preferences
    that cannot be expressed by supported attributes of a specific `CatalogObject <entity:CatalogObject>`__ instance.
    This field should not be visible to customers."""

    appointment_segments: OptionalNullable[list[AppointmentSegment]] = UNSET
    """A list of appointment segments for this booking."""

    transition_time_minutes: Optional[int] = UNSET
    """Additional time at the end of a booking. Applications should not make this field visible to customers of a
    seller."""

    all_day: Optional[bool] = UNSET
    """Whether the booking is of a full business day."""

    location_type: Optional[BusinessAppointmentSettingsBookingLocationTypeOrStr] = UNSET
    """Supported types of location where service is provided."""

    creator_details: Optional[BookingCreatorDetails] = UNSET
    """Information about a booking creator."""

    source: Optional[BookingBookingSourceOrStr] = UNSET
    """Supported sources a booking was created from."""

    address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""


class BookingDict(TypedDict):
    id: NotRequired[str]
    version: NotRequired[int]
    status: NotRequired[BookingStatusOrStr]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    start_at: NotRequired[str | None]
    location_id: NotRequired[str | None]
    customer_id: NotRequired[str | None]
    customer_note: NotRequired[str | None]
    seller_note: NotRequired[str | None]
    appointment_segments: NotRequired[list[AppointmentSegmentDict] | None]
    transition_time_minutes: NotRequired[int]
    all_day: NotRequired[bool]
    location_type: NotRequired[BusinessAppointmentSettingsBookingLocationTypeOrStr]
    creator_details: NotRequired[BookingCreatorDetailsDict]
    source: NotRequired[BookingBookingSourceOrStr]
    address: NotRequired[AddressDict]
