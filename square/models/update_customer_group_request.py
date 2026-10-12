from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .customer_group import CustomerGroup, CustomerGroupDict


class UpdateCustomerGroupRequest(SdkBaseModel):
    """Defines the body parameters that can be included in a request to the `UpdateCustomerGroup
    <api-endpoint:CustomerGroups-UpdateCustomerGroup>`__ endpoint."""

    group: CustomerGroup
    """Represents a group of customer profiles.

    Customer groups can be created, be modified, and have their membership defined using the Customers API or within the
    Customer Directory in the Square Seller Dashboard or Point of Sale."""


class UpdateCustomerGroupRequestDict(TypedDict):
    group: CustomerGroupDict
