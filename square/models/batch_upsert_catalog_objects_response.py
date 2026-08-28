from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_id_mapping import CatalogIdMapping, CatalogIdMappingDict
from .catalog_object import CatalogObject, CatalogObjectDict
from .error import Error, ErrorDict


class BatchUpsertCatalogObjectsResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    objects: Optional[list[CatalogObject]] = UNSET
    """The created successfully created CatalogObjects."""

    updated_at: Optional[str] = UNSET
    """The database `timestamp <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ of this update
    in RFC 3339 format, e.g., "2016-09-04T23:59:33.123Z"."""

    id_mappings: Optional[list[CatalogIdMapping]] = UNSET
    """The mapping between client and server IDs for this upsert."""


class BatchUpsertCatalogObjectsResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    objects: NotRequired[list[CatalogObject | CatalogObjectDict]]
    updated_at: NotRequired[str]
    id_mappings: NotRequired[list[CatalogIdMapping | CatalogIdMappingDict]]
