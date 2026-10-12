from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .vendor_created_event_object import VendorCreatedEventObject, VendorCreatedEventObjectDict


class VendorCreatedEventData(SdkBaseModel):
    """Defines the ``vendor.created`` event data structure."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the event data object. The value is ``vendor``"""

    id: Optional[str] = UNSET
    """The ID of the event data object."""

    object_: Optional[VendorCreatedEventObject] = Field(default=UNSET, alias="object")


class VendorCreatedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[VendorCreatedEventObjectDict]
