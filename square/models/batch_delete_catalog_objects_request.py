from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BatchDeleteCatalogObjectsRequest(SdkBaseModel):
    object_ids: list[str]
    """The IDs of the CatalogObjects to be deleted. When an object is deleted, other objects in the graph that depend on
    that object will be deleted as well (for example, deleting a CatalogItem will delete its CatalogItemVariation."""


class BatchDeleteCatalogObjectsRequestDict(TypedDict):
    object_ids: list[str]
