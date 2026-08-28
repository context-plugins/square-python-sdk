from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogCustomAttributeDefinitionType(str, Enum):
    """Defines the possible types for a custom attribute."""

    STRING = "STRING"
    """A free-form string containing up to 255 characters."""

    BOOLEAN = "BOOLEAN"
    """A ``true`` or ``false`` value."""

    NUMBER = "NUMBER"
    """A decimal string representation of a number. Can support up to 5 digits after the decimal point."""

    SELECTION = "SELECTION"
    """One or more choices from ``allowed_selections``."""

    __str__ = str.__str__


CatalogCustomAttributeDefinitionTypeOrStr: TypeAlias = Annotated[
    CatalogCustomAttributeDefinitionType | str, open_enum_validator(CatalogCustomAttributeDefinitionType)
]
