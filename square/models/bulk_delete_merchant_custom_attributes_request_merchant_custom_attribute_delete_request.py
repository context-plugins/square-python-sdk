from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequest(SdkBaseModel):
    """Represents an individual delete request in a `BulkDeleteMerchantCustomAttributes
    <api-endpoint:MerchantCustomAttributes-BulkDeleteMerchantCustomAttributes>`__ request. An individual request
    contains an optional ID of the associated custom attribute definition and optional key of the associated custom
    attribute definition."""

    key: Optional[str] = UNSET
    """The key of the associated custom attribute definition. Represented as a qualified key if the requesting app is
    not the definition owner."""


class BulkDeleteMerchantCustomAttributesRequestMerchantCustomAttributeDeleteRequestDict(TypedDict):
    key: NotRequired[str]
