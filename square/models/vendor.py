from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict
from .enums.vendor_status import VendorStatusOrStr
from .vendor_contact import VendorContact, VendorContactDict


class Vendor(SdkBaseModel):
    """Represents a supplier to a seller."""

    id: Optional[str] = UNSET
    """A unique Square-generated ID for the `Vendor <entity:Vendor>`__. This field is required when attempting to update
    a `Vendor <entity:Vendor>`__."""

    created_at: Optional[str] = UNSET
    """An RFC 3339-formatted timestamp that indicates when the `Vendor <entity:Vendor>`__ was created."""

    updated_at: Optional[str] = UNSET
    """An RFC 3339-formatted timestamp that indicates when the `Vendor <entity:Vendor>`__ was last updated."""

    name: OptionalNullable[str] = UNSET
    """The name of the `Vendor <entity:Vendor>`__. This field is required when attempting to create or update a `Vendor
    <entity:Vendor>`__."""

    address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    contacts: Optional[list[VendorContact | None]] = UNSET
    """The contacts of the `Vendor <entity:Vendor>`__."""

    account_number: OptionalNullable[str] = UNSET
    """The account number of the `Vendor <entity:Vendor>`__."""

    note: OptionalNullable[str] = UNSET
    """A note detailing information about the `Vendor <entity:Vendor>`__."""

    version: Optional[int] = UNSET
    """The version of the `Vendor <entity:Vendor>`__."""

    status: Optional[VendorStatusOrStr] = UNSET
    """The status of the `Vendor <entity:Vendor>`__, whether a `Vendor <entity:Vendor>`__ is active or inactive."""


class VendorDict(TypedDict):
    id: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    name: NotRequired[str | None]
    address: NotRequired[Address | AddressDict]
    contacts: NotRequired[list[VendorContact | VendorContactDict | None]]
    account_number: NotRequired[str | None]
    note: NotRequired[str | None]
    version: NotRequired[int]
    status: NotRequired[VendorStatusOrStr]
