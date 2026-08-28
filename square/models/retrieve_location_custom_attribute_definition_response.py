from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute_definition import CustomAttributeDefinition, CustomAttributeDefinitionDict
from .error import Error, ErrorDict


class RetrieveLocationCustomAttributeDefinitionResponse(SdkBaseModel):
    """Represents a `RetrieveLocationCustomAttributeDefinition
    <api-endpoint:LocationCustomAttributes-RetrieveLocationCustomAttributeDefinition>`__ response. Either
    ``custom_attribute_definition`` or ``errors`` is present in the response."""

    custom_attribute_definition: Optional[CustomAttributeDefinition] = UNSET
    """Represents a definition for custom attribute values. A custom attribute definition specifies the key, visibility,
    schema, and other properties for a custom attribute."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class RetrieveLocationCustomAttributeDefinitionResponseDict(TypedDict):
    custom_attribute_definition: NotRequired[CustomAttributeDefinition | CustomAttributeDefinitionDict]
    errors: NotRequired[list[Error | ErrorDict]]
