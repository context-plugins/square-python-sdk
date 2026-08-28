from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_delete_merchant_custom_attributes_request_merchant_custom_attribute_delete_request import (
    BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequest,
    BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestDict,
)


class BulkDeleteMerchantCustomAttributesRequest(SdkBaseModel):
    """Represents a `BulkDeleteMerchantCustomAttributes
    <api-endpoint:MerchantCustomAttributes-BulkDeleteMerchantCustomAttributes>`__ request."""

    values: dict[str, BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequest]
    """The data used to update the ``CustomAttribute`` objects. The keys must be unique and are used to map to the
    corresponding response."""


class BulkDeleteMerchantCustomAttributesRequestDict(TypedDict):
    values: dict[
        str,
        (
            BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequest
            | BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestDict
        ),
    ]
