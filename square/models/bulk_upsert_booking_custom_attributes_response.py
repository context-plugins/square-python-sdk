from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .booking_custom_attribute_upsert_response import (
    BookingCustomAttributeUpsertResponse,
    BookingCustomAttributeUpsertResponseDict,
)
from .error import Error, ErrorDict


class BulkUpsertBookingCustomAttributesResponse(SdkBaseModel):
    """Represents a `BulkUpsertBookingCustomAttributes
    <api-endpoint:BookingCustomAttributes-BulkUpsertBookingCustomAttributes>`__ response, which contains a map of
    responses that each corresponds to an individual upsert request."""

    values: Optional[dict[str, BookingCustomAttributeUpsertResponse]] = UNSET
    """A map of responses that correspond to individual upsert requests. Each response has the same ID as the
    corresponding request and contains either a ``booking_id`` and ``custom_attribute`` or an ``errors`` field."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class BulkUpsertBookingCustomAttributesResponseDict(TypedDict):
    values: NotRequired[dict[str, BookingCustomAttributeUpsertResponse | BookingCustomAttributeUpsertResponseDict]]
    errors: NotRequired[list[Error | ErrorDict]]
