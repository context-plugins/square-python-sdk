from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .vendor import Vendor, VendorDict


class CreateVendorResponse(SdkBaseModel):
    """Represents an output from a call to `CreateVendor <api-endpoint:Vendors-CreateVendor>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered when the request fails."""

    vendor: Optional[Vendor] = UNSET
    """Represents a supplier to a seller."""


class CreateVendorResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    vendor: NotRequired[VendorDict]
