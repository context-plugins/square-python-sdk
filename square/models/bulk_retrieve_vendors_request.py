from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BulkRetrieveVendorsRequest(SdkBaseModel):
    """Represents an input to a call to `BulkRetrieveVendors <api-endpoint:Vendors-BulkRetrieveVendors>`__."""

    vendor_ids: Optional[list[str | None]] = UNSET
    """IDs of the `Vendor <entity:Vendor>`__ objects to retrieve."""


class BulkRetrieveVendorsRequestDict(TypedDict):
    vendor_ids: NotRequired[list[str | None]]
