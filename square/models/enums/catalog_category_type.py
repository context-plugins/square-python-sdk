from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogCategoryType(str, Enum):
    """Indicates the type of a category."""

    REGULAR_CATEGORY = "REGULAR_CATEGORY"
    """The regular category."""

    MENU_CATEGORY = "MENU_CATEGORY"
    """The menu category."""

    KITCHEN_CATEGORY = "KITCHEN_CATEGORY"
    """Kitchen categories are used by KDS (Kitchen Display System) to route items to specific clients"""

    __str__ = str.__str__


CatalogCategoryTypeOrStr: TypeAlias = Annotated[CatalogCategoryType | str, open_enum_validator(CatalogCategoryType)]
