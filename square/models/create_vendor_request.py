from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .vendor import Vendor, VendorDict


class CreateVendorRequest(SdkBaseModel):
    """Represents an input to a call to `CreateVendor <api-endpoint:Vendors-CreateVendor>`__."""

    idempotency_key: str
    """A client-supplied, universally unique identifier (UUID) to make this `CreateVendor
    <api-endpoint:Vendors-CreateVendor>`__ call idempotent.

    See `Idempotency <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ in the `API
    Development 101 <https://developer.squareup.com/docs/buildbasics>`__ section for more information."""

    vendor: Optional[Vendor] = UNSET
    """Represents a supplier to a seller."""


class CreateVendorRequestDict(TypedDict):
    idempotency_key: str
    vendor: NotRequired[VendorDict]
