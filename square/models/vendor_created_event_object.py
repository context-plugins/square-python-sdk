from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.vendor_created_event_object_operation import VendorCreatedEventObjectOperationOrStr
from .vendor import Vendor, VendorDict


class VendorCreatedEventObject(SdkBaseModel):
    operation: Optional[VendorCreatedEventObjectOperationOrStr] = UNSET
    """The operation that can be performed against a vendor to cause the event to be published."""

    vendor: Optional[Vendor] = UNSET
    """Represents a supplier to a seller."""


class VendorCreatedEventObjectDict(TypedDict):
    operation: NotRequired[VendorCreatedEventObjectOperationOrStr]
    vendor: NotRequired[Vendor | VendorDict]
