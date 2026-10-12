from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer import Customer, CustomerDict
from .error import Error, ErrorDict


class ListCustomersResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the ``ListCustomers`` endpoint.

    Either ``errors`` or ``customers`` is present in a given response (never both)."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    customers: Optional[list[Customer]] = UNSET
    """The customer profiles associated with the Square account or an empty object (``{}``) if none are found. Only
    customer profiles with public information (``given_name``, ``family_name``, ``company_name``, ``email_address``, or
    ``phone_number``) are included in the response."""

    cursor: Optional[str] = UNSET
    """A pagination cursor to retrieve the next set of results for the original query. A cursor is only present if the
    request succeeded and additional results are available.

    For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    count: Optional[int] = UNSET
    """The total count of customers associated with the Square account. Only customer profiles with public information
    (``given_name``, ``family_name``, ``company_name``, ``email_address``, or ``phone_number``) are counted. This field
    is present only if ``count`` is set to ``true`` in the request."""


class ListCustomersResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    customers: NotRequired[list[CustomerDict]]
    cursor: NotRequired[str]
    count: NotRequired[int]
