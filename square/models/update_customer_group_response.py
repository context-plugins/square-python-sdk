from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_group import CustomerGroup, CustomerGroupDict
from .error import Error, ErrorDict


class UpdateCustomerGroupResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `UpdateCustomerGroup
    <api-endpoint:CustomerGroups-UpdateCustomerGroup>`__ endpoint.

    Either ``errors`` or ``group`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    group: Optional[CustomerGroup] = UNSET
    """Represents a group of customer profiles.

    Customer groups can be created, be modified, and have their membership defined using the Customers API or within the
    Customer Directory in the Square Seller Dashboard or Point of Sale."""


class UpdateCustomerGroupResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    group: NotRequired[CustomerGroup | CustomerGroupDict]
