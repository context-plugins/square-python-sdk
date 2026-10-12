from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .customer_custom_attribute_filter_value import (
    CustomerCustomAttributeFilterValue,
    CustomerCustomAttributeFilterValueDict,
)
from .time_range import TimeRange, TimeRangeDict


class CustomerCustomAttributeFilter(SdkBaseModel):
    """The custom attribute filter. Use this filter in a set of `custom attribute filters
    <entity:CustomerCustomAttributeFilters>`__ to search based on the value or last updated date of a customer-related
    `custom attribute <entity:CustomAttribute>`__."""

    key: str
    """The ``key`` of the `custom attribute <entity:CustomAttribute>`__ to filter by. The key is the identifier of the
    custom attribute (and the corresponding custom attribute definition) and can be retrieved using the `Customer Custom
    Attributes API <api:CustomerCustomAttributes>`__."""

    filter: Optional[CustomerCustomAttributeFilterValue] = UNSET
    """A type-specific filter used in a `custom attribute filter <entity:CustomerCustomAttributeFilter>`__ to search
    based on the value of a customer-related `custom attribute <entity:CustomAttribute>`__."""

    updated_at: Optional[TimeRange] = UNSET
    """Represents a generic time range. The start and end values are represented in RFC 3339 format. Time ranges are
    customized to be inclusive or exclusive based on the needs of a particular endpoint. Refer to the relevant
    endpoint-specific documentation to determine how time ranges are handled."""


class CustomerCustomAttributeFilterDict(TypedDict):
    key: str
    filter: NotRequired[CustomerCustomAttributeFilterValueDict]
    updated_at: NotRequired[TimeRangeDict]
