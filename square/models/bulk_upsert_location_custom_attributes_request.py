from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_upsert_location_custom_attributes_request_location_custom_attribute_upsert_request import (
    BulkUpsertLocationCustomAttributesRequestLocationCustomAttributeUpsertRequest,
    BulkUpsertLocationCustomAttributesRequestLocationCustomAttributeUpsertRequestDict,
)


class BulkUpsertLocationCustomAttributesRequest(SdkBaseModel):
    """Represents a `BulkUpsertLocationCustomAttributes
    <api-endpoint:LocationCustomAttributes-BulkUpsertLocationCustomAttributes>`__ request."""

    values: dict[str, BulkUpsertLocationCustomAttributesRequestLocationCustomAttributeUpsertRequest]
    """A map containing 1 to 25 individual upsert requests. For each request, provide an arbitrary ID that is unique for
    this ``BulkUpsertLocationCustomAttributes`` request and the information needed to create or update a custom
    attribute."""


class BulkUpsertLocationCustomAttributesRequestDict(TypedDict):
    values: dict[str, BulkUpsertLocationCustomAttributesRequestLocationCustomAttributeUpsertRequestDict]
