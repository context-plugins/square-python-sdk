from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict


class CreateCatalogImageRequest(SdkBaseModel):
    idempotency_key: str
    """A unique string that identifies this CreateCatalogImage request. Keys can be any valid string but must be unique
    for every CreateCatalogImage request.

    See `Idempotency keys <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__ for more
    information."""

    object_id: Optional[str] = UNSET
    """Unique ID of the ``CatalogObject`` to attach this ``CatalogImage`` object to. Leave this field empty to create
    unattached images, for example if you are building an integration where an image can be attached to catalog items at
    a later time."""

    image: CatalogObject
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

    is_primary: Optional[bool] = UNSET
    """If this is set to ``true``, the image created will be the primary, or first image of the object referenced by
    ``object_id``. If the ``CatalogObject`` already has a primary ``CatalogImage``, setting this field to ``true`` will
    replace the primary image. If this is set to ``false`` and you use the Square API version 2021-12-15 or later, the
    image id will be appended to the list of ``image_ids`` on the object.

    With Square API version 2021-12-15 or later, the default value is ``false``. Otherwise, the effective default value
    is ``true``."""


class CreateCatalogImageRequestDict(TypedDict):
    idempotency_key: str
    object_id: NotRequired[str]
    image: CatalogObject | CatalogObjectDict
    is_primary: NotRequired[bool]
