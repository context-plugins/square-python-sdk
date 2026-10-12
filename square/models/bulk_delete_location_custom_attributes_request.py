from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_delete_location_custom_attributes_request_location_custom_attribute_delete_request import (
    BulkDeleteLocationCustomAttributesRequestLocationCustomAttributeDeleteRequest,
    BulkDeleteLocationCustomAttributesRequestLocationCustomAttributeDeleteRequestDict,
)


class BulkDeleteLocationCustomAttributesRequest(SdkBaseModel):
    """Represents a `BulkDeleteLocationCustomAttributes
    <api-endpoint:LocationCustomAttributes-BulkDeleteLocationCustomAttributes>`__ request."""

    values: dict[str, BulkDeleteLocationCustomAttributesRequestLocationCustomAttributeDeleteRequest]
    """The data used to update the ``CustomAttribute`` objects. The keys must be unique and are used to map to the
    corresponding response."""


class BulkDeleteLocationCustomAttributesRequestDict(TypedDict):
    values: dict[str, BulkDeleteLocationCustomAttributesRequestLocationCustomAttributeDeleteRequestDict]
