from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_upsert_merchant_custom_attributes_response_merchant_custom_attribute_upsert_response import (
    BulkUpsertMerchantCustomAttributesResponseMerchantCustomAttributeUpsertResponse,
    BulkUpsertMerchantCustomAttributesResponseMerchantCustomAttributeUpsertResponseDict,
)
from .error import Error, ErrorDict


class BulkUpsertMerchantCustomAttributesResponse(SdkBaseModel):
    """Represents a `BulkUpsertMerchantCustomAttributes
    <api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes>`__ response, which contains a map of
    responses that each corresponds to an individual upsert request."""

    values: Optional[dict[str, BulkUpsertMerchantCustomAttributesResponseMerchantCustomAttributeUpsertResponse]] = UNSET
    """A map of responses that correspond to individual upsert requests. Each response has the same ID as the
    corresponding request and contains either a ``merchant_id`` and ``custom_attribute`` or an ``errors`` field."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class BulkUpsertMerchantCustomAttributesResponseDict(TypedDict):
    values: NotRequired[
        dict[
            str,
            (
                BulkUpsertMerchantCustomAttributesResponseMerchantCustomAttributeUpsertResponse
                | BulkUpsertMerchantCustomAttributesResponseMerchantCustomAttributeUpsertResponseDict
            ),
        ]
    ]
    errors: NotRequired[list[Error | ErrorDict]]
