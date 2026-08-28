from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .update_vendor_response import UpdateVendorResponse, UpdateVendorResponseDict


class BulkUpdateVendorsResponse(SdkBaseModel):
    """Represents an output from a call to `BulkUpdateVendors <api-endpoint:Vendors-BulkUpdateVendors>`__."""

    errors: Optional[list[Error]] = UNSET
    """Errors encountered when the request fails."""

    responses: Optional[dict[str, UpdateVendorResponse]] = UNSET
    """A set of `UpdateVendorResponse <entity:UpdateVendorResponse>`__ objects encapsulating successfully created
    `Vendor <entity:Vendor>`__ objects or error responses for failed attempts. The set is represented by a collection of
    ``Vendor``-ID/``UpdateVendorResponse``-object or ``Vendor``-ID/error-object pairs."""


class BulkUpdateVendorsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    responses: NotRequired[dict[str, UpdateVendorResponse | UpdateVendorResponseDict]]
