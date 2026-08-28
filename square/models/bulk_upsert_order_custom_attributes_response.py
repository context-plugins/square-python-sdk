from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .upsert_order_custom_attribute_response import (
    UpsertOrderCustomAttributeResponse,
    UpsertOrderCustomAttributeResponseDict,
)


class BulkUpsertOrderCustomAttributesResponse(SdkBaseModel):
    """Represents a response from a bulk upsert of order custom attributes."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    values: dict[str, UpsertOrderCustomAttributeResponse]
    """A map of responses that correspond to individual upsert operations for custom attributes."""


class BulkUpsertOrderCustomAttributesResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    values: dict[str, UpsertOrderCustomAttributeResponse | UpsertOrderCustomAttributeResponseDict]
