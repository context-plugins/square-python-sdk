from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .inventory_count_updated_event_object import InventoryCountUpdatedEventObject, InventoryCountUpdatedEventObjectDict


class InventoryCountUpdatedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type. For this event, the value is ``inventory_counts``."""

    id: Optional[str] = UNSET
    """ID of the affected object."""

    object_: Optional[InventoryCountUpdatedEventObject] = Field(default=UNSET, alias="object")


class InventoryCountUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[InventoryCountUpdatedEventObjectDict]
