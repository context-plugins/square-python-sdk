from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ComponentComponentType(str, Enum):
    """An enum for ComponentType."""

    APPLICATION = "APPLICATION"
    CARD_READER = "CARD_READER"
    BATTERY = "BATTERY"
    WIFI = "WIFI"
    ETHERNET = "ETHERNET"
    PRINTER = "PRINTER"

    __str__ = str.__str__


ComponentComponentTypeOrStr: TypeAlias = Annotated[
    ComponentComponentType | str, open_enum_validator(ComponentComponentType)
]
