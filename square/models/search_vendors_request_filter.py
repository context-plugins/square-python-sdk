from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.vendor_status import VendorStatusOrStr


class SearchVendorsRequestFilter(SdkBaseModel):
    """Defines supported query expressions to search for vendors by."""

    name: Optional[list[str | None]] = UNSET
    """The names of the `Vendor <entity:Vendor>`__ objects to retrieve."""

    status: Optional[list[VendorStatusOrStr | None]] = UNSET
    """The statuses of the `Vendor <entity:Vendor>`__ objects to retrieve. See `VendorStatus <#type-vendorstatus>`__ for
    possible values"""


class SearchVendorsRequestFilterDict(TypedDict):
    name: NotRequired[list[str | None]]
    status: NotRequired[list[VendorStatusOrStr | None]]
