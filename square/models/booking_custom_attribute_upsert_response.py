from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict
from .error import Error, ErrorDict


class BookingCustomAttributeUpsertResponse(SdkBaseModel):
    """Represents a response for an individual upsert request in a `BulkUpsertBookingCustomAttributes
    <api-endpoint:BookingCustomAttributes-BulkUpsertBookingCustomAttributes>`__ operation."""

    booking_id: Optional[str] = UNSET
    """The ID of the `booking <entity:Booking>`__ associated with the custom attribute."""

    custom_attribute: Optional[CustomAttribute] = UNSET
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred while processing the individual request."""


class BookingCustomAttributeUpsertResponseDict(TypedDict):
    booking_id: NotRequired[str]
    custom_attribute: NotRequired[CustomAttributeDict]
    errors: NotRequired[list[ErrorDict]]
