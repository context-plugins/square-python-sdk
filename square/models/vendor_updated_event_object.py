from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.vendor_updated_event_object_operation import VendorUpdatedEventObjectOperationOrStr
from .vendor import Vendor, VendorDict


class VendorUpdatedEventObject(SdkBaseModel):
    operation: Optional[VendorUpdatedEventObjectOperationOrStr] = UNSET
    """The operation that can be performed against a vendor to cause the event to be published."""

    vendor: Optional[Vendor] = UNSET
    """Represents a supplier to a seller."""


class VendorUpdatedEventObjectDict(TypedDict):
    operation: NotRequired[VendorUpdatedEventObjectOperationOrStr]
    vendor: NotRequired[Vendor | VendorDict]
