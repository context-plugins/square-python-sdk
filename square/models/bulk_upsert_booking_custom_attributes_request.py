from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .booking_custom_attribute_upsert_request import (
    BookingCustomAttributeUpsertRequest,
    BookingCustomAttributeUpsertRequestDict,
)


class BulkUpsertBookingCustomAttributesRequest(SdkBaseModel):
    """Represents a `BulkUpsertBookingCustomAttributes
    <api-endpoint:BookingCustomAttributes-BulkUpsertBookingCustomAttributes>`__ request."""

    values: dict[str, BookingCustomAttributeUpsertRequest]
    """A map containing 1 to 25 individual upsert requests. For each request, provide an arbitrary ID that is unique for
    this ``BulkUpsertBookingCustomAttributes`` request and the information needed to create or update a custom
    attribute."""


class BulkUpsertBookingCustomAttributesRequestDict(TypedDict):
    values: dict[str, BookingCustomAttributeUpsertRequestDict]
