from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute_definition import CustomAttributeDefinition, CustomAttributeDefinitionDict


class CustomAttributeDefinitionEventDataObject(SdkBaseModel):
    custom_attribute_definition: Optional[CustomAttributeDefinition] = UNSET
    """Represents a definition for custom attribute values. A custom attribute definition specifies the key, visibility,
    schema, and other properties for a custom attribute."""


class CustomAttributeDefinitionEventDataObjectDict(TypedDict):
    custom_attribute_definition: NotRequired[CustomAttributeDefinition | CustomAttributeDefinitionDict]
