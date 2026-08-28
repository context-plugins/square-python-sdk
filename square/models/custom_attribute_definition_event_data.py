from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_definition_event_data_object import (
    CustomAttributeDefinitionEventDataObject,
    CustomAttributeDefinitionEventDataObjectDict,
)


class CustomAttributeDefinitionEventData(SdkBaseModel):
    """Represents an object in the CustomAttributeDefinition event notification payload that contains the affected
    custom attribute definition."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of the event data object. The value is ``"custom_attribute_definition"``."""

    id: Optional[str] = UNSET
    """The ID of the event data object."""

    object_: Optional[CustomAttributeDefinitionEventDataObject] = Field(default=UNSET, alias="object")


class CustomAttributeDefinitionEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[CustomAttributeDefinitionEventDataObject | CustomAttributeDefinitionEventDataObjectDict]
