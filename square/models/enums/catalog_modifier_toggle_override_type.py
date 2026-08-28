from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogModifierToggleOverrideType(str, Enum):
    """Item level overrides for bool attributes"""

    NO = "NO"
    """False override"""

    YES = "YES"
    """True override"""

    NOT_SET = "NOT_SET"
    """No override"""

    __str__ = str.__str__


CatalogModifierToggleOverrideTypeOrStr: TypeAlias = Annotated[
    CatalogModifierToggleOverrideType | str, open_enum_validator(CatalogModifierToggleOverrideType)
]
