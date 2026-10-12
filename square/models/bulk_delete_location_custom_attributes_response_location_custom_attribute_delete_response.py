from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class BulkDeleteLocationCustomAttributesResponseLocationCustomAttributeDeleteResponse(SdkBaseModel):
    """Represents an individual delete response in a `BulkDeleteLocationCustomAttributes
    <api-endpoint:LocationCustomAttributes-BulkDeleteLocationCustomAttributes>`__ request."""

    location_id: Optional[str] = UNSET
    """The ID of the location associated with the custom attribute."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred while processing the individual LocationCustomAttributeDeleteRequest request"""


class BulkDeleteLocationCustomAttributesResponseLocationCustomAttributeDeleteResponseDict(TypedDict):
    location_id: NotRequired[str]
    errors: NotRequired[list[ErrorDict]]
