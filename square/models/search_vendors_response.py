from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .vendor import Vendor, VendorDict


class SearchVendorsResponse(SdkBaseModel):
    """Represents an output from a call to `SearchVendors <api-endpoint:Vendors-SearchVendors>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered when the request fails."""

    vendors: Optional[list[Vendor]] = UNSET
    """The `Vendor <entity:Vendor>`__ objects matching the specified search filter."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If unset, this is the final response.

    See the `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more
    information."""


class SearchVendorsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    vendors: NotRequired[list[Vendor | VendorDict]]
    cursor: NotRequired[str]
