from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BulkRetrieveCustomersRequest(SdkBaseModel):
    """Defines the body parameters that can be included in requests to the `BulkRetrieveCustomers
    <api-endpoint:Customers-BulkRetrieveCustomers>`__ endpoint."""

    customer_ids: list[str]
    """The IDs of the `customer profiles <entity:Customer>`__ to retrieve."""


class BulkRetrieveCustomersRequestDict(TypedDict):
    customer_ids: list[str]
