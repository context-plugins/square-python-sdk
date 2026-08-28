from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer import Customer, CustomerDict
from .error import Error, ErrorDict


class SearchCustomersResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the ``SearchCustomers`` endpoint.

    Either ``errors`` or ``customers`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    customers: Optional[list[Customer]] = UNSET
    """The customer profiles that match the search query. If any search condition is not met, the result is an empty
    object (``{}``). Only customer profiles with public information (``given_name``, ``family_name``, ``company_name``,
    ``email_address``, or ``phone_number``) are included in the response."""

    cursor: Optional[str] = UNSET
    """A pagination cursor that can be used during subsequent calls to ``SearchCustomers`` to retrieve the next set of
    results associated with the original query. Pagination cursors are only present when a request succeeds and
    additional results are available.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    count: Optional[int] = UNSET
    """The total count of customers associated with the Square account that match the search query. Only customer
    profiles with public information (``given_name``, ``family_name``, ``company_name``, ``email_address``, or
    ``phone_number``) are counted. This field is present only if ``count`` is set to ``true`` in the request."""


class SearchCustomersResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    customers: NotRequired[list[Customer | CustomerDict]]
    cursor: NotRequired[str]
    count: NotRequired[int]
