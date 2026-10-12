from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .booking_custom_attribute_delete_response import (
    BookingCustomAttributeDeleteResponse,
    BookingCustomAttributeDeleteResponseDict,
)
from .error import Error, ErrorDict


class BulkDeleteBookingCustomAttributesResponse(SdkBaseModel):
    """Represents a `BulkDeleteBookingCustomAttributes
    <api-endpoint:BookingCustomAttributes-BulkDeleteBookingCustomAttributes>`__ response, which contains a map of
    responses that each corresponds to an individual delete request."""

    values: Optional[dict[str, BookingCustomAttributeDeleteResponse]] = UNSET
    """A map of responses that correspond to individual delete requests. Each response has the same ID as the
    corresponding request and contains ``booking_id`` and ``errors`` field."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class BulkDeleteBookingCustomAttributesResponseDict(TypedDict):
    values: NotRequired[dict[str, BookingCustomAttributeDeleteResponseDict]]
    errors: NotRequired[list[ErrorDict]]
