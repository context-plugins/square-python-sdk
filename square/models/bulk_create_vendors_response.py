from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .create_vendor_response import CreateVendorResponse, CreateVendorResponseDict
from .error import Error, ErrorDict


class BulkCreateVendorsResponse(SdkBaseModel):
    """Represents an output from a call to `BulkCreateVendors <api-endpoint:Vendors-BulkCreateVendors>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    responses: Optional[dict[str, CreateVendorResponse]] = UNSET
    """A set of `CreateVendorResponse <entity:CreateVendorResponse>`__ objects encapsulating successfully created
    `Vendor <entity:Vendor>`__ objects or error responses for failed attempts. The set is represented by a collection of
    idempotency-key/``Vendor``-object or idempotency-key/error-object pairs. The idempotency keys correspond to those
    specified in the input."""


class BulkCreateVendorsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    responses: NotRequired[dict[str, CreateVendorResponse | CreateVendorResponseDict]]
