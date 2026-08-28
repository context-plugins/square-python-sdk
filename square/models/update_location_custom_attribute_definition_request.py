from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .custom_attribute_definition import CustomAttributeDefinition, CustomAttributeDefinitionDict


class UpdateLocationCustomAttributeDefinitionRequest(SdkBaseModel):
    """Represents an `UpdateLocationCustomAttributeDefinition
    <api-endpoint:LocationCustomAttributes-UpdateLocationCustomAttributeDefinition>`__ request."""

    custom_attribute_definition: CustomAttributeDefinition
    """Represents a definition for custom attribute values. A custom attribute definition specifies the key, visibility,
    schema, and other properties for a custom attribute."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A unique identifier for this request, used to ensure idempotency. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class UpdateLocationCustomAttributeDefinitionRequestDict(TypedDict):
    custom_attribute_definition: CustomAttributeDefinition | CustomAttributeDefinitionDict
    idempotency_key: NotRequired[str | None]
