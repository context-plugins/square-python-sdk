from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .vendor import Vendor, VendorDict


class BulkCreateVendorsRequest(SdkBaseModel):
    """Represents an input to a call to `BulkCreateVendors <api-endpoint:Vendors-BulkCreateVendors>`__."""

    vendors: dict[str, Vendor]
    """Specifies a set of new `Vendor <entity:Vendor>`__ objects as represented by a collection of
    idempotency-key/``Vendor``-object pairs."""


class BulkCreateVendorsRequestDict(TypedDict):
    vendors: dict[str, Vendor | VendorDict]
