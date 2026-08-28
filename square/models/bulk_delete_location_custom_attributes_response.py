from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_delete_location_custom_attributes_response_location_custom_attribute_delete_response import (
    BulkDeleteLocationCustomAttributesResponseLocationCustomAttributeDeleteResponse,
    BulkDeleteLocationCustomAttributesResponseLocationCustomAttributeDeleteResponseDict,
)
from .error import Error, ErrorDict


class BulkDeleteLocationCustomAttributesResponse(SdkBaseModel):
    """Represents a `BulkDeleteLocationCustomAttributes
    <api-endpoint:LocationCustomAttributes-BulkDeleteLocationCustomAttributes>`__ response, which contains a map of
    responses that each corresponds to an individual delete request."""

    values: dict[str, BulkDeleteLocationCustomAttributesResponseLocationCustomAttributeDeleteResponse]
    """A map of responses that correspond to individual delete requests. Each response has the same key as the
    corresponding request."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class BulkDeleteLocationCustomAttributesResponseDict(TypedDict):
    values: dict[
        str,
        (
            BulkDeleteLocationCustomAttributesResponseLocationCustomAttributeDeleteResponse
            | BulkDeleteLocationCustomAttributesResponseLocationCustomAttributeDeleteResponseDict
        ),
    ]
    errors: NotRequired[list[Error | ErrorDict]]
