from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.country import CountryOrStr


class Address(SdkBaseModel):
    """Represents a postal address in a country. For more information, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    address_line_1: OptionalNullable[str] = UNSET
    """The first line of the address.

    Fields that start with ``address_line`` provide the address's most specific details, like street number, street
    name, and building name. They do *not* provide less specific details like city, state/province, or country (these
    details are provided in other fields)."""

    address_line_2: OptionalNullable[str] = UNSET
    """The second line of the address, if any."""

    address_line_3: OptionalNullable[str] = UNSET
    """The third line of the address, if any."""

    locality: OptionalNullable[str] = UNSET
    """The city or town of the address. For a full list of field meanings by country, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    sublocality: OptionalNullable[str] = UNSET
    """A civil region within the address's ``locality``, if any."""

    sublocality_2: OptionalNullable[str] = UNSET
    """A civil region within the address's ``sublocality``, if any."""

    sublocality_3: OptionalNullable[str] = UNSET
    """A civil region within the address's ``sublocality_2``, if any."""

    administrative_district_level_1: OptionalNullable[str] = UNSET
    """A civil entity within the address's country. In the US, this is the state. For a full list of field meanings by
    country, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    administrative_district_level_2: OptionalNullable[str] = UNSET
    """A civil entity within the address's ``administrative_district_level_1``. In the US, this is the county."""

    administrative_district_level_3: OptionalNullable[str] = UNSET
    """A civil entity within the address's ``administrative_district_level_2``, if any."""

    postal_code: OptionalNullable[str] = UNSET
    """The address's postal code. For a full list of field meanings by country, see `Working with Addresses
    <https://developer.squareup.com/docs/build-basics/working-with-addresses>`__."""

    country: Optional[CountryOrStr] = UNSET
    """Indicates the country associated with another entity, such as a business. Values are in `ISO 3166-1-alpha-2
    format <http://www.iso.org/iso/home/standards/country_codes.htm>`__."""

    first_name: OptionalNullable[str] = UNSET
    """Optional first name when it's representing recipient."""

    last_name: OptionalNullable[str] = UNSET
    """Optional last name when it's representing recipient."""


class AddressDict(TypedDict):
    address_line_1: NotRequired[str | None]
    address_line_2: NotRequired[str | None]
    address_line_3: NotRequired[str | None]
    locality: NotRequired[str | None]
    sublocality: NotRequired[str | None]
    sublocality_2: NotRequired[str | None]
    sublocality_3: NotRequired[str | None]
    administrative_district_level_1: NotRequired[str | None]
    administrative_district_level_2: NotRequired[str | None]
    administrative_district_level_3: NotRequired[str | None]
    postal_code: NotRequired[str | None]
    country: NotRequired[CountryOrStr]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
