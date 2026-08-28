from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict


class FulfillmentRecipient(SdkBaseModel):
    """Information about the fulfillment recipient."""

    customer_id: OptionalNullable[str] = UNSET
    """The ID of the customer associated with the fulfillment.

    If ``customer_id`` is provided, the fulfillment recipient's ``display_name``, ``email_address``, and
    ``phone_number`` are automatically populated from the targeted customer profile. If these fields are set in the
    request, the request values override the information from the customer profile. If the targeted customer profile
    does not contain the necessary information and these fields are left unset, the request results in an error."""

    display_name: OptionalNullable[str] = UNSET
    """The display name of the fulfillment recipient. This field is required.

    If provided, the display name overrides the corresponding customer profile value indicated by ``customer_id``."""

    email_address: OptionalNullable[str] = UNSET
    """The email address of the fulfillment recipient.

    If provided, the email address overrides the corresponding customer profile value indicated by ``customer_id``."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number of the fulfillment recipient. This field is required.

    If provided, the phone number overrides the corresponding customer profile value indicated by ``customer_id``."""

    address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""


class FulfillmentRecipientDict(TypedDict):
    customer_id: NotRequired[str | None]
    display_name: NotRequired[str | None]
    email_address: NotRequired[str | None]
    phone_number: NotRequired[str | None]
    address: NotRequired[Address | AddressDict]
