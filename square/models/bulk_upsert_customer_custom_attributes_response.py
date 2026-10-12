from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .bulk_upsert_customer_custom_attributes_response_customer_custom_attribute_upsert_response import (
    BulkUpsertCustomerCustomAttributesResponseCustomerCustomAttributeUpsertResponse,
    BulkUpsertCustomerCustomAttributesResponseCustomerCustomAttributeUpsertResponseDict,
)
from .error import Error, ErrorDict


class BulkUpsertCustomerCustomAttributesResponse(SdkBaseModel):
    """Represents a `BulkUpsertCustomerCustomAttributes
    <api-endpoint:CustomerCustomAttributes-BulkUpsertCustomerCustomAttributes>`__ response, which contains a map of
    responses that each corresponds to an individual upsert request."""

    values: Optional[dict[str, BulkUpsertCustomerCustomAttributesResponseCustomerCustomAttributeUpsertResponse]] = UNSET
    """A map of responses that correspond to individual upsert requests. Each response has the same ID as the
    corresponding request and contains either a ``customer_id`` and ``custom_attribute`` or an ``errors`` field."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class BulkUpsertCustomerCustomAttributesResponseDict(TypedDict):
    values: NotRequired[dict[str, BulkUpsertCustomerCustomAttributesResponseCustomerCustomAttributeUpsertResponseDict]]
    errors: NotRequired[list[ErrorDict]]
