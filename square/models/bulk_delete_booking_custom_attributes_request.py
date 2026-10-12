from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .booking_custom_attribute_delete_request import (
    BookingCustomAttributeDeleteRequest,
    BookingCustomAttributeDeleteRequestDict,
)


class BulkDeleteBookingCustomAttributesRequest(SdkBaseModel):
    """Represents a `BulkDeleteBookingCustomAttributes
    <api-endpoint:BookingCustomAttributes-BulkDeleteBookingCustomAttributes>`__ request."""

    values: dict[str, BookingCustomAttributeDeleteRequest]
    """A map containing 1 to 25 individual Delete requests. For each request, provide an arbitrary ID that is unique for
    this ``BulkDeleteBookingCustomAttributes`` request and the information needed to delete a custom attribute."""


class BulkDeleteBookingCustomAttributesRequestDict(TypedDict):
    values: dict[str, BookingCustomAttributeDeleteRequestDict]
