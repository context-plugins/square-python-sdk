from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_creation_source_filter import CustomerCreationSourceFilter, CustomerCreationSourceFilterDict
from .customer_custom_attribute_filters import CustomerCustomAttributeFilters, CustomerCustomAttributeFiltersDict
from .customer_text_filter import CustomerTextFilter, CustomerTextFilterDict
from .filter_value import FilterValue, FilterValueDict
from .time_range import TimeRange, TimeRangeDict


class CustomerFilter(SdkBaseModel):
    """Represents the filtering criteria in a `search query <entity:CustomerQuery>`__ that defines how to filter
    customer profiles returned in `SearchCustomers <api-endpoint:Customers-SearchCustomers>`__ results."""

    creation_source: Optional[CustomerCreationSourceFilter] = UNSET
    """The creation source filter.

    If one or more creation sources are set, customer profiles are included in, or excluded from, the result if they
    match at least one of the filter criteria."""

    created_at: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    updated_at: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""

    email_address: Optional[CustomerTextFilter] = UNSET
    """A filter to select customers based on exact or fuzzy matching of customer attributes against a specified query.
    Depending on the customer attributes, the filter can be case-sensitive. This filter can be exact or fuzzy, but it
    cannot be both."""

    phone_number: Optional[CustomerTextFilter] = UNSET
    """A filter to select customers based on exact or fuzzy matching of customer attributes against a specified query.
    Depending on the customer attributes, the filter can be case-sensitive. This filter can be exact or fuzzy, but it
    cannot be both."""

    reference_id: Optional[CustomerTextFilter] = UNSET
    """A filter to select customers based on exact or fuzzy matching of customer attributes against a specified query.
    Depending on the customer attributes, the filter can be case-sensitive. This filter can be exact or fuzzy, but it
    cannot be both."""

    group_ids: Optional[FilterValue] = UNSET
    """A filter to select resources based on an exact field value. For any given value, the value can only be in one
    property. Depending on the field, either all properties can be set or only a subset will be available.

    Refer to the documentation of the field."""

    custom_attribute: Optional[CustomerCustomAttributeFilters] = UNSET
    """The custom attribute filters in a set of `customer filters <entity:CustomerFilter>`__ used in a search query. Use
    this filter to search based on `custom attributes <entity:CustomAttribute>`__ that are assigned to customer
    profiles. For more information, see `Search by custom attribute
    <https://developer.squareup.com/docs/customers-api/use-the-api/search-customers#search-by-custom-attribute>`__."""

    segment_ids: Optional[FilterValue] = UNSET
    """A filter to select resources based on an exact field value. For any given value, the value can only be in one
    property. Depending on the field, either all properties can be set or only a subset will be available.

    Refer to the documentation of the field."""


class CustomerFilterDict(TypedDict):
    creation_source: NotRequired[CustomerCreationSourceFilterDict]
    created_at: NotRequired[TimeRangeDict]
    updated_at: NotRequired[TimeRangeDict]
    email_address: NotRequired[CustomerTextFilterDict]
    phone_number: NotRequired[CustomerTextFilterDict]
    reference_id: NotRequired[CustomerTextFilterDict]
    group_ids: NotRequired[FilterValueDict]
    custom_attribute: NotRequired[CustomerCustomAttributeFiltersDict]
    segment_ids: NotRequired[FilterValueDict]
