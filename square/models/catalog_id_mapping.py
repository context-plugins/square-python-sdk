from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogIdMapping(SdkBaseModel):
    """A mapping between a temporary client-supplied ID and a permanent server-generated ID.

    When calling `UpsertCatalogObject <api-endpoint:Catalog-UpsertCatalogObject>`__ or `BatchUpsertCatalogObjects
    <api-endpoint:Catalog-BatchUpsertCatalogObjects>`__ to create a `CatalogObject <entity:CatalogObject>`__ instance,
    you can supply a temporary ID for the to-be-created object, especially when the object is to be referenced elsewhere
    in the same request body. This temporary ID can be any string unique within the call, but must be prefixed by "#".

    After the request is submitted and the object created, a permanent server-generated ID is assigned to the new
    object. The permanent ID is unique across the Square catalog."""

    client_object_id: OptionalNullable[str] = UNSET
    """The client-supplied temporary ``#``-prefixed ID for a new ``CatalogObject``."""

    object_id: OptionalNullable[str] = UNSET
    """The permanent ID for the CatalogObject created by the server."""


class CatalogIdMappingDict(TypedDict):
    client_object_id: NotRequired[str | None]
    object_id: NotRequired[str | None]
