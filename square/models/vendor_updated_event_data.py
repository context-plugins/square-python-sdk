from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .vendor_updated_event_object import VendorUpdatedEventObject, VendorUpdatedEventObjectDict


class VendorUpdatedEventData(SdkBaseModel):
    """Defines the ``vendor.updated`` event data structure."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the event data object. The value is ``vendor``."""

    id: Optional[str] = UNSET
    """The ID of the event data object."""

    object_: Optional[VendorUpdatedEventObject] = Field(default=UNSET, alias="object")


class VendorUpdatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[VendorUpdatedEventObjectDict]
