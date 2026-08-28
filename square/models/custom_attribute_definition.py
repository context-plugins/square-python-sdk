from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.custom_attribute_definition_visibility import CustomAttributeDefinitionVisibilityOrStr


class CustomAttributeDefinition(SdkBaseModel):
    """Represents a definition for custom attribute values. A custom attribute definition specifies the key, visibility,
    schema, and other properties for a custom attribute."""

    key: OptionalNullable[str] = UNSET
    """The identifier of the custom attribute definition and its corresponding custom attributes. This value can be a
    simple key, which is the key that is provided when the custom attribute definition is created, or a qualified key,
    if the requesting application is not the definition owner. The qualified key consists of the application ID of the
    custom attribute definition owner followed by the simple key that was provided when the definition was created. It
    has the format application_id:simple key.

    The value for a simple key can contain up to 60 alphanumeric characters, periods (.), underscores (_), and hyphens
    (-).

    This field can not be changed after the custom attribute definition is created. This field is required when creating
    a definition and must be unique per application, seller, and resource type."""

    schema_value: OptionalNullable[Any] = Field(default=UNSET, alias="schema")
    """The JSON schema for the custom attribute definition, which determines the data type of the corresponding custom
    attributes. For more information, see `Custom Attributes Overview
    <https://developer.squareup.com/docs/devtools/customattributes/overview>`__. This field is required when creating a
    definition."""

    name: OptionalNullable[str] = UNSET
    """The name of the custom attribute definition for API and seller-facing UI purposes. The name must be unique within
    the seller and application pair. This field is required if the ``visibility`` field is ``VISIBILITY_READ_ONLY`` or
    ``VISIBILITY_READ_WRITE_VALUES``."""

    description: OptionalNullable[str] = UNSET
    """Seller-oriented description of the custom attribute definition, including any constraints that the seller should
    observe. May be displayed as a tooltip in Square UIs. This field is required if the ``visibility`` field is
    ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``."""

    visibility: Optional[CustomAttributeDefinitionVisibilityOrStr] = UNSET
    """The level of permission that a seller or other applications requires to view this custom attribute definition.
    The ``Visibility`` field controls who can read and write the custom attribute values and custom attribute
    definition."""

    version: Optional[int] = UNSET
    """Read only. The current version of the custom attribute definition. The value is incremented each time the custom
    attribute definition is updated. When updating a custom attribute definition, you can provide this field and specify
    the current version of the custom attribute definition to enable `optimistic concurrency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__.

    On writes, this field must be set to the latest version. Stale writes are rejected.

    This field can also be used to enforce strong consistency for reads. For more information about strong consistency
    for reads, see `Custom Attributes Overview
    <https://developer.squareup.com/docs/devtools/customattributes/overview>`__."""

    updated_at: Optional[str] = UNSET
    """The timestamp that indicates when the custom attribute definition was created or most recently updated, in RFC
    3339 format."""

    created_at: Optional[str] = UNSET
    """The timestamp that indicates when the custom attribute definition was created, in RFC 3339 format."""


class CustomAttributeDefinitionDict(TypedDict):
    key: NotRequired[str | None]
    schema_value: NotRequired[Any | None]
    name: NotRequired[str | None]
    description: NotRequired[str | None]
    visibility: NotRequired[CustomAttributeDefinitionVisibilityOrStr]
    version: NotRequired[int]
    updated_at: NotRequired[str]
    created_at: NotRequired[str]
