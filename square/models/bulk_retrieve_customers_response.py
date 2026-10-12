from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .retrieve_customer_response import RetrieveCustomerResponse, RetrieveCustomerResponseDict


class BulkRetrieveCustomersResponse(SdkBaseModel):
    """Defines the fields included in the response body from the `BulkRetrieveCustomers
    <api-endpoint:Customers-BulkRetrieveCustomers>`__ endpoint."""

    responses: Optional[dict[str, RetrieveCustomerResponse]] = UNSET
    """A map of responses that correspond to individual retrieve requests, represented by key-value pairs.

    Each key is the customer ID that was specified for a retrieve request and each value is the corresponding response.
    If the request succeeds, the value is the requested customer profile. If the request fails, the value contains any
    errors that occurred during the request."""

    errors: Optional[list[Error]] = UNSET
    """Any top-level errors that prevented the bulk operation from running."""


class BulkRetrieveCustomersResponseDict(TypedDict):
    responses: NotRequired[dict[str, RetrieveCustomerResponseDict]]
    errors: NotRequired[list[ErrorDict]]
