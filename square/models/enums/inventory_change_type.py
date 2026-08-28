from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InventoryChangeType(str, Enum):
    """Indicates how the inventory change was applied to a tracked product quantity."""

    PHYSICAL_COUNT = "PHYSICAL_COUNT"
    """The change occurred as part of a physical count update."""

    ADJUSTMENT = "ADJUSTMENT"
    """The change occurred as part of the normal lifecycle of goods (e.g., as an inventory adjustment)."""

    __str__ = str.__str__


InventoryChangeTypeOrStr: TypeAlias = Annotated[InventoryChangeType | str, open_enum_validator(InventoryChangeType)]
