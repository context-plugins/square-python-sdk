from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_upsert_merchant_custom_attributes_request_merchant_custom_attribute_upsert_request import (
    BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequest,
    BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestDict,
)


class BulkUpsertMerchantCustomAttributesRequest(SdkBaseModel):
    """Represents a `BulkUpsertMerchantCustomAttributes
    <api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes>`__ request."""

    values: dict[str, BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequest]
    """A map containing 1 to 25 individual upsert requests. For each request, provide an arbitrary ID that is unique for
    this ``BulkUpsertMerchantCustomAttributes`` request and the information needed to create or update a custom
    attribute."""


class BulkUpsertMerchantCustomAttributesRequestDict(TypedDict):
    values: dict[
        str,
        (
            BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequest
            | BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequestDict
        ),
    ]
