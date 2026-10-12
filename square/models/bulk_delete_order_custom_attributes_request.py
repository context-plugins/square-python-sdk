from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_delete_order_custom_attributes_request_delete_custom_attribute import (
    BulkDeleteOrderCustomAttributesRequestDeleteCustomAttribute,
    BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeDict,
)


class BulkDeleteOrderCustomAttributesRequest(SdkBaseModel):
    """Represents a bulk delete request for one or more order custom attributes."""

    values: dict[str, BulkDeleteOrderCustomAttributesRequestDeleteCustomAttribute]
    """A map of requests that correspond to individual delete operations for custom attributes."""


class BulkDeleteOrderCustomAttributesRequestDict(TypedDict):
    values: dict[str, BulkDeleteOrderCustomAttributesRequestDeleteCustomAttributeDict]
