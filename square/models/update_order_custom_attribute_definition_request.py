from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .custom_attribute_definition import CustomAttributeDefinition, CustomAttributeDefinitionDict


class UpdateOrderCustomAttributeDefinitionRequest(SdkBaseModel):
    """Represents an update request for an order custom attribute definition."""

    custom_attribute_definition: CustomAttributeDefinition
    """Represents a definition for custom attribute values. A custom attribute definition specifies the key, visibility,
    schema, and other properties for a custom attribute."""

    idempotency_key: OptionalNullable[str] = UNSET
    """A unique identifier for this request, used to ensure idempotency. For more information, see `Idempotency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency>`__."""


class UpdateOrderCustomAttributeDefinitionRequestDict(TypedDict):
    custom_attribute_definition: CustomAttributeDefinitionDict
    idempotency_key: NotRequired[str | None]
