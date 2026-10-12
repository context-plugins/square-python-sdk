from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict


class PrePopulatedData(SdkBaseModel):
    """Describes buyer data to prepopulate in the payment form. For more information, see `Optional Checkout
    Configurations <https://developer.squareup.com/docs/checkout-api/optional-checkout-configurations>`__."""

    buyer_email: OptionalNullable[str] = UNSET
    """The buyer email to prepopulate in the payment form."""

    buyer_phone_number: OptionalNullable[str] = UNSET
    """The buyer phone number to prepopulate in the payment form."""

    buyer_address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""


class PrePopulatedDataDict(TypedDict):
    buyer_email: NotRequired[str | None]
    buyer_phone_number: NotRequired[str | None]
    buyer_address: NotRequired[AddressDict]
