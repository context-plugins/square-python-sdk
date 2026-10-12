from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .customer_tax_ids import CustomerTaxIds, CustomerTaxIdsDict


class CreateCustomerRequest(SdkBaseModel):
    """Defines the body parameters that can be included in a request to the ``CreateCustomer`` endpoint."""

    idempotency_key: Optional[str] = UNSET
    """The idempotency key for the request. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""

    given_name: Optional[str] = UNSET
    """The given name (that is, the first name) associated with the customer profile.

    The maximum length for this value is 300 characters."""

    family_name: Optional[str] = UNSET
    """The family name (that is, the last name) associated with the customer profile.

    The maximum length for this value is 300 characters."""

    company_name: Optional[str] = UNSET
    """A business name associated with the customer profile.

    The maximum length for this value is 500 characters."""

    nickname: Optional[str] = UNSET
    """A nickname for the customer profile.

    The maximum length for this value is 100 characters."""

    email_address: Optional[str] = UNSET
    """The email address associated with the customer profile.

    The maximum length for this value is 254 characters."""

    address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    phone_number: Optional[str] = UNSET
    """The phone number associated with the customer profile. The phone number must be valid and can contain 9–16
    digits, with an optional ``+`` prefix and country code. For more information, see `Customer phone numbers
    <https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#phone-number>`__."""

    reference_id: Optional[str] = UNSET
    """An optional second ID used to associate the customer profile with an entity in another system.

    The maximum length for this value is 100 characters."""

    note: Optional[str] = UNSET
    """A custom note associated with the customer profile."""

    birthday: Optional[str] = UNSET
    """The birthday associated with the customer profile, in ``YYYY-MM-DD`` or ``MM-DD`` format. For example, specify
    ``1998-09-21`` for September 21, 1998, or ``09-21`` for September 21. Birthdays are returned in ``YYYY-MM-DD``
    format, where ``YYYY`` is the specified birth year or ``0000`` if a birth year is not specified."""

    tax_ids: Optional[CustomerTaxIds] = UNSET
    """Represents the tax ID associated with a `customer profile <entity:Customer>`__. The corresponding ``tax_ids``
    field is available only for customers of sellers in EU countries or the United Kingdom. For more information, see
    `Customer tax IDs <https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids>`__."""


class CreateCustomerRequestDict(TypedDict):
    idempotency_key: NotRequired[str]
    given_name: NotRequired[str]
    family_name: NotRequired[str]
    company_name: NotRequired[str]
    nickname: NotRequired[str]
    email_address: NotRequired[str]
    address: NotRequired[AddressDict]
    phone_number: NotRequired[str]
    reference_id: NotRequired[str]
    note: NotRequired[str]
    birthday: NotRequired[str]
    tax_ids: NotRequired[CustomerTaxIdsDict]
