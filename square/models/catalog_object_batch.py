from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .catalog_object import CatalogObject, CatalogObjectDict


class CatalogObjectBatch(SdkBaseModel):
    """A batch of catalog objects."""

    objects: list[CatalogObject]
    """A list of CatalogObjects belonging to this batch."""


class CatalogObjectBatchDict(TypedDict):
    objects: list[CatalogObject | CatalogObjectDict]
