from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CatalogV1Id(SdkBaseModel):
    """A Square API V1 identifier of an item, including the object ID and its associated location ID."""

    catalog_v1_id: OptionalNullable[str] = UNSET
    """The ID for an object used in the Square API V1, if the object ID differs from the Square API V2 object ID."""

    location_id: OptionalNullable[str] = UNSET
    """The ID of the ``Location`` this Connect V1 ID is associated with."""


class CatalogV1IdDict(TypedDict):
    catalog_v1_id: NotRequired[str | None]
    location_id: NotRequired[str | None]
