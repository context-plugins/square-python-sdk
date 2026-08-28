from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CustomAttributeDefinitionVisibility(str, Enum):
    """The level of permission that a seller or other applications requires to view this custom attribute definition.
    The ``Visibility`` field controls who can read and write the custom attribute values and custom attribute
    definition."""

    VISIBILITY_HIDDEN = "VISIBILITY_HIDDEN"
    """The custom attribute definition and values are hidden from the seller (except on export of all seller data) and
    other developers."""

    VISIBILITY_READ_ONLY = "VISIBILITY_READ_ONLY"
    """The seller and other developers can read the custom attribute definition and values on resources."""

    VISIBILITY_READ_WRITE_VALUES = "VISIBILITY_READ_WRITE_VALUES"
    """The seller and other developers can read the custom attribute definition, and can read and write values on
    resources. A custom attribute definition can only be edited or deleted by the application that created it."""

    __str__ = str.__str__


CustomAttributeDefinitionVisibilityOrStr: TypeAlias = Annotated[
    CustomAttributeDefinitionVisibility | str, open_enum_validator(CustomAttributeDefinitionVisibility)
]
