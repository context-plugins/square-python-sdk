from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict
from .error import Error, ErrorDict


class BulkUpsertCustomerCustomAttributesResponseCustomerCustomAttributeUpsertResponse(SdkBaseModel):
    """Represents a response for an individual upsert request in a `BulkUpsertCustomerCustomAttributes
    <api-endpoint:CustomerCustomAttributes-BulkUpsertCustomerCustomAttributes>`__ operation."""

    customer_id: Optional[str] = UNSET
    """The ID of the customer profile associated with the custom attribute."""

    custom_attribute: Optional[CustomAttribute] = UNSET
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred while processing the individual request."""


class BulkUpsertCustomerCustomAttributesResponseCustomerCustomAttributeUpsertResponseDict(TypedDict):
    customer_id: NotRequired[str]
    custom_attribute: NotRequired[CustomAttributeDict]
    errors: NotRequired[list[ErrorDict]]
