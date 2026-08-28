from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SearchCatalogItemsRequestStockLevel(str, Enum):
    """Defines supported stock levels of the item inventory."""

    OUT = "OUT"
    """The item inventory is empty."""

    LOW = "LOW"
    """The item inventory is low."""

    __str__ = str.__str__


SearchCatalogItemsRequestStockLevelOrStr: TypeAlias = Annotated[
    SearchCatalogItemsRequestStockLevel | str, open_enum_validator(SearchCatalogItemsRequestStockLevel)
]
