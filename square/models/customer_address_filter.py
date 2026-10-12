from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_text_filter import CustomerTextFilter, CustomerTextFilterDict
from .enums.country import CountryOrStr


class CustomerAddressFilter(SdkBaseModel):
    """The customer address filter. This filter is used in a `CustomerCustomAttributeFilterValue
    <entity:CustomerCustomAttributeFilterValue>`__ filter when searching by an ``Address``-type custom attribute."""

    postal_code: Optional[CustomerTextFilter] = UNSET
    """A filter to select customers based on exact or fuzzy matching of customer attributes against a specified query.
    Depending on the customer attributes, the filter can be case-sensitive. This filter can be exact or fuzzy, but it
    cannot be both."""

    country: Optional[CountryOrStr] = UNSET
    """Indicates the country associated with another entity, such as a business. Values are in `ISO 3166-1-alpha-2
    format <http://www.iso.org/iso/home/standards/country_codes.htm>`__."""


class CustomerAddressFilterDict(TypedDict):
    postal_code: NotRequired[CustomerTextFilterDict]
    country: NotRequired[CountryOrStr]
