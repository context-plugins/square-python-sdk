from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .custom_attribute_definition import CustomAttributeDefinition, CustomAttributeDefinitionDict
from .enums.custom_attribute_definition_visibility import CustomAttributeDefinitionVisibilityOrStr


class CustomAttribute(SdkBaseModel):
    """A custom attribute value. Each custom attribute value has a corresponding ``CustomAttributeDefinition``
    object."""

    key: OptionalNullable[str] = UNSET
    """The identifier of the custom attribute definition and its corresponding custom attributes. This value can be a
    simple key, which is the key that is provided when the custom attribute definition is created, or a qualified key,
    if the requesting application is not the definition owner. The qualified key consists of the application ID of the
    custom attribute definition owner followed by the simple key that was provided when the definition was created. It
    has the format application_id:simple key.

    The value for a simple key can contain up to 60 alphanumeric characters, periods (.), underscores (_), and hyphens
    (-)."""

    value: OptionalNullable[Any] = UNSET
    """The value assigned to the custom attribute. It is validated against the custom attribute definition's schema on
    write operations. For more information about custom attribute values, see `Custom Attributes Overview
    <https://developer.squareup.com/docs/devtools/customattributes/overview>`__."""

    version: Optional[int] = UNSET
    """Read only. The current version of the custom attribute. This field is incremented when the custom attribute is
    changed. When updating an existing custom attribute value, you can provide this field and specify the current
    version of the custom attribute to enable `optimistic concurrency
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__. This field can
    also be used to enforce strong consistency for reads. For more information about strong consistency for reads, see
    `Custom Attributes Overview <https://developer.squareup.com/docs/devtools/customattributes/overview>`__."""

    visibility: Optional[CustomAttributeDefinitionVisibilityOrStr] = UNSET
    """The level of permission that a seller or other applications requires to view this custom attribute definition.
    The ``Visibility`` field controls who can read and write the custom attribute values and custom attribute
    definition."""

    definition: Optional[CustomAttributeDefinition] = UNSET
    """Represents a definition for custom attribute values. A custom attribute definition specifies the key, visibility,
    schema, and other properties for a custom attribute."""

    updated_at: Optional[str] = UNSET
    """The timestamp that indicates when the custom attribute was created or was most recently updated, in RFC 3339
    format."""

    created_at: Optional[str] = UNSET
    """The timestamp that indicates when the custom attribute was created, in RFC 3339 format."""


class CustomAttributeDict(TypedDict):
    key: NotRequired[str | None]
    value: NotRequired[Any | None]
    version: NotRequired[int]
    visibility: NotRequired[CustomAttributeDefinitionVisibilityOrStr]
    definition: NotRequired[CustomAttributeDefinition | CustomAttributeDefinitionDict]
    updated_at: NotRequired[str]
    created_at: NotRequired[str]
