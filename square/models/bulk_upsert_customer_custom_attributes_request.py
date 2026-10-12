from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_upsert_customer_custom_attributes_request_customer_custom_attribute_upsert_request import (
    BulkUpsertCustomerCustomAttributesRequestCustomerCustomAttributeUpsertRequest,
    BulkUpsertCustomerCustomAttributesRequestCustomerCustomAttributeUpsertRequestDict,
)


class BulkUpsertCustomerCustomAttributesRequest(SdkBaseModel):
    """Represents a `BulkUpsertCustomerCustomAttributes
    <api-endpoint:CustomerCustomAttributes-BulkUpsertCustomerCustomAttributes>`__ request."""

    values: dict[str, BulkUpsertCustomerCustomAttributesRequestCustomerCustomAttributeUpsertRequest]
    """A map containing 1 to 25 individual upsert requests. For each request, provide an arbitrary ID that is unique for
    this ``BulkUpsertCustomerCustomAttributes`` request and the information needed to create or update a custom
    attribute."""


class BulkUpsertCustomerCustomAttributesRequestDict(TypedDict):
    values: dict[str, BulkUpsertCustomerCustomAttributesRequestCustomerCustomAttributeUpsertRequestDict]
