from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BulkDeleteCustomersRequest(SdkBaseModel):
    """Defines the body parameters that can be included in requests to the `BulkDeleteCustomers
    <api-endpoint:Customers-BulkDeleteCustomers>`__ endpoint."""

    customer_ids: list[str]
    """The IDs of the `customer profiles <entity:Customer>`__ to delete."""


class BulkDeleteCustomersRequestDict(TypedDict):
    customer_ids: list[str]
