from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_upsert_order_custom_attributes_request_upsert_custom_attribute import (
    BulkUpsertOrderCustomAttributesRequestUpsertCustomAttribute,
    BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeDict,
)


class BulkUpsertOrderCustomAttributesRequest(SdkBaseModel):
    """Represents a bulk upsert request for one or more order custom attributes."""

    values: dict[str, BulkUpsertOrderCustomAttributesRequestUpsertCustomAttribute]
    """A map of requests that correspond to individual upsert operations for custom attributes."""


class BulkUpsertOrderCustomAttributesRequestDict(TypedDict):
    values: dict[str, BulkUpsertOrderCustomAttributesRequestUpsertCustomAttributeDict]
