from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_query_exact import CatalogQueryExact, CatalogQueryExactDict
from .catalog_query_item_variations_for_item_option_values import (
    CatalogQueryItemVariationsForItemOptionValues,
    CatalogQueryItemVariationsForItemOptionValuesDict,
)
from .catalog_query_items_for_item_options import CatalogQueryItemsForItemOptions, CatalogQueryItemsForItemOptionsDict
from .catalog_query_items_for_modifier_list import (
    CatalogQueryItemsForModifierList,
    CatalogQueryItemsForModifierListDict,
)
from .catalog_query_items_for_tax import CatalogQueryItemsForTax, CatalogQueryItemsForTaxDict
from .catalog_query_prefix import CatalogQueryPrefix, CatalogQueryPrefixDict
from .catalog_query_range import CatalogQueryRange, CatalogQueryRangeDict
from .catalog_query_set import CatalogQuerySet, CatalogQuerySetDict
from .catalog_query_sorted_attribute import CatalogQuerySortedAttribute, CatalogQuerySortedAttributeDict
from .catalog_query_text import CatalogQueryText, CatalogQueryTextDict


class CatalogQuery(SdkBaseModel):
    """A query composed of one or more different types of filters to narrow the scope of targeted objects when calling
    the ``SearchCatalogObjects`` endpoint.

    Although a query can have multiple filters, only certain query types can be combined per call to
    `SearchCatalogObjects <api-endpoint:Catalog-SearchCatalogObjects>`__. Any combination of the following types may be
    used together:
    - `exact_query <entity:CatalogQueryExact>`__
    - `prefix_query <entity:CatalogQueryPrefix>`__
    - `range_query <entity:CatalogQueryRange>`__
    - `sorted_attribute_query <entity:CatalogQuerySortedAttribute>`__
    - `text_query <entity:CatalogQueryText>`__

    All other query types cannot be combined with any others.

    When a query filter is based on an attribute, the attribute must be searchable. Searchable attributes are listed as
    follows, along their parent types that can be searched for with applicable query filters.

    Searchable attribute and objects queryable by searchable attributes:
    - ``name``: ``CatalogItem``, ``CatalogItemVariation``, ``CatalogCategory``, ``CatalogTax``, ``CatalogDiscount``,
        ``CatalogModifier``, ``CatalogModifierList``, ``CatalogItemOption``, ``CatalogItemOptionValue``
    - ``description``: ``CatalogItem``, ``CatalogItemOptionValue``
    - ``abbreviation``: ``CatalogItem``
    - ``upc``: ``CatalogItemVariation``
    - ``sku``: ``CatalogItemVariation``
    - ``caption``: ``CatalogImage``
    - ``display_name``: ``CatalogItemOption``

    For example, to search for `CatalogItem <entity:CatalogItem>`__ objects by searchable attributes, you can use the
    ``"name"``, ``"description"``, or ``"abbreviation"`` attribute in an applicable query filter."""

    sorted_attribute_query: Optional[CatalogQuerySortedAttribute] = UNSET
    """The query expression to specify the key to sort search results."""

    exact_query: Optional[CatalogQueryExact] = UNSET
    """The query filter to return the search result by exact match of the specified attribute name and value."""

    set_query: Optional[CatalogQuerySet] = UNSET
    """The query filter to return the search result(s) by exact match of the specified ``attribute_name`` and any of the
    ``attribute_values``."""

    prefix_query: Optional[CatalogQueryPrefix] = UNSET
    """The query filter to return the search result whose named attribute values are prefixed by the specified attribute
    value."""

    range_query: Optional[CatalogQueryRange] = UNSET
    """The query filter to return the search result whose named attribute values fall between the specified range."""

    text_query: Optional[CatalogQueryText] = UNSET
    """The query filter to return the search result whose searchable attribute values contain all of the specified
    keywords or tokens, independent of the token order or case."""

    items_for_tax_query: Optional[CatalogQueryItemsForTax] = UNSET
    """The query filter to return the items containing the specified tax IDs."""

    items_for_modifier_list_query: Optional[CatalogQueryItemsForModifierList] = UNSET
    """The query filter to return the items containing the specified modifier list IDs."""

    items_for_item_options_query: Optional[CatalogQueryItemsForItemOptions] = UNSET
    """The query filter to return the items containing the specified item option IDs."""

    item_variations_for_item_option_values_query: Optional[CatalogQueryItemVariationsForItemOptionValues] = UNSET
    """The query filter to return the item variations containing the specified item option value IDs."""


class CatalogQueryDict(TypedDict):
    sorted_attribute_query: NotRequired[CatalogQuerySortedAttributeDict]
    exact_query: NotRequired[CatalogQueryExactDict]
    set_query: NotRequired[CatalogQuerySetDict]
    prefix_query: NotRequired[CatalogQueryPrefixDict]
    range_query: NotRequired[CatalogQueryRangeDict]
    text_query: NotRequired[CatalogQueryTextDict]
    items_for_tax_query: NotRequired[CatalogQueryItemsForTaxDict]
    items_for_modifier_list_query: NotRequired[CatalogQueryItemsForModifierListDict]
    items_for_item_options_query: NotRequired[CatalogQueryItemsForItemOptionsDict]
    item_variations_for_item_option_values_query: NotRequired[CatalogQueryItemVariationsForItemOptionValuesDict]
