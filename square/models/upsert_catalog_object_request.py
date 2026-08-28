from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict


class UpsertCatalogObjectRequest(SdkBaseModel):
    idempotency_key: str
    """A value you specify that uniquely identifies this request among all your requests. A common way to create a valid
    idempotency key is to use a Universally unique identifier (UUID).

    If you're unsure whether a particular request was successful, you can reattempt it with the same idempotency key
    without worrying about creating duplicate objects.

    See `Idempotency <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ for more
    information."""

    object_: CatalogObject = Field(alias="object")
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


class UpsertCatalogObjectRequestDict(TypedDict):
    idempotency_key: str
    object_: CatalogObject | CatalogObjectDict
