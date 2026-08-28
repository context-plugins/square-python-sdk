from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .catalog_version_updated_event_object import CatalogVersionUpdatedEventObject, CatalogVersionUpdatedEventObjectDict


class CatalogVersionUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type."""

    object_: Optional[CatalogVersionUpdatedEventObject] = Field(default=UNSET, alias="object")


class CatalogVersionUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    object_: NotRequired[CatalogVersionUpdatedEventObject | CatalogVersionUpdatedEventObjectDict]
