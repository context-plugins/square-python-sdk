from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.country import CountryOrStr
from .enums.currency import CurrencyOrStr
from .enums.merchant_status import MerchantStatusOrStr


class Merchant(SdkBaseModel):
    """Represents a business that sells with Square."""

    id: Optional[str] = UNSET
    """The Square-issued ID of the merchant."""

    business_name: OptionalNullable[str] = UNSET
    """The name of the merchant's overall business."""

    country: CountryOrStr
    """Indicates the country associated with another entity, such as a business. Values are in `ISO 3166-1-alpha-2
    format <http://www.iso.org/iso/home/standards/country_codes.htm>`__."""

    language_code: OptionalNullable[str] = UNSET
    """The code indicating the `language preferences
    <https://developer.squareup.com/docs/build-basics/general-considerations/language-preferences>`__ of the merchant,
    in `BCP 47 format <https://tools.ietf.org/html/bcp47#appendix-A>`__. For example, ``en-US`` or ``fr-CA``."""

    currency: Optional[CurrencyOrStr] = UNSET
    """Indicates the associated currency for an amount of money. Values correspond to `ISO 4217
    <https://wikipedia.org/wiki/ISO_4217>`__."""

    status: Optional[MerchantStatusOrStr] = UNSET
    main_location_id: OptionalNullable[str] = UNSET
    """The ID of the https://developer.squareup.com/docs/locations-api#about-the-main-location for this merchant."""

    created_at: Optional[str] = UNSET
    """The time when the merchant was created, in RFC 3339 format.
       For more information, see `Working with Dates
        <https://developer.squareup.com/docs/build-basics/working-with-dates>`__."""


class MerchantDict(TypedDict):
    id: NotRequired[str]
    business_name: NotRequired[str | None]
    country: CountryOrStr
    language_code: NotRequired[str | None]
    currency: NotRequired[CurrencyOrStr]
    status: NotRequired[MerchantStatusOrStr]
    main_location_id: NotRequired[str | None]
    created_at: NotRequired[str]
