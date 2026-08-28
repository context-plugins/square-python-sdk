from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .customer_address_filter import CustomerAddressFilter, CustomerAddressFilterDict
from .customer_text_filter import CustomerTextFilter, CustomerTextFilterDict
from .filter_value import FilterValue, FilterValueDict
from .float_number_range import FloatNumberRange, FloatNumberRangeDict
from .time_range import TimeRange, TimeRangeDict


class CustomerCustomAttributeFilterValue(SdkBaseModel):
    """A type-specific filter used in a `custom attribute filter <entity:CustomerCustomAttributeFilter>`__ to search
    based on the value of a customer-related `custom attribute <entity:CustomAttribute>`__."""

    email: Optional[CustomerTextFilter] = UNSET
    """A filter to select customers based on exact or fuzzy matching of customer attributes against a specified query.
    Depending on the customer attributes, the filter can be case-sensitive. This filter can be exact or fuzzy, but it
    cannot be both."""

    phone: Optional[CustomerTextFilter] = UNSET
    """A filter to select customers based on exact or fuzzy matching of customer attributes against a specified query.
    Depending on the customer attributes, the filter can be case-sensitive. This filter can be exact or fuzzy, but it
    cannot be both."""

    text: Optional[CustomerTextFilter] = UNSET
    """A filter to select customers based on exact or fuzzy matching of customer attributes against a specified query.
    Depending on the customer attributes, the filter can be case-sensitive. This filter can be exact or fuzzy, but it
    cannot be both."""

    selection: Optional[FilterValue] = UNSET
    """A filter to select resources based on an exact field value. For any given value, the value can only be in one
    property. Depending on the field, either all properties can be set or only a subset will be available.

    Refer to the documentation of the field."""

    date: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    number: Optional[FloatNumberRange] = UNSET
    """Specifies a decimal number range."""

    boolean: OptionalNullable[bool] = UNSET
    """A filter for a query based on the value of a ``Boolean``-type custom attribute."""

    address: Optional[CustomerAddressFilter] = UNSET
    """The customer address filter. This filter is used in a `CustomerCustomAttributeFilterValue
    <entity:CustomerCustomAttributeFilterValue>`__ filter when searching by an ``Address``-type custom attribute."""


class CustomerCustomAttributeFilterValueDict(TypedDict):
    email: NotRequired[CustomerTextFilter | CustomerTextFilterDict]
    phone: NotRequired[CustomerTextFilter | CustomerTextFilterDict]
    text: NotRequired[CustomerTextFilter | CustomerTextFilterDict]
    selection: NotRequired[FilterValue | FilterValueDict]
    date: NotRequired[TimeRange | TimeRangeDict]
    number: NotRequired[FloatNumberRange | FloatNumberRangeDict]
    boolean: NotRequired[bool | None]
    address: NotRequired[CustomerAddressFilter | CustomerAddressFilterDict]
