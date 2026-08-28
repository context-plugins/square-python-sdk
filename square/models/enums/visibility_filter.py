from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VisibilityFilter(str, Enum):
    """Enumeration of visibility-filter values used to set the ability to view custom attributes or custom attribute
    definitions."""

    ALL = "ALL"
    """All custom attributes or custom attribute definitions."""

    READ = "READ"
    """All custom attributes or custom attribute definitions with the ``visibility`` field set to
    ``VISIBILITY_READ_ONLY`` or ``VISIBILITY_READ_WRITE_VALUES``."""

    READ_WRITE = "READ_WRITE"
    """All custom attributes or custom attribute definitions with the ``visibility`` field set to
    ``VISIBILITY_READ_WRITE_VALUES``."""

    __str__ = str.__str__


VisibilityFilterOrStr: TypeAlias = Annotated[VisibilityFilter | str, open_enum_validator(VisibilityFilter)]
