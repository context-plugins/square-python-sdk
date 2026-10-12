from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute_definition import CustomAttributeDefinition, CustomAttributeDefinitionDict
from .error import Error, ErrorDict


class UpdateMerchantCustomAttributeDefinitionResponse(SdkBaseModel):
    """Represents an `UpdateMerchantCustomAttributeDefinition
    <api-endpoint:MerchantCustomAttributes-UpdateMerchantCustomAttributeDefinition>`__ response. Either
    ``custom_attribute_definition`` or ``errors`` is present in the response."""

    custom_attribute_definition: Optional[CustomAttributeDefinition] = UNSET
    """Represents a definition for custom attribute values. A custom attribute definition specifies the key, visibility,
    schema, and other properties for a custom attribute."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class UpdateMerchantCustomAttributeDefinitionResponseDict(TypedDict):
    custom_attribute_definition: NotRequired[CustomAttributeDefinitionDict]
    errors: NotRequired[list[ErrorDict]]
