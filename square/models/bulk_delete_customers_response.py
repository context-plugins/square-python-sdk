from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .delete_customer_response import DeleteCustomerResponse, DeleteCustomerResponseDict
from .error import Error, ErrorDict


class BulkDeleteCustomersResponse(SdkBaseModel):
    """Defines the fields included in the response body from the `BulkDeleteCustomers
    <api-endpoint:Customers-BulkDeleteCustomers>`__ endpoint."""

    responses: Optional[dict[str, DeleteCustomerResponse]] = UNSET
    """A map of responses that correspond to individual delete requests, represented by key-value pairs.

    Each key is the customer ID that was specified for a delete request and each value is the corresponding response. If
    the request succeeds, the value is an empty object (``{ }``). If the request fails, the value contains any errors
    that occurred during the request."""

    errors: Optional[list[Error]] = UNSET
    """Any top-level errors that prevented the bulk operation from running."""


class BulkDeleteCustomersResponseDict(TypedDict):
    responses: NotRequired[dict[str, DeleteCustomerResponse | DeleteCustomerResponseDict]]
    errors: NotRequired[list[Error | ErrorDict]]
