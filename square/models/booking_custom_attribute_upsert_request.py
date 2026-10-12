from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict


class BookingCustomAttributeUpsertRequest(SdkBaseModel):
    """Represents an individual upsert request in a `BulkUpsertBookingCustomAttributes
    <api-endpoint:BookingCustomAttributes-BulkUpsertBookingCustomAttributes>`__ request. An individual request contains
    a booking ID, the custom attribute to create or update, and an optional idempotency key."""

    booking_id: str
    """The ID of the target `booking <entity:Booking>`__."""

    custom_attribute: CustomAttribute
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A unique identifier for this individual upsert request, used to ensure idempotency. For more information, see
    `Idempotency <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class BookingCustomAttributeUpsertRequestDict(TypedDict):
    booking_id: str
    custom_attribute: CustomAttributeDict
    idempotency_key: NotRequired[str | None]
