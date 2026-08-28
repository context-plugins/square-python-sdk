from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProductType(str, Enum):
    TERMINAL_API = "TERMINAL_API"

    __str__ = str.__str__


ProductTypeOrStr: TypeAlias = Annotated[ProductType | str, open_enum_validator(ProductType)]
