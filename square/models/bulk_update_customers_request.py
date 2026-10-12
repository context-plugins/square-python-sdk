from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .bulk_update_customer_data import BulkUpdateCustomerData, BulkUpdateCustomerDataDict


class BulkUpdateCustomersRequest(SdkBaseModel):
    """Defines the body parameters that can be included in requests to the `BulkUpdateCustomers
    <api-endpoint:Customers-BulkUpdateCustomers>`__ endpoint."""

    customers: dict[str, BulkUpdateCustomerData]
    """A map of 1 to 100 individual update requests, represented by ``customer ID: { customer data }`` key-value pairs.

    Each key is the ID of the `customer profile <entity:Customer>`__ to update. To update a customer profile that was
    created by merging existing profiles, provide the ID of the newly created profile.

    Each value contains the updated customer data. Only new or changed fields are required. To add or update a field,
    specify the new value. To remove a field, specify ``null``."""


class BulkUpdateCustomersRequestDict(TypedDict):
    customers: dict[str, BulkUpdateCustomerDataDict]
