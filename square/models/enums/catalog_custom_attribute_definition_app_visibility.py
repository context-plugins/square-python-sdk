from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogCustomAttributeDefinitionAppVisibility(str, Enum):
    """Defines the visibility of a custom attribute to applications other than their creating application."""

    APP_VISIBILITY_HIDDEN = "APP_VISIBILITY_HIDDEN"
    """Other applications cannot read this custom attribute."""

    APP_VISIBILITY_READ_ONLY = "APP_VISIBILITY_READ_ONLY"
    """Other applications can read this custom attribute definition and values."""

    APP_VISIBILITY_READ_WRITE_VALUES = "APP_VISIBILITY_READ_WRITE_VALUES"
    """Other applications can read and write custom attribute values on objects. They can read but cannot edit the
    custom attribute definition."""

    __str__ = str.__str__


CatalogCustomAttributeDefinitionAppVisibilityOrStr: TypeAlias = Annotated[
    CatalogCustomAttributeDefinitionAppVisibility | str,
    open_enum_validator(CatalogCustomAttributeDefinitionAppVisibility),
]
