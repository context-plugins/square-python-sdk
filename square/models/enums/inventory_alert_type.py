from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class InventoryAlertType(str, Enum):
    """Indicates whether Square should alert the merchant when the inventory quantity of a CatalogItemVariation is
    low."""

    NONE = "NONE"
    """The variation does not display an alert."""

    LOW_QUANTITY = "LOW_QUANTITY"
    """The variation generates an alert when its quantity is low."""

    __str__ = str.__str__


InventoryAlertTypeOrStr: TypeAlias = Annotated[InventoryAlertType | str, open_enum_validator(InventoryAlertType)]
