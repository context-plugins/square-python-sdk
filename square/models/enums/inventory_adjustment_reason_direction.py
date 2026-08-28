from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InventoryAdjustmentReasonDirection(str, Enum):
    INCREASE = "INCREASE"
    DECREASE = "DECREASE"

    __str__ = str.__str__


InventoryAdjustmentReasonDirectionOrStr: TypeAlias = Annotated[
    InventoryAdjustmentReasonDirection | str, open_enum_validator(InventoryAdjustmentReasonDirection)
]
