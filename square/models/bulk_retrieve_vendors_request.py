from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class BulkRetrieveVendorsRequest(SdkBaseModel):
    """Represents an input to a call to `BulkRetrieveVendors <api-endpoint:Vendors-BulkRetrieveVendors>`__."""

    vendor_ids: OptionalNullable[list[str]] = UNSET
    """IDs of the `Vendor <entity:Vendor>`__ objects to retrieve."""


class BulkRetrieveVendorsRequestDict(TypedDict):
    vendor_ids: NotRequired[list[str] | None]
