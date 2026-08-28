from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict
from .customer_preferences import CustomerPreferences, CustomerPreferencesDict
from .customer_tax_ids import CustomerTaxIds, CustomerTaxIdsDict
from .enums.customer_creation_source import CustomerCreationSourceOrStr


class Customer(SdkBaseModel):
    """Represents a Square customer profile in the Customer Directory of a Square seller."""

    id: Optional[str] = UNSET
    """A unique Square-assigned ID for the customer profile.

    If you need this ID for an API request, use the ID returned when you created the customer profile or call the
    `SearchCustomers <api-endpoint:Customers-SearchCustomers>`__ or `ListCustomers
    <api-endpoint:Customers-ListCustomers>`__ endpoint."""

    created_at: Optional[str] = UNSET
    """The timestamp when the customer profile was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the customer profile was last updated, in RFC 3339 format."""

    given_name: OptionalNullable[str] = UNSET
    """The given name (that is, the first name) associated with the customer profile."""

    family_name: OptionalNullable[str] = UNSET
    """The family name (that is, the last name) associated with the customer profile."""

    nickname: OptionalNullable[str] = UNSET
    """A nickname for the customer profile."""

    company_name: OptionalNullable[str] = UNSET
    """A business name associated with the customer profile."""

    email_address: OptionalNullable[str] = UNSET
    """The email address associated with the customer profile."""

    address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number associated with the customer profile."""

    birthday: OptionalNullable[str] = UNSET
    """The birthday associated with the customer profile, in ``YYYY-MM-DD`` format. For example, ``1998-09-21``
    represents September 21, 1998, and ``0000-09-21`` represents September 21 (without a birth year)."""

    reference_id: OptionalNullable[str] = UNSET
    """An optional second ID used to associate the customer profile with an entity in another system."""

    note: OptionalNullable[str] = UNSET
    """A custom note associated with the customer profile."""

    preferences: Optional[CustomerPreferences] = UNSET
    """Represents communication preferences for the customer profile."""

    creation_source: Optional[CustomerCreationSourceOrStr] = UNSET
    """Indicates the method used to create the customer profile."""

    group_ids: Optional[list[str | None]] = UNSET
    """The IDs of `customer groups <entity:CustomerGroup>`__ the customer belongs to."""

    segment_ids: Optional[list[str | None]] = UNSET
    """The IDs of `customer segments <entity:CustomerSegment>`__ the customer belongs to."""

    version: Optional[int] = UNSET
    """The Square-assigned version number of the customer profile. The version number is incremented each time an update
    is committed to the customer profile, except for changes to customer segment membership."""

    tax_ids: Optional[CustomerTaxIds] = UNSET
    """Represents the tax ID associated with a `customer profile <entity:Customer>`__. The corresponding ``tax_ids``
    field is available only for customers of sellers in EU countries or the United Kingdom. For more information, see
    `Customer tax IDs <https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids>`__."""


class CustomerDict(TypedDict):
    id: NotRequired[str]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    given_name: NotRequired[str | None]
    family_name: NotRequired[str | None]
    nickname: NotRequired[str | None]
    company_name: NotRequired[str | None]
    email_address: NotRequired[str | None]
    address: NotRequired[Address | AddressDict]
    phone_number: NotRequired[str | None]
    birthday: NotRequired[str | None]
    reference_id: NotRequired[str | None]
    note: NotRequired[str | None]
    preferences: NotRequired[CustomerPreferences | CustomerPreferencesDict]
    creation_source: NotRequired[CustomerCreationSourceOrStr]
    group_ids: NotRequired[list[str | None]]
    segment_ids: NotRequired[list[str | None]]
    version: NotRequired[int]
    tax_ids: NotRequired[CustomerTaxIds | CustomerTaxIdsDict]
