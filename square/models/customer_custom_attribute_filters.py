from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .customer_custom_attribute_filter import CustomerCustomAttributeFilter, CustomerCustomAttributeFilterDict


class CustomerCustomAttributeFilters(SdkBaseModel):
    """The custom attribute filters in a set of `customer filters <entity:CustomerFilter>`__ used in a search query. Use
    this filter to search based on `custom attributes <entity:CustomAttribute>`__ that are assigned to customer
    profiles. For more information, see `Search by custom attribute
    <https://developer.squareup.com/docs/customers-api/use-the-api/search-customers#search-by-custom-attribute>`__."""

    filters: OptionalNullable[list[CustomerCustomAttributeFilter]] = UNSET
    """The custom attribute filters. Each filter must specify ``key`` and include the ``filter`` field with a
    type-specific filter, the ``updated_at`` field, or both. The provided keys must be unique within the list of custom
    attribute filters."""


class CustomerCustomAttributeFiltersDict(TypedDict):
    filters: NotRequired[list[CustomerCustomAttributeFilterDict] | None]
