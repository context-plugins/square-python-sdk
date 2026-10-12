from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_upsert_location_custom_attributes_response_location_custom_attribute_upsert_response import (
    BulkUpsertLocationCustomAttributesResponseLocationCustomAttributeUpsertResponse,
    BulkUpsertLocationCustomAttributesResponseLocationCustomAttributeUpsertResponseDict,
)
from .error import Error, ErrorDict


class BulkUpsertLocationCustomAttributesResponse(SdkBaseModel):
    """Represents a `BulkUpsertLocationCustomAttributes
    <api-endpoint:LocationCustomAttributes-BulkUpsertLocationCustomAttributes>`__ response, which contains a map of
    responses that each corresponds to an individual upsert request."""

    values: Optional[dict[str, BulkUpsertLocationCustomAttributesResponseLocationCustomAttributeUpsertResponse]] = UNSET
    """A map of responses that correspond to individual upsert requests. Each response has the same ID as the
    corresponding request and contains either a ``location_id`` and ``custom_attribute`` or an ``errors`` field."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class BulkUpsertLocationCustomAttributesResponseDict(TypedDict):
    values: NotRequired[dict[str, BulkUpsertLocationCustomAttributesResponseLocationCustomAttributeUpsertResponseDict]]
    errors: NotRequired[list[ErrorDict]]
