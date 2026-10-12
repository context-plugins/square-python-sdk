from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute_filter import CustomAttributeFilter, CustomAttributeFilterDict
from .enums.archived_state import ArchivedStateOrStr
from .enums.catalog_item_product_type import CatalogItemProductTypeOrStr
from .enums.search_catalog_items_request_stock_level import SearchCatalogItemsRequestStockLevelOrStr
from .enums.sort_order import SortOrderOrStr


class SearchCatalogItemsRequest(SdkBaseModel):
    """Defines the request body for the `SearchCatalogItems <api-endpoint:Catalog-SearchCatalogItems>`__ endpoint."""

    text_filter: Optional[str] = UNSET
    """The text filter expression to return items or item variations containing specified text in the ``name``,
    ``description``, or ``abbreviation`` attribute value of an item, or in the ``name``, ``sku``, or ``upc`` attribute
    value of an item variation."""

    category_ids: Optional[list[str]] = UNSET
    """The category id query expression to return items containing the specified category IDs."""

    stock_levels: Optional[list[SearchCatalogItemsRequestStockLevelOrStr]] = UNSET
    """The stock-level query expression to return item variations with the specified stock levels. See
    `SearchCatalogItemsRequestStockLevel <#type-searchcatalogitemsrequeststocklevel>`__ for possible values"""

    enabled_location_ids: Optional[list[str]] = UNSET
    """The enabled-location query expression to return items and item variations having specified enabled locations."""

    cursor: Optional[str] = UNSET
    """The pagination token, returned in the previous response, used to fetch the next batch of pending results."""

    limit: Optional[int] = UNSET
    """The maximum number of results to return per page. The default value is 100."""

    sort_order: Optional[SortOrderOrStr] = UNSET
    """The order (e.g., chronological or alphabetical) in which results from a request are returned."""

    product_types: Optional[list[CatalogItemProductTypeOrStr]] = UNSET
    """The product types query expression to return items or item variations having the specified product types."""

    custom_attribute_filters: Optional[list[CustomAttributeFilter]] = UNSET
    """The customer-attribute filter to return items or item variations matching the specified custom attribute
    expressions. A maximum number of 10 custom attribute expressions are supported in a single call to the
    `SearchCatalogItems <api-endpoint:Catalog-SearchCatalogItems>`__ endpoint."""

    archived_state: Optional[ArchivedStateOrStr] = UNSET
    """Defines the values for the ``archived_state`` query expression used in `SearchCatalogItems
    <api-endpoint:Catalog-SearchCatalogItems>`__ to return the archived, not archived or either type of catalog
    items."""


class SearchCatalogItemsRequestDict(TypedDict):
    text_filter: NotRequired[str]
    category_ids: NotRequired[list[str]]
    stock_levels: NotRequired[list[SearchCatalogItemsRequestStockLevelOrStr]]
    enabled_location_ids: NotRequired[list[str]]
    cursor: NotRequired[str]
    limit: NotRequired[int]
    sort_order: NotRequired[SortOrderOrStr]
    product_types: NotRequired[list[CatalogItemProductTypeOrStr]]
    custom_attribute_filters: NotRequired[list[CustomAttributeFilterDict]]
    archived_state: NotRequired[ArchivedStateOrStr]
