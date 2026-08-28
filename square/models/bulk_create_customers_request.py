from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_create_customer_data import BulkCreateCustomerData, BulkCreateCustomerDataDict


class BulkCreateCustomersRequest(SdkBaseModel):
    """Defines the body parameters that can be included in requests to the `BulkCreateCustomers
    <api-endpoint:Customers-BulkCreateCustomers>`__ endpoint."""

    customers: dict[str, BulkCreateCustomerData]
    """A map of 1 to 100 individual create requests, represented by ``idempotency key: { customer data }`` key-value
    pairs.

    Each key is an `idempotency key
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ that uniquely identifies the
    create request. Each value contains the customer data used to create the customer profile."""


class BulkCreateCustomersRequestDict(TypedDict):
    customers: dict[str, BulkCreateCustomerData | BulkCreateCustomerDataDict]
