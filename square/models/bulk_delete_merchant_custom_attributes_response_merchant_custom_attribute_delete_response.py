from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class BulkDeleteMerchantCustomAttributesResponseMerchantCustomAttributeDeleteResponse(SdkBaseModel):
    """Represents an individual delete response in a `BulkDeleteMerchantCustomAttributes
    <api-endpoint:MerchantCustomAttributes-BulkDeleteMerchantCustomAttributes>`__ request."""

    errors: Optional[list[Error]] = UNSET
    """Errors that occurred while processing the individual MerchantCustomAttributeDeleteRequest request"""


class BulkDeleteMerchantCustomAttributesResponseMerchantCustomAttributeDeleteResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
