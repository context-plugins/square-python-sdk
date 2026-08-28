from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_event_data_object import CustomAttributeEventDataObject, CustomAttributeEventDataObjectDict


class CustomAttributeEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the event data object. The value is ``"custom_attribute"``."""

    id: Optional[str] = UNSET
    """The ID of the event data object."""

    object_: Optional[CustomAttributeEventDataObject] = Field(default=UNSET, alias="object")


class CustomAttributeEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[CustomAttributeEventDataObject | CustomAttributeEventDataObjectDict]
