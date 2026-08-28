from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_group import CustomerGroup, CustomerGroupDict


class CreateCustomerGroupRequest(SdkBaseModel):
    """Defines the body parameters that can be included in a request to the `CreateCustomerGroup
    <api-endpoint:CustomerGroups-CreateCustomerGroup>`__ endpoint."""

    idempotency_key: Optional[str] = UNSET
    """The idempotency key for the request. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""

    group: CustomerGroup
    """Represents a group of customer profiles.

    Customer groups can be created, be modified, and have their membership defined using the Customers API or within the
    Customer Directory in the Square Seller Dashboard or Point of Sale."""


class CreateCustomerGroupRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    group: CustomerGroup | CustomerGroupDict
