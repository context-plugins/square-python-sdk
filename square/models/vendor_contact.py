from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class VendorContact(SdkBaseModel):
    """Represents a contact of a `Vendor <entity:Vendor>`__."""

    id: Optional[str] = UNSET
    """A unique Square-generated ID for the `VendorContact <entity:VendorContact>`__. This field is required when
    attempting to update a `VendorContact <entity:VendorContact>`__."""

    name: OptionalNullable[str] = UNSET
    """The name of the `VendorContact <entity:VendorContact>`__. This field is required when attempting to create a
    `Vendor <entity:Vendor>`__."""

    email_address: OptionalNullable[str] = UNSET
    """The email address of the `VendorContact <entity:VendorContact>`__."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number of the `VendorContact <entity:VendorContact>`__."""

    removed: OptionalNullable[bool] = UNSET
    """The state of the `VendorContact <entity:VendorContact>`__."""

    ordinal: int
    """The ordinal of the `VendorContact <entity:VendorContact>`__."""


class VendorContactDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str | None]
    email_address: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    removed: NotRequired[bool | None]
    ordinal: int
