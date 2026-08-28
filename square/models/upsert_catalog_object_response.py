from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_id_mapping import CatalogIdMapping, CatalogIdMappingDict
from .catalog_object import CatalogObject, CatalogObjectDict
from .error import Error, ErrorDict


class UpsertCatalogObjectResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    catalog_object: Optional[CatalogObject] = UNSET
    """The wrapper object for the catalog entries of a given object type.

    Depending on the ``type`` attribute value, a ``CatalogObject`` instance assumes a type-specific data to yield the
    corresponding type of catalog object.

    For example, if ``type=ITEM``, the ``CatalogObject`` instance must have the ITEM-specific data set on the
    ``item_data`` attribute. The resulting ``CatalogObject`` instance is also a ``CatalogItem`` instance.

    In general, if ``type=<OBJECT_TYPE>``, the ``CatalogObject`` instance must have the ``<OBJECT_TYPE>``-specific data
    set on the ``<object_type>_data`` attribute. The resulting ``CatalogObject`` instance is also a
    ``Catalog<ObjectType>`` instance.

    For a more detailed discussion of the Catalog data model, please see the `Design a Catalog
    <https://developer.squareup.com/docs/catalog-api/design-a-catalog>`__ guide."""

    id_mappings: Optional[list[CatalogIdMapping]] = UNSET
    """The mapping between client and server IDs for this upsert."""


class UpsertCatalogObjectResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    catalog_object: NotRequired[CatalogObject | CatalogObjectDict]
    id_mappings: NotRequired[list[CatalogIdMapping | CatalogIdMappingDict]]
