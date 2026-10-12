from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict
from .error import Error, ErrorDict


class ListCatalogResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    cursor: Optional[str] = UNSET
    """The pagination cursor to be used in a subsequent request. If unset, this is the final response. See `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__ for more information."""

    objects: Optional[list[CatalogObject]] = UNSET
    """The CatalogObjects returned."""


class ListCatalogResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    cursor: NotRequired[str]
    objects: NotRequired[list[CatalogObjectDict]]
