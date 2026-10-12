from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .address import Address, AddressDict
from .business_hours import BusinessHours, BusinessHoursDict
from .coordinates import Coordinates, CoordinatesDict
from .enums.country import CountryOrStr
from .enums.currency import CurrencyOrStr
from .enums.location_capability import LocationCapabilityOrStr
from .enums.location_status import LocationStatusOrStr
from .enums.location_type import LocationTypeOrStr
from .tax_ids import TaxIds, TaxIdsDict


class Location(SdkBaseModel):
    """Represents one of a business' `locations <https://developer.squareup.com/docs/locations-api>`__."""

    id: Optional[str] = UNSET
    """A short generated string of letters and numbers that uniquely identifies this location instance."""

    name: OptionalNullable[str] = UNSET
    """The name of the location. This information appears in the Seller Dashboard as the nickname. A location name must
    be unique within a seller account."""

    address: Optional[Address] = UNSET
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    timezone: OptionalNullable[str] = UNSET
    """The `IANA time zone <https://www.iana.org/time-zones>`__ identifier for the time zone of the location. For
    example, ``America/Los_Angeles``."""

    capabilities: Optional[list[LocationCapabilityOrStr]] = UNSET
    """The Square features that are enabled for the location. See `LocationCapability <entity:LocationCapability>`__ for
    possible values. See `LocationCapability <#type-locationcapability>`__ for possible values"""

    status: Optional[LocationStatusOrStr] = UNSET
    """A location's status."""

    created_at: Optional[str] = UNSET
    """The time when the location was created, in RFC 3339 format. For more information, see `Working with Dates
    <https://developer.squareup.com/docs/build-basics/working-with-dates>`__."""

    merchant_id: Optional[str] = UNSET
    """The ID of the merchant that owns the location."""

    country: Optional[CountryOrStr] = UNSET
    """Indicates the country associated with another entity, such as a business. Values are in `ISO 3166-1-alpha-2
    format <http://www.iso.org/iso/home/standards/country_codes.htm>`__."""

    language_code: OptionalNullable[str] = UNSET
    """The language associated with the location, in `BCP 47 format <https://tools.ietf.org/html/bcp47#appendix-A>`__.
    For more information, see `Language Preferences
    <https://developer.squareup.com/docs/build-basics/general-considerations/language-preferences>`__."""

    currency: Optional[CurrencyOrStr] = UNSET
    """Indicates the associated currency for an amount of money. Values correspond to `ISO 4217
    <https://wikipedia.org/wiki/ISO_4217>`__."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number of the location. For example, ``+1 855-700-6000``."""

    business_name: OptionalNullable[str] = UNSET
    """The name of the location's overall business. This name is present on receipts and other customer-facing branding,
    and can be changed no more than three times in a twelve-month period."""

    type_: Optional[LocationTypeOrStr] = Field(default=UNSET, alias="type")
    """A location's type."""

    website_url: OptionalNullable[str] = UNSET
    """The website URL of the location. For example, ``https://squareup.com``."""

    business_hours: Optional[BusinessHours] = UNSET
    """The hours of operation for a location."""

    business_email: OptionalNullable[str] = UNSET
    """The email address of the location. This can be unique to the location and is not always the email address for the
    business owner or administrator."""

    description: OptionalNullable[str] = UNSET
    """The description of the location. For example, ``Main Street location``."""

    twitter_username: OptionalNullable[str] = UNSET
    """The Twitter username of the location without the '@' symbol. For example, ``Square``."""

    instagram_username: OptionalNullable[str] = UNSET
    """The Instagram username of the location without the '@' symbol. For example, ``square``."""

    facebook_url: OptionalNullable[str] = UNSET
    """The Facebook profile URL of the location. The URL should begin with 'facebook.com/'. For example,
    ``https://www.facebook.com/square``."""

    coordinates: Optional[Coordinates] = UNSET
    """Latitude and longitude coordinates."""

    logo_url: Optional[str] = UNSET
    """The URL of the logo image for the location. When configured in the Seller Dashboard (Receipts section), the logo
    appears on transactions (such as receipts and invoices) that Square generates on behalf of the seller. This image
    should have a roughly square (1:1) aspect ratio and should be at least 200x200 pixels."""

    pos_background_url: Optional[str] = UNSET
    """The URL of the Point of Sale background image for the location."""

    mcc: OptionalNullable[str] = UNSET
    """A four-digit number that describes the kind of goods or services sold at the location. The `merchant category
    code (MCC) <https://developer.squareup.com/docs/locations-api#initialize-a-merchant-category-code>`__ of the
    location as standardized by ISO 18245. For example, ``5045``, for a location that sells computer goods and
    software."""

    full_format_logo_url: Optional[str] = UNSET
    """The URL of a full-format logo image for the location. When configured in the Seller Dashboard (Receipts section),
    the logo appears on transactions (such as receipts and invoices) that Square generates on behalf of the seller. This
    image can be wider than it is tall and should be at least 1280x648 pixels."""

    tax_ids: Optional[TaxIds] = UNSET
    """Identifiers for the location used by various governments for tax purposes."""


class LocationDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str | None]
    address: NotRequired[AddressDict]
    timezone: NotRequired[str | None]
    capabilities: NotRequired[list[LocationCapabilityOrStr]]
    status: NotRequired[LocationStatusOrStr]
    created_at: NotRequired[str]
    merchant_id: NotRequired[str]
    country: NotRequired[CountryOrStr]
    language_code: NotRequired[str | None]
    currency: NotRequired[CurrencyOrStr]
    phone_number: NotRequired[str | None]
    business_name: NotRequired[str | None]
    type_: NotRequired[LocationTypeOrStr]
    website_url: NotRequired[str | None]
    business_hours: NotRequired[BusinessHoursDict]
    business_email: NotRequired[str | None]
    description: NotRequired[str | None]
    twitter_username: NotRequired[str | None]
    instagram_username: NotRequired[str | None]
    facebook_url: NotRequired[str | None]
    coordinates: NotRequired[CoordinatesDict]
    logo_url: NotRequired[str]
    pos_background_url: NotRequired[str]
    mcc: NotRequired[str | None]
    full_format_logo_url: NotRequired[str]
    tax_ids: NotRequired[TaxIdsDict]
