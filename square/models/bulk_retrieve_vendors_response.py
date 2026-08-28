from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .retrieve_vendor_response import RetrieveVendorResponse, RetrieveVendorResponseDict


class BulkRetrieveVendorsResponse(SdkBaseModel):
    """Represents an output from a call to `BulkRetrieveVendors <api-endpoint:Vendors-BulkRetrieveVendors>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    responses: Optional[dict[str, RetrieveVendorResponse]] = UNSET
    """The set of `RetrieveVendorResponse <entity:RetrieveVendorResponse>`__ objects encapsulating successfully
    retrieved `Vendor <entity:Vendor>`__ objects or error responses for failed attempts. The set is represented by a
    collection of ``Vendor``-ID/``Vendor``-object or ``Vendor``-ID/error-object pairs."""


class BulkRetrieveVendorsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    responses: NotRequired[dict[str, RetrieveVendorResponse | RetrieveVendorResponseDict]]
