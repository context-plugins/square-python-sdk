from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogObjectReference(SdkBaseModel):
    """A reference to a Catalog object at a specific version. In general this is used as an entry point into a graph of
    catalog objects, where the objects exist at a specific version."""

    object_id: OptionalNullable[str] = UNSET
    """The ID of the referenced object."""

    catalog_version: OptionalNullable[int] = UNSET
    """The version of the object."""


class CatalogObjectReferenceDict(TypedDict):
    object_id: NotRequired[str | None]
    catalog_version: NotRequired[int | None]
