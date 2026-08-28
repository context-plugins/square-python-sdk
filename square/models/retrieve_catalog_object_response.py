from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict
from .error import Error, ErrorDict


class RetrieveCatalogObjectResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    object_: Optional[CatalogObject] = Field(default=UNSET, alias="object")
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

    related_objects: Optional[list[CatalogObject]] = UNSET
    """A list of ``CatalogObject``s referenced by the object in the ``object`` field."""


class RetrieveCatalogObjectResponseDict(TypedDict):
    errors: NotRequired[list[Error | ErrorDict]]
    object_: NotRequired[CatalogObject | CatalogObjectDict]
    related_objects: NotRequired[list[CatalogObject | CatalogObjectDict]]
