from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_group import CustomerGroup, CustomerGroupDict
from .error import Error, ErrorDict


class ListCustomerGroupsResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the `ListCustomerGroups
    <api-endpoint:CustomerGroups-ListCustomerGroups>`__ endpoint.

    Either ``errors`` or ``groups`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    groups: Optional[list[CustomerGroup]] = UNSET
    """A list of customer groups belonging to the current seller."""

    cursor: Optional[str] = UNSET
    """A pagination cursor to retrieve the next set of results for your original query to the endpoint. This value is
    present only if the request succeeded and additional results are available.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListCustomerGroupsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    groups: NotRequired[list[CustomerGroup | CustomerGroupDict]]
    cursor: NotRequired[str]
