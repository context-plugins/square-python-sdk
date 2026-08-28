from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_vendor_request import UpdateVendorRequest, UpdateVendorRequestDict


class BulkUpdateVendorsRequest(SdkBaseModel):
    """Represents an input to a call to `BulkUpdateVendors <api-endpoint:Vendors-BulkUpdateVendors>`__."""

    vendors: dict[str, UpdateVendorRequest]
    """A set of `UpdateVendorRequest <entity:UpdateVendorRequest>`__ objects encapsulating to-be-updated `Vendor
    <entity:Vendor>`__ objects. The set is represented by a collection of ``Vendor``-ID/``UpdateVendorRequest``-object
    pairs."""


class BulkUpdateVendorsRequestDict(TypedDict):
    vendors: dict[str, UpdateVendorRequest | UpdateVendorRequestDict]
