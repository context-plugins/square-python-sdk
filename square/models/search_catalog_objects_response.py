from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict
from .error import Error, ErrorDict


class SearchCatalogObjectsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If unset, this is the final response. See `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more information."""

    objects: Optional[list[CatalogObject]] = UNSET
    """The CatalogObjects returned."""

    related_objects: Optional[list[CatalogObject]] = UNSET
    """A list of CatalogObjects referenced by the objects in the ``objects`` field."""

    latest_time: Optional[str] = UNSET
    """When the associated product catalog was last updated. Will match the value for ``end_time`` or ``cursor`` if
    either field is included in the ``SearchCatalog`` request."""


class SearchCatalogObjectsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    cursor: NotRequired[str]
    objects: NotRequired[list[CatalogObject | CatalogObjectDict]]
    related_objects: NotRequired[list[CatalogObject | CatalogObjectDict]]
    latest_time: NotRequired[str]
