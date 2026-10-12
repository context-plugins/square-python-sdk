from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict
from .customer_tax_ids import CustomerTaxIds, CustomerTaxIdsDict


class BulkUpdateCustomerData(SdkBaseModel):
    """Defines the customer data provided in individual update requests for a `BulkUpdateCustomers
    <api-endpoint:Customers-BulkUpdateCustomers>`__ operation."""

    given_name: OptionalNullable[str] = UNSET
    """The given name (that is, the first name) associated with the customer profile."""

    family_name: OptionalNullable[str] = UNSET
    """The family name (that is, the last name) associated with the customer profile."""

    company_name: OptionalNullable[str] = UNSET
    """A business name associated with the customer profile."""

    nickname: OptionalNullable[str] = UNSET
    """A nickname for the customer profile."""

    email_address: OptionalNullable[str] = UNSET
    """The email address associated with the customer profile."""

    address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number associated with the customer profile. The phone number must be valid and can contain 9–16
    digits, with an optional ``+`` prefix and country code. For more information, see `Customer phone numbers
    <https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#phone-number>`__."""

    reference_id: OptionalNullable[str] = UNSET
    """An optional second ID used to associate the customer profile with an entity in another system."""

    note: OptionalNullable[str] = UNSET
    """An custom note associates with the customer profile."""

    birthday: OptionalNullable[str] = UNSET
    """The birthday associated with the customer profile, in ``YYYY-MM-DD`` or ``MM-DD`` format. For example, specify
    ``1998-09-21`` for September 21, 1998, or ``09-21`` for September 21. Birthdays are returned in ``YYYY-MM-DD``
    format, where ``YYYY`` is the specified birth year or ``0000`` if a birth year is not specified."""

    tax_ids: Optional[CustomerTaxIds] = UNSET
    """Represents the tax ID associated with a `customer profile <entity:Customer>`__. The corresponding ``tax_ids``
    field is available only for customers of sellers in EU countries or the United Kingdom. For more information, see
    `Customer tax IDs <https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids>`__."""

    version: Optional[int] = UNSET
    """The current version of the customer profile.

    As a best practice, you should include this field to enable `optimistic concurrency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__ control."""


class BulkUpdateCustomerDataDict(TypedDict):
    given_name: NotRequired[str | None]
    family_name: NotRequired[str | None]
    company_name: NotRequired[str | None]
    nickname: NotRequired[str | None]
    email_address: NotRequired[str | None]
    address: NotRequired[AddressDict]
    phone_number: NotRequired[str | None]
    reference_id: NotRequired[str | None]
    note: NotRequired[str | None]
    birthday: NotRequired[str | None]
    tax_ids: NotRequired[CustomerTaxIdsDict]
    version: NotRequired[int]
