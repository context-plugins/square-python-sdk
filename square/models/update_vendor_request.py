from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .vendor import Vendor, VendorDict


class UpdateVendorRequest(SdkBaseModel):
    """Represents an input to a call to `UpdateVendor <api-endpoint:Vendors-UpdateVendor>`__."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A client-supplied, universally unique identifier (UUID) for the request.

    See `Idempotency <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ in the `API
    Development 101 <https://developer.squareup.com/docs/buildbasics>`__ section for more information."""

    vendor: Vendor
    """Represents a supplier to a seller."""


class UpdateVendorRequestDict(TypedDict):
    idempotency_key: NotRequired[str | None]
    vendor: VendorDict
