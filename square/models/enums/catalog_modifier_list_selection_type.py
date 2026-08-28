from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogModifierListSelectionType(str, Enum):
    """Indicates whether a CatalogModifierList supports multiple selections."""

    SINGLE = "SINGLE"
    """Indicates that a CatalogModifierList allows only a single CatalogModifier to be selected."""

    MULTIPLE = "MULTIPLE"
    """Indicates that a CatalogModifierList allows multiple CatalogModifier to be selected."""

    __str__ = str.__str__


CatalogModifierListSelectionTypeOrStr: TypeAlias = Annotated[
    CatalogModifierListSelectionType | str, open_enum_validator(CatalogModifierListSelectionType)
]
