from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict
from .error import Error, ErrorDict


class BatchRetrieveCatalogObjectsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    objects: Optional[list[CatalogObject]] = UNSET
    """A list of `CatalogObject <entity:CatalogObject>`__s returned."""

    related_objects: Optional[list[CatalogObject]] = UNSET
    """A list of `CatalogObject <entity:CatalogObject>`__s referenced by the object in the ``objects`` field."""


class BatchRetrieveCatalogObjectsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    objects: NotRequired[list[CatalogObject | CatalogObjectDict]]
    related_objects: NotRequired[list[CatalogObject | CatalogObjectDict]]
