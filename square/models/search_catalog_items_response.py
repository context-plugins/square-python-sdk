from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict
from .error import Error, ErrorDict


class SearchCatalogItemsResponse(SdkBaseModel):
    """Defines the response body returned from the `SearchCatalogItems <api-endpoint:Catalog-SearchCatalogItems>`__
    endpoint."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    items: Optional[list[CatalogObject]] = UNSET
    """Returned items matching the specified query expressions."""

    cursor: Optional[str] = UNSET
    """Pagination token used in the next request to return more of the search result."""

    matched_variation_ids: Optional[list[str]] = UNSET
    """Ids of returned item variations matching the specified query expression."""


class SearchCatalogItemsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    items: NotRequired[list[CatalogObject | CatalogObjectDict]]
    cursor: NotRequired[str]
    matched_variation_ids: NotRequired[list[str]]
