from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .vendor import Vendor, VendorDict


class UpdateVendorResponse(SdkBaseModel):
    """Represents an output from a call to `UpdateVendor <api-endpoint:Vendors-UpdateVendor>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors occurred when the request fails."""

    vendor: Optional[Vendor] = UNSET
    """Represents a supplier to a seller."""


class UpdateVendorResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    vendor: NotRequired[VendorDict]
