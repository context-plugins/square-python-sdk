from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer import Customer, CustomerDict
from .error import Error, ErrorDict


class CreateCustomerResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `CreateCustomer
    <api-endpoint:Customers-CreateCustomer>`__ or `BulkCreateCustomers <api-endpoint:Customers-BulkCreateCustomers>`__
    endpoint.

    Either ``errors`` or ``customer`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    customer: Optional[Customer] = UNSET
    """Represents a Square customer profile in the Customer Directory of a Square seller."""


class CreateCustomerResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    customer: NotRequired[Customer | CustomerDict]
