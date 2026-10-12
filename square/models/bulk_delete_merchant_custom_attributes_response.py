from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_delete_merchant_custom_attributes_response_merchant_custom_attribute_delete_response import (
    BulkDeleteMerchantCustomAttributesResponseMerchantCustomAttributeDeleteResponse,
    BulkDeleteMerchantCustomAttributesResponseMerchantCustomAttributeDeleteResponseDict,
)
from .error import Error, ErrorDict


class BulkDeleteMerchantCustomAttributesResponse(SdkBaseModel):
    """Represents a `BulkDeleteMerchantCustomAttributes
    <api-endpoint:MerchantCustomAttributes-BulkDeleteMerchantCustomAttributes>`__ response, which contains a map of
    responses that each corresponds to an individual delete request."""

    values: dict[str, BulkDeleteMerchantCustomAttributesResponseMerchantCustomAttributeDeleteResponse]
    """A map of responses that correspond to individual delete requests. Each response has the same key as the
    corresponding request."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class BulkDeleteMerchantCustomAttributesResponseDict(TypedDict):
    values: dict[str, BulkDeleteMerchantCustomAttributesResponseMerchantCustomAttributeDeleteResponseDict]
    errors: NotRequired[list[ErrorDict]]
