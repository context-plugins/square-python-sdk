from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class OrderServiceChargeType(str, Enum):
    AUTO_GRATUITY = "AUTO_GRATUITY"
    CUSTOM = "CUSTOM"

    __str__ = str.__str__


OrderServiceChargeTypeOrStr: TypeAlias = Annotated[
    OrderServiceChargeType | str, open_enum_validator(OrderServiceChargeType)
]
