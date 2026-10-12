from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .update_customer_response import UpdateCustomerResponse, UpdateCustomerResponseDict


class BulkUpdateCustomersResponse(SdkBaseModel):
    """Defines the fields included in the response body from the `BulkUpdateCustomers
    <api-endpoint:Customers-BulkUpdateCustomers>`__ endpoint."""

    responses: Optional[dict[str, UpdateCustomerResponse]] = UNSET
    """A map of responses that correspond to individual update requests, represented by key-value pairs.

    Each key is the customer ID that was specified for an update request and each value is the corresponding response.
    If the request succeeds, the value is the updated customer profile. If the request fails, the value contains any
    errors that occurred during the request."""

    errors: Optional[list[Error]] = UNSET
    """Any top-level errors that prevented the bulk operation from running."""


class BulkUpdateCustomersResponseDict(TypedDict):
    responses: NotRequired[dict[str, UpdateCustomerResponseDict]]
    errors: NotRequired[list[ErrorDict]]
