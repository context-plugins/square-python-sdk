from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogModifierListModifierType(str, Enum):
    """Defines the type of ``CatalogModifierList``."""

    LIST = "LIST"
    """The ``CatalogModifierList`` instance is a non-empty list of non text-based modifiers."""

    TEXT = "TEXT"
    """The ``CatalogModifierList`` instance is a single text-based modifier."""

    __str__ = str.__str__


CatalogModifierListModifierTypeOrStr: TypeAlias = Annotated[
    CatalogModifierListModifierType | str, open_enum_validator(CatalogModifierListModifierType)
]
