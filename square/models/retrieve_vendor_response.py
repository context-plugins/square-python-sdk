from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .vendor import Vendor, VendorDict


class RetrieveVendorResponse(SdkBaseModel):
    """Represents an output from a call to `RetrieveVendor <api-endpoint:Vendors-RetrieveVendor>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered when the request fails."""

    vendor: Optional[Vendor] = UNSET
    """Represents a supplier to a seller."""


class RetrieveVendorResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    vendor: NotRequired[Vendor | VendorDict]
