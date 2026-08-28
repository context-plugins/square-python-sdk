from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .delete_order_custom_attribute_response import (
    DeleteOrderCustomAttributeResponse,
    DeleteOrderCustomAttributeResponseDict,
)
from .error import Error, ErrorDict


class BulkDeleteOrderCustomAttributesResponse(SdkBaseModel):
    """Represents a response from deleting one or more order custom attributes."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    values: dict[str, DeleteOrderCustomAttributeResponse]
    """A map of responses that correspond to individual delete requests. Each response has the same ID as the
    corresponding request and contains either a ``custom_attribute`` or an ``errors`` field."""


class BulkDeleteOrderCustomAttributesResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    values: dict[str, DeleteOrderCustomAttributeResponse | DeleteOrderCustomAttributeResponseDict]
